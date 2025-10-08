"""
Tutor Tools Blueprint - Keep Existing OCR/PDF/Doc Features
Integrates existing tutor functionality into new platform
"""
from flask import Blueprint, render_template, request, jsonify, flash, redirect, url_for
from werkzeug.utils import secure_filename
import os

# Import existing tutor functions
from file_processor import process_uploaded_file
from lesson_generator import generate_lesson_from_text, generate_practice_problems
from worksheet_ai_converter import convert_worksheet_to_lesson
from worksheet_generator_api import generate_worksheet

tutor_bp = Blueprint('tutor', __name__, url_prefix='/tutor')


@tutor_bp.route('/')
def index():
    """Tutor tools home"""
    return render_template('pages/tutor/index.html')


@tutor_bp.route('/ingest', methods=['GET', 'POST'])
def ingest():
    """Ingest PDF/Doc/Image and convert to lessons"""
    if request.method == 'POST':
        if 'file' not in request.files:
            return jsonify({'error': 'No file provided'}), 400
        
        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        # Process file
        filename = secure_filename(file.filename)
        file_bytes = file.read()
        
        file_type, extracted_text = process_uploaded_file(filename, file_bytes)
        
        if extracted_text:
            # Generate lesson data
            lesson_data = generate_lesson_from_text(extracted_text)
            
            return jsonify({
                'success': True,
                'file_type': file_type,
                'text_length': len(extracted_text),
                'lesson_data': lesson_data
            })
        else:
            return jsonify({'error': 'Could not extract text'}), 400
    
    return render_template('pages/tutor/ingest.html')


@tutor_bp.route('/worksheet/convert', methods=['POST'])
def convert_worksheet():
    """Convert worksheet to interactive lesson"""
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400
    
    file = request.files['file']
    subject = request.form.get('subject', 'Math')
    
    # Save temporarily
    filename = secure_filename(file.filename)
    temp_path = os.path.join('temp', filename)
    file.save(temp_path)
    
    try:
        result = convert_worksheet_to_lesson(temp_path, subject)
        os.remove(temp_path)
        return jsonify(result)
    except Exception as e:
        if os.path.exists(temp_path):
            os.remove(temp_path)
        return jsonify({'error': str(e)}), 500


@tutor_bp.route('/worksheet/generate', methods=['POST'])
def generate_worksheet_pdf():
    """Generate worksheet PDF"""
    data = request.json
    
    worksheet = generate_worksheet(
        topic=data.get('topic'),
        subject=data.get('subject'),
        grade=data.get('grade')
    )
    
    return jsonify(worksheet)
