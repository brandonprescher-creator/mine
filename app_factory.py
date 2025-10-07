"""
App factory for Ultimate Tutor
Creates Flask app with proper configuration
"""

import os
from flask import Flask
from flask_socketio import SocketIO
from config import get_config
from blueprints import main_bp, api_bp, uploads_bp, games_bp
from blueprints.parent import parent_bp
from open_learning.router import bp as open_learning_bp


def create_app(test_config=None):
    """Create and configure Flask app."""
    app = Flask(__name__)

    # Load configuration
    if test_config:
        app.config.update(test_config)
    else:
        config = get_config()
        app.config.update(
            {
                "SECRET_KEY": config.SECRET_KEY,
                "UPLOAD_FOLDER": config.UPLOAD_FOLDER,
                "MAX_CONTENT_LENGTH": config.MAX_CONTENT_LENGTH,
            }
        )

    # Register blueprints
    app.register_blueprint(main_bp)
    app.register_blueprint(api_bp, url_prefix="/api")
    app.register_blueprint(uploads_bp, url_prefix="/uploads")
    app.register_blueprint(games_bp, url_prefix="/games")
    app.register_blueprint(parent_bp)
    app.register_blueprint(open_learning_bp, url_prefix="/api")

    # Initialize SocketIO
    socketio = SocketIO(app, cors_allowed_origins="*")

    return app, socketio


# For backward compatibility
def create_app_only():
    """Create app without SocketIO for testing."""
    app = Flask(__name__)

    config = get_config()
    app.config.update(
        {
            "SECRET_KEY": config.SECRET_KEY,
            "UPLOAD_FOLDER": config.UPLOAD_FOLDER,
            "MAX_CONTENT_LENGTH": config.MAX_CONTENT_LENGTH,
        }
    )

    # Register blueprints
    app.register_blueprint(main_bp)
    app.register_blueprint(api_bp, url_prefix="/api")
    app.register_blueprint(uploads_bp, url_prefix="/uploads")
    app.register_blueprint(games_bp, url_prefix="/games")
    app.register_blueprint(parent_bp)
    app.register_blueprint(open_learning_bp, url_prefix="/api")

    return app
