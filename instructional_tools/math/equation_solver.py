"""
Step-by-step Equation Solver
Shows multiple solving strategies with progressive hints
"""
from typing import Dict, List, Any, Optional, Tuple
import re
from ..base.activity_base import MathActivity, ActivityType
from ..cross_curricular.hints import HintSystem


class EquationStep:
    """A single step in solving an equation"""
    
    def __init__(
        self,
        step_number: int,
        description: str,
        equation: str,
        operation: str,
        explanation: str
    ):
        self.step_number = step_number
        self.description = description
        self.equation = equation
        self.operation = operation
        self.explanation = explanation
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            'step_number': self.step_number,
            'description': self.description,
            'equation': self.equation,
            'operation': self.operation,
            'explanation': self.explanation
        }


class SolutionStrategy:
    """A strategy for solving an equation"""
    
    def __init__(
        self,
        name: str,
        description: str,
        steps: List[EquationStep],
        difficulty: str = 'medium'
    ):
        self.name = name
        self.description = description
        self.steps = steps
        self.difficulty = difficulty
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            'name': self.name,
            'description': self.description,
            'steps': [s.to_dict() for s in self.steps],
            'difficulty': self.difficulty,
            'total_steps': len(self.steps)
        }


class EquationSolver(MathActivity):
    """
    Step-by-step Equation Solver
    
    Features:
    - Multiple solution strategies
    - Progressive hints
    - Step-by-step validation
    - Visual representations
    """
    
    def __init__(
        self,
        activity_id: int,
        title: str,
        description: str,
        equation: str,
        lesson_id: Optional[int] = None,
        config: Optional[Dict[str, Any]] = None
    ):
        super().__init__(
            activity_id=activity_id,
            activity_type=ActivityType.EQUATION_SOLVER,
            title=title,
            description=description,
            lesson_id=lesson_id,
            config=config
        )
        
        self.equation = equation
        self.strategies = []
        self.current_strategy = None
        self.student_steps = []
        
        # Generate solution strategies
        self._generate_strategies()
    
    def _generate_strategies(self):
        """Generate multiple solving strategies"""
        # For demonstration - would be more sophisticated in production
        equation_type = self._classify_equation()
        
        if equation_type == 'linear':
            self.strategies = self._solve_linear_strategies()
        elif equation_type == 'quadratic':
            self.strategies = self._solve_quadratic_strategies()
        else:
            self.strategies = self._solve_general_strategies()
    
    def _classify_equation(self) -> str:
        """Classify the equation type"""
        if 'x^2' in self.equation or 'x²' in self.equation:
            return 'quadratic'
        elif 'x' in self.equation:
            return 'linear'
        else:
            return 'general'
    
    def _solve_linear_strategies(self) -> List[SolutionStrategy]:
        """Generate strategies for linear equations"""
        # Example: 2x + 5 = 13
        
        # Strategy 1: Standard algebraic method
        strategy1 = SolutionStrategy(
            name='Algebraic Method',
            description='Use inverse operations to isolate the variable',
            steps=[
                EquationStep(
                    1,
                    'Start with the equation',
                    self.equation,
                    'given',
                    'This is our starting equation'
                ),
                EquationStep(
                    2,
                    'Subtract constant from both sides',
                    '2x = 8',
                    'subtraction',
                    'We subtract 5 from both sides to isolate terms with x'
                ),
                EquationStep(
                    3,
                    'Divide both sides by coefficient',
                    'x = 4',
                    'division',
                    'We divide both sides by 2 to solve for x'
                )
            ],
            difficulty='beginner'
        )
        
        # Strategy 2: Working backwards
        strategy2 = SolutionStrategy(
            name='Working Backwards',
            description='Undo operations in reverse order',
            steps=[
                EquationStep(
                    1,
                    'Identify the operations on x',
                    self.equation,
                    'analysis',
                    'x is multiplied by 2, then 5 is added'
                ),
                EquationStep(
                    2,
                    'Work backwards: Subtract 5',
                    '2x = 8',
                    'subtraction',
                    'First undo the addition: 13 - 5 = 8'
                ),
                EquationStep(
                    3,
                    'Work backwards: Divide by 2',
                    'x = 4',
                    'division',
                    'Then undo the multiplication: 8 ÷ 2 = 4'
                )
            ],
            difficulty='beginner'
        )
        
        return [strategy1, strategy2]
    
    def _solve_quadratic_strategies(self) -> List[SolutionStrategy]:
        """Generate strategies for quadratic equations"""
        return [
            SolutionStrategy(
                name='Quadratic Formula',
                description='Use the quadratic formula',
                steps=[],
                difficulty='advanced'
            ),
            SolutionStrategy(
                name='Factoring',
                description='Factor and use zero product property',
                steps=[],
                difficulty='intermediate'
            )
        ]
    
    def _solve_general_strategies(self) -> List[SolutionStrategy]:
        """General solving strategies"""
        return [
            SolutionStrategy(
                name='Standard Method',
                description='Solve step by step',
                steps=[],
                difficulty='medium'
            )
        ]
    
    def check_step(
        self,
        step_number: int,
        student_equation: str,
        strategy_name: Optional[str] = None
    ) -> Dict[str, Any]:
        """Check if a student's step is correct"""
        
        # Find the strategy
        strategy = None
        if strategy_name:
            strategy = next((s for s in self.strategies if s.name == strategy_name), None)
        else:
            strategy = self.strategies[0] if self.strategies else None
        
        if not strategy or step_number > len(strategy.steps):
            return {
                'correct': False,
                'feedback': 'Invalid step number',
                'hint': ''
            }
        
        expected_step = strategy.steps[step_number - 1]
        
        # Simplified checking - in production would use symbolic math
        student_clean = student_equation.replace(' ', '').lower()
        expected_clean = expected_step.equation.replace(' ', '').lower()
        
        correct = student_clean == expected_clean
        
        return {
            'correct': correct,
            'feedback': expected_step.explanation if correct else 'Not quite right. Try again or use a hint!',
            'hint': self._generate_step_hint(step_number, strategy),
            'expected_equation': expected_step.equation if not correct else None
        }
    
    def _generate_step_hint(
        self,
        step_number: int,
        strategy: SolutionStrategy
    ) -> str:
        """Generate a hint for a specific step"""
        if step_number > len(strategy.steps):
            return ''
        
        step = strategy.steps[step_number - 1]
        return f"Try using {step.operation}. {step.description}"
    
    def generate_hints(self, current_step: int = 0) -> List[Dict[str, str]]:
        """Generate progressive hints for the equation"""
        if not self.strategies:
            return []
        
        strategy = self.strategies[0]
        
        if current_step == 0:
            # General hints
            return HintSystem.create_math_hints('equation', {'equation': self.equation})
        else:
            # Specific step hints
            if current_step <= len(strategy.steps):
                step = strategy.steps[current_step - 1]
                return [
                    {
                        'level': 'mild',
                        'hint': f'Think about what operation is needed: {step.operation}'
                    },
                    {
                        'level': 'medium',
                        'hint': f'{step.description}'
                    },
                    {
                        'level': 'strong',
                        'hint': f'{step.explanation}. The result is: {step.equation}'
                    }
                ]
            return []
    
    def validate_submission(self, submission_data: Dict[str, Any]) -> Tuple[bool, List[str]]:
        """Validate a complete solution submission"""
        errors = []
        
        student_steps = submission_data.get('steps', [])
        chosen_strategy = submission_data.get('strategy')
        
        if not student_steps:
            errors.append('No steps provided')
        
        if self.show_work_required and len(student_steps) < 2:
            errors.append('Please show at least 2 steps of your work')
        
        return len(errors) == 0, errors
    
    def auto_grade(self, submission_data: Dict[str, Any]) -> Dict[str, Any]:
        """Auto-grade the equation solution"""
        student_steps = submission_data.get('steps', [])
        strategy_used = submission_data.get('strategy', 'Algebraic Method')
        
        # Find the strategy
        strategy = next((s for s in self.strategies if s.name == strategy_used), self.strategies[0])
        
        # Check each step
        correct_steps = 0
        total_steps = len(student_steps)
        
        for i, student_step in enumerate(student_steps):
            result = self.check_step(i + 1, student_step.get('equation', ''), strategy.name)
            if result['correct']:
                correct_steps += 1
        
        accuracy = (correct_steps / total_steps * 100) if total_steps > 0 else 0
        
        feedback_parts = []
        if accuracy == 100:
            feedback_parts.append('🎉 Perfect! All steps are correct!\n\n')
        elif accuracy >= 80:
            feedback_parts.append('Great work! Most steps are correct.\n\n')
        elif accuracy >= 60:
            feedback_parts.append('Good effort. Review the highlighted steps.\n\n')
        else:
            feedback_parts.append('Keep practicing! Let\'s work through this together.\n\n')
        
        feedback_parts.append(f'**Steps Correct:** {correct_steps}/{total_steps}\n')
        feedback_parts.append(f'**Accuracy:** {accuracy:.1f}%\n')
        feedback_parts.append(f'**Strategy Used:** {strategy_used}\n')
        
        return {
            'score': accuracy,
            'feedback': ''.join(feedback_parts),
            'details': {
                'correct_steps': correct_steps,
                'total_steps': total_steps,
                'accuracy': accuracy,
                'strategy': strategy_used
            }
        }
    
    def get_all_strategies(self) -> List[Dict[str, Any]]:
        """Get all solution strategies"""
        return [s.to_dict() for s in self.strategies]
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        base_dict = super().to_dict()
        base_dict.update({
            'equation': self.equation,
            'strategies': self.get_all_strategies(),
            'equation_type': self._classify_equation()
        })
        return base_dict
