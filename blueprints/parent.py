"""
Parent Dashboard Blueprint
Password-protected mission control for parents
"""

from flask import Blueprint, render_template, request, jsonify, session, redirect, url_for
from functools import wraps
from parent_dashboard import parent_dashboard
from database_parent_features import (
    get_student_profile,
    create_student_profile,
    update_student_interests,
    add_parent_note,
    create_sister_quest,
    get_active_sister_quests,
    complete_sister_quest_task,
)

parent_bp = Blueprint("parent", __name__)

# Simple password protection (in production, use proper authentication)
PARENT_PASSWORD = "homeschool2024"  # Change this!


def parent_required(f):
    """Decorator to protect parent routes"""

    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get("parent_authenticated"):
            return redirect(url_for("parent.parent_login"))
        return f(*args, **kwargs)

    return decorated_function


@parent_bp.route("/parent/login", methods=["GET", "POST"])
def parent_login():
    """Parent login page"""
    if request.method == "POST":
        password = request.form.get("password")
        if password == PARENT_PASSWORD:
            session["parent_authenticated"] = True
            return redirect(url_for("parent.parent_dashboard_home"))
        else:
            return render_template("parent_login.html", error="Incorrect password")

    return render_template("parent_login.html")


@parent_bp.route("/parent/logout")
def parent_logout():
    """Parent logout"""
    session.pop("parent_authenticated", None)
    return redirect(url_for("home"))


@parent_bp.route("/parent/dashboard")
@parent_required
def parent_dashboard_home():
    """Main parent dashboard - mission control"""
    # Get both daughters' profiles (assuming you have 2 students)
    student1 = get_student_profile("student_1")
    student2 = get_student_profile("student_2")

    # Get daily digests
    digest1 = parent_dashboard.get_daily_digest("student_1") if student1 else None
    digest2 = parent_dashboard.get_daily_digest("student_2") if student2 else None

    # Get struggle alerts
    struggles1 = (
        parent_dashboard.get_struggle_recommendations("student_1") if student1 else []
    )
    struggles2 = (
        parent_dashboard.get_struggle_recommendations("student_2") if student2 else []
    )

    return render_template(
        "parent_dashboard.html",
        student1=student1,
        student2=student2,
        digest1=digest1,
        digest2=digest2,
        struggles1=struggles1,
        struggles2=struggles2,
    )


@parent_bp.route("/parent/weekly-progress/<student_id>")
@parent_required
def weekly_progress(student_id):
    """Detailed weekly progress for a student"""
    student = get_student_profile(student_id)
    progress = parent_dashboard.get_weekly_progress(student_id)

    return render_template(
        "weekly_progress.html", student=student, progress=progress
    )


@parent_bp.route("/parent/create-playlist", methods=["POST"])
@parent_required
def create_playlist():
    """Create a learning playlist"""
    data = request.json
    student_id = data.get("student_id")
    playlist_name = data.get("name")
    lesson_ids = data.get("lesson_ids", [])

    result = parent_dashboard.create_learning_playlist(
        student_id, playlist_name, lesson_ids
    )

    return jsonify(result)


@parent_bp.route("/parent/schedule-lesson", methods=["POST"])
@parent_required
def schedule_lesson():
    """Schedule a lesson for a student"""
    data = request.json
    student_id = data.get("student_id")
    lesson_id = data.get("lesson_id")
    scheduled_date = data.get("date")

    result = parent_dashboard.schedule_lesson(student_id, lesson_id, scheduled_date)

    return jsonify(result)


@parent_bp.route("/parent/update-interests", methods=["POST"])
@parent_required
def update_interests():
    """Update student interests"""
    data = request.json
    student_id = data.get("student_id")
    interests = data.get("interests", [])

    update_student_interests(student_id, interests)

    # Get new interest-based suggestions
    suggestions = parent_dashboard.get_interest_based_suggestions(
        student_id, interests
    )

    return jsonify({"success": True, "suggestions": suggestions})


@parent_bp.route("/parent/create-sister-quest", methods=["GET", "POST"])
@parent_required
def create_quest():
    """Create a collaborative sister quest"""
    if request.method == "POST":
        data = request.json
        quest_id = create_sister_quest(
            quest_name=data["quest_name"],
            description=data["description"],
            student1_id=data["student1_id"],
            student2_id=data["student2_id"],
            student1_task=data["student1_task"],
            student2_task=data["student2_task"],
            reward=data["reward"],
        )

        return jsonify({"success": True, "quest_id": quest_id})

    return render_template("create_sister_quest.html")


@parent_bp.route("/parent/sister-quests")
@parent_required
def view_sister_quests():
    """View all active sister quests"""
    quests1 = get_active_sister_quests("student_1")
    quests2 = get_active_sister_quests("student_2")

    # Combine and deduplicate (since they share quests)
    all_quests = {quest["id"]: quest for quest in quests1 + quests2}.values()

    return render_template("sister_quests_parent.html", quests=list(all_quests))


@parent_bp.route("/parent/create-reward", methods=["POST"])
@parent_required
def create_reward():
    """Create a custom reward coupon"""
    data = request.json
    student_id = data.get("student_id")
    reward_name = data.get("reward_name")
    requirement = data.get("requirement")

    result = parent_dashboard.create_reward_coupon(
        student_id, reward_name, requirement
    )

    return jsonify(result)


@parent_bp.route("/parent/add-note", methods=["POST"])
@parent_required
def add_note():
    """Add a note about a student's progress"""
    data = request.json
    student_id = data.get("student_id")
    note_text = data.get("note")
    lesson_id = data.get("lesson_id")
    note_type = data.get("type", "general")

    add_parent_note(student_id, note_text, lesson_id, note_type)

    return jsonify({"success": True})


@parent_bp.route("/parent/curriculum-planner")
@parent_required
def curriculum_planner():
    """Interactive curriculum planner with calendar"""
    from database import get_all_subjects, get_topics_by_subject

    subjects = get_all_subjects()

    return render_template("curriculum_planner.html", subjects=subjects)


@parent_bp.route("/parent/print-certificate/<student_id>/<achievement_id>")
@parent_required
def print_certificate(student_id, achievement_id):
    """Generate a printable achievement certificate"""
    from certificate_generator import generate_certificate

    student = get_student_profile(student_id)

    pdf_path = generate_certificate(
        student_name=student["name"], achievement_id=achievement_id
    )

    return jsonify({"success": True, "pdf_url": f"/certificates/{pdf_path}"})


@parent_bp.route("/parent/add-student", methods=["GET"])
@parent_required
def add_student_page():
    """Add student page"""
    return render_template("add_student.html")


@parent_bp.route("/parent/create-student", methods=["POST"])
@parent_required
def create_student_profile():
    """Create a new student profile from parent dashboard"""
    import random
    
    data = request.json
    
    # Generate unique student ID
    student_id = f"student_{random.randint(1000, 9999)}"
    
    # Create profile
    profile_id = create_student_profile(
        student_id=student_id,
        name=data["name"],
        grade_level=data["grade_level"],
        age=data["age"],
        interests=data.get("interests", []),
        learning_style=data.get("learning_style", "visual")
    )
    
    return jsonify({
        "success": True,
        "student_id": student_id,
        "profile_id": profile_id,
        "message": f"Student profile created for {data['name']}!"
    })

