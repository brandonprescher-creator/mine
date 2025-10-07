"""
Educational API integrations for pulling additional content from free/open sources.
"""

import requests
from typing import List, Dict, Optional
import time
from database import cache_api_response, get_cached_api_response

# API base URLs
WIKIPEDIA_API = "https://en.wikipedia.org/api/rest_v1/page/summary/"
KHAN_ACADEMY_API = "https://www.khanacademy.org/api/v1/"  # Note: Limited public access
OPENSTAX_API = "https://openstax.org/api/v2/"

def search_wikipedia(query: str) -> Optional[Dict]:
    """
    Search Wikipedia for educational content.
    Returns summary, extract, and URL.
    """
    # Check cache first
    cached = get_cached_api_response("wikipedia", query)
    if cached:
        return cached
    
    try:
        # Wikipedia API for page summary
        url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{query.replace(' ', '_')}"
        response = requests.get(url, timeout=5)
        
        if response.status_code == 200:
            data = response.json()
            result = {
                'source': 'Wikipedia',
                'title': data.get('title', ''),
                'summary': data.get('extract', ''),
                'url': data.get('content_urls', {}).get('desktop', {}).get('page', ''),
                'thumbnail': data.get('thumbnail', {}).get('source', '') if 'thumbnail' in data else None
            }
            cache_api_response("wikipedia", query, result)
            return result
    except Exception as e:
        print(f"Wikipedia API error: {e}")
    
    return None

def search_wikibooks(query: str) -> Optional[Dict]:
    """
    Search Wikibooks for educational textbook content.
    """
    cached = get_cached_api_response("wikibooks", query)
    if cached:
        return cached
    
    try:
        # Search Wikibooks
        url = f"https://en.wikibooks.org/w/api.php"
        params = {
            'action': 'query',
            'list': 'search',
            'srsearch': query,
            'format': 'json',
            'srlimit': 3
        }
        response = requests.get(url, params=params, timeout=5)
        
        if response.status_code == 200:
            data = response.json()
            results = data.get('query', {}).get('search', [])
            if results:
                result = {
                    'source': 'Wikibooks',
                    'results': [
                        {
                            'title': r['title'],
                            'snippet': r['snippet'].replace('<span class="searchmatch">', '').replace('</span>', ''),
                            'url': f"https://en.wikibooks.org/wiki/{r['title'].replace(' ', '_')}"
                        }
                        for r in results[:3]
                    ]
                }
                cache_api_response("wikibooks", query, result)
                return result
    except Exception as e:
        print(f"Wikibooks API error: {e}")
    
    return None

def search_educational_youtube(query: str) -> List[Dict]:
    """
    Search for educational videos.
    Note: YouTube API requires an API key. This is a placeholder structure.
    For production, you'd need to set up YouTube Data API.
    """
    # Return curated educational channel suggestions instead
    educational_channels = {
        'math': [
            {'title': 'Khan Academy Math', 'channel': 'Khan Academy', 'url': 'https://www.youtube.com/@khanacademy'},
            {'title': 'Math Antics', 'channel': 'Math Antics', 'url': 'https://www.youtube.com/@mathantics'},
            {'title': 'NumberPhile', 'channel': 'NumberPhile', 'url': 'https://www.youtube.com/@numberphile'},
        ],
        'science': [
            {'title': 'Crash Course Science', 'channel': 'Crash Course', 'url': 'https://www.youtube.com/@crashcourse'},
            {'title': 'SciShow Kids', 'channel': 'SciShow Kids', 'url': 'https://www.youtube.com/@scishowkids'},
            {'title': 'National Geographic Kids', 'channel': 'Nat Geo Kids', 'url': 'https://www.youtube.com/@NatGeoKids'},
        ],
        'reading': [
            {'title': 'Storyline Online', 'channel': 'Storyline Online', 'url': 'https://www.youtube.com/@StorylineOnline'},
            {'title': 'Epic Books for Kids', 'channel': 'Epic!', 'url': 'https://www.youtube.com/@getepic'},
        ]
    }
    
    query_lower = query.lower()
    if any(word in query_lower for word in ['math', 'division', 'multiplication', 'algebra', 'geometry']):
        return educational_channels['math']
    elif any(word in query_lower for word in ['science', 'biology', 'chemistry', 'physics', 'space']):
        return educational_channels['science']
    elif any(word in query_lower for word in ['reading', 'writing', 'story', 'book']):
        return educational_channels['reading']
    
    return []

