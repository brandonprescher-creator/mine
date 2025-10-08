"""
Data Tables & Graph Interpretation
Create, analyze, and interpret scientific data
"""
from typing import Dict, List, Any, Optional, Tuple


class DataTable:
    """A data table for scientific observations"""
    
    def __init__(self, title: str, columns: List[str]):
        self.title = title
        self.columns = columns
        self.rows: List[List[Any]] = []
    
    def add_row(self, row: List[Any]):
        """Add a data row"""
        if len(row) != len(self.columns):
            raise ValueError(f"Row must have {len(self.columns)} values")
        self.rows.append(row)
    
    def get_column_data(self, column_index: int) -> List[Any]:
        """Get all data from a specific column"""
        return [row[column_index] for row in self.rows]
    
    def calculate_average(self, column_index: int) -> float:
        """Calculate average for a numeric column"""
        data = self.get_column_data(column_index)
        numeric_data = [float(x) for x in data if isinstance(x, (int, float)) or str(x).replace('.','').isdigit()]
        return sum(numeric_data) / len(numeric_data) if numeric_data else 0
    
    def to_dict(self) -> Dict[str, Any]:
        return {'title': self.title, 'columns': self.columns, 'rows': self.rows, 'row_count': len(self.rows)}


class GraphInterpretation:
    """Analyze and interpret graphs"""
    
    GRAPH_TYPES = ['line', 'bar', 'scatter', 'pie']
    
    def __init__(self, graph_type: str, title: str, data: Dict[str, Any]):
        self.graph_type = graph_type
        self.title = title
        self.data = data
    
    def get_analysis_prompts(self) -> List[Dict[str, str]]:
        """Get prompts for analyzing the graph"""
        return [
            {'prompt': 'What is the main trend or pattern you observe?', 'type': 'trend'},
            {'prompt': 'What is the highest value? What is the lowest?', 'type': 'extremes'},
            {'prompt': 'Are there any outliers or unusual data points?', 'type': 'outliers'},
            {'prompt': 'What conclusions can you draw from this data?', 'type': 'conclusion'},
            {'prompt': 'What questions does this data raise?', 'type': 'questions'}
        ]
    
    def validate_interpretation(self, student_responses: Dict[str, str]) -> tuple[bool, List[str]]:
        """Validate student's graph interpretation"""
        errors = []
        required_fields = ['trend', 'conclusion']
        
        for field in required_fields:
            if not student_responses.get(field, '').strip():
                errors.append(f'Please answer: {field}')
        
        return len(errors) == 0, errors
