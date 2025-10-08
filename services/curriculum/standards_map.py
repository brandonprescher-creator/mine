"""
Standards Mapping Service
Map activities to educational standards (CCSS, NGSS, etc.)
"""
from models.database import db, Standard, Skill


class StandardsMapper:
    """Map content to standards"""
    
    @staticmethod
    def get_standards_for_grade_subject(grade, subject):
        """Get all standards for a grade/subject"""
        return Standard.query.filter_by(grade=grade, subject=subject).all()
    
    @staticmethod
    def find_matching_standards(topic, subject, grade=None):
        """Find standards matching a topic"""
        query = Standard.query.filter_by(subject=subject)
        
        if grade:
            query = query.filter_by(grade=grade)
        
        query = query.filter(
            db.or_(
                Standard.name.ilike(f'%{topic}%'),
                Standard.description.ilike(f'%{topic}%')
            )
        )
        
        return query.all()
    
    @staticmethod
    def get_skill_progression(standard_id):
        """Get skills in recommended order for a standard"""
        skills = Skill.query.filter_by(standard_id=standard_id).all()
        
        # Sort by difficulty
        order = {'easy': 0, 'medium': 1, 'hard': 2}
        return sorted(skills, key=lambda s: order.get(s.difficulty, 1))
