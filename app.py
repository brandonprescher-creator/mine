"""
Ultimate Tutor Platform - Comprehensive K-12 Homeschool System
Flask + SQLAlchemy + Redis + PWA
"""
import os
from flask import Flask, render_template, redirect, url_for
from flask_login import LoginManager, current_user
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_migrate import Migrate
from config import get_config

# Initialize extensions
from models.database import db
login_manager = LoginManager()
limiter = Limiter(key_func=get_remote_address)
migrate = Migrate()

def create_app(config_name=None):
    """Application factory"""
    app = Flask(__name__)
    
    # Load configuration
    if config_name is None:
        config_name = os.getenv('FLASK_ENV', 'development')
    app.config.from_object(get_config(config_name))
    
    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)
    limiter.init_app(app)
    migrate.init_app(app, db)
    
    # Login manager config
    login_manager.login_view = 'auth.login'
    login_manager.login_message = 'Please log in to access this page'
    login_manager.login_message_category = 'info'
    
    # User loader
    @login_manager.user_loader
    def load_user(user_id):
        from models.database import User
        return User.query.get(int(user_id))
    
    # Register blueprints
    from blueprints.auth.routes import auth_bp
    from blueprints.main.routes import main_bp
    from blueprints.student.routes import student_bp
    from blueprints.parent.routes import parent_bp
    from blueprints.assess.routes import assess_bp
    from blueprints.curriculum.routes import curriculum_bp
    from blueprints.apis.routes import apis_bp
    from blueprints.tutor.routes import tutor_bp
    
    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)
    app.register_blueprint(student_bp)
    app.register_blueprint(parent_bp)
    app.register_blueprint(assess_bp)
    app.register_blueprint(curriculum_bp)
    app.register_blueprint(apis_bp)
    app.register_blueprint(tutor_bp)
    
    # Error handlers
    @app.errorhandler(404)
    def not_found(error):
        return render_template('errors/404.html'), 404
    
    @app.errorhandler(500)
    def internal_error(error):
        db.session.rollback()
        return render_template('errors/500.html'), 500
    
    # Security headers
    @app.after_request
    def security_headers(response):
        response.headers['X-Content-Type-Options'] = 'nosniff'
        response.headers['X-Frame-Options'] = 'SAMEORIGIN'
        response.headers['X-XSS-Protection'] = '1; mode=block'
        
        if not app.debug:
            response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
        
        return response
    
    # Context processors
    @app.context_processor
    def inject_globals():
        return {
            'current_user': current_user,
            'now': datetime.utcnow
        }
    
    # Health check
    @app.route('/healthz')
    def healthz():
        """Health check endpoint"""
        try:
            # Check database
            db.session.execute(db.text('SELECT 1'))
            return {'status': 'healthy', 'database': 'connected'}, 200
        except Exception as e:
            return {'status': 'unhealthy', 'error': str(e)}, 500
    
    # PWA manifest
    @app.route('/manifest.json')
    def manifest():
        return {
            'name': 'Ultimate Tutor Platform',
            'short_name': 'Tutor',
            'description': 'Comprehensive K-12 homeschool platform',
            'start_url': '/',
            'display': 'standalone',
            'background_color': '#0f172a',
            'theme_color': '#0ea5e9',
            'icons': [
                {'src': '/static/images/icon-192.png', 'sizes': '192x192', 'type': 'image/png'},
                {'src': '/static/images/icon-512.png', 'sizes': '512x512', 'type': 'image/png'}
            ]
        }
    
    # Service worker
    @app.route('/sw.js')
    def service_worker():
        return app.send_static_file('sw.js')
    
    return app


# Create app instance
app = create_app()

if __name__ == '__main__':
    from datetime import datetime
    
    with app.app_context():
        # Create tables
        db.create_all()
        
        # Seed initial data
        from services.curriculum.seed import seed_database
        seed_database()
    
    # Run app
    app.run(debug=True, host='0.0.0.0', port=5001)