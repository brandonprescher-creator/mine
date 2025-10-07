"""
Wikipedia REST API Adapter
FREE & UNLIMITED educational content!
"""

from urllib.parse import quote
from open_learning.http_client import sync_get, safe_get
from open_learning.cache import cache_get, cache_set
from open_learning.schemas import ContentCard


def search_summary(title: str) -> ContentCard:
    """Get Wikipedia summary for any topic"""
    # Check cache first
    cache_key = f"wikipedia:{title.lower()}"
    cached = cache_get(cache_key)
    if cached:
        return cached

    # Fetch from API
    url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{quote(title)}"
    data = safe_get(url, default={})

    if "title" not in data:
        return None

    # Create ContentCard
    card = ContentCard(
        source="Wikipedia",
        title=data.get("title", title),
        url=data.get("content_urls", {}).get("desktop", {}).get("page", ""),
        text=data.get("extract", ""),
        image=(data.get("thumbnail") or {}).get("source", ""),
        meta={
            "page_id": data.get("pageid"),
            "lang": data.get("lang", "en"),
            "description": data.get("description", ""),
        },
    )

    # Cache for 1 hour
    cache_set(cache_key, card, ttl=3600)

    return card


def search_multiple(queries: list[str]) -> list[ContentCard]:
    """Search multiple topics at once"""
    results = []

    for query in queries:
        card = search_summary(query)
        if card:
            results.append(card)

    return results
