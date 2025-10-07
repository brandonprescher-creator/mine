"""
Enhanced database module with transaction support and typing
"""

import sqlite3
import json
from datetime import datetime
from typing import List, Dict, Optional, Tuple, Any
from contextlib import contextmanager
from dataclasses import dataclass
from config import get_config


@dataclass
class Subject:
    """Subject data class."""

    id: int
    name: str
    description: str
    icon: str
    display_order: int
    created_at: str


@dataclass
class Topic:
    """Topic data class."""

    id: int
    subject_id: int
    name: str
    description: str
    display_order: int
    created_at: str


@dataclass
class Lesson:
    """Lesson data class."""

    id: int
    topic_id: int
    title: str
    description: str
    steps: List[str]
    examples: List[Dict]
    source_type: str
    source_file: Optional[str]
    display_order: int
    difficulty: str
    estimated_time: int
    created_at: str


@dataclass
class PracticeProblem:
    """Practice problem data class."""

    id: int
    lesson_id: int
    question: str
    answer: str
    explanation: List[str]
    hints: List[str]
    difficulty: str
    display_order: int
    created_at: str


class DatabaseManager:
    """Enhanced database manager with transaction support."""

    def __init__(self):
        self.config = get_config()
        self.database_url = self.config.DATABASE_URL

    @contextmanager
    def get_connection(self):
        """Get database connection with proper cleanup."""
        conn = sqlite3.connect(self.database_url, check_same_thread=False)
        conn.row_factory = sqlite3.Row
        try:
            yield conn
        finally:
            conn.close()

    @contextmanager
    def transaction(self):
        """Get database connection with transaction support."""
        conn = sqlite3.connect(self.database_url, check_same_thread=False)
        conn.row_factory = sqlite3.Row
        try:
            yield conn
            conn.commit()
        except Exception:
            conn.rollback()
            raise
        finally:
            conn.close()

    def init_database(self):
        """Initialize the database with all required tables."""
        with self.get_connection() as conn:
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
                    steps TEXT,
                    examples TEXT,
                    additional_resources TEXT,
                    source_type TEXT DEFAULT 'builtin',
                    source_file TEXT,
                    display_order INTEGER DEFAULT 0,
                    difficulty TEXT DEFAULT 'Medium',
                    estimated_time INTEGER DEFAULT 30,
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
                    explanation TEXT,
                    hints TEXT,
                    difficulty TEXT DEFAULT 'Medium',
                    display_order INTEGER DEFAULT 0,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (lesson_id) REFERENCES lessons(id)
                )
            """
            )

            # User progress table
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS user_progress (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id TEXT NOT NULL,
                    lesson_id INTEGER NOT NULL,
                    completed BOOLEAN DEFAULT FALSE,
                    score REAL DEFAULT 0.0,
                    time_spent INTEGER DEFAULT 0,
                    completed_at TIMESTAMP,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (lesson_id) REFERENCES lessons(id)
                )
            """
            )

            # User achievements table
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS user_achievements (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id TEXT NOT NULL,
                    achievement_id TEXT NOT NULL,
                    earned_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    UNIQUE(user_id, achievement_id)
                )
            """
            )

            conn.commit()

    def get_all_subjects(self) -> List[Subject]:
        """Get all subjects."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM subjects ORDER BY display_order")
            rows = cursor.fetchall()
            return [Subject(**dict(row)) for row in rows]

    def get_subject_by_id(self, subject_id: int) -> Optional[Subject]:
        """Get subject by ID."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM subjects WHERE id = ?", (subject_id,))
            row = cursor.fetchone()
            return Subject(**dict(row)) if row else None

    def add_subject(
        self, name: str, description: str, icon: str, display_order: int
    ) -> int:
        """Add a new subject."""
        with self.transaction() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO subjects (name, description, icon, display_order) VALUES (?, ?, ?, ?)",
                (name, description, icon, display_order),
            )
            return cursor.lastrowid

    def get_topics_by_subject(self, subject_id: int) -> List[Topic]:
        """Get topics for a subject."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM topics WHERE subject_id = ? ORDER BY display_order",
                (subject_id,),
            )
            rows = cursor.fetchall()
            return [Topic(**dict(row)) for row in rows]

    def add_topic(
        self, subject_id: int, name: str, description: str, display_order: int
    ) -> int:
        """Add a new topic."""
        with self.transaction() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO topics (subject_id, name, description, display_order) VALUES (?, ?, ?, ?)",
                (subject_id, name, description, display_order),
            )
            return cursor.lastrowid

    def get_lessons_by_topic(self, topic_id: int) -> List[Lesson]:
        """Get lessons for a topic."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM lessons WHERE topic_id = ? ORDER BY display_order",
                (topic_id,),
            )
            rows = cursor.fetchall()
            lessons = []
            for row in rows:
                lesson_dict = dict(row)
                lesson_dict["steps"] = (
                    json.loads(lesson_dict["steps"]) if lesson_dict["steps"] else []
                )
                lesson_dict["examples"] = (
                    json.loads(lesson_dict["examples"])
                    if lesson_dict["examples"]
                    else []
                )
                lessons.append(Lesson(**lesson_dict))
            return lessons

    def get_lesson_by_id(self, lesson_id: int) -> Optional[Lesson]:
        """Get lesson by ID with subject info."""
        with self.get_connection() as conn:
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
            if row:
                lesson_dict = dict(row)
                lesson_dict["steps"] = (
                    json.loads(lesson_dict["steps"]) if lesson_dict["steps"] else []
                )
                lesson_dict["examples"] = (
                    json.loads(lesson_dict["examples"])
                    if lesson_dict["examples"]
                    else []
                )
                lesson_dict["additional_resources"] = (
                    json.loads(lesson_dict["additional_resources"])
                    if lesson_dict["additional_resources"]
                    else []
                )
                return Lesson(**lesson_dict)
            return None

    def add_lesson(
        self,
        topic_id: int,
        title: str,
        description: str,
        steps: List[str],
        examples: List[Dict],
        source_type: str = "builtin",
        source_file: str = None,
        display_order: int = 0,
    ) -> int:
        """Add a new lesson."""
        with self.transaction() as conn:
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
            return cursor.lastrowid

    def get_practice_problems_by_topic(self, topic_id: int) -> List[PracticeProblem]:
        """Get practice problems for a topic."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                SELECT pp.* FROM practice_problems pp
                JOIN lessons l ON pp.lesson_id = l.id
                WHERE l.topic_id = ? ORDER BY pp.display_order
            """,
                (topic_id,),
            )
            rows = cursor.fetchall()
            problems = []
            for row in rows:
                problem_dict = dict(row)
                problem_dict["explanation"] = (
                    json.loads(problem_dict["explanation"])
                    if problem_dict["explanation"]
                    else []
                )
                problem_dict["hints"] = (
                    json.loads(problem_dict["hints"]) if problem_dict["hints"] else []
                )
                problems.append(PracticeProblem(**problem_dict))
            return problems

    def add_practice_problem(
        self,
        lesson_id: int,
        question: str,
        answer: str,
        explanation: List[str],
        hints: List[str],
        difficulty: str = "Medium",
        display_order: int = 0,
    ) -> int:
        """Add a new practice problem."""
        with self.transaction() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """INSERT INTO practice_problems (lesson_id, question, answer, explanation, hints, 
                   difficulty, display_order) VALUES (?, ?, ?, ?, ?, ?, ?)""",
                (
                    lesson_id,
                    question,
                    answer,
                    json.dumps(explanation),
                    json.dumps(hints),
                    difficulty,
                    display_order,
                ),
            )
            return cursor.lastrowid

    def update_user_progress(
        self,
        user_id: str,
        lesson_id: int,
        completed: bool,
        score: float = 0.0,
        time_spent: int = 0,
    ):
        """Update user progress."""
        with self.transaction() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT OR REPLACE INTO user_progress 
                (user_id, lesson_id, completed, score, time_spent, completed_at)
                VALUES (?, ?, ?, ?, ?, ?)
            """,
                (
                    user_id,
                    lesson_id,
                    completed,
                    score,
                    time_spent,
                    datetime.now().isoformat() if completed else None,
                ),
            )

    def get_user_progress(self, user_id: str) -> Dict[str, Any]:
        """Get user progress summary."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                SELECT 
                    COUNT(*) as total_lessons,
                    SUM(CASE WHEN completed = 1 THEN 1 ELSE 0 END) as completed_lessons,
                    AVG(score) as average_score,
                    SUM(time_spent) as total_time
                FROM user_progress 
                WHERE user_id = ?
            """,
                (user_id,),
            )
            row = cursor.fetchone()
            return dict(row) if row else {}


