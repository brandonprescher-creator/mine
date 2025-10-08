"""USGS Earthquake API Adapter"""
from typing import List, Dict, Any, Optional
from .base import APIAdapter


class USGSAdapter(APIAdapter):
    """USGS Earthquake data"""
    
    def __init__(self):
        super().__init__()
        self.base_url = 'https://earthquake.usgs.gov/fdsnws/event/1'
    
    def search(self, topic: str, subject: Optional[str] = None, grade_band: Optional[str] = None,
               media_type: Optional[str] = None, limit: int = 10) -> List[Dict[str, Any]]:
        """Get recent earthquake data"""
        url = f'{self.base_url}/query'
        params = {'format': 'geojson', 'limit': limit}
        
        data = self._make_request(url, params)
        
        if not data or 'features' not in data:
            return []
        
        results = []
        for feature in data['features'][:limit]:
            props = feature.get('properties', {})
            coords = feature.get('geometry', {}).get('coordinates', [0, 0, 0])
            
            results.append({
                'title': props.get('title', 'Earthquake'),
                'url': props.get('url', ''),
                'summary': f"Magnitude {props.get('mag', 'N/A')} earthquake. Location: {props.get('place', 'Unknown')}",
                'subject': 'Science',
                'grade_band': '6-12',
                'topics': ['earthquakes', 'seismology', 'earth science'],
                'media_type': 'data',
                'length_minutes': 10,
                'provider': 'USGS',
                'attribution': 'U.S. Geological Survey',
                'thumbnail': None
            })
        
        return results
