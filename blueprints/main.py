"""
Main blueprint for core pages
Handles home, subjects, topics, lessons
"""

from flask import Blueprint, render_template, request, jsonify
from database import (
    get_all_subjects,
    get_topics_by_subject,
    get_lessons_by_topic,
    get_lesson_by_id,
)

main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def home():
    """Home page."""
    return render_template("home.html")


@main_bp.route("/subjects")
def subjects():
    """Subjects page."""
    subjects = get_all_subjects()
    return render_template("subjects.html", subjects=subjects)


@main_bp.route("/subject/<int:subject_id>")
def subject_topics(subject_id):
    """Topics for a subject."""
    topics = get_topics_by_subject(subject_id)
    subject = next((s for s in get_all_subjects() if s["id"] == subject_id), None)
    return render_template("topics.html", topics=topics, subject=subject)


@main_bp.route("/topic/<int:topic_id>")
def topic_lessons(topic_id):
    """Lessons for a topic."""
    lessons = get_lessons_by_topic(topic_id)
    # Get topic info
    from database import get_connection

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT t.*, s.name as subject_name 
        FROM topics t 
        JOIN subjects s ON t.subject_id = s.id 
        WHERE t.id = ?
    """,
        (topic_id,),
    )
    topic = dict(cursor.fetchone())
    conn.close()

    return render_template("lessons.html", lessons=lessons, topic=topic)


@main_bp.route("/lesson/<int:lesson_id>")
def lesson_view(lesson_id):
    """Individual lesson view."""
    lesson = get_lesson_by_id(lesson_id)
    if not lesson:
        return "Lesson not found", 404

    return render_template("lesson.html", lesson=lesson)
