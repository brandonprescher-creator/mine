"""
Progressive Hint System
Provides scaffolded support from mild hints to full solutions
"""
from typing import Dict, List, Any, Optional
from datetime import datetime

from ..base.activity_base import ActivityBase, ActivityType


class HintLevel:
    """Levels of hint support"""
    MILD = "mild"
    MEDIUM = "medium"
    STRONG = "strong"
    SOLUTION = "solution"


class HintSystem:
    """
    Progressive Hint System
    
    Provides scaffolded hints that gradually increase in support:
    1. Mild - Gentle nudge in right direction
    2. Medium - More specific guidance
    3. Strong - Step-by-step breakdown
    4. Solution - Complete answer with explanation
    """
    
    def __init__(
        self,
        problem_id: int,
        hints: List[Dict[str, str]],
        solution: Dict[str, Any]
    ):
        self.problem_id = problem_id
        self.hints = hints
        self.solution = solution
        self.hints_revealed = 0
    
    def get_next_hint(self) -> Optional[Dict[str, str]]:
        """Get the next hint in sequence"""
        if self.hints_revealed < len(self.hints):
            hint = self.hints[self.hints_revealed]
            self.hints_revealed += 1
            return {
                'level': hint['level'],
                'content': hint['content'],
                'hint_number': self.hints_revealed,
                'total_hints': len(self.hints)
            }
        return None
    
    def get_solution(self) -> Dict[str, Any]:
        """Get the complete solution"""
        return {
            'answer': self.solution['answer'],
            'explanation': self.solution['explanation'],
            'steps': self.solution.get('steps', [])
        }
    
    def reset(self):
        """Reset hints for a new attempt"""
        self.hints_revealed = 0
    
    @staticmethod
    def create_math_hints(
        problem_type: str,
        problem_data: Dict[str, Any]
    ) -> List[Dict[str, str]]:
        """Generate hints for math problems"""
        
        if problem_type == 'equation':
            return [
                {
                    'level': HintLevel.MILD,
                    'content': 'Think about what operation you need to isolate the variable.'
                },
                {
                    'level': HintLevel.MEDIUM,
                    'content': 'Start by combining like terms on each side of the equation.'
                },
                {
                    'level': HintLevel.STRONG,
                    'content': 'First, combine like terms. Then, use inverse operations to isolate the variable on one side.'
                }
            ]
        
        elif problem_type == 'word_problem':
            return [
                {
                    'level': HintLevel.MILD,
                    'content': 'What information do you know? What do you need to find?'
                },
                {
                    'level': HintLevel.MEDIUM,
                    'content': 'List the known values and identify the unknown. What operation connects them?'
                },
                {
                    'level': HintLevel.STRONG,
                    'content': 'Known: [list values]. Unknown: [variable]. Write an equation that relates them.'
                }
            ]
        
        elif problem_type == 'fraction':
            return [
                {
                    'level': HintLevel.MILD,
                    'content': 'Do you need a common denominator for this operation?'
                },
                {
                    'level': HintLevel.MEDIUM,
                    'content': 'Find the least common denominator (LCD) of the fractions.'
                },
                {
                    'level': HintLevel.STRONG,
                    'content': 'LCD is [value]. Convert each fraction to have this denominator, then perform the operation.'
                }
            ]
        
        else:
            return [
                {
                    'level': HintLevel.MILD,
                    'content': 'Break the problem into smaller steps.'
                },
                {
                    'level': HintLevel.MEDIUM,
                    'content': 'What strategy have you used for similar problems?'
                },
                {
                    'level': HintLevel.STRONG,
                    'content': 'Try working backwards or drawing a diagram to visualize the problem.'
                }
            ]
    
    @staticmethod
    def create_reading_hints(
        question_type: str,
        passage_excerpt: Optional[str] = None
    ) -> List[Dict[str, str]]:
        """Generate hints for reading comprehension"""
        
        if question_type == 'main_idea':
            return [
                {
                    'level': HintLevel.MILD,
                    'content': 'What is the passage mostly about?'
                },
                {
                    'level': HintLevel.MEDIUM,
                    'content': 'Look at the topic sentence and conclusion. What theme connects them?'
                },
                {
                    'level': HintLevel.STRONG,
                    'content': 'The main idea is usually stated in the first or last paragraph. Supporting details back it up throughout.'
                }
            ]
        
        elif question_type == 'inference':
            return [
                {
                    'level': HintLevel.MILD,
                    'content': 'What clues does the author give you?'
                },
                {
                    'level': HintLevel.MEDIUM,
                    'content': 'Combine what the text says with what you already know.'
                },
                {
                    'level': HintLevel.STRONG,
                    'content': 'Text evidence + your background knowledge = inference. Look for key words and context clues.'
                }
            ]
        
        elif question_type == 'vocabulary':
            return [
                {
                    'level': HintLevel.MILD,
                    'content': 'Look at the words around the unknown word for context.'
                },
                {
                    'level': HintLevel.MEDIUM,
                    'content': 'Does the sentence give an example, definition, or synonym?'
                },
                {
                    'level': HintLevel.STRONG,
                    'content': 'Use context clues (definition, example, antonym, synonym) and word parts (prefix, root, suffix).'
                }
            ]
        
        else:
            return [
                {
                    'level': HintLevel.MILD,
                    'content': 'Reread the relevant section of the text.'
                },
                {
                    'level': HintLevel.MEDIUM,
                    'content': 'Find evidence in the text that supports your answer.'
                },
                {
                    'level': HintLevel.STRONG,
                    'content': 'Quote or paraphrase specific details from the text to support your response.'
                }
            ]
    
    @staticmethod
    def create_science_hints(
        concept: str,
        question_type: str = 'general'
    ) -> List[Dict[str, str]]:
        """Generate hints for science questions"""
        
        if question_type == 'hypothesis':
            return [
                {
                    'level': HintLevel.MILD,
                    'content': 'What do you predict will happen?'
                },
                {
                    'level': HintLevel.MEDIUM,
                    'content': 'Use "If... then..." format. What is your independent variable?'
                },
                {
                    'level': HintLevel.STRONG,
                    'content': 'If [independent variable changes], then [dependent variable will...] because [reasoning].'
                }
            ]
        
        elif question_type == 'experiment_design':
            return [
                {
                    'level': HintLevel.MILD,
                    'content': 'What variables do you need to control?'
                },
                {
                    'level': HintLevel.MEDIUM,
                    'content': 'Identify independent, dependent, and controlled variables.'
                },
                {
                    'level': HintLevel.STRONG,
                    'content': 'Change ONE variable (independent), measure another (dependent), keep everything else the same (controlled).'
                }
            ]
        
        elif question_type == 'data_analysis':
            return [
                {
                    'level': HintLevel.MILD,
                    'content': 'What patterns do you see in the data?'
                },
                {
                    'level': HintLevel.MEDIUM,
                    'content': 'Look for trends: increasing, decreasing, constant, or cyclical.'
                },
                {
                    'level': HintLevel.STRONG,
                    'content': 'Describe the relationship between variables. Use specific numbers from your data as evidence.'
                }
            ]
        
        else:
            return [
                {
                    'level': HintLevel.MILD,
                    'content': 'What scientific concept applies here?'
                },
                {
                    'level': HintLevel.MEDIUM,
                    'content': 'Think about cause and effect. What is making this happen?'
                },
                {
                    'level': HintLevel.STRONG,
                    'content': 'Apply the scientific principle of [concept]. Consider the evidence and draw a conclusion.'
                }
            ]
    
    @staticmethod
    def create_writing_hints(
        task_type: str
    ) -> List[Dict[str, str]]:
        """Generate hints for writing tasks"""
        
        if task_type == 'thesis':
            return [
                {
                    'level': HintLevel.MILD,
                    'content': 'What is your main argument or point?'
                },
                {
                    'level': HintLevel.MEDIUM,
                    'content': 'State your position clearly in one sentence.'
                },
                {
                    'level': HintLevel.STRONG,
                    'content': 'A strong thesis: 1) States your position, 2) Is debatable, 3) Previews your main points.'
                }
            ]
        
        elif task_type == 'evidence':
            return [
                {
                    'level': HintLevel.MILD,
                    'content': 'What examples support your point?'
                },
                {
                    'level': HintLevel.MEDIUM,
                    'content': 'Use specific details, quotes, or data to back up your claim.'
                },
                {
                    'level': HintLevel.STRONG,
                    'content': 'Introduce evidence, quote/cite it, then explain how it supports your thesis.'
                }
            ]
        
        elif task_type == 'organization':
            return [
                {
                    'level': HintLevel.MILD,
                    'content': 'Does each paragraph have a clear topic?'
                },
                {
                    'level': HintLevel.MEDIUM,
                    'content': 'Use transition words to connect ideas between paragraphs.'
                },
                {
                    'level': HintLevel.STRONG,
                    'content': 'Introduction (thesis) → Body paragraphs (one point each) → Conclusion (restate and extend).'
                }
            ]
        
        else:
            return [
                {
                    'level': HintLevel.MILD,
                    'content': 'Read your work aloud. Does it flow smoothly?'
                },
                {
                    'level': HintLevel.MEDIUM,
                    'content': 'Check: Is your purpose clear? Do you have enough support? Is it well-organized?'
                },
                {
                    'level': HintLevel.STRONG,
                    'content': 'Revise for: 1) Clear thesis, 2) Strong evidence, 3) Logical organization, 4) Smooth transitions.'
                }
            ]
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert hint system to dictionary"""
        return {
            'problem_id': self.problem_id,
            'hints': self.hints,
            'hints_revealed': self.hints_revealed,
            'total_hints': len(self.hints),
            'has_solution': bool(self.solution)
        }
