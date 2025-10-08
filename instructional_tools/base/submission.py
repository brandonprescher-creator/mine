"""
Submission management for student work
"""
from datetime import datetime
from typing import Dict, List, Any, Optional
import sqlite3
import json


class SubmissionManager:
    """Manage student submissions for activities"""
    
    def __init__(self, db_path: str = 'tutor_app.db'):
        self.db_path = db_path
        self._init_tables()
    
    def _init_tables(self):
        """Initialize submission tables"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Activities table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS activities (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                tool_type TEXT NOT NULL,
                title TEXT NOT NULL,
                description TEXT,
                lesson_id INTEGER,
                config TEXT,
                created_at TEXT NOT NULL,
                FOREIGN KEY (lesson_id) REFERENCES lessons (id)
            )
        ''')
        
        # Submissions table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS submissions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                activity_id INTEGER NOT NULL,
                student_id INTEGER NOT NULL,
                work_data TEXT NOT NULL,
                submitted_at TEXT NOT NULL,
                status TEXT DEFAULT 'submitted',
                score REAL,
                feedback TEXT,
                FOREIGN KEY (activity_id) REFERENCES activities (id),
                FOREIGN KEY (student_id) REFERENCES users (id)
            )
        ''')
        
        # Teacher feedback table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS teacher_feedback (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                submission_id INTEGER NOT NULL,
                teacher_id INTEGER NOT NULL,
                comments TEXT,
                score REAL,
                rubric_data TEXT,
                created_at TEXT NOT NULL,
                FOREIGN KEY (submission_id) REFERENCES submissions (id),
                FOREIGN KEY (teacher_id) REFERENCES users (id)
            )
        ''')
        
        # Portfolio items table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS portfolio_items (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_id INTEGER NOT NULL,
                submission_id INTEGER NOT NULL,
                reflection TEXT,
                featured BOOLEAN DEFAULT 0,
                added_at TEXT NOT NULL,
                FOREIGN KEY (student_id) REFERENCES users (id),
                FOREIGN KEY (submission_id) REFERENCES submissions (id)
            )
        ''')
        
        conn.commit()
        conn.close()
    
    def create_activity(
        self,
        tool_type: str,
        title: str,
        description: str,
        lesson_id: Optional[int] = None,
        config: Optional[Dict[str, Any]] = None
    ) -> int:
        """Create a new activity"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO activities (tool_type, title, description, lesson_id, config, created_at)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (
            tool_type,
            title,
            description,
            lesson_id,
            json.dumps(config) if config else None,
            datetime.utcnow().isoformat()
        ))
        
        activity_id = cursor.lastrowid
        conn.commit()
        conn.close()
        
        return activity_id
    
    def submit_work(
        self,
        activity_id: int,
        student_id: int,
        work_data: Dict[str, Any]
    ) -> int:
        """Submit student work for an activity"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO submissions (activity_id, student_id, work_data, submitted_at, status)
            VALUES (?, ?, ?, ?, 'submitted')
        ''', (
            activity_id,
            student_id,
            json.dumps(work_data),
            datetime.utcnow().isoformat()
        ))
        
        submission_id = cursor.lastrowid
        conn.commit()
        conn.close()
        
        return submission_id
    
    def get_submission(self, submission_id: int) -> Optional[Dict[str, Any]]:
        """Get a submission by ID"""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT s.*, a.tool_type, a.title as activity_title
            FROM submissions s
            JOIN activities a ON s.activity_id = a.id
            WHERE s.id = ?
        ''', (submission_id,))
        
        row = cursor.fetchone()
        conn.close()
        
        if row:
            return {
                'id': row['id'],
                'activity_id': row['activity_id'],
                'student_id': row['student_id'],
                'work_data': json.loads(row['work_data']),
                'submitted_at': row['submitted_at'],
                'status': row['status'],
                'score': row['score'],
                'feedback': row['feedback'],
                'tool_type': row['tool_type'],
                'activity_title': row['activity_title']
            }
        
        return None
    
    def get_student_submissions(
        self,
        student_id: int,
        activity_id: Optional[int] = None
    ) -> List[Dict[str, Any]]:
        """Get all submissions for a student"""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        if activity_id:
            cursor.execute('''
                SELECT s.*, a.tool_type, a.title as activity_title
                FROM submissions s
                JOIN activities a ON s.activity_id = a.id
                WHERE s.student_id = ? AND s.activity_id = ?
                ORDER BY s.submitted_at DESC
            ''', (student_id, activity_id))
        else:
            cursor.execute('''
                SELECT s.*, a.tool_type, a.title as activity_title
                FROM submissions s
                JOIN activities a ON s.activity_id = a.id
                WHERE s.student_id = ?
                ORDER BY s.submitted_at DESC
            ''', (student_id,))
        
        rows = cursor.fetchall()
        conn.close()
        
        return [
            {
                'id': row['id'],
                'activity_id': row['activity_id'],
                'work_data': json.loads(row['work_data']),
                'submitted_at': row['submitted_at'],
                'status': row['status'],
                'score': row['score'],
                'feedback': row['feedback'],
                'tool_type': row['tool_type'],
                'activity_title': row['activity_title']
            }
            for row in rows
        ]
    
    def add_feedback(
        self,
        submission_id: int,
        teacher_id: int,
        score: Optional[float] = None,
        comments: Optional[str] = None,
        rubric_data: Optional[Dict[str, Any]] = None
    ) -> int:
        """Add teacher feedback to a submission"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Update submission
        cursor.execute('''
            UPDATE submissions
            SET score = ?, feedback = ?, status = 'graded'
            WHERE id = ?
        ''', (score, comments, submission_id))
        
        # Add feedback record
        cursor.execute('''
            INSERT INTO teacher_feedback (
                submission_id, teacher_id, comments, score, rubric_data, created_at
            )
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (
            submission_id,
            teacher_id,
            comments,
            score,
            json.dumps(rubric_data) if rubric_data else None,
            datetime.utcnow().isoformat()
        ))
        
        feedback_id = cursor.lastrowid
        conn.commit()
        conn.close()
        
        return feedback_id
    
    def add_to_portfolio(
        self,
        student_id: int,
        submission_id: int,
        reflection: Optional[str] = None,
        featured: bool = False
    ) -> int:
        """Add a submission to student's portfolio"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO portfolio_items (
                student_id, submission_id, reflection, featured, added_at
            )
            VALUES (?, ?, ?, ?, ?)
        ''', (
            student_id,
            submission_id,
            reflection,
            featured,
            datetime.utcnow().isoformat()
        ))
        
        portfolio_id = cursor.lastrowid
        conn.commit()
        conn.close()
        
        return portfolio_id
    
    def get_portfolio(self, student_id: int) -> List[Dict[str, Any]]:
        """Get student's portfolio"""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT p.*, s.work_data, a.title as activity_title, a.tool_type
            FROM portfolio_items p
            JOIN submissions s ON p.submission_id = s.id
            JOIN activities a ON s.activity_id = a.id
            WHERE p.student_id = ?
            ORDER BY p.featured DESC, p.added_at DESC
        ''', (student_id,))
        
        rows = cursor.fetchall()
        conn.close()
        
        return [
            {
                'id': row['id'],
                'submission_id': row['submission_id'],
                'reflection': row['reflection'],
                'featured': bool(row['featured']),
                'added_at': row['added_at'],
                'work_data': json.loads(row['work_data']),
                'activity_title': row['activity_title'],
                'tool_type': row['tool_type']
            }
            for row in rows
        ]


# Global instance
submission_manager = SubmissionManager()
