"""
Weekly Lesson Planner
Generates comprehensive weekly lesson plans
"""
from datetime import date, timedelta
from models.database import db, LessonPlan, LessonItem, Assignment, Skill, Standard
from services.curriculum.scope_sequence import get_skills_for_grade_subject
from services.curriculum.pacing import calculate_lesson_distribution
import random


class WeeklyPlanner:
    """Generate weekly lesson plans for students"""
    
    def __init__(self, child):
        self.child = child
        self.grade = child.grade
    
    def generate_week(self, week_start, subjects, minutes_per_subject=45):
        """Generate a complete week of lessons"""
        
        # Create lesson plan
        lesson_plan = LessonPlan(
            child_id=self.child.id,
            week_start_date=week_start
        )
        lesson_plan.settings = {
            'subjects': subjects,
            'minutes_per_subject': minutes_per_subject,
            'school_days': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
        }
        
        db.session.add(lesson_plan)
        db.session.flush()  # Get ID
        
        # Generate items for each subject and day
        for day_offset in range(5):  # Mon-Fri
            lesson_date = week_start + timedelta(days=day_offset)
            
            for subject in subjects:
                # Get skills for this grade/subject
                skills = get_skills_for_grade_subject(self.grade, subject)
                
                if not skills:
                    continue
                
                # Select skill for this lesson
                skill = random.choice(skills)
                
                # Create lesson item
                item = self._create_lesson_item(
                    lesson_plan.id,
                    subject,
                    [skill.id],
                    minutes_per_subject
                )
                
                db.session.add(item)
                db.session.flush()
                
                # Create assignment for this day
                assignment = Assignment(
                    child_id=self.child.id,
                    lesson_item_id=item.id,
                    date=lesson_date,
                    status='pending'
                )
                db.session.add(assignment)
        
        db.session.commit()
        return lesson_plan
    
    def _create_lesson_item(self, lesson_plan_id, subject, skill_ids, est_minutes):
        """Create a single lesson item"""
        
        # Determine lesson type based on day/subject
        lesson_types = ['lesson', 'practice', 'review', 'assessment']
        weights = [0.5, 0.3, 0.15, 0.05]
        item_type = random.choices(lesson_types, weights=weights)[0]
        
        item = LessonItem(
            lesson_plan_id=lesson_plan_id,
            subject=subject,
            type=item_type,
            est_minutes=est_minutes
        )
        item.skill_ids = skill_ids
        item.resource_ids = []  # Would fetch from resources
        
        return item
    
    def reorder_item(self, item_id, new_index):
        """Reorder lesson item"""
        item = LessonItem.query.get(item_id)
        if item:
            item.order_index = new_index
            db.session.commit()
    
    def carry_over_incomplete(self, from_date):
        """Carry over incomplete assignments to next day"""
        incomplete = Assignment.query.filter_by(
            child_id=self.child.id,
            date=from_date,
            status='pending'
        ).all()
        
        next_date = from_date + timedelta(days=1)
        
        for assignment in incomplete:
            new_assignment = Assignment(
                child_id=self.child.id,
                lesson_item_id=assignment.lesson_item_id,
                date=next_date,
                status='pending'
            )
            db.session.add(new_assignment)
        
        db.session.commit()
        return len(incomplete)