def get_common_core_standards(subject: str, grade: str = "") -> List[Dict]:
    """
    Get Common Core standards information.
    This is a simplified version - for production, integrate with a standards database.
    """
    standards = {
        'Math': {
            'Division': [
                "CCSS.MATH.CONTENT.3.OA.A.2: Interpret whole-number quotients of whole numbers",
                "CCSS.MATH.CONTENT.3.OA.A.3: Use multiplication and division within 100 to solve word problems",
                "CCSS.MATH.CONTENT.4.NBT.B.6: Find whole-number quotients using strategies based on place value",
                "CCSS.MATH.CONTENT.5.NBT.B.6: Find quotients of whole numbers with up to four-digit dividends"
            ],
            'Fractions': [
                "CCSS.MATH.CONTENT.3.NF.A.1: Understand a fraction as a part of a whole",
                "CCSS.MATH.CONTENT.4.NF.A.1: Explain why fractions are equivalent",
                "CCSS.MATH.CONTENT.5.NF.A.1: Add and subtract fractions with unlike denominators"
            ]
        },
        'ELA': {
            'Reading': [
                "CCSS.ELA-LITERACY.RL.3.1: Ask and answer questions to demonstrate understanding",
                "CCSS.ELA-LITERACY.RL.4.2: Determine theme from details; summarize",
                "CCSS.ELA-LITERACY.RL.5.3: Compare and contrast characters, settings, events"
            ]
        }
    }
    
    results = []
    subject_data = standards.get(subject, {})
    for topic, stds in subject_data.items():
        results.extend([{'standard': s, 'topic': topic} for s in stds])
    
    return results

def search_open_educational_resources(query: str) -> List[Dict]:
    """
    Search for Open Educational Resources (OER).
    Returns curated free resource links.
    """
    resources = []
    
    # Curated OER resources by topic
    oer_links = {
        'math': [
            {'title': 'Khan Academy Math', 'url': 'https://www.khanacademy.org/math', 'description': 'Free math lessons K-12'},
            {'title': 'CK-12 Math', 'url': 'https://www.ck12.org/math/', 'description': 'Free math textbooks and practice'},
            {'title': 'Math is Fun', 'url': 'https://www.mathsisfun.com/', 'description': 'Math explanations and games'},
        ],
        'science': [
            {'title': 'CK-12 Science', 'url': 'https://www.ck12.org/science/', 'description': 'Free science textbooks'},
            {'title': 'Khan Academy Science', 'url': 'https://www.khanacademy.org/science', 'description': 'Science lessons and videos'},
            {'title': 'NASA Kids Club', 'url': 'https://www.nasa.gov/kidsclub/', 'description': 'Space and science resources'},
        ],
        'reading': [
            {'title': 'CommonLit', 'url': 'https://www.commonlit.org/', 'description': 'Free reading passages and lessons'},
            {'title': 'Project Gutenberg', 'url': 'https://www.gutenberg.org/', 'description': 'Free classic books'},
            {'title': 'ReadWorks', 'url': 'https://www.readworks.org/', 'description': 'Reading comprehension passages'},
        ],
        'social_studies': [
            {'title': 'iCivics', 'url': 'https://www.icivics.org/', 'description': 'Civics games and lessons'},
            {'title': 'National Geographic Education', 'url': 'https://education.nationalgeographic.org/', 'description': 'Geography and culture resources'},
        ]
    }
    
    query_lower = query.lower()
    for category, links in oer_links.items():
        if category in query_lower:
            resources.extend(links)
    
    # If no specific match, return general resources
    if not resources:
        resources = [
            {'title': 'Khan Academy', 'url': 'https://www.khanacademy.org/', 'description': 'Free lessons in all subjects'},
            {'title': 'CK-12 Foundation', 'url': 'https://www.ck12.org/', 'description': 'Free K-12 textbooks and resources'},
        ]
    
    return resources

def enrich_lesson_with_api_data(lesson_topic: str, lesson_title: str) -> Dict:
    """
    Enrich a lesson with data from multiple APIs.
    Returns a dictionary with additional resources.
    """
    enriched_data = {
        'wikipedia': None,
        'wikibooks': None,
        'videos': [],
        'standards': [],
        'oer_resources': []
    }
    
    # Search Wikipedia
    wiki_result = search_wikipedia(lesson_topic)
    if wiki_result:
        enriched_data['wikipedia'] = wiki_result
    
    # Search Wikibooks
    wikibooks_result = search_wikibooks(lesson_topic)
    if wikibooks_result:
        enriched_data['wikibooks'] = wikibooks_result
    
    # Get video suggestions
    videos = search_educational_youtube(lesson_topic)
    enriched_data['videos'] = videos
    
    # Get standards
    subject = "Math"  # This would be determined dynamically
    standards = get_common_core_standards(subject)
    enriched_data['standards'] = standards
    
    # Get OER resources
    oer = search_open_educational_resources(lesson_topic)
    enriched_data['oer_resources'] = oer
    
    return enriched_data

def search_all_sources(query: str) -> Dict:
    """
    Search all available educational sources for a query.
    Used for the Q&A / Ask Tutor feature.
    """
    results = {
        'query': query,
        'sources': []
    }
    
    # Wikipedia
    wiki = search_wikipedia(query)
    if wiki:
        results['sources'].append(wiki)
    
    # Wikibooks
    wikibooks = search_wikibooks(query)
    if wikibooks:
        results['sources'].append(wikibooks)
    
    # OER Resources
    oer = search_open_educational_resources(query)
    if oer:
        results['sources'].append({
            'source': 'Open Educational Resources',
            'resources': oer
        })
    
    # Video suggestions
    videos = search_educational_youtube(query)
    if videos:
        results['sources'].append({
            'source': 'Educational Videos',
            'videos': videos
        })
    
    return results

