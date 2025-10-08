"""
Math Manipulatives
Interactive visual tools for hands-on learning
"""
from typing import Dict, List, Any, Optional
from ..base.activity_base import MathActivity, ActivityType


class MathManipulatives(MathActivity):
    """
    Virtual Math Manipulatives
    
    Tools:
    - Fraction bars
    - Algebra tiles
    - Number lines
    - Base-10 blocks
    - Geometry shapes
    """
    
    MANIPULATIVE_TYPES = {
        'fraction_bars': {'name': 'Fraction Bars', 'icon': '▬', 'subjects': ['fractions', 'decimals']},
        'algebra_tiles': {'name': 'Algebra Tiles', 'icon': '▢', 'subjects': ['algebra', 'equations']},
        'number_lines': {'name': 'Number Lines', 'icon': '↔', 'subjects': ['integers', 'operations']},
        'base10_blocks': {'name': 'Base-10 Blocks', 'icon': '▣', 'subjects': ['place value', 'operations']},
        'pattern_blocks': {'name': 'Pattern Blocks', 'icon': '⬡', 'subjects': ['geometry', 'fractions']},
        'counters': {'name': 'Counters', 'icon': '●', 'subjects': ['counting', 'operations']}
    }
    
    def __init__(self, activity_id: int, title: str, description: str, manipulative_type: str, lesson_id: Optional[int] = None, config: Optional[Dict[str, Any]] = None):
        super().__init__(activity_id=activity_id, activity_type=ActivityType.MANIPULATIVES, title=title, description=description, lesson_id=lesson_id, config=config)
        self.manipulative_type = manipulative_type
        self.problem_data = self.config.get('problem_data', {})
    
    def get_instructions(self) -> str:
        """Get instructions for using this manipulative"""
        instructions = {
            'fraction_bars': 'Use the fraction bars to represent and compare fractions. Drag bars to show each fraction.',
            'algebra_tiles': 'Use tiles to model equations. Positive tiles are blue, negative tiles are red. Group like terms.',
            'number_lines': 'Plot numbers and operations on the number line. Use arrows to show jumps.',
            'base10_blocks': 'Use blocks to show place value. Ones=small cubes, Tens=rods, Hundreds=flats, Thousands=cubes.',
            'pattern_blocks': 'Use pattern blocks to explore shapes and fractions. Each shape has a value.',
            'counters': 'Use counters to model numbers and operations. Group, add, subtract, or arrange counters.'
        }
        return instructions.get(self.manipulative_type, 'Use the manipulatives to solve the problem.')
