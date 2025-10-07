"""
HTTP Client with retry logic and error handling
"""

import requests
from typing import Dict, Optional, Any
import time
from functools import wraps

DEFAULT_TIMEOUT = 12.0
MAX_RETRIES = 3
RETRY_DELAY = 0.5

def retry_on_failure(max_attempts=MAX_RETRIES, delay=RETRY_DELAY):
    """Decorator for retrying failed requests"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    if attempt < max_attempts - 1:
                        wait_time = delay * (2 ** attempt)  # Exponential backoff
                        time.sleep(wait_time)
                    else:
                        # Last attempt failed
                        print(f"Request failed after {max_attempts} attempts: {e}")
            
            # All attempts failed
            raise last_exception
        
        return wrapper
    return decorator

@retry_on_failure(max_attempts=3, delay=0.5)
def sync_get(url: str, params: Optional[Dict] = None, headers: Optional[Dict] = None) -> Dict[str, Any]:
    """
    Synchronous GET request with retry logic
    """
    if headers is None:
        headers = {}
    
    # Add user agent
    headers['User-Agent'] = 'Ultimate-Badass-Tutor/1.0 (Educational App)'
    
    response = requests.get(url, params=params, headers=headers, timeout=DEFAULT_TIMEOUT)
    response.raise_for_status()
    
    # Try to return JSON
    try:
        return response.json()
    except:
        return {'raw_content': response.text}

def async_get(url: str, params: Optional[Dict] = None, headers: Optional[Dict] = None) -> Dict[str, Any]:
    """
    Async get (for now, just calls sync version)
    In future, could use aiohttp for true async
    """
    return sync_get(url, params, headers)

def safe_get(url: str, params: Optional[Dict] = None, headers: Optional[Dict] = None, default: Any = None) -> Any:
    """
    Safe GET that returns default value on error
    """
    try:
        return sync_get(url, params, headers)
    except Exception as e:
        print(f"Safe GET failed for {url}: {e}")
        return default or {'error': str(e)}

