"""
Authentication blueprint for the Ultimate Tutor Platform
"""
from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash
from models import User

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    """User login"""
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        remember = request.form.get('remember', False)
        
        if not username or not password:
            flash('Please enter both username and password', 'error')
            return render_template('auth/login.html')
        
        # Verify credentials
        if User.verify_password(username, password):
            user = User.get_by_username(username)
            login_user(user, remember=remember)
            
            next_page = request.args.get('next')
            if not next_page or not next_page.startswith('/'):
                if user.role == 'parent':
                    next_page = url_for('parent.dashboard')
                elif user.role == 'teacher':
                    next_page = url_for('teacher.dashboard')
                else:
                    next_page = url_for('home')
            
            flash(f'Welcome back, {user.username}!', 'success')
            return redirect(next_page)
        else:
            flash('Invalid username or password', 'error')
    
    return render_template('auth/login.html')


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    """User registration"""
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        role = request.form.get('role', 'student')
        
        # Validation
        if not all([username, email, password, confirm_password]):
            flash('All fields are required', 'error')
            return render_template('auth/register.html')
        
        if password != confirm_password:
            flash('Passwords do not match', 'error')
            return render_template('auth/register.html')
        
        if len(password) < 6:
            flash('Password must be at least 6 characters', 'error')
            return render_template('auth/register.html')
        
        if role not in ['student', 'teacher', 'parent']:
            flash('Invalid role selected', 'error')
            return render_template('auth/register.html')
        
        # Check if user exists
        if User.get_by_username(username):
            flash('Username already exists', 'error')
            return render_template('auth/register.html')
        
        if User.get_by_email(email):
            flash('Email already registered', 'error')
            return render_template('auth/register.html')
        
        # Create user
        user = User.create(username, email, password, role)
        if user:
            login_user(user)
            flash(f'Welcome, {username}! Your account has been created.', 'success')
            
            if role == 'parent':
                return redirect(url_for('parent.dashboard'))
            elif role == 'teacher':
                return redirect(url_for('teacher.dashboard'))
            else:
                return redirect(url_for('home'))
        else:
            flash('Error creating account. Please try again.', 'error')
    
    return render_template('auth/register.html')


@auth_bp.route('/logout')
@login_required
def logout():
    """User logout"""
    logout_user()
    flash('You have been logged out', 'success')
    return redirect(url_for('home'))


@auth_bp.route('/profile')
@login_required
def profile():
    """User profile page"""
    return render_template('auth/profile.html', user=current_user)


@auth_bp.route('/profile/edit', methods=['GET', 'POST'])
@login_required
def edit_profile():
    """Edit user profile"""
    if request.method == 'POST':
        # Handle profile updates
        flash('Profile updated successfully', 'success')
        return redirect(url_for('auth.profile'))
    
    return render_template('auth/edit_profile.html', user=current_user)
