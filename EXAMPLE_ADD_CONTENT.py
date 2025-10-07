"""
Example: How to programmatically add custom content to the tutor

Run this script to add your own subjects, topics, lessons, and practice problems.
"""

from database import (
    init_database,
    add_subject,
    add_topic,
    add_lesson,
    add_practice_problem,
    get_all_subjects,
)


def add_custom_content():
    """Example of adding custom educational content."""

    # Initialize database
    init_database()

    # Option 1: Add to existing subject
    subjects = get_all_subjects()
    math_subject = next((s for s in subjects if s["name"] == "Mathematics"), None)

    if math_subject:
        # Add a new topic
        topic_id = add_topic(
            subject_id=math_subject["id"],
            name="Money & Counting Coins",
            description="Learn to count and work with money",
            display_order=11,
        )

        # Add a lesson
        lesson_id = add_lesson(
            topic_id=topic_id,
            title="Counting Pennies, Nickels, and Dimes",
            description="Learn the value of different coins and how to count them",
            steps=[
                "A penny is worth 1 cent (1¢)",
                "A nickel is worth 5 cents (5¢)",
                "A dime is worth 10 cents (10¢)",
                "To count mixed coins, start with the largest value",
                "Add up all the values to get the total",
            ],
            examples=[
                {
                    "title": "Example 1",
                    "content": "2 dimes + 3 nickels = 20¢ + 15¢ = 35¢",
                },
                {
                    "title": "Example 2",
                    "content": "1 dime + 4 pennies = 10¢ + 4¢ = 14¢",
                },
            ],
            source_type="custom",
            display_order=1,
        )

        # Add practice problems
        add_practice_problem(
            lesson_id=lesson_id,
            question="How much is 3 dimes and 2 pennies?",
            answer="32 cents",
            steps=[
                "Count the dimes: 3 × 10¢ = 30¢",
                "Count the pennies: 2 × 1¢ = 2¢",
                "Add them together: 30¢ + 2¢ = 32¢",
            ],
            hints=["Start with the bigger coins", "Remember: 1 dime = 10 cents"],
            difficulty="easy",
            display_order=1,
        )

        add_practice_problem(
            lesson_id=lesson_id,
            question="You have 2 nickels and 5 pennies. How much money do you have?",
            answer="15 cents",
            steps=[
                "Count the nickels: 2 × 5¢ = 10¢",
                "Count the pennies: 5 × 1¢ = 5¢",
                "Add them: 10¢ + 5¢ = 15¢",
            ],
            hints=["A nickel is worth 5 cents"],
            difficulty="easy",
            display_order=2,
        )

        print("✅ Custom content added successfully!")
        print(f"   - Topic: Money & Counting Coins")
        print(f"   - Lesson: Counting Pennies, Nickels, and Dimes")
        print(f"   - Practice Problems: 2")

    # Option 2: Create a completely new subject
    cooking_id = add_subject(
        name="Cooking & Life Skills",
        description="Learn practical cooking and household skills",
        icon="👨‍🍳",
        display_order=10,
    )

    cooking_topic = add_topic(
        subject_id=cooking_id,
        name="Basic Cooking Safety",
        description="Stay safe in the kitchen",
        display_order=1,
    )

    safety_lesson = add_lesson(
        topic_id=cooking_topic,
        title="Kitchen Safety Rules",
        description="Important safety rules for cooking",
        steps=[
            "Always ask an adult before using the stove or oven",
            "Wash your hands before cooking",
            "Keep pot handles turned inward",
            "Use oven mitts for hot items",
            "Never leave cooking food unattended",
            "Clean up spills immediately to prevent slips",
        ],
        examples=[
            {
                "title": "Safe Cooking",
                "content": "When making soup, keep the pot handle turned to the side so it won't get knocked over.",
            }
        ],
        source_type="custom",
        display_order=1,
    )

    print("✅ New subject created: Cooking & Life Skills")
    print("   - Topic: Basic Cooking Safety")
    print("   - Lesson: Kitchen Safety Rules")

    print("\n🎓 Run 'streamlit run tutor.py' to see your new content!")


if __name__ == "__main__":
    add_custom_content()
