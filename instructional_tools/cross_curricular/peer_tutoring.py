"""
Peer Tutoring System
'Teach it back' prompts and collaborative learning
"""
from typing import Dict, List, Any, Optional
from datetime import datetime


class TeachBackPrompt:
    """A prompt for students to explain concepts"""
    def __init__(self, concept: str, prompts: List[str], success_criteria: List[str]):
        self.concept = concept
        self.prompts = prompts
        self.success_criteria = success_criteria
    
    def to_dict(self) -> Dict[str, Any]:
        return {'concept': self.concept, 'prompts': self.prompts, 'success_criteria': self.success_criteria}


class PeerTutoringSession:
    """A peer tutoring session"""
    
    def __init__(self, tutor_id: int, tutee_id: int, topic: str):
        self.tutor_id = tutor_id
        self.tutee_id = tutee_id
        self.topic = topic
        self.started_at = datetime.utcnow().isoformat()
        self.ended_at = None
        self.tutor_explanation = ''
        self.tutee_understanding = 0  # 1-5 scale
        self.notes = []
    
    def record_explanation(self, explanation: str):
        """Record tutor's explanation"""
        self.tutor_explanation = explanation
    
    def record_understanding(self, level: int):
        """Record tutee's understanding level"""
        self.tutee_understanding = max(1, min(5, level))
    
    def add_note(self, note: str):
        """Add a session note"""
        self.notes.append({'text': note, 'timestamp': datetime.utcnow().isoformat()})
    
    def end_session(self):
        """End the tutoring session"""
        self.ended_at = datetime.utcnow().isoformat()
    
    def to_dict(self) -> Dict[str, Any]:
        return {'tutor_id': self.tutor_id, 'tutee_id': self.tutee_id, 'topic': self.topic, 'started_at': self.started_at, 'ended_at': self.ended_at, 'explanation': self.tutor_explanation, 'understanding_level': self.tutee_understanding, 'notes': self.notes}


class PeerTutoringSystem:
    """Manage peer tutoring activities"""
    
    TEACH_BACK_PROMPTS = {
        'math': [
            'Explain this concept to a friend who missed class today',
            'What are the key steps someone should follow?',
            'What mistakes should someone avoid?',
            'Can you show an example and explain each step?'
        ],
        'science': [
            'Explain this scientific concept in your own words',
            'What real-world example would help someone understand?',
            'How would you demonstrate this to a younger student?',
            'What questions might someone have about this?'
        ],
        'literacy': [
            'Explain this reading strategy to a classmate',
            'What tips would help someone write better?',
            'How can you break this down into simple steps?',
            'What example would make this clearer?'
        ],
        'general': [
            'Teach this concept to someone who doesn\'t know it',
            'What are the most important points to remember?',
            'How is this useful in real life?',
            'What helped YOU understand this?'
        ]
    }
    
    @staticmethod
    def get_prompts(subject: str = 'general') -> List[str]:
        """Get teach-back prompts for a subject"""
        return PeerTutoringSystem.TEACH_BACK_PROMPTS.get(subject, PeerTutoringSystem.TEACH_BACK_PROMPTS['general'])
    
    @staticmethod
    def create_success_criteria(concept: str) -> List[str]:
        """Generate success criteria for teaching back"""
        return [
            'Student explains concept in their own words',
            'Student provides clear examples',
            'Student answers questions accurately',
            'Explanation is organized and easy to follow',
            'Student checks for understanding'
        ]
