"""
API blueprint for Ultimate Tutor
Handles all API endpoints
"""

from flask import Blueprint, request, jsonify
from database import (
    get_all_subjects,
    get_topics_by_subject,
    get_lessons_by_topic,
    get_lesson_by_id,
    get_practice_problems_by_topic,
)
from worksheet_generator_api import generate_worksheet, generate_worksheet_pack
from visual_content_generator import generate_visual_content
from MEGA_AI_TUTOR import MegaAITutor
from personalized_learning import create_student_path

api_bp = Blueprint("api", __name__)


@api_bp.route("/subjects")
def api_subjects():
    """Get all subjects."""
    subjects = get_all_subjects()
    return jsonify(subjects)


@api_bp.route("/subjects/<int:subject_id>/topics")
def api_subject_topics(subject_id):
    """Get topics for a subject."""
    topics = get_topics_by_subject(subject_id)
    return jsonify(topics)


@api_bp.route("/topics/<int:topic_id>/lessons")
def api_topic_lessons(topic_id):
    """Get lessons for a topic."""
    lessons = get_lessons_by_topic(topic_id)
    return jsonify(lessons)


@api_bp.route("/lessons/<int:lesson_id>")
def api_lesson(lesson_id):
    """Get a specific lesson."""
    lesson = get_lesson_by_id(lesson_id)
    if not lesson:
        return jsonify({"error": "Lesson not found"}), 404
    return jsonify(lesson)


@api_bp.route("/topics/<int:topic_id>/practice")
def api_topic_practice(topic_id):
    """Get practice problems for a topic."""
    problems = get_practice_problems_by_topic(topic_id)
    return jsonify(problems)


@api_bp.route("/generate/visuals/<int:lesson_id>")
def api_generate_visuals(lesson_id):
    """Generate visual content for a lesson."""
    try:
        lesson = get_lesson_by_id(lesson_id)
        if not lesson:
            return jsonify({"error": "Lesson not found"}), 404

        visuals = generate_visual_content(lesson)
        return jsonify({"success": True, "visuals": visuals})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@api_bp.route("/generate/worksheet", methods=["POST"])
def api_generate_worksheet():
    """Generate a worksheet."""
    try:
        data = request.get_json()
        topic = data.get("topic", "Math")
        subject = data.get("subject", "Mathematics")
        grade = data.get("grade", "3rd")
        num_problems = data.get("num_problems", 10)

        worksheet = generate_worksheet(topic, subject, grade, num_problems)
        return jsonify({"success": True, "worksheet": worksheet})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@api_bp.route("/generate/worksheet-pack/<grade>/<subject>")
def api_generate_worksheet_pack(grade, subject):
    """Generate a worksheet pack."""
    try:
        pack = generate_worksheet_pack(grade, subject)
        return jsonify({"success": True, "pack": pack})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@api_bp.route("/user/stats")
def api_user_stats():
    """Get user statistics."""
    # TODO: Implement user stats
    return jsonify(
        {"lessons_completed": 0, "practice_score": 0, "achievements": [], "streak": 0}
    )


@api_bp.route("/leaderboard")
def api_leaderboard():
    """Get leaderboard data."""
    # TODO: Implement leaderboard
    return jsonify({"top_learners": [], "recent_achievements": []})


@api_bp.route("/ask-tutor", methods=["POST"])
def api_ask_tutor():
    """Ask the AI tutor a question."""
    try:
        data = request.get_json()
        question = data.get("question", "")
        context = data.get("context", {})

        tutor = MegaAITutor()
        response = tutor.answer_question(question, context)

        return jsonify({"success": True, "response": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@api_bp.route("/create-learning-path", methods=["POST"])
def api_create_learning_path():
    """Create a personalized learning path."""
    try:
        data = request.get_json()
        student_profile = data.get("profile", {})
        goals = data.get("goals", [])

        path = create_student_path(student_profile)

        return jsonify({"success": True, "learning_path": path})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@api_bp.route("/study-plan/<topic>/<time>/<level>")
def api_study_plan(topic, time, level):
    """Generate a study plan."""
    try:
        # TODO: Implement study plan generation
        plan = {
            "topic": topic,
            "time_available": time,
            "level": level,
            "sessions": [],
            "goals": [],
        }

        return jsonify({"success": True, "plan": plan})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@api_bp.route("/tutor/conversation-history")
def api_tutor_history():
    """Get tutor conversation history."""
    # TODO: Implement conversation history
    return jsonify({"conversations": [], "total_questions": 0})
