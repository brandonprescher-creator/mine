"""
Ultimate Tutor Platform - Professional Flask Application
Comprehensive K-12 education platform with modern architecture
"""

from flask import Flask, render_template, request, jsonify, flash, redirect, url_for
from flask_login import LoginManager, login_required, current_user
from flask_socketio import SocketIO
import os
from datetime import datetime

# Initialize Flask app
app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "change-this-secret-key-in-production")
app.config["DATABASE_URL"] = os.getenv("DATABASE_URL", "tutor_app.db")
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024  # 16MB max file size

# Initialize extensions
socketio = SocketIO(app, cors_allowed_origins="*")
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'
login_manager.login_message = 'Please log in to access this page'
login_manager.login_message_category = 'info'

# Import models and initialize auth tables
from models import User, init_auth_tables

# Import database functions
from database import (
    init_database,
    get_all_subjects,
    get_topics_by_subject,
    get_lessons_by_topic,
    get_lesson_by_id,
    get_practice_problems_by_lesson,
    record_practice_attempt,
    get_lesson_progress,
    get_overall_progress,
    get_topic_by_id,
    get_subject_by_id,
)
from curriculum_data import seed_curriculum

# User loader for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

# Initialize database
_database_initialized = False

def initialize_database():
    """Initialize database and auth tables"""
    global _database_initialized
    if _database_initialized:
        return
    init_database()
    init_auth_tables()
    seed_curriculum()
    _database_initialized = True

@app.before_request
def ensure_database_ready():
    """Ensure database is ready before handling requests"""
    if not app.config.get("TESTING"):
        initialize_database()

# Register blueprints
from auth import auth_bp
from blueprints.parent import parent_bp
from blueprints.activities import activities_bp
from open_learning.router import bp as open_learning_bp

app.register_blueprint(auth_bp)
app.register_blueprint(parent_bp)
app.register_blueprint(activities_bp)
app.register_blueprint(open_learning_bp)

# Error handlers
@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('errors/500.html'), 500

# Main routes
@app.route("/")
def home():
    """Home page"""
    return render_template("home.html")

@app.route("/subjects")
def subjects():
    """Subjects page"""
    subjects = get_all_subjects()
    return render_template("subjects.html", subjects=subjects)

@app.route("/subject/<int:subject_id>")
def subject_topics(subject_id):
    """Topics for a specific subject"""
    subject = get_subject_by_id(subject_id)
    if not subject:
        flash("Subject not found", "error")
        return redirect(url_for("subjects"))
    
    topics = get_topics_by_subject(subject_id)
    return render_template("topics.html", subject=subject, topics=topics)

@app.route("/topic/<int:topic_id>")
def topic_lessons(topic_id):
    """Lessons for a specific topic"""
    topic = get_topic_by_id(topic_id)
    if not topic:
        flash("Topic not found", "error")
        return redirect(url_for("subjects"))
    
    lessons = get_lessons_by_topic(topic_id)
    return render_template("lessons.html", topic=topic, lessons=lessons)

@app.route("/lesson/<int:lesson_id>")
def lesson_view(lesson_id):
    """Individual lesson view"""
    lesson = get_lesson_by_id(lesson_id)
    if not lesson:
        flash("Lesson not found", "error")
        return redirect(url_for("subjects"))
    
    return render_template("lesson.html", lesson=lesson)

@app.route("/practice/<int:lesson_id>")
@login_required
def practice_view(lesson_id):
    """Practice mode"""
    lesson = get_lesson_by_id(lesson_id)
    if not lesson:
        flash("Lesson not found", "error")
        return redirect(url_for("subjects"))
    
    problems = get_practice_problems_by_lesson(lesson_id)
    return render_template("practice.html", lesson=lesson, problems=problems)

@app.route("/games")
def games():
    """Games hub"""
    return render_template("games.html")

@app.route("/achievements")
@login_required
def achievements():
    """Achievements page"""
    progress = get_overall_progress()
    return render_template("achievements.html", progress=progress)

@app.route("/upload")
def upload_page():
    """Upload page"""
    return render_template("upload.html")

@app.route("/worksheets")
def worksheets_page():
    """Worksheet generator"""
    return render_template("worksheets.html")

@app.route("/api-explorer")
def api_explorer():
    """API explorer directory"""
    return render_template("api_directory.html")

@app.route("/books-reader")
def books_reader():
    """Books reader"""
    return render_template("books_reader.html")

# API Routes
@app.route("/api/subjects")
def api_subjects():
    """Get all subjects"""
    subjects = get_all_subjects()
    return jsonify(subjects)

@app.route("/api/subject/<int:subject_id>/topics")
def api_subject_topics(subject_id):
    """Get topics for a subject"""
    topics = get_topics_by_subject(subject_id)
    return jsonify(topics)

@app.route("/api/topic/<int:topic_id>/lessons")
def api_topic_lessons(topic_id):
    """Get lessons for a topic"""
    lessons = get_lessons_by_topic(topic_id)
    return jsonify(lessons)

@app.route("/api/lesson/<int:lesson_id>")
def api_lesson(lesson_id):
    """Get a specific lesson"""
    lesson = get_lesson_by_id(lesson_id)
    if not lesson:
        return jsonify({"error": "Lesson not found"}), 404
    return jsonify(lesson)

@app.route("/api/lesson/<int:lesson_id>/problems")
def api_lesson_problems(lesson_id):
    """Get practice problems for a lesson"""
    problems = get_practice_problems_by_lesson(lesson_id)
    return jsonify(problems)

@app.route("/api/submit_answer", methods=["POST"])
@login_required
def submit_answer():
    """Submit answer for practice problem"""
    data = request.json
    lesson_id = data.get("lesson_id")
    problem_id = data.get("problem_id")
    answer = data.get("answer")
    
    problems = get_practice_problems_by_lesson(lesson_id)
    problem = next((p for p in problems if p["id"] == problem_id), None)
    
    if not problem:
        return jsonify({"error": "Problem not found"}), 404
    
    is_correct = answer.strip().lower() == problem["answer"].strip().lower()
    record_practice_attempt(lesson_id, problem_id, is_correct)
    
    return jsonify({
        "correct": is_correct,
        "correct_answer": problem["answer"],
        "feedback": "Excellent work!" if is_correct else "Try again!",
    })

@app.route("/api/user/stats")
def get_user_stats():
    """Get user statistics"""
    progress = get_overall_progress()
    return jsonify({
        "lessons": progress.get("lessons_started", 0),
        "problems": progress.get("problems_mastered", 0),
        "achievements": 0,
        "streak": 0,
    })

# Context processor for templates
@app.context_processor
def inject_user():
    """Inject current user into all templates"""
    return dict(current_user=current_user)

def create_app(config_override=None):
    """Application factory"""
    if config_override:
        app.config.update(config_override)
    return app

if __name__ == "__main__":
    with app.app_context():
        initialize_database()
    socketio.run(app, debug=True, host="0.0.0.0", port=5001)
