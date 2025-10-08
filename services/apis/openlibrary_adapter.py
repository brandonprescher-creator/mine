"""Open Library API Adapter"""
from typing import List, Dict, Any, Optional
from .base import APIAdapter


class OpenLibraryAdapter(APIAdapter):
    """Open Library books database"""
    
    def __init__(self):
        super().__init__()
        self.base_url = 'https://openlibrary.org'
    
    def search(self, topic: str, subject: Optional[str] = None, grade_band: Optional[str] = None,
               media_type: Optional[str] = None, limit: int = 10) -> List[Dict[str, Any]]:
        """Search Open Library"""
        url = f'{self.base_url}/search.json'
        params = {'q': topic, 'limit': limit}
        
        data = self._make_request(url, params)
        
        if not data or 'docs' not in data:
            return []
        
        results = []
        for doc in data['docs']:
            results.append({
                'title': doc.get('title', ''),
                'url': f"{self.base_url}{doc.get('key', '')}",
                'summary': f"By {', '.join(doc.get('author_name', ['Unknown']))}. Published {doc.get('first_publish_year', 'N/A')}.",
                'subject': subject or 'Reading',
                'grade_band': grade_band or 'All',
                'topics': doc.get('subject', [])[:5],
                'media_type': 'book',
                'length_minutes': 60,
                'provider': 'Open Library',
                'attribution': 'Open Library - Internet Archive',
                'thumbnail': f"https://covers.openlibrary.org/b/id/{doc.get('cover_i', '')}-M.jpg" if doc.get('cover_i') else None
            })
        
        return results
