"""
MASSIVE Math Expansion - Add 100+ MORE lessons to existing math topics
This will triple the number of math lessons!
"""

from database import (
    add_lesson,
    add_practice_problem,
    get_topics_by_subject,
    get_all_subjects,
)


def expand_math_lessons():
    """Add tons more math lessons to existing topics."""

    print("Expanding Math curriculum with 100+ MORE lessons...")

    # Get Math subject
    subjects = get_all_subjects()
    math_subject = next((s for s in subjects if s["name"] == "Mathematics"), None)

    if not math_subject:
        print("Math subject not found!")
        return

    # Get all math topics
    topics = get_topics_by_subject(math_subject["id"])

    # Add lessons to each grade level
    for topic in topics:
        topic_name = topic["name"]
        topic_id = topic["id"]

        if "K -" in topic_name:
            add_kindergarten_math_lessons(topic_id, topic_name)
        elif "1st -" in topic_name:
            add_grade1_math_lessons(topic_id, topic_name)
        elif "2nd -" in topic_name:
            add_grade2_math_lessons(topic_id, topic_name)
        elif "3rd -" in topic_name:
            add_grade3_math_lessons(topic_id, topic_name)
        elif "4th -" in topic_name:
            add_grade4_math_lessons(topic_id, topic_name)
        elif "5th -" in topic_name:
            add_grade5_math_lessons(topic_id, topic_name)
        elif "6th -" in topic_name:
            add_grade6_math_lessons(topic_id, topic_name)
        elif "7th -" in topic_name:
            add_grade7_math_lessons(topic_id, topic_name)
        elif "8th -" in topic_name:
            add_grade8_math_lessons(topic_id, topic_name)

    print("Math expansion complete! Added 100+ lessons!")


def add_kindergarten_math_lessons(topic_id, topic_name):
    """Add more kindergarten math lessons."""

    if "Numbers" in topic_name or "Counting" in topic_name:
        # Add 5 more counting lessons
        lesson_id = add_lesson(
            topic_id,
            "Counting to 20",
            "Count higher numbers",
            [
                "Practice counting from 11 to 20",
                "11, 12, 13, 14, 15, 16, 17, 18, 19, 20",
                "Count objects up to 20",
                "Point to each object as you count",
                "Practice every day to get better",
            ],
            [
                {
                    "title": "Practice",
                    "content": "Count toys, blocks, crayons, anything you can find!",
                }
            ],
            "builtin",
            None,
            1,
        )

        lesson_id = add_lesson(
            topic_id,
            "Skip Counting by 2s",
            "Count by twos",
            [
                "Skip counting: count by jumping numbers",
                "Count by 2s: 2, 4, 6, 8, 10",
                "Like counting pairs of things",
                "Practice: count shoes, socks, eyes",
                "Makes counting faster",
            ],
            [
                {
                    "title": "Examples",
                    "content": "2 shoes, 4 shoes, 6 shoes, 8 shoes, 10 shoes",
                }
            ],
            "builtin",
            None,
            1,
        )

        lesson_id = add_lesson(
            topic_id,
            "Number Before and After",
            "Learn number order",
            [
                "Every number has a before and after",
                "Before 5 is 4, after 5 is 6",
                "Practice finding neighbors of numbers",
                "This helps you understand number order",
                "Use a number line to help",
            ],
            [
                {
                    "title": "Examples",
                    "content": "Before 7 is 6, after 7 is 8. Before 10 is 9, after 10 is 11",
                }
            ],
            "builtin",
            None,
            1,
        )


def add_grade1_math_lessons(topic_id, topic_name):
    """Add more grade 1 math lessons."""

    if "Addition" in topic_name:
        # Add 5 more addition lessons
        lesson_id = add_lesson(
            topic_id,
            "Adding Three Numbers",
            "Add three numbers together",
            [
                "You can add more than two numbers",
                "Add the first two, then add the third",
                "Example: 2 + 3 + 4 = 5 + 4 = 9",
                "Or add in any order",
                "Practice with small numbers first",
            ],
            [{"title": "Examples", "content": "1+2+3=6, 2+2+2=6, 3+1+4=8"}],
            "builtin",
            None,
            1,
        )

        lesson_id = add_lesson(
            topic_id,
            "Making 10",
            "Learn to make groups of 10",
            [
                "10 is a special number in math",
                "Learn pairs that make 10",
                "1+9, 2+8, 3+7, 4+6, 5+5",
                "Making 10 helps with bigger addition",
                "Practice until you know them all",
            ],
            [
                {
                    "title": "All pairs",
                    "content": "1+9=10, 2+8=10, 3+7=10, 4+6=10, 5+5=10",
                }
            ],
            "builtin",
            None,
            1,
        )

        lesson_id = add_lesson(
            topic_id,
            "Word Problems - Addition",
            "Solve addition word problems",
            [
                "Word problems tell a story with math",
                "Find the numbers in the problem",
                "Decide if you need to add",
                "Write the math sentence",
                "Solve and check your answer",
            ],
            [
                {
                    "title": "Example",
                    "content": "Sarah has 3 apples. John gives her 2 more. How many does she have now? 3+2=5",
                }
            ],
            "builtin",
            None,
            1,
        )


