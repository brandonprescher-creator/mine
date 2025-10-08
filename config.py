"""
Application Configuration
Environment-based settings for all deployment scenarios
"""
import os
from datetime import timedelta


class Config:
    """Base configuration"""
    
    # Flask Core
    SECRET_KEY = os.getenv('SECRET_KEY', 'change-this-in-production-please')
    DEBUG = False
    TESTING = False
    
    # Database
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///tutor_platform.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
    
    # Redis & Background Tasks
    REDIS_URL = os.getenv('REDIS_URL', 'redis://localhost:6379/0')
    RQ_REDIS_URL = REDIS_URL
    
    # Session
    SESSION_TYPE = 'filesystem'
    PERMANENT_SESSION_LIFETIME = timedelta(days=7)
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'
    
    # Security
    WTF_CSRF_ENABLED = True
    WTF_CSRF_TIME_LIMIT = None
    BCRYPT_LOG_ROUNDS = 12
    
    # Rate Limiting
    RATELIMIT_STORAGE_URL = REDIS_URL
    RATELIMIT_DEFAULT = "200 per day;50 per hour"
    RATELIMIT_LOGIN = "5 per minute"
    
    # File Upload
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB
    UPLOAD_FOLDER = os.path.join('static', 'uploads')
    ALLOWED_EXTENSIONS = {'pdf', 'doc', 'docx', 'txt', 'png', 'jpg', 'jpeg', 'gif', 'mp3', 'mp4', 'wav'}
    
    # Mail (for password reset)
    MAIL_SERVER = os.getenv('MAIL_SERVER', 'smtp.gmail.com')
    MAIL_PORT = int(os.getenv('MAIL_PORT', 587))
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = os.getenv('MAIL_DEFAULT_SENDER', 'noreply@ultimatetutor.com')
    
    # PWA
    PWA_CACHE_VERSION = 'v1'
    PWA_OFFLINE_DAYS = 7
    
    # Content Security
    CONTENT_SECURITY_POLICY = {
        'default-src': "'self'",
        'script-src': ["'self'", "'unsafe-inline'", "cdn.tailwindcss.com", "cdn.jsdelivr.net", "cdn.socket.io", "cdnjs.cloudflare.com"],
        'style-src': ["'self'", "'unsafe-inline'", "fonts.googleapis.com", "cdnjs.cloudflare.com"],
        'font-src': ["'self'", "fonts.gstatic.com", "cdnjs.cloudflare.com"],
        'img-src': ["'self'", "data:", "https:"],
        'connect-src': ["'self'", "https:"],
        'frame-src': ["'self'", "https://phet.colorado.edu", "https://www.youtube.com"],
    }
    
    # Feature Flags
    ENABLE_OAUTH = os.getenv('ENABLE_OAUTH', 'false').lower() == 'true'
    ENABLE_S3_STORAGE = os.getenv('ENABLE_S3_STORAGE', 'false').lower() == 'true'
    ENABLE_EMAIL = os.getenv('ENABLE_EMAIL', 'false').lower() == 'true'
    
    # Homeschool Settings
    DEFAULT_SUBJECTS = ['Math', 'English Language Arts', 'Science', 'Social Studies', 'Arts', 'Physical Education']
    DEFAULT_MINUTES_PER_SUBJECT = 45
    DEFAULT_SCHOOL_DAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    
    # Mastery Settings
    MASTERY_THRESHOLDS = {
        'not_attempted': 0,
        'in_progress': 1,
        'proficient': 3,
        'mastered': 5
    }
    SPACED_INTERVALS = [1, 3, 7, 14, 30]  # Days between reviews
    
    # Assessment
    AUTO_GRADE_TOLERANCE = 0.1  # 10% similarity tolerance for numeric answers
    PASSING_GRADE = 70.0


class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True
    SQLALCHEMY_ECHO = True
    SESSION_COOKIE_SECURE = False


class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False
    TESTING = False
    SESSION_COOKIE_SECURE = True
    
    # Stronger security in production
    BCRYPT_LOG_ROUNDS = 13
    
    # Production database (PostgreSQL)
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://user:pass@localhost/tutor_prod')
    
    # Force HTTPS
    PREFERRED_URL_SCHEME = 'https'


class TestingConfig(Config):
    """Testing configuration"""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
    WTF_CSRF_ENABLED = False
    RATELIMIT_ENABLED = False


# Config dictionary
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}


def get_config(env=None):
    """Get configuration based on environment"""
    if env is None:
        env = os.getenv('FLASK_ENV', 'development')
    return config.get(env, config['default'])