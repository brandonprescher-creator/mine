"""
Experiment Safety Checklist
Lab safety rules and equipment guides
"""
from typing import Dict, List, Any, Optional


class SafetyChecklistItem:
    """A safety checklist item"""
    def __init__(self, id: int, text: str, category: str, required: bool = True):
        self.id = id
        self.text = text
        self.category = category  # 'ppe', 'procedure', 'cleanup', 'emergency'
        self.required = required
    
    def to_dict(self) -> Dict[str, Any]:
        return {'id': self.id, 'text': self.text, 'category': self.category, 'required': self.required}


class ExperimentSafetyChecklist:
    """
    Lab Safety Checklist Builder
    
    Categories:
    - Personal Protective Equipment (PPE)
    - Setup & Procedure
    - Chemical/Material Handling
    - Cleanup
    - Emergency Procedures
    """
    
    STANDARD_SAFETY_ITEMS = [
        SafetyChecklistItem(1, 'Wear safety goggles at all times', 'ppe', True),
        SafetyChecklistItem(2, 'Tie back long hair', 'ppe', True),
        SafetyChecklistItem(3, 'Wear closed-toe shoes', 'ppe', True),
        SafetyChecklistItem(4, 'Read all instructions before starting', 'procedure', True),
        SafetyChecklistItem(5, 'Know location of safety equipment', 'emergency', True),
        SafetyChecklistItem(6, 'Clean workspace before beginning', 'setup', True),
        SafetyChecklistItem(7, 'Handle chemicals carefully', 'procedure', True),
        SafetyChecklistItem(8, 'Report spills immediately', 'emergency', True),
        SafetyChecklistItem(9, 'Wash hands after lab', 'cleanup', True),
        SafetyChecklistItem(10, 'Clean and return all equipment', 'cleanup', True)
    ]
    
    def __init__(self, experiment_name: str):
        self.experiment_name = experiment_name
        self.items: List[SafetyChecklistItem] = list(self.STANDARD_SAFETY_ITEMS)
        self.student_completed = []
    
    def add_custom_item(self, text: str, category: str, required: bool = True):
        """Add experiment-specific safety item"""
        item_id = len(self.items) + 1
        item = SafetyChecklistItem(item_id, text, category, required)
        self.items.append(item)
    
    def mark_completed(self, item_id: int):
        """Mark a checklist item as completed"""
        if item_id not in self.student_completed:
            self.student_completed.append(item_id)
    
    def is_complete(self) -> bool:
        """Check if all required items are completed"""
        required_ids = [item.id for item in self.items if item.required]
        return all(req_id in self.student_completed for req_id in required_ids)
    
    def get_incomplete_required(self) -> List[SafetyChecklistItem]:
        """Get incomplete required items"""
        return [item for item in self.items if item.required and item.id not in self.student_completed]
    
    def to_dict(self) -> Dict[str, Any]:
        return {'experiment_name': self.experiment_name, 'total_items': len(self.items), 'completed_items': len(self.student_completed), 'is_complete': self.is_complete(), 'items': [item.to_dict() for item in self.items], 'completed_ids': self.student_completed}
