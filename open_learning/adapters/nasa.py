"""
NASA APIs Adapter
FREE space and astronomy content!
"""

import os
from open_learning.http_client import safe_get
from open_learning.cache import cache_get, cache_set
from open_learning.schemas import ContentCard, ScientificData

NASA_API_KEY = os.getenv('NASA_API_KEY', 'DEMO_KEY')

def get_apod(date: str = None) -> ContentCard:
    """Get Astronomy Picture of the Day"""
    cache_key = f"nasa:apod:{date or 'today'}"
    cached = cache_get(cache_key)
    if cached:
        return cached
    
    url = "https://api.nasa.gov/planetary/apod"
    params = {'api_key': NASA_API_KEY}
    if date:
        params['date'] = date
    
    data = safe_get(url, params=params, default={})
    
    card = ContentCard(
        source='NASA APOD',
        title=data.get('title', 'Astronomy Picture of the Day'),
        url=data.get('hdurl', data.get('url', '')),
        text=data.get('explanation', ''),
        image=data.get('url', ''),
        meta={
            'date': data.get('date'),
            'media_type': data.get('media_type'),
            'copyright': data.get('copyright', '')
        }
    )
    
    cache_set(cache_key, card, ttl=86400)  # Cache for 24 hours
    return card

def get_mars_photos(rover: str = 'curiosity', sol: int = 1000) -> list[ContentCard]:
    """Get Mars Rover photos"""
    cache_key = f"nasa:mars:{rover}:{sol}"
    cached = cache_get(cache_key)
    if cached:
        return cached
    
    url = f"https://api.nasa.gov/mars-photos/api/v1/rovers/{rover}/photos"
    params = {
        'sol': sol,
        'api_key': NASA_API_KEY
    }
    
    data = safe_get(url, params=params, default={})
    
    results = []
    for photo in data.get('photos', [])[:10]:  # Limit to 10
        card = ContentCard(
            source=f'NASA Mars {rover.title()}',
            title=f'Mars Photo - Sol {sol}',
            url=photo.get('img_src', ''),
            text=f"Camera: {photo.get('camera', {}).get('full_name', 'Unknown')}",
            image=photo.get('img_src', ''),
            meta={
                'earth_date': photo.get('earth_date'),
                'camera': photo.get('camera', {}).get('name')
            }
        )
        results.append(card)
    
    cache_set(cache_key, results, ttl=86400)
    return results

