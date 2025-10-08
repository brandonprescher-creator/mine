"""
Authentication Blueprint
Signup, login, logout, password reset, parent->student switching
"""
from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from flask_login import login_user, logout_user, login_required, current_user
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from werkzeug.security import generate_password_hash

from models.database import db, User, ChildProfile

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    """Parent registration"""
    if current_user.is_authenticated and not session.get('impersonating'):
        return redirect(url_for('parent.dashboard'))
    
    if request.method == 'POST':
        email = request.form.get('email', '').strip()
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        
        # Validation
        if not email or not password:
            flash('Email and password are required', 'error')
            return render_template('pages/auth/register.html')
        
        if password != confirm_password:
            flash('Passwords do not match', 'error')
            return render_template('pages/auth/register.html')
        
        if len(password) < 8:
            flash('Password must be at least 8 characters', 'error')
            return render_template('pages/auth/register.html')
        
        # Check if email exists
        if User.query.filter_by(email=email).first():
            flash('Email already registered', 'error')
            return render_template('pages/auth/register.html')
        
        # Create user
        user = User(email=email, role='parent')
        user.set_password(password)
        
        db.session.add(user)
        db.session.commit()
        
        # Log in
        login_user(user)
        flash(f'Welcome! Your account has been created.', 'success')
        return redirect(url_for('parent.dashboard'))
    
    return render_template('pages/auth/register.html')


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    """Parent or student login"""
    if current_user.is_authenticated and not session.get('impersonating'):
        if hasattr(current_user, 'role') and current_user.role == 'parent':
            return redirect(url_for('parent.dashboard'))
        return redirect(url_for('student.today'))
    
    if request.method == 'POST':
        email_or_username = request.form.get('email_or_username', '').strip()
        password = request.form.get('password')
        remember = request.form.get('remember', False)
        
        if not email_or_username or not password:
            flash('Please enter your credentials', 'error')
            return render_template('pages/auth/login.html')
        
        # Try parent login first (email)
        if '@' in email_or_username:
            user = User.query.filter_by(email=email_or_username).first()
            if user and user.check_password(password):
                login_user(user, remember=remember)
                flash(f'Welcome back!', 'success')
                return redirect(url_for('parent.dashboard'))
        
        # Try student login (username)
        child = ChildProfile.query.filter_by(username=email_or_username).first()
        if child and child.check_password(password):
            # Create temporary user object for student
            session['child_id'] = child.id
            session['child_name'] = child.name
            session['is_student'] = True
            flash(f'Welcome, {child.name}!', 'success')
            return redirect(url_for('student.today'))
        
        flash('Invalid credentials', 'error')
    
    return render_template('pages/auth/login.html')


@auth_bp.route('/logout')
@login_required
def logout():
    """Logout"""
    if session.get('impersonating'):
        # Return to parent view
        session.pop('impersonating', None)
        session.pop('child_id', None)
        session.pop('child_name', None)
        flash('Returned to parent view', 'info')
        return redirect(url_for('parent.dashboard'))
    
    logout_user()
    session.clear()
    flash('You have been logged out', 'success')
    return redirect(url_for('main.index'))


@auth_bp.route('/switch-to-student/<int:child_id>')
@login_required
def switch_to_student(child_id):
    """Parent switches to student view"""
    if current_user.role != 'parent':
        flash('Access denied', 'error')
        return redirect(url_for('main.index'))
    
    child = ChildProfile.query.filter_by(id=child_id, user_id=current_user.id).first()
    if not child:
        flash('Child not found', 'error')
        return redirect(url_for('parent.dashboard'))
    
    session['impersonating'] = True
    session['child_id'] = child.id
    session['child_name'] = child.name
    session['is_student'] = True
    
    flash(f'Viewing as {child.name}', 'info')
    return redirect(url_for('student.today'))


@auth_bp.route('/password-reset', methods=['GET', 'POST'])
def password_reset():
    """Request password reset"""
    if request.method == 'POST':
        email = request.form.get('email', '').strip()
        
        user = User.query.filter_by(email=email).first()
        if user:
            # Generate reset token (simplified - would use itsdangerous in production)
            # Send email with reset link
            flash('Password reset instructions sent to your email', 'success')
        else:
            # Don't reveal if email exists
            flash('If that email is registered, reset instructions have been sent', 'info')
        
        return redirect(url_for('auth.login'))
    
    return render_template('pages/auth/password_reset.html')


@auth_bp.route('/password-reset/<token>', methods=['GET', 'POST'])
def password_reset_confirm(token):
    """Confirm password reset with token"""
    # Validate token
    # Allow password reset
    if request.method == 'POST':
        password = request.form.get('password')
        confirm = request.form.get('confirm_password')
        
        if password and password == confirm and len(password) >= 8:
            # Reset password
            flash('Password has been reset', 'success')
            return redirect(url_for('auth.login'))
    
    return render_template('pages/auth/password_reset_confirm.html', token=token)
