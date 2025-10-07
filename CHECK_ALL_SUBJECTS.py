"""
Script to check all subjects and their topic counts in the database
"""

import sqlite3


def check_all_subjects():
    """Check all subjects and their topics in the database."""

    conn = sqlite3.connect("tutor_app.db")
    cursor = conn.cursor()

    # Get all subjects
    cursor.execute(
        "SELECT id, name, description, icon FROM subjects ORDER BY display_order"
    )
    subjects = cursor.fetchall()

    print("=" * 60)
    print("MASSIVE CURRICULUM DATABASE - COMPLETE SUMMARY")
    print("=" * 60)

    total_topics = 0
    total_lessons = 0

    for subject in subjects:
        subject_id, name, description, icon = subject

        # Get topic count
        cursor.execute(
            "SELECT COUNT(*) FROM topics WHERE subject_id = ?", (subject_id,)
        )
        topic_count = cursor.fetchone()[0]

        # Get lesson count
        cursor.execute(
            """
            SELECT COUNT(*) FROM lessons 
            WHERE topic_id IN (SELECT id FROM topics WHERE subject_id = ?)
        """,
            (subject_id,),
        )
        lesson_count = cursor.fetchone()[0]

        total_topics += topic_count
        total_lessons += lesson_count

        print(f"\n{name}")
        print(f"   {description}")
        print(f"   Topics: {topic_count} | Lessons: {lesson_count}")

    print("\n" + "=" * 60)
    print(
        f"TOTAL: {len(subjects)} SUBJECTS | {total_topics} TOPICS | {total_lessons} LESSONS"
    )
    print("=" * 60)

    conn.close()


if __name__ == "__main__":
    check_all_subjects()
