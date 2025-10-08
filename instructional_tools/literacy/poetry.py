"""
Poetry & Creative Writing
Poetry forms, challenges, and sharing
"""
from typing import Dict, List, Any, Optional


class PoetryForm:
    """A poetry form/structure"""
    def __init__(self, name: str, description: str, structure: Dict[str, Any], example: str):
        self.name = name
        self.description = description
        self.structure = structure
        self.example = example
    
    def to_dict(self) -> Dict[str, Any]:
        return {'name': self.name, 'description': self.description, 'structure': self.structure, 'example': self.example}


class PoetryChallenge:
    """Poetry writing challenges"""
    
    POETRY_FORMS = {
        'haiku': PoetryForm('Haiku', '3 lines: 5-7-5 syllables', {'lines': 3, 'syllable_pattern': [5, 7, 5]}, 'An old silent pond\nA frog jumps into the pond—\nSplash! Silence again.'),
        'acrostic': PoetryForm('Acrostic', 'First letters spell a word', {'lines': 'variable', 'pattern': 'first_letter_spells_word'}, 'Sunshine bright and warm\nUmbrella stays at home\nNo clouds in the sky'),
        'limerick': PoetryForm('Limerick', '5 lines, AABBA rhyme', {'lines': 5, 'rhyme_scheme': 'AABBA'}, 'There once was a student so bright\nWho studied all through the night\nWith effort and care\nSuccess filled the air\nAnd learning became pure delight'),
        'free_verse': PoetryForm('Free Verse', 'No rules, pure expression', {'lines': 'any', 'rules': 'none'}, 'Words dance\nAcross the page\nFreedom in every line')
    }
    
    def __init__(self, form_name: str, prompt: Optional[str] = None):
        self.form = self.POETRY_FORMS.get(form_name, self.POETRY_FORMS['free_verse'])
        self.prompt = prompt
        self.submissions = []
    
    def validate_poem(self, poem_text: str) -> tuple[bool, List[str]]:
        """Validate poem follows form rules"""
        errors = []
        lines = poem_text.strip().split('\n')
        
        if self.form.name == 'haiku':
            if len(lines) != 3:
                errors.append('Haiku must have exactly 3 lines')
            # Syllable counting would go here
        
        elif self.form.name == 'limerick':
            if len(lines) != 5:
                errors.append('Limerick must have exactly 5 lines')
        
        return len(errors) == 0, errors
