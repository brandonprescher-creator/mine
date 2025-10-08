"""
Economics Graph Tools
Supply/demand, budgets, economic analysis
"""
from typing import Dict, List, Any, Optional


class EconomicsGraph:
    """Economic graph builder"""
    
    GRAPH_TYPES = ['supply_demand', 'production_possibilities', 'circular_flow', 'budget']
    
    def __init__(self, graph_type: str, title: str):
        self.graph_type = graph_type
        self.title = title
        self.data_points = []
    
    def add_point(self, x: float, y: float, label: Optional[str] = None):
        """Add a data point"""
        self.data_points.append({'x': x, 'y': y, 'label': label})
    
    def analyze_graph(self) -> Dict[str, Any]:
        """Analyze economic relationships"""
        if self.graph_type == 'supply_demand':
            return {'equilibrium': 'Point where supply equals demand', 'shifts': 'Changes in curves affect price/quantity'}
        return {}


class BudgetBuilder:
    """Personal/business budget builder"""
    
    def __init__(self, budget_type: str, total_income: float):
        self.budget_type = budget_type
        self.total_income = total_income
        self.expenses = {}
        self.savings = 0
    
    def add_expense(self, category: str, amount: float):
        """Add an expense category"""
        self.expenses[category] = amount
    
    def calculate_balance(self) -> float:
        """Calculate remaining balance"""
        total_expenses = sum(self.expenses.values())
        return self.total_income - total_expenses - self.savings
    
    def get_analysis(self) -> Dict[str, Any]:
        """Analyze budget"""
        total_expenses = sum(self.expenses.values())
        return {'income': self.total_income, 'total_expenses': total_expenses, 'savings': self.savings, 'balance': self.calculate_balance(), 'expense_percentage': round((total_expenses / self.total_income) * 100, 1) if self.total_income > 0 else 0}
