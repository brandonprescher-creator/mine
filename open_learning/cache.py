"""
Simple TTL cache for API responses
"""

import time
from typing import Any, Optional

# In-memory cache store
_cache_store: dict[str, tuple[float, Any]] = {}


def cache_get(key: str) -> Optional[Any]:
    """Get cached value if not expired"""
    hit = _cache_store.get(key)
    if not hit:
        return None

    expiry_time, value = hit

    # Check if expired
    if expiry_time < time.time():
        _cache_store.pop(key, None)
        return None

    return value


def cache_set(key: str, value: Any, ttl: int = 900):
    """
    Set cached value with TTL (time to live)
    Default TTL: 900 seconds (15 minutes)
    """
    expiry_time = time.time() + ttl
    _cache_store[key] = (expiry_time, value)


def clear_cache():
    """Clear all cached values"""
    _cache_store.clear()


def clear_expired():
    """Remove expired entries from cache"""
    current_time = time.time()
    expired_keys = [k for k, (exp, _) in _cache_store.items() if exp < current_time]

    for key in expired_keys:
        _cache_store.pop(key, None)

    return len(expired_keys)


def get_cache_stats() -> dict:
    """Get cache statistics"""
    current_time = time.time()
    active = sum(1 for exp, _ in _cache_store.values() if exp >= current_time)
    expired = len(_cache_store) - active

    return {
        "total_entries": len(_cache_store),
        "active_entries": active,
        "expired_entries": expired,
    }
