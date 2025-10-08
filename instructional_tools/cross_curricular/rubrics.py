"""
Interactive Rubrics
Student-facing rubrics for self-assessment and clear expectations
"""
from typing import Dict, List, Any, Optional
from ..base.grading import Rubric, RubricCriterion, GradingSystem


class InteractiveRubric:
    """
    Interactive rubric system that students can use for:
    - Understanding expectations before starting
    - Self-assessment during work
    - Peer review
    - Goal setting
    """
    
    def __init__(self, rubric: Rubric):
        self.rubric = rubric
        self.student_scores = {}
        self.self_assessment_notes = {}
    
    def get_student_view(self) -> Dict[str, Any]:
        """Get rubric formatted for student view"""
        return {
            'title': self.rubric.title,
            'description': self.rubric.description,
            'total_points': self.rubric.total_points,
            'criteria': [
                {
                    'name': c.name,
                    'description': c.description,
                    'max_points': c.max_points,
                    'levels': c.levels,
                    'student_friendly_tips': self._get_student_tips(c.name)
                }
                for c in self.rubric.criteria
            ]
        }
    
    def _get_student_tips(self, criterion_name: str) -> List[str]:
        """Get student-friendly tips for each criterion"""
        tips_library = {
            'Completeness': [
                'Show ALL your work - every step counts!',
                'Don\'t skip steps, even if they seem obvious',
                'Include labels and units where needed'
            ],
            'Organization': [
                'Number your steps clearly',
                'Use neat handwriting or formatting',
                'Put similar ideas together'
            ],
            'Accuracy': [
                'Check your math twice',
                'Make sure your answer makes sense',
                'Look for calculation errors'
            ],
            'Explanation': [
                'Explain WHY you chose each step',
                'Use complete sentences',
                'Pretend you\'re teaching someone else'
            ],
            'Thesis/Argument': [
                'State your main point clearly',
                'Make sure it\'s debatable',
                'Preview your supporting points'
            ],
            'Evidence': [
                'Use specific examples or quotes',
                'Explain how evidence supports your point',
                'Include multiple pieces of evidence'
            ],
            'Grammar': [
                'Check spelling and punctuation',
                'Vary your sentence structure',
                'Read it aloud to catch errors'
            ]
        }
        
        return tips_library.get(criterion_name, [
            'Do your best work',
            'Take your time',
            'Ask for help if needed'
        ])
    
    def record_self_assessment(
        self,
        criterion_name: str,
        self_score: int,
        notes: Optional[str] = None
    ):
        """Student records their self-assessment"""
        self.student_scores[criterion_name] = self_score
        if notes:
            self.self_assessment_notes[criterion_name] = notes
    
    def get_self_assessment_summary(self) -> Dict[str, Any]:
        """Get summary of student's self-assessment"""
        total_self_score = sum(self.student_scores.values())
        
        return {
            'criterion_scores': self.student_scores,
            'notes': self.self_assessment_notes,
            'total_self_score': total_self_score,
            'total_possible': self.rubric.total_points,
            'percentage': round((total_self_score / self.rubric.total_points) * 100, 2) if self.rubric.total_points > 0 else 0
        }
    
    def compare_with_teacher_scores(
        self,
        teacher_scores: Dict[str, int]
    ) -> Dict[str, Any]:
        """Compare student self-assessment with teacher scores"""
        comparison = {}
        
        for criterion_name in self.student_scores:
            student_score = self.student_scores[criterion_name]
            teacher_score = teacher_scores.get(criterion_name, 0)
            difference = student_score - teacher_score
            
            comparison[criterion_name] = {
                'student_score': student_score,
                'teacher_score': teacher_score,
                'difference': difference,
                'assessment': self._assess_accuracy(difference)
            }
        
        return comparison
    
    def _assess_accuracy(self, difference: int) -> str:
        """Assess how accurate student's self-assessment was"""
        if abs(difference) <= 2:
            return 'Accurate - great self-awareness!'
        elif difference > 2:
            return 'Slightly overestimated - be more critical'
        else:
            return 'Slightly underestimated - give yourself credit!'
    
    @staticmethod
    def create_simple_rubric(
        title: str,
        criteria_names: List[str],
        points_per_criterion: int = 25
    ) -> 'InteractiveRubric':
        """Create a simple rubric quickly"""
        criteria = []
        
        for name in criteria_names:
            levels = [
                {'points': points_per_criterion, 'description': 'Excellent'},
                {'points': int(points_per_criterion * 0.8), 'description': 'Good'},
                {'points': int(points_per_criterion * 0.6), 'description': 'Adequate'},
                {'points': int(points_per_criterion * 0.4), 'description': 'Needs Improvement'},
                {'points': 0, 'description': 'Missing'}
            ]
            
            criteria.append(RubricCriterion(
                name=name,
                description=f'Assessment of {name.lower()}',
                max_points=points_per_criterion,
                levels=levels
            ))
        
        rubric = Rubric(
            title=title,
            description=f'Rubric for {title}',
            criteria=criteria
        )
        
        return InteractiveRubric(rubric)
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for JSON/storage"""
        return {
            'rubric': self.rubric.to_dict(),
            'student_scores': self.student_scores,
            'self_assessment_notes': self.self_assessment_notes,
            'self_assessment_summary': self.get_self_assessment_summary() if self.student_scores else None
        }
