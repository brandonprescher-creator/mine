"""
Geography Quiz Builder
Create custom geography quizzes
"""
from typing import Dict, List, Any
import random


class GeographyQuiz:
    """Build geography quizzes"""
    
    QUIZ_TYPES = ['capitals', 'flags', 'landmarks', 'continents', 'regions', 'physical_features']
    
    def __init__(self, quiz_type: str, region: Optional[str] = 'world'):
        self.quiz_type = quiz_type
        self.region = region
        self.questions = []
    
    def generate_questions(self, num_questions: int = 10) -> List[Dict[str, Any]]:
        """Generate quiz questions"""
        # Simplified - in production would use geography database
        if self.quiz_type == 'capitals':
            sample_data = [
                {'country': 'France', 'capital': 'Paris'},
                {'country': 'Japan', 'capital': 'Tokyo'},
                {'country': 'Egypt', 'capital': 'Cairo'},
                {'country': 'Brazil', 'capital': 'Brasília'},
                {'country': 'Australia', 'capital': 'Canberra'}
            ]
            
            questions = []
            for data in random.sample(sample_data, min(num_questions, len(sample_data))):
                questions.append({'question': f"What is the capital of {data['country']}?", 'answer': data['capital'], 'type': 'capitals'})
            return questions
        
        return []
