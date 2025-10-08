"""
Grading and rubric system for instructional activities
"""
from typing import Dict, List, Any, Optional
from datetime import datetime


class RubricCriterion:
    """A single criterion in a rubric"""
    
    def __init__(
        self,
        name: str,
        description: str,
        max_points: int,
        levels: List[Dict[str, Any]]
    ):
        self.name = name
        self.description = description
        self.max_points = max_points
        self.levels = levels  # [{'points': 4, 'description': 'Excellent'}, ...]
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            'name': self.name,
            'description': self.description,
            'max_points': self.max_points,
            'levels': self.levels
        }


class Rubric:
    """Grading rubric for an activity"""
    
    def __init__(
        self,
        title: str,
        criteria: List[RubricCriterion],
        description: Optional[str] = None
    ):
        self.title = title
        self.description = description
        self.criteria = criteria
    
    @property
    def total_points(self) -> int:
        return sum(c.max_points for c in self.criteria)
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            'title': self.title,
            'description': self.description,
            'total_points': self.total_points,
            'criteria': [c.to_dict() for c in self.criteria]
        }
    
    def calculate_score(self, scores: Dict[str, int]) -> Dict[str, Any]:
        """
        Calculate total score from criterion scores
        scores: {'criterion_name': points_earned, ...}
        """
        total_earned = sum(scores.values())
        percentage = (total_earned / self.total_points) * 100 if self.total_points > 0 else 0
        
        return {
            'total_earned': total_earned,
            'total_possible': self.total_points,
            'percentage': round(percentage, 2),
            'letter_grade': self._get_letter_grade(percentage),
            'criterion_scores': scores
        }
    
    def _get_letter_grade(self, percentage: float) -> str:
        """Convert percentage to letter grade"""
        if percentage >= 90:
            return 'A'
        elif percentage >= 80:
            return 'B'
        elif percentage >= 70:
            return 'C'
        elif percentage >= 60:
            return 'D'
        else:
            return 'F'


