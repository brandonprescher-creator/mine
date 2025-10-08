"""
Achievement & Badge System
Reward learning behaviors and milestones
"""
from typing import Dict, List, Any, Optional
from datetime import datetime


class Achievement:
    """An achievement/badge"""
    def __init__(self, id: str, name: str, description: str, icon: str, category: str, points: int, criteria: Dict[str, Any]):
        self.id = id
        self.name = name
        self.description = description
        self.icon = icon
        self.category = category  # 'reasoning', 'persistence', 'creativity', 'mastery', 'collaboration'
        self.points = points
        self.criteria = criteria
    
    def to_dict(self) -> Dict[str, Any]:
        return {'id': self.id, 'name': self.name, 'description': self.description, 'icon': self.icon, 'category': self.category, 'points': self.points}


class StudentAchievement:
    """A student's earned achievement"""
    def __init__(self, achievement: Achievement, earned_at: Optional[str] = None):
        self.achievement = achievement
        self.earned_at = earned_at or datetime.utcnow().isoformat()
    
    def to_dict(self) -> Dict[str, Any]:
        data = self.achievement.to_dict()
        data['earned_at'] = self.earned_at
        return data


class AchievementSystem:
    """Manage achievements and badges"""
    
    def __init__(self):
        self.achievements: Dict[str, Achievement] = {}
        self._load_default_achievements()
    
    def _load_default_achievements(self):
        """Load default achievements"""
        defaults = [
            Achievement('first_lesson', 'First Steps', 'Complete your first lesson', '🎯', 'milestones', 10, {'lessons_completed': 1}),
            Achievement('show_work', 'Work Shower', 'Show your work 10 times', '📝', 'reasoning', 20, {'work_shown': 10}),
            Achievement('perfect_score', 'Perfect!', 'Get 100% on an assignment', '💯', 'mastery', 25, {'perfect_assignments': 1}),
            Achievement('persistent', 'Never Give Up', 'Complete 50 practice problems', '💪', 'persistence', 30, {'problems_completed': 50}),
            Achievement('creative_thinker', 'Creative Mind', 'Submit 5 creative projects', '🎨', 'creativity', 25, {'creative_submissions': 5}),
            Achievement('helper', 'Helpful Friend', 'Help 5 classmates', '🤝', 'collaboration', 20, {'peer_helps': 5}),
            Achievement('bookworm', 'Bookworm', 'Complete 20 reading activities', '📚', 'mastery', 30, {'reading_activities': 20}),
            Achievement('math_master', 'Math Master', 'Master 25 math standards', '🧮', 'mastery', 50, {'math_standards_mastered': 25}),
            Achievement('scientist', 'Young Scientist', 'Complete 10 lab reports', '🔬', 'mastery', 40, {'lab_reports': 10}),
            Achievement('streak_7', '7-Day Streak', 'Practice 7 days in a row', '🔥', 'persistence', 35, {'streak_days': 7})
        ]
        
        for achievement in defaults:
            self.achievements[achievement.id] = achievement
    
    def check_achievement(self, achievement_id: str, student_stats: Dict[str, int]) -> bool:
        """Check if student has earned an achievement"""
        achievement = self.achievements.get(achievement_id)
        if not achievement:
            return False
        
        for criterion, required_value in achievement.criteria.items():
            if student_stats.get(criterion, 0) < required_value:
                return False
        
        return True
    
    def get_earned_achievements(self, student_stats: Dict[str, int]) -> List[Achievement]:
        """Get all achievements earned by student"""
        earned = []
        for achievement in self.achievements.values():
            if self.check_achievement(achievement.id, student_stats):
                earned.append(achievement)
        return earned
    
    def get_next_achievements(self, student_stats: Dict[str, int], limit: int = 5) -> List[Dict[str, Any]]:
        """Get achievements student is close to earning"""
        close_achievements = []
        
        for achievement in self.achievements.values():
            if self.check_achievement(achievement.id, student_stats):
                continue  # Already earned
            
            progress = []
            for criterion, required in achievement.criteria.items():
                current = student_stats.get(criterion, 0)
                progress.append({'criterion': criterion, 'current': current, 'required': required, 'percentage': round((current / required) * 100, 1)})
            
            avg_progress = sum(p['percentage'] for p in progress) / len(progress)
            
            if avg_progress >= 50:  # At least 50% towards earning
                close_achievements.append({'achievement': achievement.to_dict(), 'progress': progress, 'overall_progress': avg_progress})
        
        return sorted(close_achievements, key=lambda x: x['overall_progress'], reverse=True)[:limit]
