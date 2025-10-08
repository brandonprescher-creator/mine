"""
Interactive Timeline Builder
Create and analyze historical timelines
"""
from typing import Dict, List, Any, Optional
from datetime import datetime


class TimelineEvent:
    """A single event in a timeline"""
    def __init__(self, id: int, date: str, title: str, description: str, significance: Optional[str] = None, image_url: Optional[str] = None):
        self.id = id
        self.date = date
        self.title = title
        self.description = description
        self.significance = significance
        self.image_url = image_url
    
    def to_dict(self) -> Dict[str, Any]:
        return {'id': self.id, 'date': self.date, 'title': self.title, 'description': self.description, 'significance': self.significance, 'image_url': self.image_url}


class TimelineBuilder:
    """Interactive Timeline Builder"""
    
    def __init__(self, title: str, start_date: Optional[str] = None, end_date: Optional[str] = None):
        self.title = title
        self.start_date = start_date
        self.end_date = end_date
        self.events: List[TimelineEvent] = []
        self.event_id_counter = 0
    
    def add_event(self, date: str, title: str, description: str, significance: Optional[str] = None, image_url: Optional[str] = None) -> TimelineEvent:
        """Add an event to the timeline"""
        event = TimelineEvent(self.event_id_counter, date, title, description, significance, image_url)
        self.events.append(event)
        self.event_id_counter += 1
        return event
    
    def get_chronological_events(self) -> List[TimelineEvent]:
        """Get events in chronological order"""
        return sorted(self.events, key=lambda e: e.date)
    
    def validate_timeline(self) -> tuple[bool, List[str]]:
        """Validate timeline completeness"""
        errors = []
        
        if len(self.events) < 3:
            errors.append('Timeline should have at least 3 events')
        
        # Check for duplicate dates
        dates = [e.date for e in self.events]
        if len(dates) != len(set(dates)):
            errors.append('Some events have duplicate dates')
        
        return len(errors) == 0, errors
    
    def to_dict(self) -> Dict[str, Any]:
        """Export timeline data"""
        return {'title': self.title, 'start_date': self.start_date, 'end_date': self.end_date, 'events': [e.to_dict() for e in self.get_chronological_events()], 'total_events': len(self.events)}
