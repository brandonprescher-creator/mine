"""
Configuration management for Ultimate Tutor
Handles environment variables and settings
"""

import os
from typing import Optional
from dataclasses import dataclass


@dataclass
class Config:
    """Base configuration class."""

    SECRET_KEY: str
    DATABASE_URL: str = "tutor_app.db"
    UPLOAD_FOLDER: str = "uploads"
    MAX_CONTENT_LENGTH: int = 16 * 1024 * 1024  # 16MB
    ALLOWED_EXTENSIONS: set = None

    # API Keys (optional)
    OPENAI_API_KEY: Optional[str] = None
    NASA_API_KEY: Optional[str] = None

    # Redis for session management
    REDIS_URL: Optional[str] = None

    def __post_init__(self):
        if self.ALLOWED_EXTENSIONS is None:
            self.ALLOWED_EXTENSIONS = {
                "txt",
                "pdf",
                "png",
                "jpg",
                "jpeg",
                "gif",
                "docx",
            }


class DevelopmentConfig(Config):
    """Development configuration."""

    DEBUG = True
    TESTING = False


class ProductionConfig(Config):
    """Production configuration."""

    DEBUG = False
    TESTING = False


class TestingConfig(Config):
    """Testing configuration."""

    DEBUG = True
    TESTING = True
    DATABASE_URL = ":memory:"


def get_config() -> Config:
    """Get configuration based on environment."""
    env = os.getenv("FLASK_ENV", "development").lower()

    if env == "production":
        return ProductionConfig(
            SECRET_KEY=os.getenv("SECRET_KEY", "dev-secret-key-change-in-production"),
            DATABASE_URL=os.getenv("DATABASE_URL", "tutor_app.db"),
            UPLOAD_FOLDER=os.getenv("UPLOAD_FOLDER", "uploads"),
            REDIS_URL=os.getenv("REDIS_URL"),
            OPENAI_API_KEY=os.getenv("OPENAI_API_KEY"),
            NASA_API_KEY=os.getenv("NASA_API_KEY"),
        )
    elif env == "testing":
        return TestingConfig(SECRET_KEY="test-secret-key")
    else:
        return DevelopmentConfig(
            SECRET_KEY=os.getenv("SECRET_KEY", "dev-secret-key"),
            DATABASE_URL=os.getenv("DATABASE_URL", "tutor_app.db"),
            UPLOAD_FOLDER=os.getenv("UPLOAD_FOLDER", "uploads"),
            REDIS_URL=os.getenv("REDIS_URL"),
            OPENAI_API_KEY=os.getenv("OPENAI_API_KEY"),
            NASA_API_KEY=os.getenv("NASA_API_KEY"),
        )
