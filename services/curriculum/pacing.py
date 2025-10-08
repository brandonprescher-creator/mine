"""
Pacing Calculator
Convert time settings to lesson counts and durations
"""


def calculate_lesson_distribution(minutes_per_subject, subjects_enabled):
    """Calculate how many lessons to generate per subject"""
    
    # Default distribution
    distribution = {}
    
    for subject in subjects_enabled:
        if minutes_per_subject >= 60:
            # Long sessions: 1 lesson + 1 practice
            distribution[subject] = {'lessons': 1, 'practice': 1, 'review': 0.2}
        elif minutes_per_subject >= 45:
            # Standard: 1 lesson
            distribution[subject] = {'lessons': 1, 'practice': 0.5, 'review': 0.2}
        else:
            # Short: focus on core
            distribution[subject] = {'lessons': 0.8, 'practice': 0.2, 'review': 0}
    
    return distribution


def estimate_time_for_lesson_type(lesson_type, base_minutes=30):
    """Estimate time needed for different lesson types"""
    multipliers = {
        'lesson': 1.0,
        'practice': 0.7,
        'review': 0.5,
        'assessment': 1.2,
        'project': 2.0
    }
    
    return int(base_minutes * multipliers.get(lesson_type, 1.0))