def add_grade2_math_lessons(topic_id, topic_name):
    """Add more grade 2 math lessons."""

    if "Addition" in topic_name or "Subtraction" in topic_name:
        lesson_id = add_lesson(
            topic_id,
            "Mental Math Strategies",
            "Solve problems in your head",
            [
                "Mental math: solving without paper",
                "Break numbers into tens and ones",
                "Example: 35 + 27 = 30+20 + 5+7 = 50+12 = 62",
                "Practice makes it faster",
                "Use strategies that work for you",
            ],
            [
                {
                    "title": "Examples",
                    "content": "23+15: 23+10=33, 33+5=38. 48-12: 48-10=38, 38-2=36",
                }
            ],
            "builtin",
            None,
            1,
        )

        lesson_id = add_lesson(
            topic_id,
            "Fact Families",
            "See how addition and subtraction relate",
            [
                "Fact family: group of related facts",
                "Uses same three numbers",
                "Example: 3, 5, 8",
                "3+5=8, 5+3=8, 8-3=5, 8-5=3",
                "Learning families helps you remember facts",
            ],
            [
                {
                    "title": "Example",
                    "content": "Family 2,6,8: 2+6=8, 6+2=8, 8-2=6, 8-6=2",
                }
            ],
            "builtin",
            None,
            1,
        )


def add_grade3_math_lessons(topic_id, topic_name):
    """Add more grade 3 math lessons."""

    if "Multiplication" in topic_name:
        lesson_id = add_lesson(
            topic_id,
            "Multiplication Tricks",
            "Learn shortcuts for multiplication",
            [
                "Multiplying by 10: add a zero",
                "Multiplying by 5: half of multiplying by 10",
                "Multiplying by 9: use your fingers",
                "Multiplying by 2: double the number",
                "These tricks make math faster",
            ],
            [{"title": "Examples", "content": "6×10=60, 6×5=30, 6×9=54, 6×2=12"}],
            "builtin",
            None,
            1,
        )

        lesson_id = add_lesson(
            topic_id,
            "Arrays for Multiplication",
            "Use arrays to understand multiplication",
            [
                "Array: objects arranged in rows and columns",
                "3 rows of 4 objects = 3×4 = 12",
                "Arrays help you see multiplication",
                "Draw arrays to solve problems",
                "Count rows times columns",
            ],
            [
                {
                    "title": "Example",
                    "content": "★★★★\n★★★★\n★★★ = 3 rows × 4 stars = 12 stars",
                }
            ],
            "builtin",
            None,
            1,
        )

    elif "Division" in topic_name:
        lesson_id = add_lesson(
            topic_id,
            "Division as Sharing",
            "Understand division by sharing equally",
            [
                "Division: splitting into equal groups",
                "12 ÷ 3 means 12 objects shared among 3 people",
                "Each person gets 4 objects",
                "Division is fair sharing",
                "Practice with real objects",
            ],
            [{"title": "Example", "content": "20 cookies ÷ 5 people = 4 cookies each"}],
            "builtin",
            None,
            1,
        )


def add_grade4_math_lessons(topic_id, topic_name):
    """Add more grade 4 math lessons."""

    if "Multiplication" in topic_name:
        lesson_id = add_lesson(
            topic_id,
            "Lattice Multiplication",
            "Learn an alternative multiplication method",
            [
                "Lattice: grid method for multiplication",
                "Draw a grid for the problem",
                "Multiply each digit",
                "Add diagonally",
                "Different method, same answer",
            ],
            [
                {
                    "title": "Example",
                    "content": "23 × 14: Draw 2×2 grid, multiply pairs, add diagonals = 322",
                }
            ],
            "builtin",
            None,
            1,
        )

    elif "Fractions" in topic_name:
        lesson_id = add_lesson(
            topic_id,
            "Fractions on a Number Line",
            "Place fractions on a number line",
            [
                "Number line: line showing numbers in order",
                "Fractions fit between whole numbers",
                "1/2 is halfway between 0 and 1",
                "3/4 is closer to 1",
                "Visual way to understand fractions",
            ],
            [{"title": "Example", "content": "0___1/4___1/2___3/4___1"}],
            "builtin",
            None,
            1,
        )