class GradingSystem:
    """System for managing grading and feedback"""
    
    @staticmethod
    def create_basic_rubric(
        activity_type: str,
        max_points: int = 100
    ) -> Rubric:
        """Create a basic rubric for common activity types"""
        
        rubrics = {
            'work_notebook': Rubric(
                title='Show Your Work Assessment',
                description='Evaluates completeness and clarity of work shown',
                criteria=[
                    RubricCriterion(
                        name='Completeness',
                        description='All steps and work shown',
                        max_points=25,
                        levels=[
                            {'points': 25, 'description': 'All work clearly shown with every step'},
                            {'points': 20, 'description': 'Most work shown, minor gaps'},
                            {'points': 15, 'description': 'Some work shown, significant gaps'},
                            {'points': 10, 'description': 'Minimal work shown'},
                            {'points': 0, 'description': 'No work shown'}
                        ]
                    ),
                    RubricCriterion(
                        name='Organization',
                        description='Work is organized and easy to follow',
                        max_points=25,
                        levels=[
                            {'points': 25, 'description': 'Exceptionally organized and labeled'},
                            {'points': 20, 'description': 'Well organized, easy to follow'},
                            {'points': 15, 'description': 'Somewhat organized'},
                            {'points': 10, 'description': 'Disorganized but understandable'},
                            {'points': 0, 'description': 'Cannot follow the work'}
                        ]
                    ),
                    RubricCriterion(
                        name='Accuracy',
                        description='Work demonstrates correct understanding',
                        max_points=30,
                        levels=[
                            {'points': 30, 'description': 'All work is correct'},
                            {'points': 25, 'description': 'Minor errors only'},
                            {'points': 20, 'description': 'Some significant errors'},
                            {'points': 15, 'description': 'Many errors but shows effort'},
                            {'points': 0, 'description': 'Incorrect throughout'}
                        ]
                    ),
                    RubricCriterion(
                        name='Explanation',
                        description='Student explains their thinking',
                        max_points=20,
                        levels=[
                            {'points': 20, 'description': 'Clear, thorough explanations'},
                            {'points': 15, 'description': 'Good explanations for most steps'},
                            {'points': 10, 'description': 'Basic explanations provided'},
                            {'points': 5, 'description': 'Minimal explanation'},
                            {'points': 0, 'description': 'No explanation'}
                        ]
                    )
                ]
            ),
            'essay': Rubric(
                title='Essay Rubric',
                description='Evaluates writing quality and organization',
                criteria=[
                    RubricCriterion(
                        name='Thesis/Argument',
                        description='Clear, focused thesis statement',
                        max_points=20,
                        levels=[
                            {'points': 20, 'description': 'Strong, clear, focused thesis'},
                            {'points': 15, 'description': 'Clear thesis, minor issues'},
                            {'points': 10, 'description': 'Thesis present but unclear'},
                            {'points': 5, 'description': 'Weak thesis'},
                            {'points': 0, 'description': 'No thesis'}
                        ]
                    ),
                    RubricCriterion(
                        name='Evidence',
                        description='Supporting evidence and examples',
                        max_points=30,
                        levels=[
                            {'points': 30, 'description': 'Strong, relevant evidence throughout'},
                            {'points': 25, 'description': 'Good evidence, well integrated'},
                            {'points': 20, 'description': 'Adequate evidence'},
                            {'points': 10, 'description': 'Weak or irrelevant evidence'},
                            {'points': 0, 'description': 'No evidence'}
                        ]
                    ),
                    RubricCriterion(
                        name='Organization',
                        description='Logical structure and flow',
                        max_points=25,
                        levels=[
                            {'points': 25, 'description': 'Excellent organization and flow'},
                            {'points': 20, 'description': 'Good organization'},
                            {'points': 15, 'description': 'Adequate organization'},
                            {'points': 10, 'description': 'Poor organization'},
                            {'points': 0, 'description': 'No clear organization'}
                        ]
                    ),
                    RubricCriterion(
                        name='Writing Quality',
                        description='Grammar, spelling, clarity',
                        max_points=25,
                        levels=[
                            {'points': 25, 'description': 'Excellent writing, no errors'},
                            {'points': 20, 'description': 'Good writing, minor errors'},
                            {'points': 15, 'description': 'Adequate writing, some errors'},
                            {'points': 10, 'description': 'Poor writing, many errors'},
                            {'points': 0, 'description': 'Incomprehensible'}
                        ]
                    )
                ]
            ),
            'lab_report': Rubric(
                title='Lab Report Rubric',
                description='Evaluates scientific inquiry and reporting',
                criteria=[
                    RubricCriterion(
                        name='Hypothesis',
                        description='Clear, testable hypothesis',
                        max_points=15,
                        levels=[
                            {'points': 15, 'description': 'Excellent hypothesis, testable'},
                            {'points': 12, 'description': 'Good hypothesis'},
                            {'points': 9, 'description': 'Adequate hypothesis'},
                            {'points': 6, 'description': 'Weak hypothesis'},
                            {'points': 0, 'description': 'No hypothesis'}
                        ]
                    ),
                    RubricCriterion(
                        name='Procedure',
                        description='Clear, detailed methods',
                        max_points=20,
                        levels=[
                            {'points': 20, 'description': 'Detailed, replicable procedure'},
                            {'points': 15, 'description': 'Clear procedure'},
                            {'points': 10, 'description': 'Basic procedure'},
                            {'points': 5, 'description': 'Incomplete procedure'},
                            {'points': 0, 'description': 'No procedure'}
                        ]
                    ),
                    RubricCriterion(
                        name='Data & Analysis',
                        description='Accurate data collection and analysis',
                        max_points=30,
                        levels=[
                            {'points': 30, 'description': 'Excellent data and analysis'},
                            {'points': 25, 'description': 'Good data and analysis'},
                            {'points': 20, 'description': 'Adequate data and analysis'},
                            {'points': 10, 'description': 'Incomplete data/analysis'},
                            {'points': 0, 'description': 'No data/analysis'}
                        ]
                    ),
                    RubricCriterion(
                        name='Conclusion',
                        description='Conclusion relates to hypothesis',
                        max_points=20,
                        levels=[
                            {'points': 20, 'description': 'Excellent conclusion, well supported'},
                            {'points': 15, 'description': 'Good conclusion'},
                            {'points': 10, 'description': 'Basic conclusion'},
                            {'points': 5, 'description': 'Weak conclusion'},
                            {'points': 0, 'description': 'No conclusion'}
                        ]
                    ),
                    RubricCriterion(
                        name='Scientific Communication',
                        description='Proper scientific writing and terminology',
                        max_points=15,
                        levels=[
                            {'points': 15, 'description': 'Excellent scientific communication'},
                            {'points': 12, 'description': 'Good use of scientific language'},
                            {'points': 9, 'description': 'Adequate communication'},
                            {'points': 6, 'description': 'Poor communication'},
                            {'points': 0, 'description': 'Unscientific writing'}
                        ]
                    )
                ]
            )
        }
        
        return rubrics.get(activity_type, rubrics['work_notebook'])
    
    @staticmethod
    def generate_feedback(
        score_percentage: float,
        strengths: List[str],
        areas_for_improvement: List[str]
    ) -> str:
        """Generate formatted feedback based on score and observations"""
        
        feedback_parts = []
        
        # Opening based on score
        if score_percentage >= 90:
            feedback_parts.append("Excellent work! ")
        elif score_percentage >= 80:
            feedback_parts.append("Great job! ")
        elif score_percentage >= 70:
            feedback_parts.append("Good effort! ")
        elif score_percentage >= 60:
            feedback_parts.append("Nice try! ")
        else:
            feedback_parts.append("Keep working on this. ")
        
        # Strengths
        if strengths:
            feedback_parts.append("\n\n**Strengths:**\n")
            for strength in strengths:
                feedback_parts.append(f"- {strength}\n")
        
        # Areas for improvement
        if areas_for_improvement:
            feedback_parts.append("\n**Areas for Improvement:**\n")
            for area in areas_for_improvement:
                feedback_parts.append(f"- {area}\n")
        
        # Encouragement
        feedback_parts.append("\nKeep up the good work!")
        
        return ''.join(feedback_parts)
