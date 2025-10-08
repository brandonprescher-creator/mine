"""
Mastery Tracking Engine
Updates skill levels based on evidence and spaced repetition
"""
from datetime import datetime, timedelta
from models.database import db, SkillState, Submission, Assignment
from sqlalchemy import func


class MasteryEngine:
    """Track and update skill mastery levels"""
    
    LEVELS = {
        0: 'not_attempted',
        1: 'in_progress',
        2: 'developing',
        3: 'proficient',
        4: 'approaching_mastery',
        5: 'mastered'
    }
    
    SPACED_INTERVALS = [1, 3, 7, 14, 30]  # Days
    
    @staticmethod
    def record_practice(child_id, skill_id, success, score=None):
        """Record a practice attempt and update mastery"""
        
        # Get or create skill state
        skill_state = SkillState.query.filter_by(
            child_id=child_id,
            skill_id=skill_id
        ).first()
        
        if not skill_state:
            skill_state = SkillState(
                child_id=child_id,
                skill_id=skill_id,
                level=0
            )
            db.session.add(skill_state)
        
        # Update history
        history = skill_state.history
        history.append({
            'date': datetime.utcnow().isoformat(),
            'success': success,
            'score': score
        })
        skill_state.history = history
        
        skill_state.evidence_count += 1
        skill_state.last_practice = datetime.utcnow()
        
        # Update level
        skill_state.level = MasteryEngine._calculate_new_level(history, skill_state.level)
        
        # Calculate next review date
        skill_state.next_due = MasteryEngine._calculate_next_review(skill_state.level)
        
        db.session.commit()
        
        return skill_state
    
    @staticmethod
    def _calculate_new_level(history, current_level):
        """Calculate new mastery level based on history"""
        if len(history) < 3:
            return min(1, current_level + 1) if history[-1]['success'] else current_level
        
        # Look at last 5 attempts
        recent = history[-5:]
        success_rate = sum(1 for h in recent if h['success']) / len(recent)
        
        if success_rate >= 0.9 and len(history) >= 5:
            return min(5, current_level + 1)
        elif success_rate >= 0.75:
            return min(4, current_level + 1)
        elif success_rate >= 0.6:
            return min(3, current_level)
        elif success_rate < 0.4:
            return max(1, current_level - 1)
        
        return current_level
    
    @staticmethod
    def _calculate_next_review(level):
        """Calculate next review date based on mastery level"""
        if level >= len(MasteryEngine.SPACED_INTERVALS):
            days = MasteryEngine.SPACED_INTERVALS[-1]
        else:
            days = MasteryEngine.SPACED_INTERVALS[level]
        
        return datetime.utcnow() + timedelta(days=days)
    
    @staticmethod
    def get_skills_for_review(child_id, limit=5):
        """Get skills due for review"""
        now = datetime.utcnow()
        
        skills = SkillState.query.filter(
            SkillState.child_id == child_id,
            SkillState.next_due <= now,
            SkillState.level < 5
        ).order_by(SkillState.next_due, SkillState.level).limit(limit).all()
        
        return skills
