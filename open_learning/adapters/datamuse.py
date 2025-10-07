"""
Datamuse API Adapter
FREE vocabulary and word relationships!
"""

from open_learning.http_client import safe_get
from open_learning.cache import cache_get, cache_set
from open_learning.schemas import ContentCard


def related_words(word: str, limit: int = 10) -> ContentCard:
    """Get words related by meaning"""
    cache_key = f"datamuse:related:{word.lower()}"
    cached = cache_get(cache_key)
    if cached:
        return cached

    url = "https://api.datamuse.com/words"
    data = safe_get(url, params={"ml": word, "max": limit}, default=[])

    words = [item.get("word", "") for item in data if item.get("word")]

    card = ContentCard(
        source="Datamuse",
        title=f'Words related to "{word}"',
        text=", ".join(words) if words else "No related words found",
        meta={"count": len(words), "words": words},
    )

    cache_set(cache_key, card, ttl=3600)
    return card


def rhyming_words(word: str, limit: int = 10) -> ContentCard:
    """Get rhyming words"""
    cache_key = f"datamuse:rhyme:{word.lower()}"
    cached = cache_get(cache_key)
    if cached:
        return cached

    url = "https://api.datamuse.com/words"
    data = safe_get(url, params={"rel_rhy": word, "max": limit}, default=[])

    words = [item.get("word", "") for item in data if item.get("word")]

    card = ContentCard(
        source="Datamuse",
        title=f'Words that rhyme with "{word}"',
        text=", ".join(words) if words else "No rhymes found",
        meta={"count": len(words), "words": words},
    )

    cache_set(cache_key, card, ttl=3600)
    return card


def synonyms(word: str, limit: int = 10) -> ContentCard:
    """Get synonyms"""
    cache_key = f"datamuse:synonym:{word.lower()}"
    cached = cache_get(cache_key)
    if cached:
        return cached

    url = "https://api.datamuse.com/words"
    data = safe_get(url, params={"rel_syn": word, "max": limit}, default=[])

    words = [item.get("word", "") for item in data if item.get("word")]

    card = ContentCard(
        source="Datamuse",
        title=f'Synonyms for "{word}"',
        text=", ".join(words) if words else "No synonyms found",
        meta={"count": len(words), "words": words},
    )

    cache_set(cache_key, card, ttl=3600)
    return card
