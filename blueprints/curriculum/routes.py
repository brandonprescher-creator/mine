"""
Curriculum Blueprint - Grade/Subject/Topic Browser, Standards Map
"""
from flask import Blueprint, render_template, request, jsonify
from models.database import db, Standard, Skill
from sqlalchemy import func

curriculum_bp = Blueprint('curriculum', __name__, url_prefix='/curriculum')


@curriculum_bp.route('/')
def index():
    """Curriculum browser home"""
    # Get available grades and subjects
    grades = db.session.query(Standard.grade).distinct().order_by(Standard.grade).all()
    subjects = db.session.query(Standard.subject).distinct().order_by(Standard.subject).all()
    
    return render_template('pages/curriculum/index.html',
                         grades=[g[0] for g in grades],
                         subjects=[s[0] for s in subjects])


@curriculum_bp.route('/grade/<int:grade>')
def by_grade(grade):
    """View curriculum for a grade"""
    standards = Standard.query.filter_by(grade=grade).all()
    
    # Group by subject
    by_subject = {}
    for standard in standards:
        if standard.subject not in by_subject:
            by_subject[standard.subject] = []
        by_subject[standard.subject].append(standard)
    
    return render_template('pages/curriculum/grade.html', grade=grade, by_subject=by_subject)


@curriculum_bp.route('/standard/<int:standard_id>')
def standard_detail(standard_id):
    """View standard details and skills"""
    standard = Standard.query.get_or_404(standard_id)
    skills = standard.skills.all()
    
    return render_template('pages/curriculum/standard.html', standard=standard, skills=skills)
