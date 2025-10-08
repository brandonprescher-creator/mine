"""
Main Blueprint - Home, Search, Generic Pages
"""
from flask import Blueprint, render_template, request, jsonify
from flask_login import current_user
from models.database import db, ChildProfile, Resource, Standard
from sqlalchemy import or_

main_bp = Blueprint('main', __name__)


@main_bp.route('/')
def index():
    """Home page - redirects based on auth status"""
    if current_user.is_authenticated:
        return render_template('pages/main/home_logged_in.html')
    return render_template('pages/main/home.html')


@main_bp.route('/search')
def search():
    """Global search across curriculum and resources"""
    query = request.args.get('q', '').strip()
    
    if not query:
        return render_template('pages/main/search.html', results={})
    
    # Search standards
    standards = Standard.query.filter(
        or_(
            Standard.name.ilike(f'%{query}%'),
            Standard.description.ilike(f'%{query}%'),
            Standard.code.ilike(f'%{query}%')
        )
    ).limit(20).all()
    
    # Search resources
    resources = Resource.query.filter(
        or_(
            Resource.title.ilike(f'%{query}%'),
            Resource.attribution.ilike(f'%{query}%')
        )
    ).limit(20).all()
    
    results = {
        'query': query,
        'standards': standards,
        'resources': resources,
        'total': len(standards) + len(resources)
    }
    
    return render_template('pages/main/search.html', results=results)


@main_bp.route('/about')
def about():
    """About page"""
    return render_template('pages/main/about.html')


@main_bp.route('/help')
def help_page():
    """Help and documentation"""
    return render_template('pages/main/help.html')
