"""
OPEN LEARNING MODULE
Integrates 50+ free education APIs for unlimited content!
"""

from .http_client import async_get, sync_get
from .cache import cache_get, cache_set, clear_cache
from .schemas import ContentCard, QAItem, SchoolData, ArtworkData

__all__ = [
    "async_get",
    "sync_get",
    "cache_get",
    "cache_set",
    "clear_cache",
    "ContentCard",
    "QAItem",
    "SchoolData",
    "ArtworkData",
]
