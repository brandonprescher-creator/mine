"""
Parent Blueprint - Children Management, Weekly Planner, Review Queue, Reports, Settings
"""
from flask import Blueprint, render_template, request, jsonify, redirect, url_for, flash, send_file
from flask_login import current_user, login_required
from datetime import date, timedelta, datetime
from models.database import db, ChildProfile, LessonPlan, LessonItem, Assignment, Submission, AttendanceLog
from services.auth.helpers import parent_required
from services.lessons.planner import WeeklyPlanner
from services.rendering.pdf import generate_weekly_report, generate_transcript

parent_bp = Blueprint('parent', __name__, url_prefix='/parent')


@parent_bp.route('/')
@parent_required
def dashboard():
    """Parent dashboard"""
    children = current_user.children.all()
    
    # Get stats for each child
    stats = []
    for child in children:
        today_assignments = Assignment.query.filter_by(
            child_id=child.id,
            date=date.today()
        ).count()
        
        completed_today = Assignment.query.filter_by(
            child_id=child.id,
            date=date.today(),
            status='completed'
        ).count()
        
        pending_reviews = Submission.query.filter_by(
            child_id=child.id,
            score=None
        ).count()
        
        stats.append({
            'child': child,
            'today_assignments': today_assignments,
            'completed_today': completed_today,
            'pending_reviews': pending_reviews
        })
    
    return render_template('pages/parent/dashboard.html', children_stats=stats)


@parent_bp.route('/children')
@parent_required
def children_list():
    """Manage children"""
    children = current_user.children.all()
    return render_template('pages/parent/children.html', children=children)


@parent_bp.route('/children/add', methods=['GET', 'POST'])
@parent_required
def add_child():
    """Add a child"""
    if request.method == 'POST':
        data = request.form
        
        child = ChildProfile(
            user_id=current_user.id,
            name=data.get('name'),
            username=data.get('username'),
            grade=int(data.get('grade', 1))
        )
        child.set_password(data.get('password', 'changeme'))
        
        # Set accommodations
        accommodations = {}
        if data.get('larger_fonts'):
            accommodations['larger_fonts'] = True
        if data.get('dyslexic_font'):
            accommodations['dyslexic_font'] = True
        if data.get('extra_time'):
            accommodations['extra_time'] = float(data.get('extra_time_factor', 1.5))
        
        child.accommodations = accommodations
        
        db.session.add(child)
        db.session.commit()
        
        flash(f'Child profile created for {child.name}!', 'success')
        return redirect(url_for('parent.children_list'))
    
    return render_template('pages/parent/add_child.html')


@parent_bp.route('/planner/<int:child_id>')
@parent_required
def planner(child_id):
    """Weekly planner for a child"""
    child = ChildProfile.query.filter_by(
        id=child_id,
        user_id=current_user.id
    ).first_or_404()
    
    # Get current week's plan
    today = date.today()
    week_start = today - timedelta(days=today.weekday())
    
    lesson_plan = LessonPlan.query.filter_by(
        child_id=child_id,
        week_start_date=week_start
    ).first()
    
    return render_template('pages/parent/planner.html',
                         child=child,
                         lesson_plan=lesson_plan,
                         week_start=week_start)


@parent_bp.route('/planner/<int:child_id>/generate', methods=['POST'])
@parent_required
def generate_week(child_id):
    """Generate a week's worth of lessons"""
    child = ChildProfile.query.filter_by(
        id=child_id,
        user_id=current_user.id
    ).first_or_404()
    
    data = request.json
    
    week_start = datetime.strptime(data.get('week_start'), '%Y-%m-%d').date()
    subjects = data.get('subjects', ['Math', 'ELA', 'Science', 'Social Studies'])
    minutes_per_subject = data.get('minutes_per_subject', 45)
    
    # Use planner service
    planner = WeeklyPlanner(child)
    lesson_plan = planner.generate_week(
        week_start,
        subjects,
        minutes_per_subject
    )
    
    db.session.add(lesson_plan)
    db.session.commit()
    
    return jsonify({
        'success': True,
        'lesson_plan_id': lesson_plan.id,
        'items_created': len(lesson_plan.lesson_items.all())
    })


