"""
PARENT DASHBOARD - MISSION CONTROL
Complete oversight and management system for homeschool parents
"""

import json
from datetime import datetime, timedelta
from typing import Dict, List, Optional
from database import (
    get_connection,
    get_all_subjects,
    get_topics_by_subject,
    get_lessons_by_topic,
)


class ParentDashboard:
    """Mission Control for parents managing multiple students"""

    def __init__(self):
        self.students = {}  # Will be populated from database

    def get_daily_digest(self, student_id: str) -> Dict:
        """Get comprehensive daily summary for a student"""
        conn = get_connection()
        cursor = conn.cursor()

        # Get today's activity
        today = datetime.now().date()
        cursor.execute(
            """
            SELECT 
                COUNT(DISTINCT lesson_id) as lessons_worked,
                SUM(time_spent) as total_time,
                AVG(score) as avg_score,
                COUNT(*) as total_attempts
            FROM user_progress 
            WHERE user_id = ? AND DATE(created_at) = ?
        """,
            (student_id, today),
        )

        activity = dict(cursor.fetchone())

        # Get recent achievements
        cursor.execute(
            """
            SELECT achievement_id, earned_at
            FROM user_achievements
            WHERE user_id = ? AND DATE(earned_at) = ?
            ORDER BY earned_at DESC
        """,
            (student_id, today),
        )

        achievements = [dict(row) for row in cursor.fetchall()]

        # Get struggle areas (wrong answers > 3 times)
        cursor.execute(
            """
            SELECT l.title, COUNT(*) as error_count
            FROM user_progress up
            JOIN lessons l ON up.lesson_id = l.id
            WHERE up.user_id = ? AND up.completed = 0 
            AND DATE(up.created_at) >= DATE('now', '-7 days')
            GROUP BY up.lesson_id
            HAVING error_count >= 3
            ORDER BY error_count DESC
            LIMIT 5
        """,
            (student_id,),
        )

        struggles = [dict(row) for row in cursor.fetchall()]

        # Get mastery progress
        cursor.execute(
            """
            SELECT mastery_level, COUNT(*) as count
            FROM user_progress
            WHERE user_id = ?
            GROUP BY mastery_level
        """,
            (student_id,),
        )

        mastery = {row["mastery_level"]: row["count"] for row in cursor.fetchall()}

        conn.close()

        return {
            "student_id": student_id,
            "date": str(today),
            "activity": activity,
            "achievements_today": achievements,
            "struggle_areas": struggles,
            "mastery_distribution": mastery,
            "time_spent_minutes": activity.get("total_time", 0) or 0,
            "lessons_completed": activity.get("lessons_worked", 0) or 0,
        }

    def get_weekly_progress(self, student_id: str) -> Dict:
        """Get weekly progress summary"""
        conn = get_connection()
        cursor = conn.cursor()

        week_ago = (datetime.now() - timedelta(days=7)).date()

        cursor.execute(
            """
            SELECT 
                DATE(created_at) as day,
                COUNT(DISTINCT lesson_id) as lessons,
                SUM(time_spent) as time_spent,
                AVG(score) as avg_score
            FROM user_progress
            WHERE user_id = ? AND DATE(created_at) >= ?
            GROUP BY DATE(created_at)
            ORDER BY day
        """,
            (student_id, week_ago),
        )

        daily_stats = [dict(row) for row in cursor.fetchall()]

        conn.close()

        return {
            "student_id": student_id,
            "week_start": str(week_ago),
            "daily_breakdown": daily_stats,
            "total_time": sum(day.get("time_spent", 0) or 0 for day in daily_stats),
            "total_lessons": sum(day.get("lessons", 0) or 0 for day in daily_stats),
            "avg_score": (
                sum(day.get("avg_score", 0) or 0 for day in daily_stats)
                / len(daily_stats)
                if daily_stats
                else 0
            ),
        }

    def create_learning_playlist(
        self, student_id: str, playlist_name: str, lesson_ids: List[int]
    ) -> Dict:
        """Create a custom learning playlist for a student"""
        conn = get_connection()
        cursor = conn.cursor()

        # Create playlist
        cursor.execute(
            """
            INSERT INTO learning_playlists (student_id, name, lesson_ids, created_at)
            VALUES (?, ?, ?, ?)
        """,
            (student_id, playlist_name, json.dumps(lesson_ids), datetime.now()),
        )

        playlist_id = cursor.lastrowid
        conn.commit()
        conn.close()

        return {
            "playlist_id": playlist_id,
            "name": playlist_name,
            "lesson_count": len(lesson_ids),
            "created": str(datetime.now()),
        }

    def schedule_lesson(
        self, student_id: str, lesson_id: int, scheduled_date: str
    ) -> Dict:
        """Schedule a lesson for a specific date"""
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO lesson_schedule (student_id, lesson_id, scheduled_date, created_at)
            VALUES (?, ?, ?, ?)
        """,
            (student_id, lesson_id, scheduled_date, datetime.now()),
        )

        conn.commit()
        conn.close()

        return {
            "student_id": student_id,
            "lesson_id": lesson_id,
            "scheduled_for": scheduled_date,
            "status": "scheduled",
        }

    def get_struggle_recommendations(self, student_id: str) -> List[Dict]:
        """AI-powered recommendations for struggling areas"""
        digest = self.get_daily_digest(student_id)
        struggles = digest["struggle_areas"]

        recommendations = []
        for struggle in struggles:
            recommendations.append(
                {
                    "topic": struggle["title"],
                    "error_count": struggle["error_count"],
                    "severity": (
                        "high"
                        if struggle["error_count"] > 5
                        else "medium" if struggle["error_count"] > 3 else "low"
                    ),
                    "suggested_action": self._generate_recommendation(
                        struggle["title"], struggle["error_count"]
                    ),
                }
            )

        return recommendations

    def _generate_recommendation(self, topic: str, error_count: int) -> Dict:
        """Generate specific recommendations for struggling topics"""
        if "division" in topic.lower():
            return {
                "type": "visual",
                "description": "Try using visual aids like fraction circles or drawing groups",
                "activity": "Practice with real objects (cookies, toys) to demonstrate division",
                "video_suggestion": "Look up 'division with remainders' on Khan Academy",
            }
        elif "fraction" in topic.lower():
            return {
                "type": "hands-on",
                "description": "Baking is the perfect way to understand fractions",
                "activity": "Make cookies and measure ingredients using fractions",
                "video_suggestion": "Search for 'fraction basics' visual explanations",
            }
        elif "multiplication" in topic.lower():
            return {
                "type": "practice",
                "description": "Build muscle memory with consistent practice",
                "activity": "Create flashcards for times tables up to 12",
                "video_suggestion": "Fun multiplication songs and tricks",
            }
        else:
            return {
                "type": "review",
                "description": "Review the fundamentals of this topic",
                "activity": "Watch a simplified video explanation together",
                "video_suggestion": f"Search for '{topic} explained simply'",
            }

    def get_interest_based_suggestions(
        self, student_id: str, interests: List[str]
    ) -> List[Dict]:
        """Suggest lessons based on student interests"""
        conn = get_connection()
        cursor = conn.cursor()

        suggestions = []

        for interest in interests:
            # Find lessons that match the interest
            cursor.execute(
                """
                SELECT l.id, l.title, l.description, s.name as subject
                FROM lessons l
                JOIN topics t ON l.topic_id = t.id
                JOIN subjects s ON t.subject_id = s.id
                WHERE l.title LIKE ? OR l.description LIKE ?
                LIMIT 5
            """,
                (f"%{interest}%", f"%{interest}%"),
            )

            matching_lessons = [dict(row) for row in cursor.fetchall()]

            if matching_lessons:
                suggestions.append(
                    {
                        "interest": interest,
                        "suggested_lessons": matching_lessons,
                        "connection": f"These lessons connect to their interest in {interest}",
                    }
                )

        conn.close()
        return suggestions

    def create_reward_coupon(
        self, student_id: str, reward_name: str, requirement: Dict
    ) -> Dict:
        """Create a custom reward coupon"""
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO reward_coupons (student_id, reward_name, requirement, created_at, earned)
            VALUES (?, ?, ?, ?, 0)
        """,
            (student_id, reward_name, json.dumps(requirement), datetime.now()),
        )

        coupon_id = cursor.lastrowid
        conn.commit()
        conn.close()

        return {
            "coupon_id": coupon_id,
            "reward_name": reward_name,
            "requirement": requirement,
            "status": "active",
        }

    def check_and_award_coupons(self, student_id: str) -> List[Dict]:
        """Check if student has earned any reward coupons"""
        conn = get_connection()
        cursor = conn.cursor()

        # Get unearn coupons
        cursor.execute(
            """
            SELECT id, reward_name, requirement
            FROM reward_coupons
            WHERE student_id = ? AND earned = 0
        """,
            (student_id,),
        )

        coupons = [dict(row) for row in cursor.fetchall()]
        earned_coupons = []

        for coupon in coupons:
            requirement = json.loads(coupon["requirement"])

            # Check if requirement is met
            if requirement["type"] == "lessons_completed":
                cursor.execute(
                    """
                    SELECT COUNT(*) as count
                    FROM user_progress
                    WHERE user_id = ? AND completed = 1
                """,
                    (student_id,),
                )
                count = cursor.fetchone()["count"]

                if count >= requirement["value"]:
                    # Mark as earned
                    cursor.execute(
                        "UPDATE reward_coupons SET earned = 1, earned_at = ? WHERE id = ?",
                        (datetime.now(), coupon["id"]),
                    )
                    earned_coupons.append(coupon)

            elif requirement["type"] == "mastery_level":
                cursor.execute(
                    """
                    SELECT COUNT(*) as count
                    FROM user_progress
                    WHERE user_id = ? AND mastery_level = 'mastered'
                """,
                    (student_id,),
                )
                count = cursor.fetchone()["count"]

                if count >= requirement["value"]:
                    cursor.execute(
                        "UPDATE reward_coupons SET earned = 1, earned_at = ? WHERE id = ?",
                        (datetime.now(), coupon["id"]),
                    )
                    earned_coupons.append(coupon)

        conn.commit()
        conn.close()

        return earned_coupons


# Initialize parent dashboard
parent_dashboard = ParentDashboard()

