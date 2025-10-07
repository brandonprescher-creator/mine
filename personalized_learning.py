"""
PERSONALIZED LEARNING PATH SYSTEM
Creates custom learning journeys for each student based on their:
- Current level
- Learning style  
- Strengths and weaknesses
- Goals and interests
- Progress and performance
"""

import json
from typing import Dict, List
from datetime import datetime, timedelta
from database import get_all_subjects, get_topics_by_subject, get_lessons_by_topic

class PersonalizedLearningPath:
    def __init__(self):
        """Initialize personalized learning system"""
        self.learning_styles = {
            'visual': {
                'preference': 'Images, diagrams, videos, colors',
                'strategies': ['Use diagrams', 'Watch videos', 'Draw concepts', 'Use flashcards']
            },
            'auditory': {
                'preference': 'Listening, discussions, explanations',
                'strategies': ['Listen to lectures', 'Discuss with others', 'Read aloud', 'Use mnemonics']
            },
            'kinesthetic': {
                'preference': 'Hands-on, movement, practice',
                'strategies': ['Build models', 'Act out concepts', 'Use manipulatives', 'Practice physically']
            },
            'reading_writing': {
                'preference': 'Reading texts, writing notes',
                'strategies': ['Take detailed notes', 'Rewrite concepts', 'Create summaries', 'Make lists']
            }
        }
        
    def create_learning_path(self, student_profile: Dict) -> Dict:
        """Create a complete personalized learning path"""
        
        # Extract student info
        name = student_profile.get('name', 'Student')
        grade = student_profile.get('grade', 5)
        learning_style = student_profile.get('learning_style', 'visual')
        strengths = student_profile.get('strengths', [])
        weaknesses = student_profile.get('weaknesses', [])
        goals = student_profile.get('goals', [])
        interests = student_profile.get('interests', [])
        time_available = student_profile.get('daily_time', 30)  # minutes per day
        
        # Generate personalized path
        path = {
            'student_name': name,
            'created_date': datetime.now().isoformat(),
            'learning_profile': self.analyze_learning_profile(student_profile),
            'recommended_schedule': self.create_study_schedule(time_available, grade),
            'priority_topics': self.identify_priority_topics(weaknesses, grade),
            'enrichment_topics': self.identify_enrichment(strengths, interests, grade),
            'daily_plan': self.create_daily_plan(time_available, learning_style),
            'weekly_goals': self.set_weekly_goals(goals, grade),
            'monthly_milestones': self.set_monthly_milestones(grade),
            'adaptive_strategies': self.get_adaptive_strategies(learning_style),
            'progress_checkpoints': self.create_checkpoints(),
            'parent_tips': self.generate_parent_tips(learning_style)
        }
        
        return path
    
    def analyze_learning_profile(self, profile: Dict) -> Dict:
        """Analyze student's learning profile"""
        learning_style = profile.get('learning_style', 'visual')
        
        return {
            'primary_learning_style': learning_style,
            'learning_preferences': self.learning_styles[learning_style]['preference'],
            'recommended_strategies': self.learning_styles[learning_style]['strategies'],
            'strengths': profile.get('strengths', []),
            'areas_for_growth': profile.get('weaknesses', []),
            'motivation_factors': self.identify_motivation(profile),
            'optimal_study_time': self.find_optimal_study_time(profile)
        }
    
    def create_study_schedule(self, daily_minutes: int, grade: int) -> Dict:
        """Create personalized study schedule"""
        
        # Distribute time across subjects
        subjects = self.get_subject_time_allocation(daily_minutes, grade)
        
        return {
            'daily_commitment': f'{daily_minutes} minutes',
            'weekly_hours': f'{daily_minutes * 5 / 60:.1f} hours',
            'subject_breakdown': subjects,
            'recommended_times': [
                {'time': 'After school (3-5 PM)', 'benefit': 'Fresh from school, concepts still in mind'},
                {'time': 'Before dinner (5-6 PM)', 'benefit': 'Good energy levels, quiet time'},
                {'time': 'After dinner (7-8 PM)', 'benefit': 'Settled, focused time'}
            ],
            'break_schedule': self.create_break_schedule(daily_minutes),
            'weekend_plan': self.create_weekend_plan(daily_minutes)
        }
    
    def get_subject_time_allocation(self, total_minutes: int, grade: int) -> List[Dict]:
        """Allocate time across subjects based on grade level"""
        
        if grade <= 2:
            return [
                {'subject': 'Reading', 'minutes': total_minutes * 0.4, 'priority': 'High'},
                {'subject': 'Math', 'minutes': total_minutes * 0.4, 'priority': 'High'},
                {'subject': 'Writing', 'minutes': total_minutes * 0.2, 'priority': 'Medium'}
            ]
        elif grade <= 5:
            return [
                {'subject': 'Math', 'minutes': total_minutes * 0.35, 'priority': 'High'},
                {'subject': 'Reading/ELA', 'minutes': total_minutes * 0.30, 'priority': 'High'},
                {'subject': 'Science', 'minutes': total_minutes * 0.20, 'priority': 'Medium'},
                {'subject': 'Social Studies', 'minutes': total_minutes * 0.15, 'priority': 'Medium'}
            ]
        else:
            return [
                {'subject': 'Math', 'minutes': total_minutes * 0.30, 'priority': 'High'},
                {'subject': 'English', 'minutes': total_minutes * 0.25, 'priority': 'High'},
                {'subject': 'Science', 'minutes': total_minutes * 0.25, 'priority': 'High'},
                {'subject': 'Social Studies', 'minutes': total_minutes * 0.20, 'priority': 'Medium'}
            ]
    
    def identify_priority_topics(self, weaknesses: List[str], grade: int) -> List[Dict]:
        """Identify topics that need immediate attention"""
        
        priorities = []
        
        for weakness in weaknesses:
            priorities.append({
                'topic': weakness,
                'why_important': f'Foundational skill for grade {grade} success',
                'estimated_time': '2-3 weeks of focused practice',
                'resources': [
                    'Dedicated lessons with step-by-step guidance',
                    'Extra practice problems',
                    'Visual aids and manipulatives',
                    'One-on-one tutoring sessions'
                ],
                'success_indicators': [
                    'Can explain concept to others',
                    '80%+ accuracy on practice problems',
                    'Confidence in applying skill'
                ]
            })
        
        # Add grade-level priorities
        if grade >= 3:
            priorities.append({
                'topic': 'Multiplication Facts',
                'why_important': 'Essential for all higher-level math',
                'estimated_time': '1 month of daily practice',
                'resources': ['Flashcards', 'Games', 'Timed drills'],
                'success_indicators': ['Automatic recall', 'Quick mental math']
            })
        
        return priorities
    
    def identify_enrichment(self, strengths: List[str], interests: List[str], grade: int) -> List[Dict]:
        """Identify enrichment opportunities"""
        
        enrichment = []
        
        for strength in strengths:
            enrichment.append({
                'area': strength,
                'enrichment_activities': [
                    f'Advanced {strength} challenges',
                    f'Creative projects in {strength}',
                    f'Peer tutoring in {strength}',
                    f'Competition/contest opportunities'
                ],
                'extension_topics': [
                    f'Beyond grade-level {strength}',
                    f'Real-world applications',
                    f'Cross-disciplinary connections'
                ]
            })
        
        for interest in interests:
            enrichment.append({
                'area': interest,
                'connection_to_learning': f'Use {interest} to enhance engagement',
                'project_ideas': [
                    f'{interest}-based math problems',
                    f'{interest}-themed reading',
                    f'Research project on {interest}'
                ]
            })
        
        return enrichment
    
    def create_daily_plan(self, total_minutes: int, learning_style: str) -> Dict:
        """Create detailed daily study plan"""
        
        return {
            'total_time': f'{total_minutes} minutes',
            'phases': [
                {
                    'name': 'Warm-up',
                    'duration': '5 min',
                    'activities': ['Review yesterday', 'Quick mental math', 'Preview today']
                },
                {
                    'name': 'New Learning',
                    'duration': f'{total_minutes * 0.4:.0f} min',
                    'activities': [
                        'Watch lesson video' if learning_style == 'visual' else 'Read lesson',
                        'Take notes',
                        'Try examples'
                    ]
                },
                {
                    'name': 'Practice',
                    'duration': f'{total_minutes * 0.3:.0f} min',
                    'activities': ['Solve problems', 'Check answers', 'Review mistakes']
                },
                {
                    'name': 'Application',
                    'duration': f'{total_minutes * 0.15:.0f} min',
                    'activities': ['Real-world problem', 'Creative exercise', 'Challenge question']
                },
                {
                    'name': 'Review & Reflect',
                    'duration': f'{total_minutes * 0.15:.0f} min',
                    'activities': ['Summarize learnings', 'Self-quiz', 'Plan tomorrow']
                }
            ],
            'tips': [
                'Start with easiest task to build momentum',
                'Take 5-minute break halfway through',
                'End with something fun or interesting',
                'Celebrate completed work!'
            ]
        }
    
    def set_weekly_goals(self, goals: List[str], grade: int) -> List[Dict]:
        """Set achievable weekly goals"""
        
        weekly_goals = []
        
        # Academic goals
        weekly_goals.append({
            'type': 'Academic',
            'goals': [
                'Complete all assigned lessons',
                'Practice 30 minutes daily',
                'Master 1-2 new concepts',
                'Review previous week material'
            ],
            'tracking': 'Check off daily progress'
        })
        
        # Skill development
        weekly_goals.append({
            'type': 'Skill Development',
            'goals': [
                'Improve speed on timed drills',
                'Write more detailed explanations',
                'Ask at least 3 good questions',
                'Help a classmate understand'
            ],
            'tracking': 'Journal progress'
        })
        
        # Personal goals from student
        if goals:
            weekly_goals.append({
                'type': 'Personal Goals',
                'goals': goals[:3],  # Top 3 personal goals
                'tracking': 'Self-assessment at week end'
            })
        
        return weekly_goals
    
    def set_monthly_milestones(self, grade: int) -> List[Dict]:
        """Set monthly achievement milestones"""
        
        return [
            {
                'month': 1,
                'milestone': 'Foundation Building',
                'objectives': [
                    'Master all prerequisite skills',
                    'Build daily study habit',
                    'Complete diagnostic assessment'
                ],
                'celebration': 'First month success badge!'
            },
            {
                'month': 2,
                'milestone': 'Skill Development',
                'objectives': [
                    'Advance to new topics',
                    'Improve accuracy by 20%',
                    'Complete 50+ practice problems'
                ],
                'celebration': 'Skill builder achievement!'
            },
            {
                'month': 3,
                'milestone': 'Application & Mastery',
                'objectives': [
                    'Apply skills to real problems',
                    'Achieve 85%+ mastery',
                    'Help others learn'
                ],
                'celebration': 'Expert learner status!'
            }
        ]
    
    def get_adaptive_strategies(self, learning_style: str) -> Dict:
        """Get strategies that adapt to learning style"""
        
        strategies = {
            'visual': {
                'techniques': [
                    'Use color coding for different concepts',
                    'Draw diagrams and flowcharts',
                    'Watch educational videos',
                    'Create mind maps',
                    'Use flashcards with images'
                ],
                'tools': ['Colored pens', 'Graph paper', 'Whiteboard', 'Online visualizations']
            },
            'auditory': {
                'techniques': [
                    'Read problems aloud',
                    'Explain concepts to yourself',
                    'Listen to educational podcasts',
                    'Create songs or rhymes',
                    'Participate in discussions'
                ],
                'tools': ['Voice recorder', 'Educational podcasts', 'Study groups']
            },
            'kinesthetic': {
                'techniques': [
                    'Use manipulatives (blocks, counters)',
                    'Act out word problems',
                    'Build physical models',
                    'Take movement breaks',
                    'Use gestures to remember'
                ],
                'tools': ['Math manipulatives', 'Building materials', 'Movement space']
            },
            'reading_writing': {
                'techniques': [
                    'Write detailed notes',
                    'Create summary sheets',
                    'Rewrite examples',
                    'Make study guides',
                    'Journal about learning'
                ],
                'tools': ['Notebooks', 'Highlighters', 'Study guides', 'Templates']
            }
        }
        
        return strategies.get(learning_style, strategies['visual'])
    
    def create_checkpoints(self) -> List[Dict]:
        """Create progress checkpoints"""
        
        return [
            {
                'checkpoint': 'Daily',
                'check': 'Did I complete today\'s plan?',
                'action': 'Review and adjust tomorrow\'s plan'
            },
            {
                'checkpoint': 'Weekly',
                'check': 'Am I meeting my weekly goals?',
                'action': 'Identify what\'s working and what needs adjustment'
            },
            {
                'checkpoint': 'Bi-weekly',
                'check': 'Take practice quiz/assessment',
                'action': 'Identify gaps and create focused practice'
            },
            {
                'checkpoint': 'Monthly',
                'check': 'Have I achieved monthly milestones?',
                'action': 'Celebrate success and set new goals'
            }
        ]
    
    def generate_parent_tips(self, learning_style: str) -> List[str]:
        """Generate tips for parents"""
        
        return [
            f"💡 Your child is a {learning_style} learner - use their strengths!",
            "🕐 Establish consistent study time and routine",
            "📊 Review progress together weekly",
            "🎉 Celebrate small wins and effort, not just grades",
            "❓ Ask 'What did you learn today?' instead of 'What's your homework?'",
            "🤝 Be available for questions but encourage independence",
            "📚 Provide quiet, organized study space",
            "⏰ Help manage time but let them own their schedule",
            "💪 Focus on growth mindset - mistakes are learning opportunities",
            "🌟 Connect learning to their interests and real life"
        ]
    
    def create_break_schedule(self, total_minutes: int) -> Dict:
        """Create optimal break schedule"""
        
        if total_minutes <= 20:
            return {'breaks': 'No break needed', 'note': 'Stay focused for short duration'}
        elif total_minutes <= 40:
            return {
                'breaks': [{'after': '20 min', 'duration': '5 min', 'activity': 'Stretch, water, quick walk'}],
                'note': 'One break to refresh'
            }
        else:
            return {
                'breaks': [
                    {'after': '20 min', 'duration': '5 min', 'activity': 'Stretch and hydrate'},
                    {'after': '45 min', 'duration': '10 min', 'activity': 'Snack, move around, relax eyes'}
                ],
                'note': 'Regular breaks improve focus and retention'
            }
    
    def create_weekend_plan(self, daily_minutes: int) -> Dict:
        """Create weekend study plan"""
        
        return {
            'saturday': {
                'focus': 'Review and practice',
                'time': f'{daily_minutes} minutes',
                'activities': [
                    'Review entire week',
                    'Extra practice on weak areas',
                    'Fun educational games',
                    'Creative project or exploration'
                ]
            },
            'sunday': {
                'focus': 'Preview and prepare',
                'time': f'{daily_minutes * 0.5:.0f} minutes',
                'activities': [
                    'Preview next week topics',
                    'Organize materials',
                    'Set weekly goals',
                    'Light review only'
                ]
            },
            'flexibility': 'Adjust based on family schedule and student energy'
        }
    
    def identify_motivation(self, profile: Dict) -> List[str]:
        """Identify what motivates the student"""
        
        motivators = []
        
        interests = profile.get('interests', [])
        if interests:
            motivators.append(f"Uses {', '.join(interests)} as learning themes")
        
        goals = profile.get('goals', [])
        if goals:
            motivators.append(f"Working towards: {', '.join(goals)}")
        
        # Add general motivators
        motivators.extend([
            "Achievement and progress visibility",
            "Gamification and rewards",
            "Positive reinforcement",
            "Real-world connections",
            "Choice and autonomy in learning"
        ])
        
        return motivators
    
    def find_optimal_study_time(self, profile: Dict) -> str:
        """Find optimal study time for student"""
        
        # This would use actual data about when student performs best
        # For now, provide general guidance
        
        return """
        Research suggests most elementary students focus best:
        - Mid-morning (after breakfast, before lunch)
        - Late afternoon (after school, before dinner)
        - Early evening (after dinner, before bedtime routine)
        
        Experiment to find YOUR child's peak focus time!
        """


# Global instance
personalized_learning = PersonalizedLearningPath()


def create_student_path(profile: Dict) -> Dict:
    """Quick function to create personalized learning path"""
    return personalized_learning.create_learning_path(profile)

