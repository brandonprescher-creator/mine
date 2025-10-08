"""
Assessment Blueprint - Quizzes, Exams, Grading
"""
from flask import Blueprint, render_template, request, jsonify
from flask_login import current_user
from datetime import datetime
from models.database import db, Assessment, AssessmentAttempt, ChildProfile
from services.auth.helpers import student_required, parent_required

assess_bp = Blueprint('assess', __name__, url_prefix='/assess')


@assess_bp.route('/<int:child_id>/schedule')
@parent_required
def schedule(child_id):
    """View assessment schedule"""
    child = ChildProfile.query.filter_by(id=child_id, user_id=current_user.id).first_or_404()
    assessments = Assessment.query.filter_by(child_id=child_id).order_by(Assessment.scheduled_for).all()
    return render_template('pages/assess/schedule.html', child=child, assessments=assessments)


@assess_bp.route('/attempt/<int:assessment_id>', methods=['GET', 'POST'])
@student_required
def take_assessment(assessment_id):
    """Take an assessment"""
    from flask import session
    child_id = session.get('child_id')
    
    assessment = Assessment.query.filter_by(id=assessment_id, child_id=child_id).first_or_404()
    
    if request.method == 'POST':
        data = request.json
        
        attempt = AssessmentAttempt(
            assessment_id=assessment_id,
            child_id=child_id,
            started_at=datetime.utcnow()
        )
        attempt.responses = data.get('responses', {})
        attempt.finished_at = datetime.utcnow()
        
        # Auto-grade objective items
        score = auto_grade_assessment(assessment, attempt)
        attempt.score = score
        
        db.session.add(attempt)
        db.session.commit()
        
        return jsonify({'success': True, 'attempt_id': attempt.id, 'score': score})
    
    return render_template('pages/assess/take.html', assessment=assessment)


def auto_grade_assessment(assessment, attempt):
    """Auto-grade objective items"""
    correct = 0
    total = 0
    
    for item in assessment.items:
        if item.get('type') in ['multiple_choice', 'true_false', 'short_answer']:
            total += 1
            student_answer = attempt.responses.get(str(item['id']))
            correct_answer = item.get('correct_answer')
            
            if student_answer and str(student_answer).strip().lower() == str(correct_answer).strip().lower():
                correct += 1
    
    return (correct / total * 100) if total > 0 else None
