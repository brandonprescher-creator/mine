"""
Error Analysis Tool
Spot the mistake exercises for deeper understanding
"""
from typing import Dict, List, Any, Optional
from ..base.activity_base import MathActivity, ActivityType


class ErrorAnalysis(MathActivity):
    """
    Error Analysis Activity
    
    Shows incorrect work and asks students to:
    1. Find the error
    2. Explain what's wrong
    3. Correct the mistake
    """
    
    COMMON_ERROR_TYPES = {
        'sign_error': 'Sign Error (+ vs -)',
        'order_of_operations': 'Order of Operations',
        'distribution': 'Distribution Error',
        'fraction_operations': 'Fraction Operations',
        'decimal_placement': 'Decimal Placement',
        'variable_handling': 'Variable Handling',
        'equation_solving': 'Equation Solving',
        'word_problem_setup': 'Problem Setup'
    }
    
    def __init__(self, activity_id: int, title: str, description: str, incorrect_work: Dict[str, Any], lesson_id: Optional[int] = None, config: Optional[Dict[str, Any]] = None):
        super().__init__(activity_id=activity_id, activity_type=ActivityType.ERROR_ANALYSIS, title=title, description=description, lesson_id=lesson_id, config=config)
        self.problem = incorrect_work.get('problem', '')
        self.incorrect_solution = incorrect_work.get('solution', [])
        self.error_location = incorrect_work.get('error_step', 0)
        self.error_type = incorrect_work.get('error_type', 'general')
        self.correct_solution = incorrect_work.get('correct_solution', [])
    
    def validate_analysis(self, student_analysis: Dict[str, Any]) -> tuple[bool, List[str]]:
        """Validate student's error analysis"""
        errors = []
        
        identified_step = student_analysis.get('error_step')
        explanation = student_analysis.get('explanation', '').strip()
        correction = student_analysis.get('correction', '').strip()
        
        if not identified_step:
            errors.append('Please identify which step contains the error')
        
        if not explanation:
            errors.append('Please explain what is wrong')
        
        if not correction:
            errors.append('Please provide the correct solution')
        
        return len(errors) == 0, errors
    
    def auto_grade(self, submission_data: Dict[str, Any]) -> Dict[str, Any]:
        """Grade the error analysis"""
        identified_step = submission_data.get('error_step')
        
        correct_identification = (identified_step == self.error_location)
        
        feedback_parts = []
        score = 0
        
        if correct_identification:
            feedback_parts.append('✅ Correct! You found the error in step ' + str(self.error_location) + '!\n\n')
            score += 50
        else:
            feedback_parts.append(f'❌ The error is actually in step {self.error_location}.\n\n')
        
        feedback_parts.append('**Your Explanation:**\n')
        feedback_parts.append(submission_data.get('explanation', 'No explanation provided') + '\n\n')
        
        if submission_data.get('correction'):
            feedback_parts.append('**Your Correction:**\n')
            feedback_parts.append(submission_data.get('correction') + '\n')
            score += 50
        
        return {'score': score, 'feedback': ''.join(feedback_parts), 'details': {'identified_correctly': correct_identification}}
