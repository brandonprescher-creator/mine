"""
Activities Blueprint
Handles instructional tool activities
"""
from flask import Blueprint, render_template, request, jsonify, redirect, url_for, flash
from flask_login import login_required, current_user

from instructional_tools.cross_curricular.work_notebook import WorkNotebook
from instructional_tools.base.submission import submission_manager

activities_bp = Blueprint('activities', __name__, url_prefix='/activity')


@activities_bp.route('/')
@login_required
def list_activities():
    """List all available activities"""
    # TODO: Get activities from database
    return render_template('activities/list.html')


@activities_bp.route('/work-notebook/<int:activity_id>')
@login_required
def work_notebook(activity_id):
    """Show Your Work Notebook activity"""
    # In a real app, load from database
    # For now, create a sample activity
    activity = {
        'id': activity_id,
        'title': 'Show Your Work',
        'description': 'Upload photos, type solutions, or draw your work to show your problem-solving process.',
        'type': 'work_notebook'
    }
    
    return render_template('activities/work_notebook.html', activity=activity)


@activities_bp.route('/api/submit/work-notebook', methods=['POST'])
@login_required
def submit_work_notebook():
    """Submit work notebook activity"""
    try:
        data = request.json
        activity_id = data.get('activity_id')
        
        if not activity_id:
            return jsonify({'error': 'Activity ID required'}), 400
        
        # Create work notebook instance
        work_notebook = WorkNotebook(
            activity_id=activity_id,
            title='Show Your Work',
            description='Student work submission'
        )
        
        # Validate submission
        is_valid, errors = work_notebook.validate_submission(data)
        
        if not is_valid:
            return jsonify({'error': 'Validation failed', 'details': errors}), 400
        
        # Auto-grade for initial feedback
        grading_result = work_notebook.auto_grade(data)
        
        # Save submission to database
        submission_id = submission_manager.submit_work(
            activity_id=activity_id,
            student_id=current_user.id,
            work_data=data
        )
        
        return jsonify({
            'success': True,
            'submission_id': submission_id,
            'feedback': grading_result['feedback'],
            'completion_score': grading_result['completion_score']
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@activities_bp.route('/my-work')
@login_required
def my_work():
    """View student's submitted work"""
    submissions = submission_manager.get_student_submissions(current_user.id)
    return render_template('activities/my_work.html', submissions=submissions)


@activities_bp.route('/submission/<int:submission_id>')
@login_required
def view_submission(submission_id):
    """View a specific submission"""
    submission = submission_manager.get_submission(submission_id)
    
    if not submission:
        flash('Submission not found', 'error')
        return redirect(url_for('activities.my_work'))
    
    # Check authorization
    if submission['student_id'] != current_user.id and current_user.role not in ['teacher', 'admin']:
        flash('Access denied', 'error')
        return redirect(url_for('activities.my_work'))
    
    return render_template('activities/view_submission.html', submission=submission)


@activities_bp.route('/portfolio')
@login_required
def portfolio():
    """View student portfolio"""
    portfolio_items = submission_manager.get_portfolio(current_user.id)
    return render_template('activities/portfolio.html', portfolio=portfolio_items)


@activities_bp.route('/api/add-to-portfolio', methods=['POST'])
@login_required
def add_to_portfolio():
    """Add a submission to portfolio"""
    try:
        data = request.json
        submission_id = data.get('submission_id')
        reflection = data.get('reflection', '')
        featured = data.get('featured', False)
        
        if not submission_id:
            return jsonify({'error': 'Submission ID required'}), 400
        
        portfolio_id = submission_manager.add_to_portfolio(
            student_id=current_user.id,
            submission_id=submission_id,
            reflection=reflection,
            featured=featured
        )
        
        return jsonify({'success': True, 'portfolio_id': portfolio_id})
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# Teacher routes
@activities_bp.route('/teacher/submissions')
@login_required
def teacher_submissions():
    """View all student submissions (teachers only)"""
    if current_user.role not in ['teacher', 'admin']:
        flash('Access denied', 'error')
        return redirect(url_for('home'))
    
    # TODO: Get all submissions for teacher's classes
    submissions = []
    return render_template('activities/teacher_submissions.html', submissions=submissions)


@activities_bp.route('/api/teacher/grade', methods=['POST'])
@login_required
def grade_submission():
    """Grade a student submission (teachers only)"""
    if current_user.role not in ['teacher', 'admin']:
        return jsonify({'error': 'Access denied'}), 403
    
    try:
        data = request.json
        submission_id = data.get('submission_id')
        score = data.get('score')
        comments = data.get('comments')
        rubric_data = data.get('rubric_data')
        
        if not submission_id:
            return jsonify({'error': 'Submission ID required'}), 400
        
        feedback_id = submission_manager.add_feedback(
            submission_id=submission_id,
            teacher_id=current_user.id,
            score=score,
            comments=comments,
            rubric_data=rubric_data
        )
        
        return jsonify({'success': True, 'feedback_id': feedback_id})
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500
