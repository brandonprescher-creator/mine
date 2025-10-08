"""
Base classes for instructional activities
"""
from enum import Enum
from datetime import datetime
from typing import Dict, List, Any, Optional
import json


class ActivityType(Enum):
    """Types of instructional activities"""
    # Math
    EQUATION_SOLVER = "equation_solver"
    WHITEBOARD = "whiteboard"
    GRAPHING = "graphing"
    MANIPULATIVES = "manipulatives"
    WORD_PROBLEM = "word_problem"
    ERROR_ANALYSIS = "error_analysis"
    PROOF = "proof"
    
    # Literacy
    ESSAY_OUTLINE = "essay_outline"
    SENTENCE_DIAGRAM = "sentence_diagram"
    VOCAB_CARDS = "vocab_cards"
    READING_COMP = "reading_comprehension"
    PEER_REVIEW = "peer_review"
    CITATION = "citation"
    WRITING_PROMPT = "writing_prompt"
    
    # Science
    LAB_REPORT = "lab_report"
    HYPOTHESIS = "hypothesis"
    CER_SCAFFOLD = "cer_scaffold"
    DIAGRAM_LABEL = "diagram_label"
    DATA_TABLE = "data_table"
    CONCEPT_MAP = "concept_map"
    
    # Social Studies
    PRIMARY_SOURCE = "primary_source"
    TIMELINE = "timeline"
    MAP_ANNOTATION = "map_annotation"
    CAUSE_EFFECT = "cause_effect"
    DEBATE_PREP = "debate_prep"
    
    # Cross-Curricular
    PROJECT_PLAN = "project_plan"
    PORTFOLIO = "portfolio"
    REFLECTION = "reflection"
    RUBRIC = "rubric"


class ActivityBase:
    """Base class for all instructional activities"""
    
    def __init__(
        self,
        activity_id: int,
        activity_type: ActivityType,
        title: str,
        description: str,
        lesson_id: Optional[int] = None,
        config: Optional[Dict[str, Any]] = None
    ):
        self.activity_id = activity_id
        self.activity_type = activity_type
        self.title = title
        self.description = description
        self.lesson_id = lesson_id
        self.config = config or {}
        self.created_at = datetime.utcnow()
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert activity to dictionary"""
        return {
            'id': self.activity_id,
            'type': self.activity_type.value,
            'title': self.title,
            'description': self.description,
            'lesson_id': self.lesson_id,
            'config': self.config,
            'created_at': self.created_at.isoformat()
        }
    
    def validate_submission(self, submission_data: Dict[str, Any]) -> tuple[bool, List[str]]:
        """
        Validate student submission
        Returns: (is_valid, error_messages)
        """
        # Override in subclasses
        return True, []
    
    def auto_grade(self, submission_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Automatically grade submission if possible
        Returns: {'score': float, 'feedback': str, 'details': dict}
        """
        # Override in subclasses
        return {
            'score': None,
            'feedback': 'Manual grading required',
            'details': {}
        }
    
    def generate_hints(self, current_step: int = 0) -> List[Dict[str, str]]:
        """
        Generate progressive hints
        Returns: List of hints with increasing support
        """
        # Override in subclasses
        return []
    
    def get_rubric(self) -> Dict[str, Any]:
        """Get grading rubric for this activity"""
        # Override in subclasses
        return {
            'criteria': [],
            'total_points': 0
        }


class MathActivity(ActivityBase):
    """Base class for math activities"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.show_work_required = self.config.get('show_work_required', True)
        self.multiple_strategies = self.config.get('multiple_strategies', False)
    
    def check_step(self, step_number: int, student_answer: str) -> Dict[str, Any]:
        """Check individual step in multi-step problem"""
        return {
            'correct': None,
            'feedback': '',
            'hint': ''
        }


class LiteracyActivity(ActivityBase):
    """Base class for literacy activities"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.word_count_min = self.config.get('word_count_min', 0)
        self.word_count_max = self.config.get('word_count_max', None)
    
    def check_word_count(self, text: str) -> tuple[bool, str]:
        """Validate word count"""
        words = len(text.split())
        
        if self.word_count_min and words < self.word_count_min:
            return False, f"Need at least {self.word_count_min} words (you have {words})"
        
        if self.word_count_max and words > self.word_count_max:
            return False, f"Maximum {self.word_count_max} words (you have {words})"
        
        return True, f"Word count: {words}"


class ScienceActivity(ActivityBase):
    """Base class for science activities"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.requires_claim = self.config.get('requires_claim', False)
        self.requires_evidence = self.config.get('requires_evidence', False)
        self.requires_reasoning = self.config.get('requires_reasoning', False)
    
    def validate_cer(self, claim: str, evidence: str, reasoning: str) -> tuple[bool, List[str]]:
        """Validate Claim-Evidence-Reasoning structure"""
        errors = []
        
        if self.requires_claim and not claim.strip():
            errors.append("Claim is required")
        
        if self.requires_evidence and not evidence.strip():
            errors.append("Evidence is required")
        
        if self.requires_reasoning and not reasoning.strip():
            errors.append("Reasoning is required")
        
        return len(errors) == 0, errors


class SocialStudiesActivity(ActivityBase):
    """Base class for social studies activities"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.requires_sources = self.config.get('requires_sources', False)
        self.min_sources = self.config.get('min_sources', 1)
    
    def validate_sources(self, sources: List[Dict[str, str]]) -> tuple[bool, str]:
        """Validate source citations"""
        if self.requires_sources and len(sources) < self.min_sources:
            return False, f"Need at least {self.min_sources} sources"
        
        return True, f"Sources provided: {len(sources)}"
