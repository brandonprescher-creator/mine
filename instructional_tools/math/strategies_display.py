"""
Strategy Display Component
Visual comparison of multiple problem-solving approaches
"""
from typing import Dict, List, Any
from .multiple_strategies import MultipleStrategiesDisplay, SolutionMethod


class StrategyComparison:
    """Compare multiple strategies side-by-side"""
    
    @staticmethod
    def create_fraction_addition(frac1: tuple, frac2: tuple) -> MultipleStrategiesDisplay:
        """Multiple strategies for adding fractions"""
        a, b = frac1
        c, d = frac2
        
        display = MultipleStrategiesDisplay(f"{a}/{b} + {c}/{d}", "fraction_addition")
        
        # Method 1: LCD
        display.add_method(SolutionMethod(
            name='Least Common Denominator',
            description='Find LCD and convert both fractions',
            steps=['Find LCD', 'Convert fractions', 'Add numerators', 'Simplify'],
            visual='LCD approach'
        ))
        
        # Method 2: Butterfly Method
        display.add_method(SolutionMethod(
            name='Butterfly Method',
            description='Cross-multiply and add',
            steps=['Cross multiply', 'Add products', 'Multiply denominators', 'Simplify'],
            visual='Butterfly diagram'
        ))
        
        return display
    
    @staticmethod
    def create_multiplication_strategies(num1: int, num2: int) -> MultipleStrategiesDisplay:
        """Multiple strategies for multiplication"""
        display = MultipleStrategiesDisplay(f"{num1} × {num2}", "multiplication")
        
        display.add_method(SolutionMethod(name='Standard Algorithm', description='Traditional multiplication', steps=['Multiply ones', 'Multiply tens', 'Add products'], visual='Standard form'))
        
        display.add_method(SolutionMethod(name='Area Model', description='Visual rectangle', steps=['Draw rectangle', 'Decompose numbers', 'Find partial products', 'Add areas'], visual='Area grid'))
        
        display.add_method(SolutionMethod(name='Lattice Method', description='Grid multiplication', steps=['Draw lattice', 'Multiply digits', 'Add diagonals'], visual='Lattice grid'))
        
        return display
