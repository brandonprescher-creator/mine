"""
Scope & Sequence
Default order of skills per grade/subject
"""
from models.database import db, Skill, Standard


def get_skills_for_grade_subject(grade, subject):
    """Get skills for a specific grade and subject"""
    # Get standards for this grade/subject
    standards = Standard.query.filter_by(
        grade=grade,
        subject=subject
    ).all()
    
    if not standards:
        return []
    
    # Get all skills for these standards
    standard_ids = [s.id for s in standards]
    skills = Skill.query.filter(
        Skill.standard_id.in_(standard_ids)
    ).all()
    
    return skills


def get_default_sequence(grade, subject):
    """Get recommended teaching sequence"""
    skills = get_skills_for_grade_subject(grade, subject)
    
    # Sort by difficulty and dependencies
    # Simplified - would have curriculum experts define proper sequence
    easy = [s for s in skills if s.difficulty == 'easy']
    medium = [s for s in skills if s.difficulty == 'medium']
    hard = [s for s in skills if s.difficulty == 'hard']
    
    return easy + medium + hard
