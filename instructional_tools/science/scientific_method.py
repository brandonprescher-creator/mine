"""
Scientific Method Step Tracker
Guide students through the scientific method
"""
from typing import Dict, List, Any, Optional
from datetime import datetime


class ScientificMethodTracker:
    """
    Scientific Method Step Tracker
    
    Steps:
    1. Ask a Question
    2. Research
    3. Hypothesis
    4. Experiment
    5. Analyze Data
    6. Conclude
    7. Communicate
    """
    
    STEPS = [
        {'id': 1, 'name': 'Ask a Question', 'description': 'What do you want to know?', 'icon': '❓'},
        {'id': 2, 'name': 'Background Research', 'description': 'What is already known?', 'icon': '📚'},
        {'id': 3, 'name': 'Hypothesis', 'description': 'What do you predict?', 'icon': '💭'},
        {'id': 4, 'name': 'Experiment', 'description': 'How will you test it?', 'icon': '🧪'},
        {'id': 5, 'name': 'Analyze Data', 'description': 'What did you observe?', 'icon': '📊'},
        {'id': 6, 'name': 'Conclusion', 'description': 'What did you learn?', 'icon': '🎯'},
        {'id': 7, 'name': 'Communicate', 'description': 'How will you share results?', 'icon': '📢'}
    ]
    
    def __init__(self, experiment_title: str):
        self.experiment_title = experiment_title
        self.step_data = {step['id']: {'completed': False, 'content': '', 'completed_at': None} for step in self.STEPS}
        self.current_step = 1
    
    def complete_step(self, step_id: int, content: str):
        """Mark a step as complete with content"""
        if step_id in self.step_data:
            self.step_data[step_id] = {'completed': True, 'content': content, 'completed_at': datetime.utcnow().isoformat()}
            
            # Advance to next uncompleted step
            for i in range(step_id + 1, 8):
                if not self.step_data[i]['completed']:
                    self.current_step = i
                    break
    
    def get_progress(self) -> Dict[str, Any]:
        """Get progress through scientific method"""
        completed_count = sum(1 for step in self.step_data.values() if step['completed'])
        return {'completed_steps': completed_count, 'total_steps': len(self.STEPS), 'percentage': round((completed_count / len(self.STEPS)) * 100, 1), 'current_step': self.current_step}
    
    def get_prompts_for_step(self, step_id: int) -> List[str]:
        """Get guiding prompts for a specific step"""
        prompts = {
            1: ['What are you curious about?', 'What problem needs solving?', 'What would you like to investigate?'],
            2: ['What information can you find about this topic?', 'What have others discovered?', 'What background knowledge do you need?'],
            3: ['What do you think will happen?', 'Why do you think that?', 'How can you test this prediction?'],
            4: ['What materials do you need?', 'What steps will you follow?', 'What variables will you control?'],
            5: ['What did you observe?', 'What patterns do you see in the data?', 'Do the results support your hypothesis?'],
            6: ['Was your hypothesis supported?', 'What did you learn?', 'What questions do you still have?'],
            7: ['How will you present your findings?', 'What are the key takeaways?', 'What should others know?']
        }
        return prompts.get(step_id, [])
    
    def to_dict(self) -> Dict[str, Any]:
        """Export tracker data"""
        return {'experiment_title': self.experiment_title, 'steps': [{'step_info': step, 'data': self.step_data[step['id']]} for step in self.STEPS], 'progress': self.get_progress()}
