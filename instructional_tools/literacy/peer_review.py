"""
Peer Review Checklist
Structured peer and self-review tools
"""
from typing import Dict, List, Any, Optional
from datetime import datetime


class ReviewChecklist:
    """A checklist for reviewing student work"""
    
    def __init__(self, title: str, items: List[Dict[str, Any]]):
        self.title = title
        self.items = items
    
    def to_dict(self) -> Dict[str, Any]:
        return {'title': self.title, 'items': self.items}


class PeerReview:
    """
    Peer Review System
    
    Features:
    - Structured checklists
    - Constructive feedback prompts
    - Anonymous reviews (optional)
    - Revision suggestions
    """
    
    def __init__(self, work_id: int, reviewer_id: int, checklist: ReviewChecklist):
        self.work_id = work_id
        self.reviewer_id = reviewer_id
        self.checklist = checklist
        self.responses = {}
        self.comments = {}
        self.overall_feedback = ''
        self.strengths = []
        self.suggestions = []
    
    def record_response(self, item_id: int, response: bool, comment: Optional[str] = None):
        """Record response to a checklist item"""
        self.responses[item_id] = response
        if comment:
            self.comments[item_id] = comment
    
    def add_strength(self, strength: str):
        """Add a strength observation"""
        self.strengths.append(strength)
    
    def add_suggestion(self, suggestion: str):
        """Add a suggestion for improvement"""
        self.suggestions.append(suggestion)
    
    def validate_review(self) -> tuple[bool, List[str]]:
        """Validate review is complete"""
        errors = []
        
        if len(self.responses) < len(self.checklist.items):
            errors.append('Please complete all checklist items')
        
        if not self.strengths:
            errors.append('Please identify at least one strength')
        
        if not self.suggestions:
            errors.append('Please provide at least one suggestion')
        
        return len(errors) == 0, errors
    
    def to_dict(self) -> Dict[str, Any]:
        """Export review data"""
        return {
            'work_id': self.work_id,
            'reviewer_id': self.reviewer_id,
            'checklist_responses': self.responses,
            'comments': self.comments,
            'overall_feedback': self.overall_feedback,
            'strengths': self.strengths,
            'suggestions': self.suggestions,
            'is_complete': self.validate_review()[0]
        }
    
    @staticmethod
    def create_writing_checklist() -> ReviewChecklist:
        """Create a standard writing review checklist"""
        return ReviewChecklist(
            title='Writing Review Checklist',
            items=[
                {'id': 1, 'text': 'Does the writing have a clear thesis or main idea?', 'category': 'content'},
                {'id': 2, 'text': 'Is there sufficient evidence to support the main idea?', 'category': 'content'},
                {'id': 3, 'text': 'Are paragraphs well-organized with topic sentences?', 'category': 'organization'},
                {'id': 4, 'text': 'Are transitions used effectively between ideas?', 'category': 'organization'},
                {'id': 5, 'text': 'Is the writing clear and easy to understand?', 'category': 'clarity'},
                {'id': 6, 'text': 'Are sentences varied in structure and length?', 'category': 'style'},
                {'id': 7, 'text': 'Is spelling and grammar correct?', 'category': 'mechanics'},
                {'id': 8, 'text': 'Does the conclusion effectively wrap up the writing?', 'category': 'content'}
            ]
        )
