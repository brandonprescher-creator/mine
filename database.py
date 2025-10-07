import sqlite3
import json
import os
from datetime import datetime
from typing import List, Dict, Optional, Tuple

from flask import current_app

DATABASE_FILE = "tutor_app.db"


def _get_database_path() -> str:
    """Resolve the database path from Flask config or environment."""
    try:
        path = current_app.config.get("DATABASE_URL", DATABASE_FILE)  # type: ignore[attr-defined]
    except RuntimeError:
        # Outside of an application context
        path = os.getenv("DATABASE_URL", DATABASE_FILE)
    
    # If it's a PostgreSQL URL, use the default SQLite file
    if path.startswith("postgresql://"):
        path = DATABASE_FILE
    
    # Ensure the directory exists
    db_dir = os.path.dirname(path)
    if db_dir and not os.path.exists(db_dir):
        os.makedirs(db_dir, exist_ok=True)
    
    return path


def get_connection():
    """Get a database connection."""
    conn = sqlite3.connect(_get_database_path(), check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn


def init_database():
    """Initialize the database with all required tables."""
    conn = get_connection()
    cursor = conn.cursor()

    # Subjects table
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS subjects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE,
            description TEXT,
            icon TEXT,
            display_order INTEGER,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """
    )

    # Topics table
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS topics (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            subject_id INTEGER NOT NULL,
            name TEXT NOT NULL,
            description TEXT,
            display_order INTEGER,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (subject_id) REFERENCES subjects(id)
        )
    """
    )

    # Lessons table
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS lessons (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            topic_id INTEGER NOT NULL,
            title TEXT NOT NULL,
            description TEXT,
            steps TEXT,  -- JSON array of teaching steps
            examples TEXT,  -- JSON array of worked examples
            additional_resources TEXT,  -- JSON for API-fetched content
            source_type TEXT DEFAULT 'builtin',  -- 'builtin', 'uploaded', 'api'
            source_file TEXT,
            display_order INTEGER,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (topic_id) REFERENCES topics(id)
        )
    """
    )

    # Practice problems table
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS practice_problems (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            lesson_id INTEGER NOT NULL,
            question TEXT NOT NULL,
            answer TEXT NOT NULL,
            steps TEXT,  -- JSON array of solution steps
            hints TEXT,  -- JSON array of hints
            difficulty TEXT DEFAULT 'medium',  -- 'easy', 'medium', 'hard'
            display_order INTEGER,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (lesson_id) REFERENCES lessons(id)
        )
    """
    )

    # Uploaded files table
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS uploaded_files (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT NOT NULL,
            file_type TEXT NOT NULL,
            extracted_text TEXT,
            processed BOOLEAN DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """
    )

    # Progress tracking table
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS student_progress (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            lesson_id INTEGER,
            practice_problem_id INTEGER,
            completed BOOLEAN DEFAULT 0,
            score INTEGER,
            attempts INTEGER DEFAULT 0,
            last_attempted TIMESTAMP,
            mastery_level TEXT DEFAULT 'not_started',  -- 'not_started', 'learning', 'practicing', 'mastered'
            FOREIGN KEY (lesson_id) REFERENCES lessons(id),
            FOREIGN KEY (practice_problem_id) REFERENCES practice_problems(id)
        )
    """
    )

    # API cache table
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS api_cache (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            api_source TEXT NOT NULL,
            query TEXT NOT NULL,
            response_data TEXT,  -- JSON
            cached_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            expires_at TIMESTAMP
        )
    """
    )

    # Standards alignment table
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS standards (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            lesson_id INTEGER NOT NULL,
            standard_type TEXT,  -- 'common_core', 'ngss', 'state'
            standard_code TEXT,
            description TEXT,
            FOREIGN KEY (lesson_id) REFERENCES lessons(id)
        )
    """
    )

    conn.commit()
    conn.close()


# CRUD operations for subjects
def add_subject(
    name: str, description: str = "", icon: str = "📚", display_order: int = 0
) -> int:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO subjects (name, description, icon, display_order) VALUES (?, ?, ?, ?)",
        (name, description, icon, display_order),
    )
    subject_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return subject_id


def get_all_subjects() -> List[Dict]:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM subjects ORDER BY display_order, name")
    subjects = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return subjects


# CRUD operations for topics
def add_topic(
    subject_id: int, name: str, description: str = "", display_order: int = 0
) -> int:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO topics (subject_id, name, description, display_order) VALUES (?, ?, ?, ?)",
        (subject_id, name, description, display_order),
    )
    topic_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return topic_id


def get_topics_by_subject(subject_id: int) -> List[Dict]:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM topics WHERE subject_id = ? ORDER BY display_order, name",
        (subject_id,),
    )
    topics = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return topics


