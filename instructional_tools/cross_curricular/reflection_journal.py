"""
Goal Setting & Reflection Journals
Metacognition and self-directed learning
"""
from typing import Dict, List, Any, Optional
from datetime import datetime


class LearningGoal:
    """A student's learning goal"""
    def __init__(self, id: int, goal_text: str, subject: str, target_date: Optional[str] = None):
        self.id = id
        self.goal_text = goal_text
        self.subject = subject
        self.target_date = target_date
        self.created_at = datetime.utcnow().isoformat()
        self.completed = False
        self.completed_at = None
        self.progress_notes = []
    
    def add_progress_note(self, note: str):
        """Add a progress note"""
        self.progress_notes.append({'date': datetime.utcnow().isoformat(), 'note': note})
    
    def complete_goal(self, reflection: str):
        """Mark goal as complete with reflection"""
        self.completed = True
        self.completed_at = datetime.utcnow().isoformat()
        self.add_progress_note(f"COMPLETED: {reflection}")
    
    def to_dict(self) -> Dict[str, Any]:
        return {'id': self.id, 'goal': self.goal_text, 'subject': self.subject, 'target_date': self.target_date, 'created_at': self.created_at, 'completed': self.completed, 'progress_notes': self.progress_notes}


class ReflectionEntry:
    """A reflection journal entry"""
    def __init__(self, id: int, prompt: str, response: str, lesson_id: Optional[int] = None):
        self.id = id
        self.prompt = prompt
        self.response = response
        self.lesson_id = lesson_id
        self.created_at = datetime.utcnow().isoformat()
    
    def to_dict(self) -> Dict[str, Any]:
        return {'id': self.id, 'prompt': self.prompt, 'response': self.response, 'lesson_id': self.lesson_id, 'created_at': self.created_at}


class ReflectionJournal:
    """Student reflection and goal setting journal"""
    
    REFLECTION_PROMPTS = [
        'What did you learn today?',
        'What was challenging? How did you overcome it?',
        'What are you most proud of?',
        'What will you do differently next time?',
        'How can you use this learning in real life?',
        'What questions do you still have?',
        'How did you grow as a learner?',
        'What strategy worked well for you?'
    ]
    
    def __init__(self, student_id: int):
        self.student_id = student_id
        self.goals: List[LearningGoal] = []
        self.reflections: List[ReflectionEntry] = []
        self.goal_id_counter = 0
        self.reflection_id_counter = 0
    
    def set_goal(self, goal_text: str, subject: str, target_date: Optional[str] = None) -> LearningGoal:
        """Set a new learning goal"""
        goal = LearningGoal(self.goal_id_counter, goal_text, subject, target_date)
        self.goals.append(goal)
        self.goal_id_counter += 1
        return goal
    
    def add_reflection(self, prompt: str, response: str, lesson_id: Optional[int] = None) -> ReflectionEntry:
        """Add a reflection entry"""
        entry = ReflectionEntry(self.reflection_id_counter, prompt, response, lesson_id)
        self.reflections.append(entry)
        self.reflection_id_counter += 1
        return entry
    
    def get_active_goals(self) -> List[LearningGoal]:
        """Get goals that are not yet completed"""
        return [g for g in self.goals if not g.completed]
    
    def get_recent_reflections(self, count: int = 5) -> List[ReflectionEntry]:
        """Get recent reflection entries"""
        return sorted(self.reflections, key=lambda r: r.created_at, reverse=True)[:count]
    
    def to_dict(self) -> Dict[str, Any]:
        return {'student_id': self.student_id, 'active_goals': [g.to_dict() for g in self.get_active_goals()], 'recent_reflections': [r.to_dict() for r in self.get_recent_reflections()], 'total_goals': len(self.goals), 'total_reflections': len(self.reflections)}
