"""
Authentication helper functions
"""
from functools import wraps
from flask import session, redirect, url_for, flash
from flask_login import current_user


def student_required(f):
    """Decorator for student-only routes"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('child_id'):
            flash('Please log in as a student', 'error')
            return redirect(url_for('auth.login'))
        return f(*args, **kwargs)
    return decorated_function


def parent_required(f):
    """Decorator for parent-only routes"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or current_user.role != 'parent':
            flash('Parent access required', 'error')
            return redirect(url_for('auth.login'))
        if session.get('impersonating'):
            flash('Return to parent view first', 'warning')
            return redirect(url_for('parent.dashboard'))
        return f(*args, **kwargs)
    return decorated_function


def admin_required(f):
    """Decorator for admin-only routes"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or current_user.role != 'admin':
            flash('Admin access required', 'error')
            return redirect(url_for('main.index'))
        return f(*args, **kwargs)
    return decorated_function
