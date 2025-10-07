"""
Blueprints package for Ultimate Tutor
Contains modular route handlers
"""

from .main import main_bp
from .api import api_bp
from .uploads import uploads_bp
from .games import games_bp

__all__ = ["main_bp", "api_bp", "uploads_bp", "games_bp"]
