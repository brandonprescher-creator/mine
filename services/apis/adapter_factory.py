"""
API Adapter Factory
Central registry for all education API adapters
"""
from .base import APIAdapter
from .wikipedia_adapter import WikipediaAdapter
from .datamuse_adapter import DatamuseAdapter
from .openlibrary_adapter import OpenLibraryAdapter
from .nasa_adapter import NASAAdapter
from .usgs_adapter import USGSAdapter

# Registry of all adapters
ADAPTERS = {
    'wikipedia': WikipediaAdapter,
    'datamuse': DatamuseAdapter,
    'openlibrary': OpenLibraryAdapter,
    'nasa': NASAAdapter,
    'usgs': USGSAdapter,
    # More will be added
}


def get_adapter(name):
    """Get an adapter instance by name"""
    adapter_class = ADAPTERS.get(name.lower())
    return adapter_class() if adapter_class else None


def list_adapters():
    """List all available adapters"""
    return list(ADAPTERS.keys())


def search_all(topic, subject=None, grade_band=None, media_type=None, limit=10):
    """Search all adapters"""
    all_results = []
    
    for name, adapter_class in ADAPTERS.items():
        adapter = adapter_class()
        try:
            results = adapter.search(
                topic=topic,
                subject=subject,
                grade_band=grade_band,
                media_type=media_type,
                limit=limit
            )
            all_results.extend(results)
        except Exception as e:
            print(f"Error searching {name}: {e}")
            continue
    
    return all_results
