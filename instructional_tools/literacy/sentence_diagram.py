"""
Sentence Diagrammer
Interactive grammar practice with visual sentence structure
"""
from typing import Dict, List, Any, Optional
from ..base.activity_base import LiteracyActivity, ActivityType


class SentencePart:
    """A part of a sentence (subject, predicate, object, etc.)"""
    def __init__(self, text: str, part_type: str, position: Dict[str, float]):
        self.text = text
        self.part_type = part_type  # 'subject', 'verb', 'object', 'modifier', etc.
        self.position = position  # {'x': 0, 'y': 0}
    
    def to_dict(self) -> Dict[str, Any]:
        return {'text': self.text, 'type': self.part_type, 'position': self.position}


class SentenceDiagrammer(LiteracyActivity):
    """
    Sentence Diagrammer Tool
    
    Features:
    - Drag-and-drop sentence parts
    - Visual grammar structure
    - Multiple sentence types
    - Step-by-step building
    """
    
    PART_TYPES = {
        'subject': {'label': 'Subject', 'color': '#3b82f6'},
        'verb': {'label': 'Verb', 'color': '#ef4444'},
        'object': {'label': 'Object', 'color': '#10b981'},
        'modifier': {'label': 'Modifier', 'color': '#f59e0b'},
        'prep_phrase': {'label': 'Prepositional Phrase', 'color': '#8b5cf6'},
        'conjunction': {'label': 'Conjunction', 'color': '#ec4899'}
    }
    
    def __init__(self, activity_id: int, title: str, description: str, sentence: str, lesson_id: Optional[int] = None, config: Optional[Dict[str, Any]] = None):
        super().__init__(activity_id=activity_id, activity_type=ActivityType.SENTENCE_DIAGRAM, title=title, description=description, lesson_id=lesson_id, config=config)
        self.sentence = sentence
        self.parts: List[SentencePart] = []
        self.difficulty = self.config.get('difficulty', 'simple')
    
    def parse_sentence(self) -> List[str]:
        """Parse sentence into words"""
        return self.sentence.split()
    
    def validate_diagram(self, student_diagram: Dict[str, Any]) -> tuple[bool, List[str]]:
        """Validate student's sentence diagram"""
        errors = []
        
        parts = student_diagram.get('parts', [])
        
        if not parts:
            errors.append('Please add sentence parts to the diagram')
        
        # Check for required parts (subject and verb minimum)
        part_types = [p.get('type') for p in parts]
        if 'subject' not in part_types:
            errors.append('Diagram must include a subject')
        if 'verb' not in part_types:
            errors.append('Diagram must include a verb')
        
        return len(errors) == 0, errors
    
    def get_hints_for_sentence(self) -> List[str]:
        """Get hints for diagramming this sentence"""
        return [
            'Find the verb first - what is the action or state of being?',
            'Find the subject - who or what is doing the action?',
            'Look for objects - who or what receives the action?',
            'Identify modifiers - words that describe other words'
        ]
