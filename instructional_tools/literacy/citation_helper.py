"""
Citation Helper
MLA/APA citation generator and bibliography builder
"""
from typing import Dict, List, Any, Optional
from datetime import datetime


class CitationHelper:
    """Citation and Bibliography Tool"""
    
    CITATION_STYLES = ['MLA', 'APA', 'Chicago']
    
    def __init__(self, style: str = 'MLA'):
        self.style = style
        self.sources = []
    
    def add_source(self, source_type: str, source_data: Dict[str, Any]) -> Dict[str, str]:
        """Add and format a source"""
        if source_type == 'book':
            return self._format_book(source_data)
        elif source_type == 'website':
            return self._format_website(source_data)
        elif source_type == 'article':
            return self._format_article(source_data)
        return {'citation': 'Unknown source type'}
    
    def _format_book(self, data: Dict[str, Any]) -> Dict[str, str]:
        """Format book citation"""
        if self.style == 'MLA':
            return {'citation': f"{data.get('author', 'Unknown')}. {data.get('title', 'Untitled')}. {data.get('publisher', '')}, {data.get('year', 'n.d.')}."}
        elif self.style == 'APA':
            return {'citation': f"{data.get('author', 'Unknown')} ({data.get('year', 'n.d.')}). {data.get('title', 'Untitled')}. {data.get('publisher', '')}."}
        return {'citation': ''}
    
    def _format_website(self, data: Dict[str, Any]) -> Dict[str, str]:
        """Format website citation"""
        if self.style == 'MLA':
            return {'citation': f"{data.get('author', 'Unknown')}. \"{data.get('title', 'Untitled')}.\" {data.get('website', '')}, {data.get('date', 'n.d.')}, {data.get('url', '')}."}
        return {'citation': ''}
    
    def _format_article(self, data: Dict[str, Any]) -> Dict[str, str]:
        """Format article citation"""
        return {'citation': f"{data.get('author', 'Unknown')}. \"{data.get('title', 'Untitled')}.\" {data.get('journal', '')}, vol. {data.get('volume', '')}, no. {data.get('issue', '')}, {data.get('year', 'n.d.')}, pp. {data.get('pages', '')}."}
    
    def generate_bibliography(self) -> List[str]:
        """Generate formatted bibliography"""
        return sorted(self.sources, key=lambda x: x.get('author', 'Z'))
