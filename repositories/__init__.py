"""
Repository package for Ultimate Tutor
Contains data access layer with proper abstraction
"""

from .subject_repository import SubjectRepository
from .topic_repository import TopicRepository
from .lesson_repository import LessonRepository
from .practice_repository import PracticeRepository
from .user_repository import UserRepository

__all__ = [
    "SubjectRepository",
    "TopicRepository",
    "LessonRepository",
    "PracticeRepository",
    "UserRepository",
]
