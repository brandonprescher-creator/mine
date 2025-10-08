"""
Essay Outline Builder
Scaffold essay writing from thesis to conclusion
"""
from typing import Dict, List, Any, Optional
from ..base.activity_base import LiteracyActivity, ActivityType


class EssayBuilder(LiteracyActivity):
    """Essay Outline and Writing Tool"""
    
    def __init__(self, activity_id: int, title: str, description: str, prompt: str, lesson_id: Optional[int] = None, config: Optional[Dict[str, Any]] = None):
        super().__init__(activity_id=activity_id, activity_type=ActivityType.ESSAY_OUTLINE, title=title, description=description, lesson_id=lesson_id, config=config)
        self.prompt = prompt
        self.required_paragraphs = self.config.get('required_paragraphs', 5)
        self.min_word_count = self.config.get('min_word_count', 300)
    
    def get_scaffold_template(self) -> Dict[str, Any]:
        """Get essay scaffold template"""
        return {
            'introduction': {'thesis': '', 'hook': '', 'background': ''},
            'body_paragraphs': [{'topic_sentence': '', 'evidence': '', 'analysis': '', 'transition': ''} for _ in range(self.required_paragraphs - 2)],
            'conclusion': {'restate_thesis': '', 'summary': '', 'final_thought': ''}
        }
