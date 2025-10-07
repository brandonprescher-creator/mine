"""
Open Library API Adapter
FREE book search and information!
"""

from open_learning.http_client import safe_get
from open_learning.cache import cache_get, cache_set
from open_learning.schemas import ContentCard

def search(query: str, limit: int = 10) -> list[ContentCard]:
    """Search for books"""
    cache_key = f"openlibrary:{query.lower()}:{limit}"
    cached = cache_get(cache_key)
    if cached:
        return cached
    
    url = "https://openlibrary.org/search.json"
    data = safe_get(url, params={'q': query, 'limit': limit}, default={})
    
    docs = data.get('docs', [])
    results = []
    
    for doc in docs:
        cover_id = doc.get('cover_i')
        image_url = f"https://covers.openlibrary.org/b/id/{cover_id}-L.jpg" if cover_id else None
        
        authors = doc.get('author_name', [])
        author_str = ', '.join(authors[:3]) if authors else 'Unknown'
        
        card = ContentCard(
            source='Open Library',
            title=doc.get('title', 'Untitled'),
            url=f"https://openlibrary.org{doc.get('key', '')}",
            text=f"By {author_str}. Published: {doc.get('first_publish_year', 'Unknown')}",
            image=image_url,
            meta={
                'authors': authors,
                'publish_year': doc.get('first_publish_year'),
                'isbn': doc.get('isbn', [])[0] if doc.get('isbn') else None
            }
        )
        results.append(card)
    
    cache_set(cache_key, results, ttl=3600)
    return results

