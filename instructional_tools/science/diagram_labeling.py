"""
Diagram Labeling Tool
Drag-and-drop labeling for scientific diagrams
"""
from typing import Dict, List, Any, Optional


class DiagramLabel:
    """A label for a diagram"""
    def __init__(self, id: int, text: str, correct_position: Dict[str, float]):
        self.id = id
        self.text = text
        self.correct_position = correct_position  # {'x': 100, 'y': 200}
        self.tolerance = 20  # pixels
    
    def check_placement(self, student_position: Dict[str, float]) -> bool:
        """Check if label is placed correctly"""
        dx = abs(student_position['x'] - self.correct_position['x'])
        dy = abs(student_position['y'] - self.correct_position['y'])
        return dx <= self.tolerance and dy <= self.tolerance
    
    def to_dict(self) -> Dict[str, Any]:
        return {'id': self.id, 'text': self.text}


class DiagramLabelingActivity:
    """
    Diagram Labeling Activity
    
    Features:
    - Drag-and-drop labels
    - Instant feedback
    - Multiple diagram types
    """
    
    DIAGRAM_TYPES = {
        'cell': {'name': 'Cell Structure', 'labels': ['nucleus', 'cytoplasm', 'cell membrane', 'mitochondria', 'chloroplast']},
        'plant': {'name': 'Plant Parts', 'labels': ['roots', 'stem', 'leaves', 'flower', 'seeds']},
        'heart': {'name': 'Heart Anatomy', 'labels': ['aorta', 'right atrium', 'left atrium', 'right ventricle', 'left ventricle']},
        'water_cycle': {'name': 'Water Cycle', 'labels': ['evaporation', 'condensation', 'precipitation', 'collection']},
        'digestive': {'name': 'Digestive System', 'labels': ['mouth', 'esophagus', 'stomach', 'small intestine', 'large intestine']}
    }
    
    def __init__(self, diagram_type: str, diagram_url: str):
        self.diagram_type = diagram_type
        self.diagram_url = diagram_url
        self.labels: List[DiagramLabel] = []
        self.label_id_counter = 0
    
    def add_label(self, text: str, x: float, y: float) -> DiagramLabel:
        """Add a label to the diagram"""
        label = DiagramLabel(self.label_id_counter, text, {'x': x, 'y': y})
        self.labels.append(label)
        self.label_id_counter += 1
        return label
    
    def check_all_labels(self, student_placements: Dict[int, Dict[str, float]]) -> Dict[str, Any]:
        """Check all label placements"""
        correct = 0
        results = {}
        
        for label in self.labels:
            if label.id in student_placements:
                is_correct = label.check_placement(student_placements[label.id])
                results[label.id] = is_correct
                if is_correct:
                    correct += 1
        
        return {'correct': correct, 'total': len(self.labels), 'accuracy': round((correct / len(self.labels)) * 100, 1) if self.labels else 0, 'label_results': results}
