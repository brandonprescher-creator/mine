"""Openverse API Adapter - Creative Commons media"""
from typing import List, Dict, Any, Optional
from .base import APIAdapter

class OpenverseAdapter(APIAdapter):
    def __init__(self):
        super().__init__()
        self.base_url = 'https://api.openverse.engineering/v1'
    
    def search(self, topic: str, subject: Optional[str] = None, grade_band: Optional[str] = None,
               media_type: Optional[str] = None, limit: int = 10) -> List[Dict[str, Any]]:
        url = f'{self.base_url}/images/'
        params = {'q': topic, 'page_size': limit}
        
        data = self._make_request(url, params)
        
        if not data or 'results' not in data:
            return []
        
        results = []
        for item in data['results']:
            results.append({
                'title': item.get('title', 'Untitled'),
                'url': item.get('foreign_landing_url', ''),
                'summary': f"By {item.get('creator', 'Unknown')}. {item.get('license', 'CC')} license.",
                'subject': subject or 'Arts',
                'grade_band': grade_band or 'All',
                'topics': [topic],
                'media_type': 'image',
                'length_minutes': 2,
                'provider': 'Openverse',
                'attribution': f"Via Openverse. License: {item.get('license', 'Unknown')}",
                'thumbnail': item.get('thumbnail', '')
            })
        return results
