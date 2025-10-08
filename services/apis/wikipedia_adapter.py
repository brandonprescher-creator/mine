"""Wikipedia API Adapter"""
from typing import List, Dict, Any, Optional
from .base import APIAdapter
import requests


class WikipediaAdapter(APIAdapter):
    """Wikipedia REST API v1 adapter"""
    
    def __init__(self):
        super().__init__()
        self.base_url = 'https://en.wikipedia.org/api/rest_v1'
    
    def search(self, topic: str, subject: Optional[str] = None, grade_band: Optional[str] = None,
               media_type: Optional[str] = None, limit: int = 10) -> List[Dict[str, Any]]:
        """Search Wikipedia"""
        
        # Search for articles
        search_url = f'{self.base_url}/page/search/{topic}'
        data = self._make_request(search_url)
        
        if not data or 'pages' not in data:
            return []
        
        results = []
        for page in data['pages'][:limit]:
            results.append({
                'title': page.get('title', ''),
                'url': f"https://en.wikipedia.org/wiki/{page.get('key', '')}",
                'summary': page.get('description', ''),
                'subject': subject or 'General',
                'grade_band': grade_band or 'All',
                'topics': [topic],
                'media_type': 'article',
                'length_minutes': 10,
                'provider': 'Wikipedia',
                'attribution': 'Wikipedia contributors. Available under CC BY-SA 3.0.',
                'thumbnail': page.get('thumbnail', {}).get('url')
            })
        
        return results
