"""
Project-Based Learning Planner
Plan and track PBL projects from objectives to reflection
"""
from typing import Dict, List, Any, Optional
from datetime import datetime


class ProjectTask:
    """A task in a project"""
    def __init__(self, id: int, title: str, description: str, due_date: Optional[str] = None):
        self.id = id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = False
        self.completed_at = None
    
    def complete(self):
        """Mark task as complete"""
        self.completed = True
        self.completed_at = datetime.utcnow().isoformat()
    
    def to_dict(self) -> Dict[str, Any]:
        return {'id': self.id, 'title': self.title, 'description': self.description, 'due_date': self.due_date, 'completed': self.completed, 'completed_at': self.completed_at}


class ProjectPlanner:
    """
    Project-Based Learning Planner
    
    Components:
    - Objectives
    - Tasks
    - Resources
    - Timeline
    - Reflection
    """
    
    def __init__(self, project_title: str, driving_question: str):
        self.project_title = project_title
        self.driving_question = driving_question
        self.objectives: List[str] = []
        self.tasks: List[ProjectTask] = []
        self.resources: List[Dict[str, str]] = []
        self.reflection = ''
        self.task_id_counter = 0
    
    def add_objective(self, objective: str):
        """Add a learning objective"""
        self.objectives.append(objective)
    
    def add_task(self, title: str, description: str, due_date: Optional[str] = None) -> ProjectTask:
        """Add a project task"""
        task = ProjectTask(self.task_id_counter, title, description, due_date)
        self.tasks.append(task)
        self.task_id_counter += 1
        return task
    
    def add_resource(self, title: str, url: str, resource_type: str):
        """Add a project resource"""
        self.resources.append({'title': title, 'url': url, 'type': resource_type})
    
    def get_progress(self) -> Dict[str, Any]:
        """Get project progress"""
        completed_tasks = sum(1 for task in self.tasks if task.completed)
        return {'completed_tasks': completed_tasks, 'total_tasks': len(self.tasks), 'percentage': round((completed_tasks / len(self.tasks)) * 100, 1) if self.tasks else 0}
    
    def to_dict(self) -> Dict[str, Any]:
        return {'title': self.project_title, 'driving_question': self.driving_question, 'objectives': self.objectives, 'tasks': [t.to_dict() for t in self.tasks], 'resources': self.resources, 'reflection': self.reflection, 'progress': self.get_progress()}
