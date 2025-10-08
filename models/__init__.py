"""
Database models for the Ultimate Tutor Platform
"""
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import sqlite3

class User(UserMixin):
    """User model for authentication"""
    
    def __init__(self, id, username, email, role, created_at=None):
        self.id = id
        self.username = username
        self.email = email
        self.role = role  # 'student', 'teacher', 'parent', 'admin'
        self.created_at = created_at or datetime.utcnow()
    
    @staticmethod
    def get(user_id, db_path='tutor_app.db'):
        """Get user by ID"""
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM users WHERE id = ?', (user_id,))
        row = cursor.fetchone()
        conn.close()
        
        if row:
            return User(
                id=row['id'],
                username=row['username'],
                email=row['email'],
                role=row['role'],
                created_at=row['created_at']
            )
        return None
    
    @staticmethod
    def get_by_username(username, db_path='tutor_app.db'):
        """Get user by username"""
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
        row = cursor.fetchone()
        conn.close()
        
        if row:
            return User(
                id=row['id'],
                username=row['username'],
                email=row['email'],
                role=row['role'],
                created_at=row['created_at']
            )
        return None
    
    @staticmethod
    def get_by_email(email, db_path='tutor_app.db'):
        """Get user by email"""
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM users WHERE email = ?', (email,))
        row = cursor.fetchone()
        conn.close()
        
        if row:
            return User(
                id=row['id'],
                username=row['username'],
                email=row['email'],
                role=row['role'],
                created_at=row['created_at']
            )
        return None
    
    @staticmethod
    def create(username, email, password, role='student', db_path='tutor_app.db'):
        """Create a new user"""
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        password_hash = generate_password_hash(password)
        created_at = datetime.utcnow().isoformat()
        
        try:
            cursor.execute('''
                INSERT INTO users (username, email, password_hash, role, created_at)
                VALUES (?, ?, ?, ?, ?)
            ''', (username, email, password_hash, role, created_at))
            
            user_id = cursor.lastrowid
            conn.commit()
            conn.close()
            
            return User(id=user_id, username=username, email=email, role=role, created_at=created_at)
        except sqlite3.IntegrityError:
            conn.close()
            return None
    
    @staticmethod
    def verify_password(username, password, db_path='tutor_app.db'):
        """Verify user password"""
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        cursor.execute('SELECT password_hash FROM users WHERE username = ?', (username,))
        row = cursor.fetchone()
        conn.close()
        
        if row and check_password_hash(row[0], password):
            return True
        return False
    
    def to_dict(self):
        """Convert user to dictionary"""
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'role': self.role,
            'created_at': self.created_at
        }


def init_auth_tables(db_path='tutor_app.db'):
    """Initialize authentication tables"""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            role TEXT NOT NULL DEFAULT 'student',
            created_at TEXT NOT NULL,
            last_login TEXT
        )
    ''')
    
    # User profiles table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user_profiles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            first_name TEXT,
            last_name TEXT,
            grade_level INTEGER,
            avatar_url TEXT,
            bio TEXT,
            preferences TEXT,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    ''')
    
    # Parent-student relationships
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS parent_students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            parent_id INTEGER NOT NULL,
            student_id INTEGER NOT NULL,
            relationship TEXT,
            created_at TEXT NOT NULL,
            FOREIGN KEY (parent_id) REFERENCES users (id),
            FOREIGN KEY (student_id) REFERENCES users (id)
        )
    ''')
    
    # Teacher-student relationships
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS teacher_students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            teacher_id INTEGER NOT NULL,
            student_id INTEGER NOT NULL,
            subject TEXT,
            created_at TEXT NOT NULL,
            FOREIGN KEY (teacher_id) REFERENCES users (id),
            FOREIGN KEY (student_id) REFERENCES users (id)
        )
    ''')
    
    conn.commit()
    conn.close()
