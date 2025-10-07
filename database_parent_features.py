"""
Database schema and functions for Parent Dashboard features
"""

import sqlite3
from datetime import datetime
from database import get_connection


def init_parent_dashboard_tables():
    """Initialize all tables needed for parent dashboard features"""
    conn = get_connection()
    cursor = conn.cursor()

    # Student profiles table
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS student_profiles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id TEXT NOT NULL UNIQUE,
            name TEXT NOT NULL,
            grade_level TEXT,
            age INTEGER,
            interests TEXT,
            learning_style TEXT,
            avatar TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """
    )

    # Learning playlists table
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS learning_playlists (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id TEXT NOT NULL,
            name TEXT NOT NULL,
            lesson_ids TEXT NOT NULL,
            description TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (student_id) REFERENCES student_profiles(student_id)
        )
    """
    )

    # Lesson schedule table
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS lesson_schedule (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id TEXT NOT NULL,
            lesson_id INTEGER NOT NULL,
            scheduled_date TEXT NOT NULL,
            completed BOOLEAN DEFAULT 0,
            completed_at TIMESTAMP,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (student_id) REFERENCES student_profiles(student_id),
            FOREIGN KEY (lesson_id) REFERENCES lessons(id)
        )
    """
    )

    # Reward coupons table
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS reward_coupons (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id TEXT NOT NULL,
            reward_name TEXT NOT NULL,
            requirement TEXT NOT NULL,
            earned BOOLEAN DEFAULT 0,
            earned_at TIMESTAMP,
            redeemed BOOLEAN DEFAULT 0,
            redeemed_at TIMESTAMP,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (student_id) REFERENCES student_profiles(student_id)
        )
    """
    )

    # Sister quests table (collaborative projects)
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS sister_quests (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            quest_name TEXT NOT NULL,
            description TEXT,
            student1_id TEXT NOT NULL,
            student2_id TEXT NOT NULL,
            student1_task TEXT,
            student2_task TEXT,
            student1_completed BOOLEAN DEFAULT 0,
            student2_completed BOOLEAN DEFAULT 0,
            reward TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            completed_at TIMESTAMP,
            FOREIGN KEY (student1_id) REFERENCES student_profiles(student_id),
            FOREIGN KEY (student2_id) REFERENCES student_profiles(student_id)
        )
    """
    )

    # Parent notes table
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS parent_notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id TEXT NOT NULL,
            lesson_id INTEGER,
            note_text TEXT NOT NULL,
            note_type TEXT DEFAULT 'general',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (student_id) REFERENCES student_profiles(student_id),
            FOREIGN KEY (lesson_id) REFERENCES lessons(id)
        )
    """
    )

    # Struggle alerts table
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS struggle_alerts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id TEXT NOT NULL,
            lesson_id INTEGER NOT NULL,
            topic TEXT NOT NULL,
            error_count INTEGER NOT NULL,
            severity TEXT NOT NULL,
            acknowledged BOOLEAN DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (student_id) REFERENCES student_profiles(student_id),
            FOREIGN KEY (lesson_id) REFERENCES lessons(id)
        )
    """
    )

    conn.commit()
    conn.close()
    print("✅ Parent Dashboard tables initialized successfully!")


def create_student_profile(
    student_id: str,
    name: str,
    grade_level: str,
    age: int,
    interests: list = None,
    learning_style: str = "visual",
) -> int:
    """Create a new student profile"""
    conn = get_connection()
    cursor = conn.cursor()

    interests_str = ",".join(interests) if interests else ""

    cursor.execute(
        """
        INSERT INTO student_profiles 
        (student_id, name, grade_level, age, interests, learning_style)
        VALUES (?, ?, ?, ?, ?, ?)
    """,
        (student_id, name, grade_level, age, interests_str, learning_style),
    )

    profile_id = cursor.lastrowid
    conn.commit()
    conn.close()

    return profile_id


def get_student_profile(student_id: str) -> dict:
    """Get student profile"""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT * FROM student_profiles WHERE student_id = ?
    """,
        (student_id,),
    )

    profile = cursor.fetchone()
    conn.close()

    if profile:
        profile_dict = dict(profile)
        profile_dict["interests"] = (
            profile_dict["interests"].split(",")
            if profile_dict["interests"]
            else []
        )
        return profile_dict
    return None


def update_student_interests(student_id: str, interests: list):
    """Update student interests"""
    conn = get_connection()
    cursor = conn.cursor()

    interests_str = ",".join(interests)

    cursor.execute(
        """
        UPDATE student_profiles SET interests = ? WHERE student_id = ?
    """,
        (interests_str, student_id),
    )

    conn.commit()
    conn.close()


def add_parent_note(
    student_id: str, note_text: str, lesson_id: int = None, note_type: str = "general"
):
    """Add a note about a student's progress"""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO parent_notes (student_id, lesson_id, note_text, note_type)
        VALUES (?, ?, ?, ?)
    """,
        (student_id, lesson_id, note_text, note_type),
    )

    conn.commit()
    conn.close()


def create_sister_quest(
    quest_name: str,
    description: str,
    student1_id: str,
    student2_id: str,
    student1_task: str,
    student2_task: str,
    reward: str,
) -> int:
    """Create a collaborative sister quest"""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO sister_quests 
        (quest_name, description, student1_id, student2_id, student1_task, student2_task, reward)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """,
        (
            quest_name,
            description,
            student1_id,
            student2_id,
            student1_task,
            student2_task,
            reward,
        ),
    )

    quest_id = cursor.lastrowid
    conn.commit()
    conn.close()

    return quest_id


def get_active_sister_quests(student_id: str) -> list:
    """Get all active sister quests for a student"""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT * FROM sister_quests 
        WHERE (student1_id = ? OR student2_id = ?)
        AND (student1_completed = 0 OR student2_completed = 0)
        ORDER BY created_at DESC
    """,
        (student_id, student_id),
    )

    quests = [dict(row) for row in cursor.fetchall()]
    conn.close()

    return quests


def complete_sister_quest_task(quest_id: int, student_id: str):
    """Mark a student's part of a sister quest as complete"""
    conn = get_connection()
    cursor = conn.cursor()

    # Check which student this is
    cursor.execute("SELECT student1_id, student2_id FROM sister_quests WHERE id = ?", (quest_id,))
    quest = cursor.fetchone()

    if quest["student1_id"] == student_id:
        cursor.execute(
            "UPDATE sister_quests SET student1_completed = 1 WHERE id = ?", (quest_id,)
        )
    elif quest["student2_id"] == student_id:
        cursor.execute(
            "UPDATE sister_quests SET student2_completed = 1 WHERE id = ?", (quest_id,)
        )

    # Check if both are complete
    cursor.execute(
        """
        SELECT student1_completed, student2_completed FROM sister_quests WHERE id = ?
    """,
        (quest_id,),
    )
    status = cursor.fetchone()

    if status["student1_completed"] and status["student2_completed"]:
        cursor.execute(
            "UPDATE sister_quests SET completed_at = ? WHERE id = ?",
            (datetime.now(), quest_id),
        )

    conn.commit()
    conn.close()


if __name__ == "__main__":
    init_parent_dashboard_tables()

