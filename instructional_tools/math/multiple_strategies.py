"""
Multiple Strategies Display
Show 2-3 methods for solving the same problem side-by-side
"""
from typing import Dict, List, Any, Optional


class SolutionMethod:
    """A method for solving a problem"""
    def __init__(self, name: str, description: str, steps: List[str], visual: Optional[str] = None):
        self.name = name
        self.description = description
        self.steps = steps
        self.visual = visual  # URL or description of visual representation
        self.difficulty = 'medium'
        self.time_estimate = '5-10 minutes'
    
    def to_dict(self) -> Dict[str, Any]:
        return {'name': self.name, 'description': self.description, 'steps': self.steps, 'visual': self.visual, 'difficulty': self.difficulty, 'time_estimate': self.time_estimate}


class MultipleStrategiesDisplay:
    """
    Display Multiple Solution Strategies
    
    Shows different approaches to the same problem:
    - Visual comparison
    - When to use each method
    - Student choice of method
    """
    
    def __init__(self, problem: str, problem_type: str):
        self.problem = problem
        self.problem_type = problem_type
        self.methods: List[SolutionMethod] = []
        self.student_preference = None
    
    def add_method(self, method: SolutionMethod):
        """Add a solution method"""
        self.methods.append(method)
    
    def get_comparison_table(self) -> Dict[str, List[str]]:
        """Get side-by-side comparison"""
        max_steps = max(len(m.steps) for m in self.methods) if self.methods else 0
        
        comparison = {'methods': [m.name for m in self.methods], 'steps': []}
        
        for i in range(max_steps):
            step_row = []
            for method in self.methods:
                step_row.append(method.steps[i] if i < len(method.steps) else '')
            comparison['steps'].append(step_row)
        
        return comparison
    
    def recommend_method(self, student_level: str, preference: str) -> SolutionMethod:
        """Recommend a method based on student needs"""
        if preference == 'visual':
            visual_methods = [m for m in self.methods if m.visual]
            return visual_methods[0] if visual_methods else self.methods[0]
        
        if student_level == 'beginner':
            return min(self.methods, key=lambda m: len(m.steps))
        
        return self.methods[0] if self.methods else None
    
    @staticmethod
    def create_division_strategies(dividend: int, divisor: int) -> 'MultipleStrategiesDisplay':
        """Create multiple strategies for division"""
        display = MultipleStrategiesDisplay(f"{dividend} ÷ {divisor}", "division")
        
        # Method 1: Long Division
        display.add_method(SolutionMethod(
            name='Long Division',
            description='Traditional algorithm',
            steps=[f"Divide {dividend} by {divisor} using long division", "Multiply back to check", "Subtract and bring down", "Repeat until done"],
            visual='Traditional division bracket'
        ))
        
        # Method 2: Partial Quotients
        display.add_method(SolutionMethod(
            name='Partial Quotients',
            description='Subtract multiples of divisor',
            steps=["Estimate how many times divisor goes into dividend", "Subtract that amount", "Repeat with remainder", "Add partial quotients"],
            visual='List of subtractions'
        ))
        
        # Method 3: Area Model
        display.add_method(SolutionMethod(
            name='Area Model',
            description='Visual rectangle method',
            steps=["Draw rectangle", "Find length and width", "Decompose into smaller rectangles", "Add areas"],
            visual='Rectangle grid'
        ))
        
        return display
