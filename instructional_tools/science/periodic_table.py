"""
Interactive Periodic Table
Element information and practice quizzes
"""
from typing import Dict, List, Any, Optional


class Element:
    """A chemical element"""
    def __init__(self, atomic_number: int, symbol: str, name: str, atomic_mass: float, category: str):
        self.atomic_number = atomic_number
        self.symbol = symbol
        self.name = name
        self.atomic_mass = atomic_mass
        self.category = category
        self.group = None
        self.period = None
        self.electron_config = ''
    
    def to_dict(self) -> Dict[str, Any]:
        return {'atomic_number': self.atomic_number, 'symbol': self.symbol, 'name': self.name, 'atomic_mass': self.atomic_mass, 'category': self.category, 'group': self.group, 'period': self.period}


class InteractivePeriodicTable:
    """Interactive Periodic Table Tool"""
    
    ELEMENT_CATEGORIES = {
        'alkali_metal': {'name': 'Alkali Metals', 'color': '#ff6b6b'},
        'alkaline_earth': {'name': 'Alkaline Earth Metals', 'color': '#ffd93d'},
        'transition_metal': {'name': 'Transition Metals', 'color': '#6bcf7f'},
        'metalloid': {'name': 'Metalloids', 'color': '#4d96ff'},
        'nonmetal': {'name': 'Nonmetals', 'color': '#a78bfa'},
        'halogen': {'name': 'Halogens', 'color': '#fb8b24'},
        'noble_gas': {'name': 'Noble Gases', 'color': '#00f5ff'}
    }
    
    def __init__(self):
        self.elements: Dict[int, Element] = {}
        self._load_essential_elements()
    
    def _load_essential_elements(self):
        """Load essential elements (simplified)"""
        essential = [
            (1, 'H', 'Hydrogen', 1.008, 'nonmetal'),
            (2, 'He', 'Helium', 4.003, 'noble_gas'),
            (6, 'C', 'Carbon', 12.011, 'nonmetal'),
            (7, 'N', 'Nitrogen', 14.007, 'nonmetal'),
            (8, 'O', 'Oxygen', 15.999, 'nonmetal'),
            (11, 'Na', 'Sodium', 22.990, 'alkali_metal'),
            (17, 'Cl', 'Chlorine', 35.45, 'halogen'),
            (26, 'Fe', 'Iron', 55.845, 'transition_metal'),
            (79, 'Au', 'Gold', 196.967, 'transition_metal')
        ]
        
        for num, sym, name, mass, cat in essential:
            self.elements[num] = Element(num, sym, name, mass, cat)
    
    def get_element(self, identifier: Any) -> Optional[Element]:
        """Get element by number, symbol, or name"""
        if isinstance(identifier, int):
            return self.elements.get(identifier)
        
        identifier_str = str(identifier).lower()
        for element in self.elements.values():
            if element.symbol.lower() == identifier_str or element.name.lower() == identifier_str:
                return element
        return None
    
    def generate_quiz(self, num_questions: int = 10, categories: Optional[List[str]] = None) -> List[Dict[str, Any]]:
        """Generate a periodic table quiz"""
        all_elements = list(self.elements.values())
        
        if categories:
            all_elements = [e for e in all_elements if e.category in categories]
        
        quiz_elements = random.sample(all_elements, min(num_questions, len(all_elements)))
        
        questions = []
        for element in quiz_elements:
            question_type = random.choice(['symbol', 'name', 'number'])
            
            if question_type == 'symbol':
                questions.append({'type': 'symbol', 'question': f'What is the symbol for {element.name}?', 'answer': element.symbol, 'element': element.name})
            elif question_type == 'name':
                questions.append({'type': 'name', 'question': f'What element has the symbol {element.symbol}?', 'answer': element.name, 'element': element.symbol})
            else:
                questions.append({'type': 'number', 'question': f'What is the atomic number of {element.name}?', 'answer': str(element.atomic_number), 'element': element.name})
        
        return questions