# Global database manager instance
db = DatabaseManager()


# Backward compatibility functions
def get_connection():
    """Get database connection (backward compatibility)."""
    return db.get_connection()


def init_database():
    """Initialize database (backward compatibility)."""
    return db.init_database()


def get_all_subjects():
    """Get all subjects (backward compatibility)."""
    return [dict(subject.__dict__) for subject in db.get_all_subjects()]


def get_subject_by_id(subject_id: int):
    """Get subject by ID (backward compatibility)."""
    subject = db.get_subject_by_id(subject_id)
    return dict(subject.__dict__) if subject else None


def get_topics_by_subject(subject_id: int):
    """Get topics by subject (backward compatibility)."""
    return [dict(topic.__dict__) for topic in db.get_topics_by_subject(subject_id)]


def get_topic_by_id(topic_id: int):
    """Get topic by ID."""
    with db.get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM topics WHERE id = ?", (topic_id,))
        row = cursor.fetchone()
        return dict(row) if row else None


def add_subject(name: str, description: str, icon: str, display_order: int):
    """Add subject (backward compatibility)."""
    return db.add_subject(name, description, icon, display_order)


def add_topic(subject_id: int, name: str, description: str, display_order: int):
    """Add topic (backward compatibility)."""
    return db.add_topic(subject_id, name, description, display_order)


def get_lessons_by_topic(topic_id: int):
    """Get lessons by topic (backward compatibility)."""
    return [dict(lesson.__dict__) for lesson in db.get_lessons_by_topic(topic_id)]


def get_lesson_by_id(lesson_id: int):
    """Get lesson by ID (backward compatibility)."""
    lesson = db.get_lesson_by_id(lesson_id)
    return dict(lesson.__dict__) if lesson else None


def add_lesson(
    topic_id: int,
    title: str,
    description: str,
    steps: List[str],
    examples: List[Dict],
    source_type: str = "builtin",
    source_file: str = None,
    display_order: int = 0,
):
    """Add lesson (backward compatibility)."""
    return db.add_lesson(
        topic_id,
        title,
        description,
        steps,
        examples,
        source_type,
        source_file,
        display_order,
    )


def get_practice_problems_by_topic(topic_id: int):
    """Get practice problems by topic (backward compatibility)."""
    return [
        dict(problem.__dict__)
        for problem in db.get_practice_problems_by_topic(topic_id)
    ]


def add_practice_problem(
    lesson_id: int,
    question: str,
    answer: str,
    explanation: List[str],
    hints: List[str],
    difficulty: str = "Medium",
    display_order: int = 0,
):
    """Add practice problem (backward compatibility)."""
    return db.add_practice_problem(
        lesson_id, question, answer, explanation, hints, difficulty, display_order
    )
