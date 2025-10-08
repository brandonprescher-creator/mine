"""
Current Events Analysis Tool
Compare sources, analyze bias, check facts
"""
from typing import Dict, List, Any, Optional
from datetime import datetime


class NewsSource:
    """A news source/article"""
    def __init__(self, id: int, title: str, url: str, publisher: str, date: str):
        self.id = id
        self.title = title
        self.url = url
        self.publisher = publisher
        self.date = date
        self.summary = ''
        self.bias_rating = 'neutral'  # 'left', 'center', 'right'
    
    def to_dict(self) -> Dict[str, Any]:
        return {'id': self.id, 'title': self.title, 'url': self.url, 'publisher': self.publisher, 'date': self.date, 'summary': self.summary, 'bias_rating': self.bias_rating}


class CurrentEventsAnalyzer:
    """Analyze and compare current events from multiple sources"""
    
    def __init__(self, topic: str):
        self.topic = topic
        self.sources: List[NewsSource] = []
        self.student_analysis = {'similarities': [], 'differences': [], 'bias_observations': [], 'fact_check': []}
    
    def add_source(self, source: NewsSource):
        """Add a news source"""
        self.sources.append(source)
    
    def get_comparison_prompts(self) -> List[Dict[str, str]]:
        """Get prompts for comparing sources"""
        return [
            {'prompt': 'What facts do all sources agree on?', 'category': 'similarities'},
            {'prompt': 'What information differs between sources?', 'category': 'differences'},
            {'prompt': 'What perspectives or biases do you notice?', 'category': 'bias'},
            {'prompt': 'What questions would you need to answer to verify claims?', 'category': 'fact_check'},
            {'prompt': 'Which source seems most reliable? Why?', 'category': 'reliability'}
        ]
    
    def record_analysis(self, category: str, observation: str):
        """Record student analysis"""
        if category in self.student_analysis:
            self.student_analysis[category].append(observation)
    
    def validate_analysis(self) -> tuple[bool, List[str]]:
        """Validate completeness of analysis"""
        errors = []
        
        if len(self.sources) < 2:
            errors.append('Need at least 2 sources to compare')
        
        if not self.student_analysis['similarities']:
            errors.append('Please identify similarities between sources')
        
        if not self.student_analysis['differences']:
            errors.append('Please identify differences between sources')
        
        return len(errors) == 0, errors
