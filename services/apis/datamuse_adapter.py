"""Datamuse Vocabulary API Adapter"""
from typing import List, Dict, Any, Optional
from .base import APIAdapter


class DatamuseAdapter(APIAdapter):
    """Datamuse vocabulary and word relationships"""
    
    def __init__(self):
        super().__init__()
        self.base_url = 'https://api.datamuse.com'
    
    def search(self, topic: str, subject: Optional[str] = None, grade_band: Optional[str] = None,
               media_type: Optional[str] = None, limit: int = 10) -> List[Dict[str, Any]]:
        """Search Datamuse for word relationships"""
        
        url = f'{self.base_url}/words'
        params = {'ml': topic, 'max': limit}  # ml = means like
        
        data = self._make_request(url, params)
        
        if not data:
            return []
        
        results = []
        for item in data:
            results.append({
                'title': item.get('word', ''),
                'url': f"https://www.merriam-webster.com/dictionary/{item.get('word', '')}",
                'summary': f"Related word: {item.get('word', '')} (score: {item.get('score', 0)})",
                'subject': 'English Language Arts',
                'grade_band': grade_band or 'All',
                'topics': ['vocabulary', topic],
                'media_type': 'reference',
                'length_minutes': 2,
                'provider': 'Datamuse',
                'attribution': 'Datamuse API - free vocabulary tool',
                'thumbnail': None
            })
        
        return results
