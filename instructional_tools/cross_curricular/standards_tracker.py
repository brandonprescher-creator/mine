"""
Standards Tracking System
Track mastery across educational standards
"""
from typing import Dict, List, Any, Optional
from datetime import datetime


class Standard:
    """An educational standard"""
    def __init__(self, id: str, code: str, description: str, subject: str, grade_level: int):
        self.id = id
        self.code = code  # e.g., "CCSS.MATH.3.OA.A.1"
        self.description = description
        self.subject = subject
        self.grade_level = grade_level
    
    def to_dict(self) -> Dict[str, Any]:
        return {'id': self.id, 'code': self.code, 'description': self.description, 'subject': self.subject, 'grade_level': self.grade_level}


class StandardMastery:
    """Track student mastery of a standard"""
    def __init__(self, student_id: int, standard: Standard):
        self.student_id = student_id
        self.standard = standard
        self.mastery_level = 0  # 0-4: Not started, Developing, Approaching, Proficient, Mastered
        self.attempts = 0
        self.successes = 0
        self.last_practiced = None
        self.evidence = []  # Links to work that demonstrates mastery
    
    def record_attempt(self, success: bool, evidence_id: Optional[int] = None):
        """Record a practice attempt"""
        self.attempts += 1
        if success:
            self.successes += 1
        
        self.last_practiced = datetime.utcnow().isoformat()
        
        # Update mastery level
        success_rate = (self.successes / self.attempts) if self.attempts > 0 else 0
        
        if self.attempts >= 5:
            if success_rate >= 0.9:
                self.mastery_level = 4  # Mastered
            elif success_rate >= 0.75:
                self.mastery_level = 3  # Proficient
            elif success_rate >= 0.6:
                self.mastery_level = 2  # Approaching
            else:
                self.mastery_level = 1  # Developing
        
        if evidence_id:
            self.evidence.append(evidence_id)
    
    @property
    def success_rate(self) -> float:
        """Get success rate percentage"""
        return (self.successes / self.attempts * 100) if self.attempts > 0 else 0
    
    def to_dict(self) -> Dict[str, Any]:
        mastery_labels = ['Not Started', 'Developing', 'Approaching', 'Proficient', 'Mastered']
        return {'student_id': self.student_id, 'standard': self.standard.to_dict(), 'mastery_level': self.mastery_level, 'mastery_label': mastery_labels[self.mastery_level], 'attempts': self.attempts, 'success_rate': round(self.success_rate, 1), 'last_practiced': self.last_practiced, 'evidence_count': len(self.evidence)}


class StandardsTracker:
    """Track standards mastery across all subjects"""
    
    def __init__(self, student_id: int):
        self.student_id = student_id
        self.standards_mastery: Dict[str, StandardMastery] = {}
    
    def track_standard(self, standard: Standard):
        """Start tracking a standard"""
        if standard.id not in self.standards_mastery:
            self.standards_mastery[standard.id] = StandardMastery(self.student_id, standard)
    
    def record_work(self, standard_id: str, success: bool, evidence_id: Optional[int] = None):
        """Record work on a standard"""
        if standard_id in self.standards_mastery:
            self.standards_mastery[standard_id].record_attempt(success, evidence_id)
    
    def get_mastery_by_subject(self, subject: str) -> List[StandardMastery]:
        """Get all mastery records for a subject"""
        return [m for m in self.standards_mastery.values() if m.standard.subject == subject]
    
    def get_mastered_standards(self) -> List[StandardMastery]:
        """Get fully mastered standards"""
        return [m for m in self.standards_mastery.values() if m.mastery_level == 4]
    
    def get_needs_practice(self) -> List[StandardMastery]:
        """Get standards that need more practice"""
        return [m for m in self.standards_mastery.values() if m.mastery_level < 3 and m.attempts > 0]
    
    def get_progress_report(self) -> Dict[str, Any]:
        """Get comprehensive progress report"""
        total = len(self.standards_mastery)
        if total == 0:
            return {'total': 0, 'mastered': 0, 'proficient': 0, 'developing': 0, 'not_started': 0}
        
        mastered = sum(1 for m in self.standards_mastery.values() if m.mastery_level == 4)
        proficient = sum(1 for m in self.standards_mastery.values() if m.mastery_level == 3)
        approaching = sum(1 for m in self.standards_mastery.values() if m.mastery_level == 2)
        developing = sum(1 for m in self.standards_mastery.values() if m.mastery_level == 1)
        not_started = sum(1 for m in self.standards_mastery.values() if m.mastery_level == 0)
        
        return {'total': total, 'mastered': mastered, 'proficient': proficient, 'approaching': approaching, 'developing': developing, 'not_started': not_started, 'mastery_percentage': round((mastered / total) * 100, 1)}
