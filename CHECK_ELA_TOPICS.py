"""
Script to check what ELA topics are in the database
"""

import sqlite3


def check_ela_topics():
    """Check what ELA topics are currently in the database."""

    conn = sqlite3.connect("tutor_app.db")
    cursor = conn.cursor()

    # Get ELA subject
    cursor.execute("SELECT id, name FROM subjects WHERE name = 'English Language Arts'")
    ela_subject = cursor.fetchone()

    if ela_subject:
        print(f"Found ELA subject: {ela_subject[1]} (ID: {ela_subject[0]})")

        # Get all topics for ELA
        cursor.execute(
            "SELECT id, name, description FROM topics WHERE subject_id = ? ORDER BY display_order",
            (ela_subject[0],),
        )
        topics = cursor.fetchall()

        print(f"\nFound {len(topics)} ELA topics:")
        for topic in topics:
            print(f"  - {topic[1]}: {topic[2]}")

        # Get lesson count for each topic
        print(f"\nLesson counts:")
        for topic in topics:
            cursor.execute(
                "SELECT COUNT(*) FROM lessons WHERE topic_id = ?", (topic[0],)
            )
            lesson_count = cursor.fetchone()[0]
            print(f"  - {topic[1]}: {lesson_count} lessons")
    else:
        print("No ELA subject found in database")

    conn.close()


if __name__ == "__main__":
    check_ela_topics()
