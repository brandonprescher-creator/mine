"""
APIs Blueprint - Single Results Template for All Education APIs
"""
from flask import Blueprint, render_template, request, jsonify
from models.database import db, Resource
from services.apis.adapter_factory import get_adapter, list_adapters

apis_bp = Blueprint('apis', __name__, url_prefix='/apis')


@apis_bp.route('/')
def index():
    """API explorer home"""
    adapters = list_adapters()
    return render_template('pages/apis/index.html', adapters=adapters)


@apis_bp.route('/search')
def search():
    """Search all APIs with single results template"""
    topic = request.args.get('topic', '')
    subject = request.args.get('subject')
    grade_band = request.args.get('grade_band')
    media_type = request.args.get('media_type')
    provider = request.args.get('provider')
    
    results = []
    
    if provider:
        # Search specific provider
        adapter = get_adapter(provider)
        if adapter:
            results = adapter.search(
                topic=topic,
                subject=subject,
                grade_band=grade_band,
                media_type=media_type
            )
    else:
        # Search all providers
        for adapter_name in list_adapters():
            adapter = get_adapter(adapter_name)
            if adapter:
                adapter_results = adapter.search(topic=topic, subject=subject, grade_band=grade_band, media_type=media_type, limit=5)
                results.extend(adapter_results)
    
    return render_template('pages/apis/results.html',
                         query=topic,
                         results=results,
                         filters={'subject': subject, 'grade_band': grade_band, 'media_type': media_type})


@apis_bp.route('/assign', methods=['POST'])
def assign_resource():
    """Assign a resource to a lesson item"""
    data = request.json
    
    # Create Resource if it doesn't exist
    resource = Resource.query.filter_by(url=data.get('url')).first()
    
    if not resource:
        resource = Resource(
            title=data.get('title'),
            url=data.get('url'),
            subject=data.get('subject'),
            grade_band=data.get('grade_band'),
            media_type=data.get('media_type'),
            provider=data.get('provider'),
            attribution=data.get('attribution')
        )
        resource.topics = data.get('topics', [])
        
        db.session.add(resource)
        db.session.commit()
    
    return jsonify({'success': True, 'resource_id': resource.id})
