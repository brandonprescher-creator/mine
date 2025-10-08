"""
Phenomena-Based Lesson Starters
Engage with real-world phenomena to drive inquiry
"""
from typing import Dict, List, Any, Optional


class Phenomenon:
    """A scientific phenomenon for investigation"""
    def __init__(self, id: int, title: str, description: str, media_url: str, media_type: str):
        self.id = id
        self.title = title
        self.description = description
        self.media_url = media_url
        self.media_type = media_type  # 'image', 'video', 'gif'
        self.subject_area = ''
        self.grade_range = (3, 8)
        self.driving_questions = []
    
    def add_driving_question(self, question: str):
        """Add a question about the phenomenon"""
        self.driving_questions.append(question)
    
    def to_dict(self) -> Dict[str, Any]:
        return {'id': self.id, 'title': self.title, 'description': self.description, 'media_url': self.media_url, 'media_type': self.media_type, 'subject_area': self.subject_area, 'driving_questions': self.driving_questions}


class PhenomenaBasedLesson:
    """Build a lesson around a phenomenon"""
    
    def __init__(self, phenomenon: Phenomenon):
        self.phenomenon = phenomenon
        self.student_observations = []
        self.student_questions = []
        self.student_hypotheses = []
        self.investigation_plan = {}
    
    def record_observation(self, observation: str):
        """Record student observation"""
        self.student_observations.append(observation)
    
    def record_question(self, question: str):
        """Record student question"""
        self.student_questions.append(question)
    
    def record_hypothesis(self, hypothesis: str):
        """Record student hypothesis"""
        self.student_hypotheses.append(hypothesis)
    
    def get_inquiry_prompts(self) -> List[str]:
        """Get prompts for inquiry"""
        return [
            'What do you notice about this phenomenon?',
            'What questions does this raise for you?',
            'What do you think is causing this to happen?',
            'How could you investigate this further?',
            'What evidence would support or refute your ideas?'
        ]
    
    def validate_inquiry(self) -> tuple[bool, List[str]]:
        """Validate student inquiry process"""
        errors = []
        
        if len(self.student_observations) < 2:
            errors.append('Record at least 2 observations')
        
        if len(self.student_questions) < 1:
            errors.append('Ask at least 1 question')
        
        if len(self.student_hypotheses) < 1:
            errors.append('Propose at least 1 hypothesis')
        
        return len(errors) == 0, errors


class PhenomenaLibrary:
    """Library of scientific phenomena"""
    
    def __init__(self):
        self.phenomena: List[Phenomenon] = []
        self._load_examples()
    
    def _load_examples(self):
        """Load example phenomena"""
        examples = [
            Phenomenon(1, 'Ice Melting in Hand', 'Why does ice melt faster in your hand than on the table?', 'ice_melt.jpg', 'image'),
            Phenomenon(2, 'Rainbow Formation', 'How do rainbows form after rain?', 'rainbow.mp4', 'video'),
            Phenomenon(3, 'Balloon Inflation', 'What makes a balloon expand when you blow into it?', 'balloon.gif', 'gif'),
            Phenomenon(4, 'Rust on Metal', 'Why does metal rust when left outside?', 'rust.jpg', 'image'),
            Phenomenon(5, 'Plant Growth', 'How do plants grow toward light?', 'phototropism.mp4', 'video')
        ]
        
        for phenom in examples:
            phenom.subject_area = 'Physical Science'
            phenom.add_driving_question(f'What causes {phenom.title.lower()}?')
            self.phenomena.append(phenom)
    
    def get_by_subject(self, subject: str) -> List[Phenomenon]:
        """Get phenomena by subject area"""
        return [p for p in self.phenomena if subject.lower() in p.subject_area.lower()]