# CRUD operations for lessons
def add_lesson(
    topic_id: int,
    title: str,
    description: str,
    steps: List[str],
    examples: List[Dict],
    source_type: str = "builtin",
    source_file: str = None,
    display_order: int = 0,
) -> int:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """INSERT INTO lessons (topic_id, title, description, steps, examples, 
           source_type, source_file, display_order) 
           VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
        (
            topic_id,
            title,
            description,
            json.dumps(steps),
            json.dumps(examples),
            source_type,
            source_file,
            display_order,
        ),
    )
    lesson_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return lesson_id


def get_lessons_by_topic(topic_id: int) -> List[Dict]:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM lessons WHERE topic_id = ? ORDER BY display_order, title",
        (topic_id,),
    )
    lessons = []
    for row in cursor.fetchall():
        lesson = dict(row)
        lesson["steps"] = json.loads(lesson["steps"]) if lesson["steps"] else []
        lesson["examples"] = (
            json.loads(lesson["examples"]) if lesson["examples"] else []
        )
        lessons.append(lesson)
    conn.close()
    return lessons


def get_lesson_by_id(lesson_id: int) -> Optional[Dict]:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT l.*, t.subject_id, s.name as subject_name
        FROM lessons l
        JOIN topics t ON l.topic_id = t.id
        JOIN subjects s ON t.subject_id = s.id
        WHERE l.id = ?
    """,
        (lesson_id,),
    )
    row = cursor.fetchone()
    conn.close()
    if row:
        lesson = dict(row)
        lesson["steps"] = json.loads(lesson["steps"]) if lesson["steps"] else []
        lesson["examples"] = (
            json.loads(lesson["examples"]) if lesson["examples"] else []
        )
        lesson["additional_resources"] = (
            json.loads(lesson["additional_resources"])
            if lesson["additional_resources"]
            else []
        )
        # Add defaults if missing
        if "difficulty" not in lesson or not lesson["difficulty"]:
            lesson["difficulty"] = "Medium"
        if "estimated_time" not in lesson or not lesson["estimated_time"]:
            lesson["estimated_time"] = 15
        return lesson
    return None


# CRUD operations for practice problems
def add_practice_problem(
    lesson_id: int,
    question: str,
    answer: str,
    steps: List[str],
    hints: List[str] = None,
    difficulty: str = "medium",
    display_order: int = 0,
) -> int:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """INSERT INTO practice_problems (lesson_id, question, answer, steps, hints, difficulty, display_order) 
           VALUES (?, ?, ?, ?, ?, ?, ?)""",
        (
            lesson_id,
            question,
            answer,
            json.dumps(steps),
            json.dumps(hints or []),
            difficulty,
            display_order,
        ),
    )
    problem_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return problem_id


def get_practice_problems_by_lesson(lesson_id: int) -> List[Dict]:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM practice_problems WHERE lesson_id = ? ORDER BY display_order",
        (lesson_id,),
    )
    problems = []
    for row in cursor.fetchall():
        problem = dict(row)
        problem["steps"] = json.loads(problem["steps"]) if problem["steps"] else []
        problem["hints"] = json.loads(problem["hints"]) if problem["hints"] else []
        problems.append(problem)
    conn.close()
    return problems


# Progress tracking functions
def record_practice_attempt(lesson_id: int, problem_id: int, is_correct: bool):
    conn = get_connection()
    cursor = conn.cursor()

    # Check if progress record exists
    cursor.execute(
        """SELECT id, attempts, score FROM student_progress 
           WHERE lesson_id = ? AND practice_problem_id = ?""",
        (lesson_id, problem_id),
    )
    existing = cursor.fetchone()

    if existing:
        attempts = existing["attempts"] + 1
        score = existing["score"] + (1 if is_correct else 0)
        mastery = (
            "mastered" if score / attempts >= 0.8 and attempts >= 3 else "practicing"
        )

        cursor.execute(
            """UPDATE student_progress 
               SET attempts = ?, score = ?, last_attempted = ?, mastery_level = ?, completed = ?
               WHERE id = ?""",
            (
                attempts,
                score,
                datetime.now(),
                mastery,
                1 if is_correct else 0,
                existing["id"],
            ),
        )
    else:
        mastery = "practicing"
        cursor.execute(
            """INSERT INTO student_progress 
               (lesson_id, practice_problem_id, attempts, score, last_attempted, mastery_level, completed)
               VALUES (?, ?, 1, ?, ?, ?, ?)""",
            (
                lesson_id,
                problem_id,
                1 if is_correct else 0,
                datetime.now(),
                mastery,
                1 if is_correct else 0,
            ),
        )

    conn.commit()
    conn.close()


def get_lesson_progress(lesson_id: int) -> Dict:
    conn = get_connection()
    cursor = conn.cursor()

    # Get all progress for this lesson
    cursor.execute(
        """SELECT COUNT(*) as total, 
           SUM(CASE WHEN mastery_level = 'mastered' THEN 1 ELSE 0 END) as mastered,
           AVG(CASE WHEN attempts > 0 THEN CAST(score AS FLOAT) / attempts ELSE 0 END) as avg_score
           FROM student_progress WHERE lesson_id = ?""",
        (lesson_id,),
    )
    result = cursor.fetchone()
    conn.close()

    return {
        "total_problems": result["total"] or 0,
        "mastered": result["mastered"] or 0,
        "avg_score": result["avg_score"] or 0,
    }