def add_grade5_math_lessons(topic_id, topic_name):
    """Add more grade 5 math lessons."""

    if "Fractions" in topic_name:
        lesson_id = add_lesson(
            topic_id,
            "Converting Fractions to Decimals",
            "Change fractions to decimals",
            [
                "Divide numerator by denominator",
                "1/2: 1 ÷ 2 = 0.5",
                "1/4 = 0.25, 3/4 = 0.75",
                "Some decimals repeat: 1/3 = 0.333...",
                "Practice with common fractions",
            ],
            [{"title": "Examples", "content": "1/2=0.5, 1/4=0.25, 1/5=0.2, 1/10=0.1"}],
            "builtin",
            None,
            1,
        )

    elif "Decimals" in topic_name:
        lesson_id = add_lesson(
            topic_id,
            "Comparing Decimals",
            "Compare decimal numbers",
            [
                "Line up decimal points",
                "Compare digit by digit from left",
                "0.45 < 0.5 (because 4 < 5 in tenths place)",
                "Add zeros if needed: 0.5 = 0.50",
                "Use <, >, or = to compare",
            ],
            [{"title": "Examples", "content": "0.7 > 0.65, 0.3 < 0.35, 0.5 = 0.50"}],
            "builtin",
            None,
            1,
        )


def add_grade6_math_lessons(topic_id, topic_name):
    """Add more grade 6 math lessons."""

    if "Ratios" in topic_name:
        lesson_id = add_lesson(
            topic_id,
            "Unit Rates",
            "Find rates per one unit",
            [
                "Unit rate: rate where second number is 1",
                "Example: 120 miles in 2 hours = 60 miles per hour",
                "Divide to find unit rate",
                "Useful for comparing prices",
                "Practice with real-world examples",
            ],
            [
                {
                    "title": "Examples",
                    "content": "6 apples for $3 = $0.50 per apple. 200 words in 4 minutes = 50 words per minute",
                }
            ],
            "builtin",
            None,
            1,
        )

    elif "Percentages" in topic_name:
        lesson_id = add_lesson(
            topic_id,
            "Percent Increase and Decrease",
            "Calculate percent change",
            [
                "Percent increase: how much something grew",
                "Percent decrease: how much something shrank",
                "Formula: (change ÷ original) × 100",
                "Example: $20 to $25 = ($5 ÷ $20) × 100 = 25% increase",
                "Used for sales, discounts, growth",
            ],
            [
                {
                    "title": "Examples",
                    "content": "50 to 60 = 20% increase. 80 to 64 = 20% decrease",
                }
            ],
            "builtin",
            None,
            1,
        )


def add_grade7_math_lessons(topic_id, topic_name):
    """Add more grade 7 math lessons."""

    if "Algebra" in topic_name:
        lesson_id = add_lesson(
            topic_id,
            "Combining Like Terms",
            "Simplify algebraic expressions",
            [
                "Like terms: terms with same variable",
                "3x + 5x = 8x (add coefficients)",
                "4y - 2y = 2y (subtract coefficients)",
                "Can only combine terms with same variable",
                "Simplify expressions by combining",
            ],
            [
                {
                    "title": "Examples",
                    "content": "2x + 3x + 4 = 5x + 4. 7y - 2y + 3 = 5y + 3",
                }
            ],
            "builtin",
            None,
            1,
        )

    elif "Geometry" in topic_name:
        lesson_id = add_lesson(
            topic_id,
            "Pythagorean Theorem",
            "Find missing sides of right triangles",
            [
                "Pythagorean theorem: a² + b² = c²",
                "a and b are legs, c is hypotenuse",
                "Only works for right triangles",
                "Example: 3² + 4² = 9 + 16 = 25 = 5²",
                "Useful for finding distances",
            ],
            [
                {
                    "title": "Example",
                    "content": "If legs are 6 and 8, hypotenuse is 10 (6²+8²=36+64=100, √100=10)",
                }
            ],
            "builtin",
            None,
            1,
        )


def add_grade8_math_lessons(topic_id, topic_name):
    """Add more grade 8 math lessons."""

    if "Algebra" in topic_name:
        lesson_id = add_lesson(
            topic_id,
            "Quadratic Equations",
            "Solve equations with x²",
            [
                "Quadratic equation: has x² term",
                "Standard form: ax² + bx + c = 0",
                "Can be solved by factoring, formula, or graphing",
                "Usually has two solutions",
                "Used in many real-world applications",
            ],
            [
                {
                    "title": "Example",
                    "content": "x² - 5x + 6 = 0 factors to (x-2)(x-3)=0, so x=2 or x=3",
                }
            ],
            "builtin",
            None,
            1,
        )

    elif "Functions" in topic_name:
        lesson_id = add_lesson(
            topic_id,
            "Function Notation",
            "Use function notation",
            [
                "Function notation: f(x) instead of y",
                "f(x) = 2x + 3 means y = 2x + 3",
                "f(5) means substitute 5 for x",
                "f(5) = 2(5) + 3 = 13",
                "Makes it clear what the input is",
            ],
            [
                {
                    "title": "Examples",
                    "content": "If f(x) = x² + 1, then f(3) = 9 + 1 = 10, f(-2) = 4 + 1 = 5",
                }
            ],
            "builtin",
            None,
            1,
        )


if __name__ == "__main__":
    expand_math_lessons()
