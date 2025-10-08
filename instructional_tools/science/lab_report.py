"""
Lab Report Builder
Scaffold scientific lab reports with hypothesis, procedure, data, conclusion
"""
from typing import Dict, List, Any, Optional
from ..base.activity_base import ScienceActivity, ActivityType


class LabReportBuilder(ScienceActivity):
    """
    Lab Report Builder
    
    Sections:
    1. Title & Purpose
    2. Hypothesis
    3. Materials
    4. Procedure
    5. Data & Observations
    6. Analysis
    7. Conclusion
    """
    
    def __init__(self, activity_id: int, title: str, description: str, experiment_name: str, lesson_id: Optional[int] = None, config: Optional[Dict[str, Any]] = None):
        super().__init__(activity_id=activity_id, activity_type=ActivityType.LAB_REPORT, title=title, description=description, lesson_id=lesson_id, config=config)
        self.experiment_name = experiment_name
        self.required_sections = self.config.get('required_sections', ['hypothesis', 'procedure', 'data', 'conclusion'])
    
    def get_template(self) -> Dict[str, Any]:
        """Get lab report template"""
        return {
            'title': '',
            'purpose': '',
            'hypothesis': {'if': '', 'then': '', 'because': ''},
            'materials': [],
            'procedure': [],
            'data': {'observations': '', 'measurements': []},
            'analysis': '',
            'conclusion': {'results': '', 'hypothesis_support': '', 'errors': '', 'further_questions': ''}
        }
    
    def validate_hypothesis(self, hypothesis: Dict[str, str]) -> tuple[bool, str]:
        """Validate hypothesis structure"""
        if not all([hypothesis.get('if'), hypothesis.get('then')]):
            return False, 'Hypothesis must include "if" and "then" statements'
        return True, 'Valid hypothesis structure'
    
    def validate_submission(self, submission_data: Dict[str, Any]) -> tuple[bool, List[str]]:
        """Validate complete lab report"""
        errors = []
        
        for section in self.required_sections:
            if not submission_data.get(section):
                errors.append(f'Section required: {section.title()}')
        
        # Validate hypothesis if present
        if 'hypothesis' in submission_data:
            is_valid, message = self.validate_hypothesis(submission_data['hypothesis'])
            if not is_valid:
                errors.append(message)
        
        return len(errors) == 0, errors
