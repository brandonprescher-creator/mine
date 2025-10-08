"""
Reading Comprehension Tool
Text annotation and evidence-based responding
"""
from typing import Dict, List, Any, Optional
from ..base.activity_base import LiteracyActivity, ActivityType


class ReadingComprehension(LiteracyActivity):
    """
    Reading Comprehension with Evidence Highlighting
    
    Features:
    - Text highlighting
    - Annotation tools
    - Evidence collection
    - Question answering with text evidence
    """
    
    def __init__(self, activity_id: int, title: str, description: str, passage: str, questions: List[Dict[str, Any]], lesson_id: Optional[int] = None, config: Optional[Dict[str, Any]] = None):
        super().__init__(activity_id=activity_id, activity_type=ActivityType.READING_COMP, title=title, description=description, lesson_id=lesson_id, config=config)
        self.passage = passage
        self.questions = questions
        self.require_text_evidence = self.config.get('require_text_evidence', True)
    
    def validate_answer(self, question_id: int, answer: str, evidence: Optional[str] = None) -> Dict[str, Any]:
        """Validate a comprehension answer"""
        if self.require_text_evidence and not evidence:
            return {'valid': False, 'message': 'Please provide text evidence for your answer'}
        return {'valid': True, 'message': 'Answer recorded'}
