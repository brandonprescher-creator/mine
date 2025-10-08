"""
Biography & Role Play Activities
Historical figures and perspective-taking
"""
from typing import Dict, List, Any, Optional


class HistoricalFigure:
    """A historical figure for study"""
    def __init__(self, name: str, era: str, significance: str):
        self.name = name
        self.era = era
        self.significance = significance
        self.birth_year = None
        self.death_year = None
        self.accomplishments = []
        self.challenges = []
        self.quotes = []
    
    def to_dict(self) -> Dict[str, Any]:
        return {'name': self.name, 'era': self.era, 'significance': self.significance, 'birth_year': self.birth_year, 'death_year': self.death_year, 'accomplishments': self.accomplishments, 'challenges': self.challenges, 'quotes': self.quotes}


class BiographyAnalysis:
    """Analyze a historical figure"""
    
    def __init__(self, figure: HistoricalFigure):
        self.figure = figure
        self.analysis = {'impact': '', 'challenges': '', 'legacy': '', 'personal_connection': ''}
    
    def get_analysis_prompts(self) -> List[Dict[str, str]]:
        """Get prompts for biography analysis"""
        return [
            {'prompt': f'What was {self.figure.name}\'s greatest impact on history?', 'category': 'impact'},
            {'prompt': 'What challenges did they face? How did they overcome them?', 'category': 'challenges'},
            {'prompt': 'What is their lasting legacy today?', 'category': 'legacy'},
            {'prompt': 'How does their story inspire or teach us?', 'category': 'connection'},
            {'prompt': 'What perspective does their story offer?', 'category': 'perspective'}
        ]


class RolePlayActivity:
    """Role play as a historical figure"""
    
    def __init__(self, figure: HistoricalFigure, scenario: str):
        self.figure = figure
        self.scenario = scenario
        self.student_responses = []
    
    def get_prompts(self) -> List[str]:
        """Get role-play prompts"""
        return [
            f'As {self.figure.name}, how would you respond to: {self.scenario}?',
            'What would be your main concerns?',
            'What actions would you take?',
            'How would your perspective differ from others at the time?'
        ]
    
    def record_response(self, prompt: str, response: str):
        """Record student response"""
        self.student_responses.append({'prompt': prompt, 'response': response, 'timestamp': datetime.utcnow().isoformat()})
