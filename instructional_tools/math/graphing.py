"""
Graphing Tool
Interactive coordinate plane for plotting points, lines, and functions
"""
from typing import Dict, List, Any, Optional, Tuple
from ..base.activity_base import MathActivity, ActivityType


class GraphingTool(MathActivity):
    """
    Interactive Graphing Tool
    
    Features:
    - Plot points
    - Draw lines/curves
    - Function graphing
    - Export graphs
    """
    
    def __init__(self, activity_id: int, title: str, description: str, lesson_id: Optional[int] = None, config: Optional[Dict[str, Any]] = None):
        super().__init__(activity_id=activity_id, activity_type=ActivityType.GRAPHING, title=title, description=description, lesson_id=lesson_id, config=config)
        self.x_min = self.config.get('x_min', -10)
        self.x_max = self.config.get('x_max', 10)
        self.y_min = self.config.get('y_min', -10)
        self.y_max = self.config.get('y_max', 10)
        self.grid_enabled = self.config.get('grid_enabled', True)
    
    def validate_point(self, x: float, y: float) -> bool:
        """Check if point is within bounds"""
        return self.x_min <= x <= self.x_max and self.y_min <= y <= self.y_max
    
    def check_plotted_points(self, student_points: List[Tuple[float, float]], expected_points: List[Tuple[float, float]], tolerance: float = 0.5) -> Dict[str, Any]:
        """Check if student plotted points correctly"""
        correct_count = 0
        for expected in expected_points:
            for student in student_points:
                if abs(student[0] - expected[0]) <= tolerance and abs(student[1] - expected[1]) <= tolerance:
                    correct_count += 1
                    break
        
        accuracy = (correct_count / len(expected_points) * 100) if expected_points else 0
        return {'correct': correct_count, 'total': len(expected_points), 'accuracy': accuracy}
