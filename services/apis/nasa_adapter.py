"""NASA API Adapter"""
from typing import List, Dict, Any, Optional
from .base import APIAdapter


class NASAAdapter(APIAdapter):
    """NASA educational resources"""
    
    def __init__(self):
        super().__init__()
        self.base_url = 'https://images-api.nasa.gov'
    
    def search(self, topic: str, subject: Optional[str] = None, grade_band: Optional[str] = None,
               media_type: Optional[str] = None, limit: int = 10) -> List[Dict[str, Any]]:
        """Search NASA image library"""
        url = f'{self.base_url}/search'
        params = {'q': topic, 'media_type': 'image'}
        
        data = self._make_request(url, params)
        
        if not data or 'collection' not in data:
            return []
        
        results = []
        items = data['collection'].get('items', [])[:limit]
        
        for item in items:
            item_data = item.get('data', [{}])[0]
            links = item.get('links', [{}])
            
            results.append({
                'title': item_data.get('title', ''),
                'url': links[0].get('href', '') if links else '',
                'summary': item_data.get('description', '')[:200],
                'subject': 'Science',
                'grade_band': grade_band or 'All',
                'topics': [topic, 'space', 'astronomy'],
                'media_type': 'image',
                'length_minutes': 5,
                'provider': 'NASA',
                'attribution': 'NASA Image Library - Public Domain',
                'thumbnail': links[0].get('href', '') if links else None
            })
        
        return results