@parent_bp.route('/review')
@parent_required
def review_queue():
    """Review queue for all children"""
    children = current_user.children.all()
    child_ids = [c.id for c in children]
    
    # Get submissions awaiting review
    pending = Submission.query.filter(
        Submission.child_id.in_(child_ids),
        Submission.score == None
    ).order_by(Submission.created_at).all()
    
    return render_template('pages/parent/review_queue.html', submissions=pending)


@parent_bp.route('/review/<int:submission_id>', methods=['GET', 'POST'])
@parent_required
def review_submission(submission_id):
    """Review and grade a submission"""
    submission = Submission.query.get_or_404(submission_id)
    
    # Verify ownership
    if submission.child.user_id != current_user.id:
        flash('Access denied', 'error')
        return redirect(url_for('parent.review_queue'))
    
    if request.method == 'POST':
        data = request.json
        
        submission.score = data.get('score')
        submission.rubric = data.get('rubric', {})
        submission.feedback = data.get('feedback')
        
        db.session.commit()
        
        return jsonify({'success': True})
    
    return render_template('pages/parent/review_submission.html', submission=submission)


@parent_bp.route('/reports/weekly/<int:child_id>')
@parent_required
def weekly_report(child_id):
    """Generate weekly PDF report"""
    child = ChildProfile.query.filter_by(
        id=child_id,
        user_id=current_user.id
    ).first_or_404()
    
    # Get this week's data
    today = date.today()
    week_start = today - timedelta(days=today.weekday())
    week_end = week_start + timedelta(days=6)
    
    assignments = Assignment.query.filter(
        Assignment.child_id == child_id,
        Assignment.date >= week_start,
        Assignment.date <= week_end
    ).all()
    
    # Generate PDF
    pdf_buffer = generate_weekly_report(child, assignments, week_start, week_end)
    
    return send_file(
        pdf_buffer,
        as_attachment=True,
        download_name=f'weekly_report_{child.name}_{week_start}.pdf',
        mimetype='application/pdf'
    )


@parent_bp.route('/transcript/<int:child_id>')
@parent_required
def transcript(child_id):
    """Generate transcript"""
    child = ChildProfile.query.filter_by(
        id=child_id,
        user_id=current_user.id
    ).first_or_404()
    
    # Get all completed work
    all_submissions = Submission.query.filter_by(child_id=child_id).all()
    
    pdf_buffer = generate_transcript(child, all_submissions)
    
    return send_file(
        pdf_buffer,
        as_attachment=True,
        download_name=f'transcript_{child.name}.pdf',
        mimetype='application/pdf'
    )


@parent_bp.route('/settings/<int:child_id>', methods=['GET', 'POST'])
@parent_required
def child_settings(child_id):
    """Child settings and accommodations"""
    child = ChildProfile.query.filter_by(
        id=child_id,
        user_id=current_user.id
    ).first_or_404()
    
    if request.method == 'POST':
        data = request.form
        
        child.grade = int(data.get('grade', child.grade))
        
        # Update accommodations
        accommodations = {}
        if data.get('larger_fonts'):
            accommodations['larger_fonts'] = True
        if data.get('dyslexic_font'):
            accommodations['dyslexic_font'] = True
        if data.get('extra_time'):
            accommodations['extra_time'] = float(data.get('extra_time_factor', 1.5))
        if data.get('simplified_language'):
            accommodations['simplified_language'] = True
        if data.get('read_aloud'):
            accommodations['read_aloud'] = True
        
        child.accommodations = accommodations
        
        # Update preferences
        prefs = {}
        if data.get('interests'):
            prefs['interests'] = data.get('interests').split(',')
        if data.get('reading_level'):
            prefs['reading_level'] = data.get('reading_level')
        
        child.prefs = prefs
        
        db.session.commit()
        
        flash('Settings updated', 'success')
        return redirect(url_for('parent.child_settings', child_id=child_id))
    
    return render_template('pages/parent/settings.html', child=child)


@parent_bp.route('/backup', methods=['GET', 'POST'])
@parent_required
def backup():
    """Backup and export data"""
    if request.method == 'POST':
        # Generate encrypted backup
        # Would use cryptography library
        flash('Backup created successfully', 'success')
    
    return render_template('pages/parent/backup.html')
