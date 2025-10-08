"""PoetryDB API Adapter"""
from typing import List, Dict, Any, Optional
from .base import APIAdapter

class PoetryDBAdapter(APIAdapter):
    def __init__(self):
        super().__init__()
        self.base_url = 'https://poetrydb.org'
    
    def search(self, topic: str, subject: Optional[str] = None, grade_band: Optional[str] = None,
               media_type: Optional[str] = None, limit: int = 10) -> List[Dict[str, Any]]:
        url = f'{self.base_url}/title/{topic}'
        data = self._make_request(url)
        
        if not data or isinstance(data, dict) and 'status' in data:
            return []
        
        results = []
        for poem in (data if isinstance(data, list) else [])[:limit]:
            results.append({
                'title': poem.get('title', ''),
                'url': f"{self.base_url}/title/{poem.get('title', '').replace(' ', '%20')}",
                'summary': f"By {poem.get('author', 'Unknown')}. {len(poem.get('lines', []))} lines.",
                'subject': 'English Language Arts',
                'grade_band': grade_band or '6-12',
                'topics': ['poetry', topic],
                'media_type': 'text',
                'length_minutes': 5,
                'provider': 'PoetryDB',
                'attribution': 'PoetryDB - Public domain poetry database',
                'thumbnail': None
            })
        return results
