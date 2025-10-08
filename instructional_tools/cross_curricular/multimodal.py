"""
Multimodal Submission System
Accept audio, video, drawings, and text submissions
"""
from typing import Dict, List, Any, Optional
from datetime import datetime
import base64
import os


class MultimodalSubmission:
    """
    Multimodal Submission Handler
    
    Supports:
    - Audio recordings (voice explanations)
    - Video uploads (demonstrations)
    - Drawings/sketches
    - Text submissions
    - Photo uploads
    """
    
    SUPPORTED_MODES = {
        'audio': {'extensions': ['.mp3', '.wav', '.m4a'], 'max_size_mb': 10, 'icon': '🎤'},
        'video': {'extensions': ['.mp4', '.mov', '.avi'], 'max_size_mb': 50, 'icon': '🎥'},
        'image': {'extensions': ['.jpg', '.png', '.gif'], 'max_size_mb': 5, 'icon': '🖼️'},
        'drawing': {'extensions': ['.png'], 'max_size_mb': 2, 'icon': '🎨'},
        'text': {'extensions': ['.txt', '.doc', '.pdf'], 'max_size_mb': 2, 'icon': '📝'}
    }
    
    def __init__(self, submission_id: int, student_id: int):
        self.submission_id = submission_id
        self.student_id = student_id
        self.items: List[Dict[str, Any]] = []
        self.created_at = datetime.utcnow().isoformat()
    
    def add_item(self, mode: str, content: Any, metadata: Optional[Dict[str, Any]] = None):
        """Add a submission item"""
        if mode not in self.SUPPORTED_MODES:
            raise ValueError(f"Unsupported mode: {mode}")
        
        item = {'id': len(self.items) + 1, 'mode': mode, 'content': content, 'metadata': metadata or {}, 'added_at': datetime.utcnow().isoformat()}
        self.items.append(item)
    
    def validate_submission(self) -> tuple[bool, List[str]]:
        """Validate multimodal submission"""
        errors = []
        
        if not self.items:
            errors.append('Submission must have at least one item')
        
        for item in self.items:
            mode = item['mode']
            # Add file size validation logic here
        
        return len(errors) == 0, errors
    
    def get_summary(self) -> Dict[str, Any]:
        """Get submission summary"""
        mode_counts = {}
        for item in self.items:
            mode = item['mode']
            mode_counts[mode] = mode_counts.get(mode, 0) + 1
        
        return {'submission_id': self.submission_id, 'student_id': self.student_id, 'total_items': len(self.items), 'modes_used': mode_counts, 'created_at': self.created_at}
    
    def to_dict(self) -> Dict[str, Any]:
        return {'submission_id': self.submission_id, 'student_id': self.student_id, 'items': self.items, 'summary': self.get_summary()}
