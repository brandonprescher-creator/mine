"""
Student Blueprint - Today, Lessons, Practice, Notebooks, Portfolio, Badges
"""
from flask import Blueprint, render_template, request, jsonify, session, redirect, url_for, flash
from datetime import date, datetime
from models.database import db, ChildProfile, Assignment, Submission, NotebookEntry, PortfolioItem, TimeOnTask
from services.auth.helpers import student_required

student_bp = Blueprint('student', __name__, url_prefix='/student')


@student_bp.route('/')
@student_required
def today():
    """Today's assignments and tasks"""
    child_id = session.get('child_id')
    child = ChildProfile.query.get_or_404(child_id)
    
    # Get today's assignments
    today = date.today()
    assignments = Assignment.query.filter_by(
        child_id=child_id,
        date=today
    ).order_by(Assignment.lesson_item_id).all()
    
    # Calculate time spent today
    total_minutes = sum(
        sum(t.seconds_active for t in a.time_entries) // 60 
        for a in assignments
    )
    
    return render_template('pages/student/today.html',
                         child=child,
                         assignments=assignments,
                         total_minutes=total_minutes)


@student_bp.route('/assignment/<int:assignment_id>')
@student_required
def assignment_detail(assignment_id):
    """Work on a specific assignment"""
    child_id = session.get('child_id')
    assignment = Assignment.query.filter_by(
        id=assignment_id,
        child_id=child_id
    ).first_or_404()
    
    # Mark as started
    if not assignment.started_at:
        assignment.started_at = datetime.utcnow()
        assignment.status = 'in_progress'
        db.session.commit()
    
    return render_template('pages/student/assignment.html', assignment=assignment)


@student_bp.route('/assignment/<int:assignment_id>/submit', methods=['POST'])
@student_required
def submit_assignment(assignment_id):
    """Submit assignment work"""
    child_id = session.get('child_id')
    assignment = Assignment.query.filter_by(
        id=assignment_id,
        child_id=child_id
    ).first_or_404()
    
    data = request.json
    
    # Create submission
    submission = Submission(
        assignment_id=assignment_id,
        child_id=child_id
    )
    submission.artifacts = data.get('artifacts', {})
    
    db.session.add(submission)
    
    # Mark assignment complete
    assignment.status = 'completed'
    assignment.completed_at = datetime.utcnow()
    
    db.session.commit()
    
    return jsonify({
        'success': True,
        'submission_id': submission.id,
        'message': 'Great work! Assignment submitted.'
    })


@student_bp.route('/notebook')
@student_required
def notebook():
    """Student's daily notebook"""
    child_id = session.get('child_id')
    
    entries = NotebookEntry.query.filter_by(
        child_id=child_id
    ).order_by(NotebookEntry.date.desc()).limit(30).all()
    
    return render_template('pages/student/notebook.html', entries=entries)


@student_bp.route('/notebook/entry', methods=['POST'])
@student_required
def save_notebook_entry():
    """Save notebook entry"""
    child_id = session.get('child_id')
    data = request.json
    
    entry = NotebookEntry(
        child_id=child_id,
        date=data.get('date', date.today()),
        content_text=data.get('content_text'),
        canvas_svg=data.get('canvas_svg')
    )
    entry.attachments = data.get('attachments', [])
    
    db.session.add(entry)
    db.session.commit()
    
    return jsonify({'success': True, 'entry_id': entry.id})


@student_bp.route('/portfolio')
@student_required
def portfolio():
    """Student portfolio"""
    child_id = session.get('child_id')
    
    items = PortfolioItem.query.filter_by(
        child_id=child_id
    ).order_by(PortfolioItem.created_at.desc()).all()
    
    return render_template('pages/student/portfolio.html', items=items)


@student_bp.route('/badges')
@student_required
def badges():
    """Achievement badges"""
    child_id = session.get('child_id')
    child = ChildProfile.query.get_or_404(child_id)
    
    # Calculate achievements
    total_assignments = Assignment.query.filter_by(child_id=child_id, status='completed').count()
    total_submissions = Submission.query.filter_by(child_id=child_id).count()
    
    return render_template('pages/student/badges.html',
                         child=child,
                         total_assignments=total_assignments,
                         total_submissions=total_submissions)
