"""
Base API Adapter Interface
All education API adapters implement this interface
"""
from typing import List, Dict, Any, Optional
import requests
from abc import ABC, abstractmethod


class APIAdapter(ABC):
    """Base class for all API adapters"""
    
    def __init__(self):
        self.name = self.__class__.__name__.replace('Adapter', '')
        self.base_url = ''
        self.rate_limit = 100  # requests per minute
        self.timeout = 10  # seconds
    
    @abstractmethod
    def search(self, topic: str, subject: Optional[str] = None, grade_band: Optional[str] = None, 
               media_type: Optional[str] = None, limit: int = 10) -> List[Dict[str, Any]]:
        """
        Search this API and return normalized results
        
        Returns List of Resource dicts:
        {
            'title': str,
            'url': str,
            'summary': str,
            'subject': str,
            'grade_band': str,  # 'K-2', '3-5', '6-8', '9-12'
            'topics': List[str],
            'media_type': str,  # 'video', 'article', 'interactive', etc.
            'length_minutes': int,
            'provider': str,
            'attribution': str,
            'thumbnail': Optional[str]
        }
        """
        pass
    
    def _make_request(self, url: str, params: Optional[Dict] = None, headers: Optional[Dict] = None) -> Optional[Dict]:
        """Make HTTP request with error handling"""
        try:
            response = requests.get(url, params=params, headers=headers, timeout=self.timeout)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"API request failed: {e}")
            return None
    
    def normalize_grade_band(self, grade_level: Optional[int]) -> str:
        """Normalize grade level to band"""
        if not grade_level:
            return 'All'
        if grade_level <= 2:
            return 'K-2'
        elif grade_level <= 5:
            return '3-5'
        elif grade_level <= 8:
            return '6-8'
        else:
            return '9-12'