def get_overall_progress() -> Dict:
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """SELECT 
           COUNT(DISTINCT lesson_id) as lessons_started,
           SUM(CASE WHEN mastery_level = 'mastered' THEN 1 ELSE 0 END) as problems_mastered,
           COUNT(*) as total_problems_attempted
           FROM student_progress"""
    )
    result = cursor.fetchone()

    cursor.execute("SELECT COUNT(*) as total_lessons FROM lessons")
    total_lessons = cursor.fetchone()["total_lessons"]

    conn.close()

    return {
        "lessons_started": result["lessons_started"] or 0,
        "total_lessons": total_lessons,
        "problems_mastered": result["problems_mastered"] or 0,
        "total_problems_attempted": result["total_problems_attempted"] or 0,
    }


# File upload tracking
def add_uploaded_file(filename: str, file_type: str, extracted_text: str) -> int:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO uploaded_files (filename, file_type, extracted_text) VALUES (?, ?, ?)",
        (filename, file_type, extracted_text),
    )
    file_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return file_id


def mark_file_processed(file_id: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE uploaded_files SET processed = 1 WHERE id = ?", (file_id,))
    conn.commit()
    conn.close()


def get_uploaded_files() -> List[Dict]:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM uploaded_files ORDER BY created_at DESC")
    files = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return files


# API cache functions
def cache_api_response(
    api_source: str, query: str, response_data: Dict, expires_hours: int = 24
):
    conn = get_connection()
    cursor = conn.cursor()
    expires_at = datetime.now().timestamp() + (expires_hours * 3600)
    cursor.execute(
        "INSERT INTO api_cache (api_source, query, response_data, expires_at) VALUES (?, ?, ?, ?)",
        (api_source, query, json.dumps(response_data), expires_at),
    )
    conn.commit()
    conn.close()


def get_cached_api_response(api_source: str, query: str) -> Optional[Dict]:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT response_data, expires_at FROM api_cache WHERE api_source = ? AND query = ?",
        (api_source, query),
    )
    row = cursor.fetchone()
    conn.close()

    if row:
        expires_at = row["expires_at"]
        if datetime.now().timestamp() < expires_at:
            return json.loads(row["response_data"])
    return None


# Search functions
def search_lessons(query: str) -> List[Dict]:
    conn = get_connection()
    cursor = conn.cursor()
    search_term = f"%{query}%"
    cursor.execute(
        """SELECT l.*, t.name as topic_name, s.name as subject_name
           FROM lessons l
           JOIN topics t ON l.topic_id = t.id
           JOIN subjects s ON t.subject_id = s.id
           WHERE l.title LIKE ? OR l.description LIKE ?
           ORDER BY l.title
           LIMIT 20""",
        (search_term, search_term),
    )
    lessons = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return lessons


# Additional functions for Flask app
def get_practice_problems_by_topic(topic_id: int) -> List[Dict]:
    """Get practice problems for a specific topic"""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """SELECT pp.*, l.title as lesson_title
           FROM practice_problems pp
           JOIN lessons l ON pp.lesson_id = l.id
           WHERE l.topic_id = ?
           ORDER BY pp.display_order""",
        (topic_id,),
    )

    problems = []
    for row in cursor.fetchall():
        problem = dict(row)
        problem["steps"] = json.loads(problem["steps"]) if problem["steps"] else []
        problem["hints"] = json.loads(problem["hints"]) if problem["hints"] else []
        # Add some mock data for the Flask app
        problem["correct_answer"] = problem["answer"]
        problem["explanation"] = (
            problem["hints"][0] if problem["hints"] else "Great job!"
        )
        problem["options"] = None  # Will be generated dynamically
        problem["image_url"] = None
        problems.append(problem)

    conn.close()
    return problems


def get_topic_by_id(topic_id: int) -> Optional[Dict]:
    """Get a specific topic by ID"""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """SELECT t.*, s.name as subject_name
           FROM topics t
           JOIN subjects s ON t.subject_id = s.id
           WHERE t.id = ?""",
        (topic_id,),
    )

    row = cursor.fetchone()
    conn.close()

    if row:
        topic = dict(row)
        # Add some mock data for the Flask app
        topic["difficulty"] = "Medium"
        topic["estimated_time"] = 15
        topic["progress"] = 0
        topic["icon"] = "📚"
        return topic
    return None


def get_subject_by_id(subject_id: int) -> Optional[Dict]:
    """Get a specific subject by ID"""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM subjects WHERE id = ?", (subject_id,))
    row = cursor.fetchone()
    conn.close()

    if row:
        return dict(row)
    return None
