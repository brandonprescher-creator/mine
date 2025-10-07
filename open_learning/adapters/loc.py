"""
Library of Congress API Adapter
FREE historical and educational content!
"""

from open_learning.http_client import safe_get
from open_learning.cache import cache_get, cache_set
from open_learning.schemas import ContentCard


def search(query: str, count: int = 10) -> list[ContentCard]:
    """Search Library of Congress"""
    cache_key = f"loc:{query.lower()}:{count}"
    cached = cache_get(cache_key)
    if cached:
        return cached

    url = "https://www.loc.gov/search/"
    params = {"q": query, "fo": "json", "c": count}

    data = safe_get(url, params=params, default={})

    results = []
    for item in data.get("results", [])[:count]:
        card = ContentCard(
            source="Library of Congress",
            title=item.get("title", "Untitled"),
            url=item.get("id", ""),
            text=(
                item.get("description", [""])[0]
                if isinstance(item.get("description"), list)
                else item.get("description", "")
            ),
            image=(
                item.get("image_url", [""])[0]
                if isinstance(item.get("image_url"), list)
                else item.get("image_url")
            ),
            meta={"date": item.get("date"), "subjects": item.get("subject", [])},
        )
        results.append(card)

    cache_set(cache_key, results, ttl=3600)
    return results
