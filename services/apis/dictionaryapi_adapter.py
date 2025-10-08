"""Free Dictionary API Adapter"""
from typing import List, Dict, Any, Optional
from .base import APIAdapter

class DictionaryAPIAdapter(APIAdapter):
    def __init__(self):
        super().__init__()
        self.base_url = 'https://api.dictionaryapi.dev/api/v2/entries/en'
    
    def search(self, topic: str, subject: Optional[str] = None, grade_band: Optional[str] = None,
               media_type: Optional[str] = None, limit: int = 10) -> List[Dict[str, Any]]:
        url = f'{self.base_url}/{topic}'
        data = self._make_request(url)
        
        if not data or not isinstance(data, list):
            return []
        
        results = []
        for entry in data[:limit]:
            meanings = entry.get('meanings', [])
            definition = meanings[0].get('definitions', [{}])[0].get('definition', '') if meanings else ''
            
            results.append({
                'title': entry.get('word', ''),
                'url': f"https://www.dictionary.com/browse/{entry.get('word', '')}",
                'summary': definition[:200],
                'subject': 'English Language Arts',
                'grade_band': grade_band or 'All',
                'topics': ['vocabulary', 'dictionary'],
                'media_type': 'reference',
                'length_minutes': 2,
                'provider': 'Free Dictionary API',
                'attribution': 'Free Dictionary API',
                'thumbnail': None
            })
        return results
