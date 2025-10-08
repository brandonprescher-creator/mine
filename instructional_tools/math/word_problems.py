"""
Word Problem Breakdown Tool
Scaffold students through solving word problems
"""
from typing import Dict, List, Any, Optional
from ..base.activity_base import MathActivity, ActivityType


class WordProblemBreakdown(MathActivity):
    """
    Word Problem Breakdown Tool
    
    Scaffolds:
    1. Read and understand
    2. Identify known/unknown
    3. Choose strategy
    4. Solve
    5. Check answer
    """
    
    def __init__(self, activity_id: int, title: str, description: str, problem_text: str, lesson_id: Optional[int] = None, config: Optional[Dict[str, Any]] = None):
        super().__init__(activity_id=activity_id, activity_type=ActivityType.WORD_PROBLEM, title=title, description=description, lesson_id=lesson_id, config=config)
        self.problem_text = problem_text
        self.solution_steps = self.config.get('solution_steps', [])
    
    def get_scaffold_prompts(self) -> List[Dict[str, str]]:
        """Get prompts for each stage of problem solving"""
        return [
            {'stage': 'understand', 'prompt': 'Read the problem carefully. What is the problem asking you to find?'},
            {'stage': 'identify', 'prompt': 'What information do you know? What do you need to find?'},
            {'stage': 'plan', 'prompt': 'What operation(s) will you use? Draw a diagram if helpful.'},
            {'stage': 'solve', 'prompt': 'Show your work step-by-step. Label each step.'},
            {'stage': 'check', 'prompt': 'Does your answer make sense? Check your work.'}
        ]
    
    def validate_breakdown(self, breakdown: Dict[str, Any]) -> tuple[bool, List[str]]:
        """Validate student's problem breakdown"""
        errors = []
        required_fields = ['known_info', 'unknown', 'strategy', 'solution', 'check']
        
        for field in required_fields:
            if not breakdown.get(field, '').strip():
                errors.append(f'Please complete: {field.replace("_", " ").title()}')
        
        return len(errors) == 0, errors
