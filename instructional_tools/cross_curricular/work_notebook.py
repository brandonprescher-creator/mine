"""
Show-Your-Work Notebook
Students can upload photos, type work, or draw solutions
"""
from typing import Dict, List, Any, Optional
from datetime import datetime
import base64
import os

from ..base.activity_base import ActivityBase, ActivityType
from ..base.grading import GradingSystem


class WorkNotebook(ActivityBase):
    """
    Show-Your-Work Notebook Activity
    
    Allows students to:
    - Upload photos of handwritten work
    - Type their solutions
    - Draw on a digital canvas
    - Add explanations and reflections
    """
    
    def __init__(
        self,
        activity_id: int,
        title: str,
        description: str,
        lesson_id: Optional[int] = None,
        config: Optional[Dict[str, Any]] = None
    ):
        super().__init__(
            activity_id=activity_id,
            activity_type=ActivityType.PROJECT_PLAN,  # Using existing enum
            title=title,
            description=description,
            lesson_id=lesson_id,
            config=config
        )
        
        # Configuration options
        self.allow_photo_upload = self.config.get('allow_photo_upload', True)
        self.allow_typed_work = self.config.get('allow_typed_work', True)
        self.allow_drawing = self.config.get('allow_drawing', True)
        self.require_explanation = self.config.get('require_explanation', False)
        self.min_work_items = self.config.get('min_work_items', 1)
    
    def validate_submission(self, submission_data: Dict[str, Any]) -> tuple[bool, List[str]]:
        """Validate that student has provided required work"""
        errors = []
        
        work_items = submission_data.get('work_items', [])
        
        # Check minimum items
        if len(work_items) < self.min_work_items:
            errors.append(f"Need at least {self.min_work_items} work item(s)")
        
        # Check each work item has content
        for i, item in enumerate(work_items):
            item_type = item.get('type')
            content = item.get('content')
            
            if not item_type or not content:
                errors.append(f"Work item {i+1} is incomplete")
            
            # Validate based on type
            if item_type == 'photo' and not self.allow_photo_upload:
                errors.append(f"Photo uploads not allowed for this activity")
            elif item_type == 'text' and not self.allow_typed_work:
                errors.append(f"Typed work not allowed for this activity")
            elif item_type == 'drawing' and not self.allow_drawing:
                errors.append(f"Drawings not allowed for this activity")
        
        # Check for explanation if required
        if self.require_explanation:
            explanation = submission_data.get('explanation', '').strip()
            if not explanation:
                errors.append("Please provide an explanation of your work")
        
        return len(errors) == 0, errors
    
    def auto_grade(self, submission_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Provide initial feedback before teacher review
        """
        work_items = submission_data.get('work_items', [])
        explanation = submission_data.get('explanation', '')
        
        # Calculate completion score
        completion_score = 0
        
        # Has multiple work items
        if len(work_items) >= self.min_work_items:
            completion_score += 25
        
        # Each item has content
        if all(item.get('content') for item in work_items):
            completion_score += 25
        
        # Has explanation (if required or provided)
        if explanation.strip():
            completion_score += 25
        
        # Has multiple types of work (shows thorough understanding)
        work_types = set(item.get('type') for item in work_items)
        if len(work_types) > 1:
            completion_score += 25
        
        feedback_parts = []
        feedback_parts.append("✅ Work submitted successfully!\n\n")
        
        if completion_score >= 75:
            feedback_parts.append("**Excellent submission!**\n")
        elif completion_score >= 50:
            feedback_parts.append("**Good submission!**\n")
        else:
            feedback_parts.append("**Submission received.**\n")
        
        feedback_parts.append(f"- {len(work_items)} work item(s) submitted\n")
        
        if explanation:
            feedback_parts.append(f"- Explanation provided ({len(explanation.split())} words)\n")
        
        feedback_parts.append("\n*Your teacher will review and provide detailed feedback.*")
        
        return {
            'score': None,  # Teacher must grade
            'completion_score': completion_score,
            'feedback': ''.join(feedback_parts),
            'details': {
                'work_items_count': len(work_items),
                'has_explanation': bool(explanation),
                'work_types': list(work_types)
            }
        }
    
    def get_rubric(self) -> Dict[str, Any]:
        """Get grading rubric for work notebook"""
        rubric = GradingSystem.create_basic_rubric('work_notebook')
        return rubric.to_dict()
    
    def generate_hints(self, current_step: int = 0) -> List[Dict[str, str]]:
        """Generate hints for completing the work notebook"""
        hints = [
            {
                'level': 'mild',
                'hint': 'Start by showing your first step clearly. What did you do first?'
            },
            {
                'level': 'medium',
                'hint': 'Make sure to label your work and show each step. You can upload a photo, type it out, or draw it.'
            },
            {
                'level': 'strong',
                'hint': 'Remember to: 1) Show all your work, 2) Label each step, 3) Explain your thinking, 4) Check your answer.'
            }
        ]
        return hints[:current_step + 1] if current_step < len(hints) else hints
    
    @staticmethod
    def save_uploaded_image(image_data: str, student_id: int, activity_id: int) -> str:
        """
        Save uploaded image and return file path
        image_data: base64 encoded image string
        """
        # Create uploads directory if it doesn't exist
        upload_dir = os.path.join('static', 'uploads', 'work', str(student_id))
        os.makedirs(upload_dir, exist_ok=True)
        
        # Generate filename
        timestamp = datetime.utcnow().strftime('%Y%m%d_%H%M%S')
        filename = f"work_{activity_id}_{timestamp}.png"
        filepath = os.path.join(upload_dir, filename)
        
        # Decode and save
        try:
            # Remove data:image/png;base64, prefix if present
            if ',' in image_data:
                image_data = image_data.split(',')[1]
            
            image_bytes = base64.b64decode(image_data)
            
            with open(filepath, 'wb') as f:
                f.write(image_bytes)
            
            # Return web-accessible path
            return filepath.replace('\\', '/')
        except Exception as e:
            raise ValueError(f"Failed to save image: {str(e)}")
    
    def format_for_teacher(self, submission_data: Dict[str, Any]) -> Dict[str, Any]:
        """Format submission for teacher review"""
        work_items = submission_data.get('work_items', [])
        explanation = submission_data.get('explanation', '')
        
        formatted = {
            'total_items': len(work_items),
            'items': [],
            'explanation': explanation,
            'submission_time': submission_data.get('submitted_at', datetime.utcnow().isoformat())
        }
        
        for item in work_items:
            formatted_item = {
                'type': item.get('type'),
                'label': item.get('label', ''),
                'content': item.get('content'),
                'notes': item.get('notes', '')
            }
            formatted['items'].append(formatted_item)
        
        return formatted
