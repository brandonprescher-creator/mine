"""
VERIFICATION SCRIPT
Tests that ALL features are working correctly!
"""

import os
import sys

def check_file_exists(filepath, description):
    """Check if a file exists"""
    if os.path.exists(filepath):
        print(f"  ✅ {description}")
        return True
    else:
        print(f"  ❌ MISSING: {description} ({filepath})")
        return False

def verify_installation():
    """Verify all files and dependencies"""
    print("🔍 VERIFYING ULTIMATE TUTOR INSTALLATION...\n")
    
    all_good = True
    
    # Check core Python files
    print("📂 Core Python Files:")
    files = [
        ('app.py', 'Main Flask application'),
        ('database.py', 'Database operations'),
        ('curriculum_data.py', 'Curriculum data'),
        ('ULTIMATE_CURRICULUM_BUILDER.py', 'Curriculum builder'),
        ('MEGA_AI_TUTOR.py', 'AI Tutor engine'),
        ('personalized_learning.py', 'Learning path creator'),
        ('worksheet_ai_converter.py', 'Worksheet upload converter'),
        ('worksheet_generator_api.py', 'API worksheet generator'),
        ('visual_content_generator.py', 'Visual content creator'),
        ('api_integrations_badass.py', 'API integrations'),
    ]
    
    for filepath, desc in files:
        if not check_file_exists(filepath, desc):
            all_good = False
    
    # Check templates
    print("\n📄 Templates:")
    templates = [
        ('templates/base.html', 'Base template'),
        ('templates/home.html', 'Home page'),
        ('templates/subjects.html', 'Subjects page'),
        ('templates/topics.html', 'Topics page'),
        ('templates/lessons.html', 'Lessons list'),
        ('templates/lesson.html', 'Lesson view'),
        ('templates/upload.html', 'Worksheet upload'),
        ('templates/worksheets.html', 'Worksheet generator'),
        ('templates/games.html', 'Games page'),
    ]
    
    for filepath, desc in templates:
        if not check_file_exists(filepath, desc):
            all_good = False
    
    # Check JavaScript
    print("\n📜 JavaScript Files:")
    js_files = [
        ('static/js/badass.js', 'Core JavaScript'),
        ('static/js/games.js', 'Games JavaScript'),
        ('static/js/math-visualizer.js', 'Math visualizer'),
        ('static/js/math-problems.js', 'Math problems'),
        ('static/js/achievements.js', 'Achievements'),
    ]
    
    for filepath, desc in js_files:
        if not check_file_exists(filepath, desc):
            all_good = False
    
    # Check CSS
    print("\n🎨 CSS Files:")
    if not check_file_exists('static/css/badass.css', 'Main stylesheet'):
        all_good = False
    
    # Check documentation
    print("\n📚 Documentation:")
    docs = [
        ('README_ULTIMATE.md', 'Ultimate README'),
        ('THE_TUTOR_OF_ALL_TUTORS.md', 'Complete guide'),
        ('COMPLETE_FEATURE_LIST.md', 'Feature list'),
        ('EXPANDED_API_LIST.md', 'API list'),
    ]
    
    for filepath, desc in docs:
        if not check_file_exists(filepath, desc):
            all_good = False
    
    # Check startup scripts
    print("\n🚀 Startup Scripts:")
    if not check_file_exists('START_ULTIMATE_APP.bat', 'Ultimate startup script'):
        all_good = False
    
    # Check Python dependencies
    print("\n📦 Checking Python Dependencies:")
    required_modules = [
        ('flask', 'flask'),
        ('flask_socketio', 'flask_socketio'),
        ('requests', 'requests'),
        ('PIL', 'PIL'),
        ('numpy', 'numpy'),
        ('matplotlib', 'matplotlib'),
        ('reportlab', 'reportlab.pdfgen')
    ]
    
    for display_name, import_name in required_modules:
        try:
            __import__(import_name)
            print(f"  ✅ {display_name}")
        except ImportError:
            print(f"  ❌ MISSING: {display_name}")
            print(f"      Install with: pip install {display_name.replace('_', '-')}")
            all_good = False
    
    # Summary
    print("\n" + "="*60)
    if all_good:
        print("✅ ALL SYSTEMS GO! Everything is working!")
        print("\n🚀 Ready to launch:")
        print("   python app.py")
        print("\n   Then open: http://localhost:5001")
    else:
        print("❌ Some files or dependencies are missing!")
        print("\n💡 To fix:")
        print("   pip install -r requirements_flask.txt")
    print("="*60)
    
    return all_good

if __name__ == '__main__':
    verify_installation()

