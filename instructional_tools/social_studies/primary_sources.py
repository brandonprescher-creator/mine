"""
Primary Source Analysis Tool
Analyze historical documents with sourcing and contextualization
"""
from typing import Dict, List, Any, Optional
from ..base.activity_base import SocialStudiesActivity, ActivityType


class PrimarySourceAnalyzer(SocialStudiesActivity):
    """
    Primary Source Analysis Tool
    
    SOAP Analysis:
    - Subject: What is it about?
    - Occasion: When/where was it created?
    - Audience: Who was it for?
    - Purpose: Why was it created?
    """
    
    def __init__(self, activity_id: int, title: str, description: str, source_text: str, source_metadata: Dict[str, Any], lesson_id: Optional[int] = None, config: Optional[Dict[str, Any]] = None):
        super().__init__(activity_id=activity_id, activity_type=ActivityType.PRIMARY_SOURCE, title=title, description=description, lesson_id=lesson_id, config=config)
        self.source_text = source_text
        self.source_metadata = source_metadata
        self.requires_sources = True
        self.min_sources = 1
    
    def get_analysis_prompts(self) -> Dict[str, str]:
        """Get SOAP analysis prompts"""
        return {
            'subject': 'What is this document about? Summarize the main topic.',
            'occasion': 'When and where was this created? What was happening at that time?',
            'audience': 'Who was the intended audience? How do you know?',
            'purpose': 'Why was this document created? What was the author trying to accomplish?',
            'perspective': 'What is the author\'s point of view? What biases might they have?',
            'significance': 'Why is this document historically important?'
        }
    
    def validate_analysis(self, analysis: Dict[str, str]) -> tuple[bool, List[str]]:
        """Validate source analysis"""
        errors = []
        required_fields = ['subject', 'occasion', 'audience', 'purpose']
        
        for field in required_fields:
            if not analysis.get(field, '').strip():
                errors.append(f'Please complete: {field.title()}')
        
        return len(errors) == 0, errors
