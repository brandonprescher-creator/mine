"""
Comprehensive K-8 curriculum data including all subjects and the detailed Division Mastery module.
"""

from database import (
    add_subject,
    add_topic,
    add_lesson,
    add_practice_problem,
    get_all_subjects,
    get_topics_by_subject,
)


def seed_curriculum():
    """Seed the database with comprehensive K-8 curriculum."""

    # Check if already seeded
    existing_subjects = get_all_subjects()
    if existing_subjects:
        print("Curriculum already seeded.")
        return

    print("Seeding curriculum...")

    # Create all subjects
    math_id = add_subject(
        "Mathematics", "Numbers, operations, algebra, geometry, and more", "🔢", 1
    )
    ela_id = add_subject(
        "English Language Arts", "Reading, writing, grammar, and vocabulary", "📚", 2
    )
    science_id = add_subject(
        "Science", "Biology, chemistry, physics, and earth science", "🔬", 3
    )
    social_studies_id = add_subject(
        "Social Studies", "History, geography, civics, and economics", "🌍", 4
    )
    arts_id = add_subject(
        "Arts", "Visual arts, music, and creative expression", "🎨", 5
    )
    languages_id = add_subject(
        "World Languages", "Spanish, French, Chinese, and ESL support", "🌐", 6
    )
    tech_id = add_subject(
        "Technology & STEAM", "Coding, media literacy, and problem-solving", "💻", 7
    )
    pe_health_id = add_subject(
        "PE & Health", "Physical education, fitness, and wellness", "⚽", 8
    )
    life_skills_id = add_subject(
        "Life & Study Skills", "Study skills, test prep, and special education", "📝", 9
    )

    # MATHEMATICS CURRICULUM
    seed_mathematics(math_id)

    # ENGLISH LANGUAGE ARTS - MASSIVE CURRICULUM
    from MASSIVE_ELA_CURRICULUM import seed_massive_ela_curriculum

    seed_massive_ela_curriculum()

    # SCIENCE
    seed_science(science_id)

    # SOCIAL STUDIES
    seed_social_studies(social_studies_id)

    # ARTS
    seed_arts(arts_id)

    # WORLD LANGUAGES
    seed_languages(languages_id)

    # TECHNOLOGY & STEAM
    seed_technology(tech_id)

    # PE & HEALTH
    seed_pe_health(pe_health_id)

    # LIFE & STUDY SKILLS
    seed_life_skills(life_skills_id)

    print("Curriculum seeding complete!")


def seed_mathematics(subject_id):
    """Seed mathematics curriculum including Division Mastery."""

    # Elementary Math Topics
    addition_topic = add_topic(subject_id, "Addition", "Learning to add numbers", 1)
    subtraction_topic = add_topic(
        subject_id, "Subtraction", "Learning to subtract numbers", 2
    )
    multiplication_topic = add_topic(
        subject_id, "Multiplication", "Learning to multiply numbers", 3
    )
    division_topic = add_topic(
        subject_id, "Division Mastery", "Master division with 10 different methods", 4
    )
    fractions_topic = add_topic(
        subject_id, "Fractions", "Understanding parts of a whole", 5
    )
    decimals_topic = add_topic(
        subject_id, "Decimals", "Working with decimal numbers", 6
    )
    measurement_topic = add_topic(
        subject_id, "Measurement", "Length, weight, volume, and time", 7
    )
    geometry_topic = add_topic(
        subject_id, "Geometry", "Shapes, angles, and spatial reasoning", 8
    )
    algebra_topic = add_topic(
        subject_id, "Pre-Algebra & Algebra", "Variables, equations, and expressions", 9
    )
    statistics_topic = add_topic(
        subject_id, "Data & Statistics", "Graphs, probability, and analysis", 10
    )

    # DIVISION MASTERY - 10 Methods
    seed_division_mastery(division_topic)

    # Quick lessons for other topics
    seed_basic_math_topics(
        addition_topic,
        subtraction_topic,
        multiplication_topic,
        fractions_topic,
        decimals_topic,
        measurement_topic,
        geometry_topic,
        algebra_topic,
        statistics_topic,
    )


def seed_division_mastery(division_topic_id):
    """Seed the complete Division Mastery module with 10 methods."""

    # Method 1: Long Division
    lesson1_id = add_lesson(
        division_topic_id,
        "Long Division Method",
        "The traditional long division algorithm - a systematic way to divide large numbers.",
        [
            "Set up the problem: Write the dividend (number being divided) inside the division bracket and the divisor (number dividing by) outside.",
            "Divide: Look at the first digit(s) of the dividend. How many times does the divisor go into it?",
            "Multiply: Multiply the divisor by your answer and write it below.",
            "Subtract: Subtract to find the difference.",
            "Bring down: Bring down the next digit from the dividend.",
            "Repeat: Continue the process until all digits are used.",
            "Write the remainder: If there's a number left over, that's your remainder.",
        ],
        [
            {
                "title": "Example: 156 ÷ 12",
                "content": "12 goes into 15 once (1). Write 1 above. 1×12=12. Subtract: 15-12=3. Bring down 6 to make 36. 12 goes into 36 three times (3). Write 3 above. 3×12=36. Subtract: 36-36=0. Answer: 13",
            }
        ],
        "builtin",
        None,
        1,
    )

    # Practice problems for Long Division
    add_practice_problem(
        lesson1_id,
        "144 ÷ 12 = ?",
        "12",
        [
            "Set up: 12)144",
            "12 into 14 goes 1 time",
            "1 × 12 = 12",
            "14 - 12 = 2",
            "Bring down 4 to make 24",
            "12 into 24 goes 2 times",
            "Answer: 12",
        ],
        [
            "Start with how many times 12 goes into 14",
            "Don't forget to bring down digits",
        ],
        "medium",
        1,
    )

    add_practice_problem(
        lesson1_id,
        "276 ÷ 23 = ?",
        "12",
        [
            "Set up: 23)276",
            "23 into 27 goes 1 time",
            "1 × 23 = 23",
            "27 - 23 = 4",
            "Bring down 6 to make 46",
            "23 into 46 goes 2 times",
            "Answer: 12",
        ],
        ["Work through one digit at a time", "Check your multiplication"],
        "medium",
        2,
    )

    add_practice_problem(
        lesson1_id,
        "3465 ÷ 15 = ?",
        "231",
        [
            "15 into 34 goes 2 times",
            "Subtract 30, bring down 6 = 46",
            "15 into 46 goes 3 times",
            "Subtract 45, bring down 5 = 15",
            "15 into 15 goes 1 time exactly",
            "Answer: 231",
        ],
        ["Take your time with each step", "This is a 4-digit number"],
        "hard",
        3,
    )

    add_practice_problem(
        lesson1_id,
        "1827 ÷ 21 = ?",
        "87",
        [
            "21 into 18 goes 0 times",
            "21 into 182 goes 8 times (8×21=168)",
            "182-168=14, bring down 7 = 147",
            "21 into 147 goes 7 times (7×21=147)",
            "Answer: 87",
        ],
        ["Sometimes the divisor doesn't go into the first digits", "Use estimation"],
        "medium",
        4,
    )

    # Method 2: Partial Quotients
    lesson2_id = add_lesson(
        division_topic_id,
        "Partial Quotients Method",
        "Divide by subtracting easy multiples until you reach zero or can't subtract anymore.",
        [
            "Write the division problem.",
            "Think of an easy multiple of the divisor that you can subtract (like 10×, 5×, or 2×).",
            "Subtract that multiple from the dividend and keep track of how many times you subtracted.",
            "Repeat with the remainder - subtract another easy multiple.",
            "Keep going until you can't subtract anymore.",
            "Add up all the partial quotients to get your answer.",
            "Any number left is the remainder.",
        ],
        [
            {
                "title": "Example: 156 ÷ 12",
                "content": "Subtract 10×12=120. That's 10. Now 156-120=36. Subtract 3×12=36. That's 3. Now 36-36=0. Add the partial quotients: 10+3=13. Answer: 13",
            }
        ],
        "builtin",
        None,
        2,
    )

    add_practice_problem(
        lesson2_id,
        "144 ÷ 12 = ?",
        "12",
        [
            "Subtract 10 × 12 = 120 (quotient: 10)",
            "144 - 120 = 24",
            "Subtract 2 × 12 = 24 (quotient: 2)",
            "24 - 24 = 0",
            "Add partial quotients: 10 + 2 = 12",
        ],
        ["Start with 10× whenever possible", "Keep subtracting until you reach 0"],
        "easy",
        1,
    )

    add_practice_problem(
        lesson2_id,
        "276 ÷ 23 = ?",
        "12",
        [
            "Subtract 10 × 23 = 230 (quotient: 10)",
            "276 - 230 = 46",
            "Subtract 2 × 23 = 46 (quotient: 2)",
            "46 - 46 = 0",
            "Add: 10 + 2 = 12",
        ],
        ["Use friendly multiples", "Keep track of each quotient"],
        "medium",
        2,
    )

    add_practice_problem(
        lesson2_id,
        "3465 ÷ 15 = ?",
        "231",
        [
            "Subtract 200 × 15 = 3000 (quotient: 200)",
            "465 left",
            "Subtract 30 × 15 = 450 (quotient: 30)",
            "15 left",
            "Subtract 1 × 15 = 15 (quotient: 1)",
            "Add: 200 + 30 + 1 = 231",
        ],
        ["Use multiples of 100, 10, and 1", "Big jumps first, then smaller"],
        "hard",
        3,
    )

    add_practice_problem(
        lesson2_id,
        "1827 ÷ 21 = ?",
        "87",
        [
            "Subtract 80 × 21 = 1680 (quotient: 80)",
            "147 left",
            "Subtract 7 × 21 = 147 (quotient: 7)",
            "0 left",
            "Add: 80 + 7 = 87",
        ],
        ["Try multiples of 10 first", "Then adjust"],
        "medium",
        4,
    )

    # Method 3: Distributive Property
    lesson3_id = add_lesson(
        division_topic_id,
        "Distributive Property Method",
        "Break the dividend into parts that are easier to divide, then add the results.",
        [
            "Look at the dividend (the number being divided).",
            "Break it into two or more parts that are easy to divide by the divisor.",
            "Divide each part separately by the divisor.",
            "Add up the quotients from each part.",
            "That sum is your answer!",
        ],
        [
            {
                "title": "Example: 144 ÷ 12",
                "content": "Break 144 into 120 + 24. Divide each: 120 ÷ 12 = 10, and 24 ÷ 12 = 2. Add them: 10 + 2 = 12. Answer: 12",
            }
        ],
        "builtin",
        None,
        3,
    )

    add_practice_problem(
        lesson3_id,
        "156 ÷ 12 = ?",
        "13",
        ["Break 156 into 120 + 36", "120 ÷ 12 = 10", "36 ÷ 12 = 3", "10 + 3 = 13"],
        ["Choose multiples that divide evenly", "Break into 2 or 3 parts"],
        "medium",
        1,
    )

    add_practice_problem(
        lesson3_id,
        "276 ÷ 23 = ?",
        "12",
        ["Break 276 into 230 + 46", "230 ÷ 23 = 10", "46 ÷ 23 = 2", "10 + 2 = 12"],
        ["Look for multiples of 10", "Keep it simple"],
        "medium",
        2,
    )

    add_practice_problem(
        lesson3_id,
        "3465 ÷ 15 = ?",
        "231",
        [
            "Break into 3000 + 450 + 15",
            "3000 ÷ 15 = 200",
            "450 ÷ 15 = 30",
            "15 ÷ 15 = 1",
            "200 + 30 + 1 = 231",
        ],
        ["Use multiples of 10 or 100", "Break into manageable pieces"],
        "hard",
        3,
    )

    add_practice_problem(
        lesson3_id,
        "1827 ÷ 21 = ?",
        "87",
        ["Break into 1680 + 147", "1680 ÷ 21 = 80", "147 ÷ 21 = 7", "80 + 7 = 87"],
        ["Find the largest easy multiple first", "Then handle the remainder"],
        "medium",
        4,
    )

    # Method 4: Repeated Subtraction
    lesson4_id = add_lesson(
        division_topic_id,
        "Repeated Subtraction Method",
        "Keep subtracting the divisor from the dividend until you reach zero, counting how many times you subtract.",
        [
            "Write down your dividend (the number being divided).",
            "Subtract the divisor from it.",
            "Keep a tally or count each time you subtract.",
            "Keep subtracting until you reach zero or can't subtract anymore.",
            "The number of times you subtracted is the quotient.",
            "Any number left over is the remainder.",
        ],
        [
            {
                "title": "Example: 36 ÷ 4",
                "content": "36 - 4 = 32 (1), 32 - 4 = 28 (2), 28 - 4 = 24 (3), 24 - 4 = 20 (4), 20 - 4 = 16 (5), 16 - 4 = 12 (6), 12 - 4 = 8 (7), 8 - 4 = 4 (8), 4 - 4 = 0 (9). Answer: 9",
            }
        ],
        "builtin",
        None,
        4,
    )

    add_practice_problem(
        lesson4_id,
        "48 ÷ 4 = ?",
        "12",
        [
            "Start: 48",
            "Subtract 4 repeatedly",
            "Count each subtraction",
            "48-4=44, 44-4=40, 40-4=36, 36-4=32, 32-4=28, 28-4=24",
            "24-4=20, 20-4=16, 16-4=12, 12-4=8, 8-4=4, 4-4=0",
            "Total subtractions: 12",
        ],
        ["Use tally marks to count", "This method works best with smaller numbers"],
        "easy",
        1,
    )

    add_practice_problem(
        lesson4_id,
        "65 ÷ 5 = ?",
        "13",
        [
            "Subtract 5 from 65 repeatedly",
            "Keep careful count",
            "After 13 subtractions you reach 0",
            "Answer: 13",
        ],
        ["Stay organized with your counting", "Check your work"],
        "medium",
        2,
    )

    add_practice_problem(
        lesson4_id,
        "91 ÷ 7 = ?",
        "13",
        [
            "Subtract 7 from 91 repeatedly",
            "Count: 91, 84, 77, 70, 63, 56, 49, 42, 35, 28, 21, 14, 7, 0",
            "Total: 13 times",
            "Answer: 13",
        ],
        ["This takes patience!", "Consider using partial quotients for large numbers"],
        "medium",
        3,
    )

    add_practice_problem(
        lesson4_id,
        "78 ÷ 6 = ?",
        "13",
        [
            "Subtract 6 from 78 repeatedly",
            "78-6=72, 72-6=66... continue",
            "After 13 subtractions: 0",
            "Answer: 13",
        ],
        ["Keep track carefully", "You can also subtract in groups"],
        "medium",
        4,
    )

    # Method 5: Equal Groups
    lesson5_id = add_lesson(
        division_topic_id,
        "Equal Groups Method",
        "Think of division as sharing items into equal groups. Visual and hands-on!",
        [
            "Understand the problem: You have a total number of items (dividend).",
            "Decide: Are you making a certain number of groups, or putting a certain number in each group?",
            "Draw circles to represent groups.",
            "Distribute the items one by one (or in chunks) into each group equally.",
            "Count how many are in each group (if you knew the number of groups) OR count how many groups you made (if you knew how many per group).",
            "That's your answer!",
        ],
        [
            {
                "title": "Example: 24 ÷ 6",
                "content": "Think: 24 items into groups of 6. Draw circles and put 6 items in each. Circle 1: 6 items, Circle 2: 6 items, Circle 3: 6 items, Circle 4: 6 items. You made 4 groups. Answer: 4",
            }
        ],
        "builtin",
        None,
        5,
    )

    add_practice_problem(
        lesson5_id,
        "20 ÷ 5 = ?",
        "4",
        [
            "Draw circles for groups",
            "Put 5 items in each group",
            "Group 1: ●●●●●",
            "Group 2: ●●●●●",
            "Group 3: ●●●●●",
            "Group 4: ●●●●●",
            "Total groups: 4",
        ],
        ["Use drawings or physical objects", "Share equally"],
        "easy",
        1,
    )

    add_practice_problem(
        lesson5_id,
        "36 ÷ 4 = ?",
        "9",
        [
            "Make 4 equal groups",
            "Distribute 36 items equally",
            "Each group gets 9 items",
            "Answer: 9",
        ],
        ["You can draw this out", "Or use counters"],
        "medium",
        2,
    )

    add_practice_problem(
        lesson5_id,
        "56 ÷ 8 = ?",
        "7",
        ["Create 8 equal groups", "Share 56 items", "Each group: 7 items", "Answer: 7"],
        ["Start with small amounts in each group", "Build up equally"],
        "medium",
        3,
    )

    add_practice_problem(
        lesson5_id,
        "72 ÷ 9 = ?",
        "8",
        [
            "Make groups of 9",
            "How many complete groups from 72?",
            "8 groups of 9",
            "Answer: 8",
        ],
        ["Count by 9s", "Use multiplication facts"],
        "medium",
        4,
    )

    # Method 6: Array / Area Model
    lesson6_id = add_lesson(
        division_topic_id,
        "Array / Area Model Method",
        "Use a rectangle (area model) to visualize division. Great for larger numbers!",
        [
            "Draw a rectangle to represent the dividend (total area).",
            "One side of the rectangle is the divisor (known dimension).",
            "Your job: find the other dimension (the quotient).",
            "Break the rectangle into easier chunks if needed (like 10s and 1s).",
            "Label each section with its area.",
            "Add up the dimensions to get the total quotient.",
        ],
        [
            {
                "title": "Example: 156 ÷ 12",
                "content": "Draw a rectangle with one side = 12. Break 156 into 120 + 36. First section: 120 ÷ 12 = 10 wide. Second section: 36 ÷ 12 = 3 wide. Total width: 10 + 3 = 13. Answer: 13",
            }
        ],
        "builtin",
        None,
        6,
    )

    add_practice_problem(
        lesson6_id,
        "144 ÷ 12 = ?",
        "12",
        [
            "Draw rectangle with height 12",
            "Break 144 into 120 + 24",
            "120 ÷ 12 = 10",
            "24 ÷ 12 = 2",
            "Total width: 10 + 2 = 12",
        ],
        ["Use graph paper if helpful", "Break into multiples of 10"],
        "medium",
        1,
    )

    add_practice_problem(
        lesson6_id,
        "276 ÷ 23 = ?",
        "12",
        [
            "Rectangle height: 23",
            "Break 276 into 230 + 46",
            "230 ÷ 23 = 10",
            "46 ÷ 23 = 2",
            "Width: 10 + 2 = 12",
        ],
        ["Visualize the area", "Break into friendly numbers"],
        "medium",
        2,
    )

    add_practice_problem(
        lesson6_id,
        "3465 ÷ 15 = ?",
        "231",
        [
            "Height: 15",
            "Break into 3000 + 450 + 15",
            "3000 ÷ 15 = 200",
            "450 ÷ 15 = 30",
            "15 ÷ 15 = 1",
            "Width: 200 + 30 + 1 = 231",
        ],
        ["Use place value sections", "Calculate each section's dimension"],
        "hard",
        3,
    )

    add_practice_problem(
        lesson6_id,
        "1827 ÷ 21 = ?",
        "87",
        [
            "Height: 21",
            "Break into 1680 + 147",
            "1680 ÷ 21 = 80",
            "147 ÷ 21 = 7",
            "Width: 80 + 7 = 87",
        ],
        ["Think about what times 21 is close to 1827", "Use area sections"],
        "hard",
        4,
    )

    # Method 7: Number Line Jumps
    lesson7_id = add_lesson(
        division_topic_id,
        "Number Line Jumps Method",
        "Jump along a number line by the divisor amount until you reach the dividend. Count your jumps!",
        [
            "Draw a number line starting at 0.",
            "Mark your dividend (the total) at the end.",
            "Make jumps of the divisor size.",
            "Count how many jumps it takes to reach the dividend.",
            "The number of jumps is your quotient!",
            "If you land before the dividend, the distance left is the remainder.",
        ],
        [
            {
                "title": "Example: 36 ÷ 9",
                "content": "Start at 0. Jump by 9s: 0 → 9 (jump 1), 9 → 18 (jump 2), 18 → 27 (jump 3), 27 → 36 (jump 4). Total: 4 jumps. Answer: 4",
            }
        ],
        "builtin",
        None,
        7,
    )

    add_practice_problem(
        lesson7_id,
        "48 ÷ 8 = ?",
        "6",
        ["Start at 0, jump by 8s", "0→8→16→24→32→40→48", "Count jumps: 6", "Answer: 6"],
        ["Draw the number line", "Mark each jump clearly"],
        "easy",
        1,
    )

    add_practice_problem(
        lesson7_id,
        "144 ÷ 12 = ?",
        "12",
        [
            "Jump by 12s from 0 to 144",
            "0→12→24→36→48→60→72→84→96→108→120→132→144",
            "Total jumps: 12",
            "Answer: 12",
        ],
        ["You can make bigger jumps (like 10×12) then smaller ones", "Count carefully"],
        "medium",
        2,
    )

    add_practice_problem(
        lesson7_id,
        "95 ÷ 10 = ?",
        "9 remainder 5",
        [
            "Jump by 10s",
            "0→10→20→30→40→50→60→70→80→90",
            "Stop at 90 (9 jumps)",
            "Distance to 95 is 5",
            "Answer: 9 R5",
        ],
        ["The remainder is the distance left", "Count complete jumps only"],
        "medium",
        3,
    )

    add_practice_problem(
        lesson7_id,
        "156 ÷ 12 = ?",
        "13",
        [
            "Jump by 12s to reach 156",
            "Make 10 jumps of 12 = 120",
            "Then 3 more jumps: 132, 144, 156",
            "Total: 13 jumps",
        ],
        ["Use big jumps first", "Then count remaining jumps"],
        "medium",
        4,
    )

    # Method 8: Ratio Table
    lesson8_id = add_lesson(
        division_topic_id,
        "Ratio Table Method",
        "Build a table showing multiples of the divisor until you reach the dividend.",
        [
            "Create a two-row table.",
            "Top row: multiples of 1 (1, 2, 3, 10, etc.).",
            "Bottom row: those multiples times the divisor.",
            "Build the table with easy numbers (×1, ×2, ×5, ×10) until you get close to the dividend.",
            "Find which multiple equals or gets closest to your dividend.",
            "That multiple is your quotient!",
        ],
        [
            {
                "title": "Example: 144 ÷ 12",
                "content": "Table: 1→12, 2→24, 10→120, 12→144. We see 12 × 12 = 144. Answer: 12",
            }
        ],
        "builtin",
        None,
        8,
    )

    add_practice_problem(
        lesson8_id,
        "156 ÷ 12 = ?",
        "13",
        [
            "Build ratio table for ×12",
            "1→12, 10→120, 13→156",
            "Find 156 in bottom row",
            "Top row shows: 13",
        ],
        ["Use multiples of 10 to get close", "Then adjust"],
        "medium",
        1,
    )

    add_practice_problem(
        lesson8_id,
        "276 ÷ 23 = ?",
        "12",
        [
            "Ratio table for ×23",
            "1→23, 10→230, 12→276",
            "276 appears at multiple 12",
            "Answer: 12",
        ],
        ["Build the table step by step", "Look for your dividend"],
        "medium",
        2,
    )

    add_practice_problem(
        lesson8_id,
        "3465 ÷ 15 = ?",
        "231",
        [
            "Table: 1→15, 10→150, 100→1500, 200→3000, 231→3465",
            "Build up: 200→3000, add 30→450, add 1→15",
            "Total: 231",
        ],
        ["Use multiples of 100, 10, and 1", "Add them up"],
        "hard",
        3,
    )

    add_practice_problem(
        lesson8_id,
        "1827 ÷ 21 = ?",
        "87",
        [
            "Table for ×21",
            "10→210, 80→1680, 87→1827",
            "1827 is at multiple 87",
            "Answer: 87",
        ],
        ["Jump by tens first", "Then fine-tune"],
        "hard",
        4,
    )

    # Method 9: Place Value Division
    lesson9_id = add_lesson(
        division_topic_id,
        "Place Value Division Method",
        "Divide each place value (hundreds, tens, ones) separately, starting with the largest.",
        [
            "Break the dividend into place values (hundreds, tens, ones).",
            "Start with the largest place value.",
            "Divide that place value by the divisor. Write the quotient.",
            "If there's a remainder, convert it to the next smaller place value.",
            "Move to the next place value, add any converted amount, and divide again.",
            "Continue until you've divided all place values.",
            "Combine all quotients for your answer.",
        ],
        [
            {
                "title": "Example: 369 ÷ 3",
                "content": "300 ÷ 3 = 100. 60 ÷ 3 = 20. 9 ÷ 3 = 3. Add: 100 + 20 + 3 = 123. Answer: 123",
            }
        ],
        "builtin",
        None,
        9,
    )

    add_practice_problem(
        lesson9_id,
        "248 ÷ 4 = ?",
        "62",
        ["200 ÷ 4 = 50", "40 ÷ 4 = 10", "8 ÷ 4 = 2", "Add: 50 + 10 + 2 = 62"],
        ["Work with place values separately", "Then add up the quotients"],
        "medium",
        1,
    )

    add_practice_problem(
        lesson9_id,
        "3465 ÷ 15 = ?",
        "231",
        ["3000 ÷ 15 = 200", "450 ÷ 15 = 30", "15 ÷ 15 = 1", "Add: 200 + 30 + 1 = 231"],
        ["Break into manageable place values", "Combine results"],
        "hard",
        2,
    )

    add_practice_problem(
        lesson9_id,
        "1827 ÷ 21 = ?",
        "87",
        [
            "1800 ÷ 21 is approximately 85.7, try 1680 ÷ 21 = 80",
            "Remaining: 147 ÷ 21 = 7",
            "Add: 80 + 7 = 87",
        ],
        ["Estimate with place values", "Handle remainders"],
        "hard",
        3,
    )

    add_practice_problem(
        lesson9_id,
        "486 ÷ 6 = ?",
        "81",
        ["400 ÷ 6 = 66 R4 → try 420 ÷ 6 = 70", "66 ÷ 6 = 11", "Add: 70 + 11 = 81"],
        ["Be flexible with place value chunks", "Adjust as needed"],
        "medium",
        4,
    )

    # Method 10: Bar Model
    lesson10_id = add_lesson(
        division_topic_id,
        "Bar Model Method",
        "Draw a bar representing the whole, then divide it into equal parts to visualize division.",
        [
            "Draw a long bar to represent the dividend (total amount).",
            "Decide: Are you dividing into a certain number of equal parts, or into parts of a certain size?",
            "Divide the bar into equal sections.",
            "Label each section or count the sections.",
            "The number of sections (or the size of each section) is your quotient.",
        ],
        [
            {
                "title": "Example: 48 ÷ 8",
                "content": "Draw a bar for 48. Divide into sections of 8. |8|8|8|8|8|8|. Count: 6 sections. Answer: 6",
            }
        ],
        "builtin",
        None,
        10,
    )

    add_practice_problem(
        lesson10_id,
        "36 ÷ 4 = ?",
        "9",
        [
            "Draw bar for 36",
            "Divide into 4 equal parts",
            "Each part: 36 ÷ 4 = 9",
            "Answer: 9",
        ],
        ["Draw the bar to scale if possible", "Label each section"],
        "easy",
        1,
    )

    add_practice_problem(
        lesson10_id,
        "144 ÷ 12 = ?",
        "12",
        [
            "Bar represents 144",
            "Make sections of 12",
            "Count sections: 12",
            "Answer: 12",
        ],
        ["Use a ruler for equal sections", "Count carefully"],
        "medium",
        2,
    )

    add_practice_problem(
        lesson10_id,
        "156 ÷ 13 = ?",
        "12",
        [
            "Draw bar for 156",
            "Divide into 13 equal parts",
            "Each part = 12",
            "Or sections of 13: count 12 of them",
        ],
        ["Bar models work both ways", "Choose what makes sense"],
        "medium",
        3,
    )

    add_practice_problem(
        lesson10_id,
        "276 ÷ 23 = ?",
        "12",
        ["Bar for 276", "Sections of 23 each", "Count: 12 sections", "Answer: 12"],
        ["Sketch it out", "Visual representation helps!"],
        "medium",
        4,
    )


def seed_basic_math_topics(
    addition_id,
    subtraction_id,
    multiplication_id,
    fractions_id,
    decimals_id,
    measurement_id,
    geometry_id,
    algebra_id,
    statistics_id,
):
    """Seed basic lessons for other math topics."""

    # Addition
    lesson_id = add_lesson(
        addition_id,
        "Adding Single Digits",
        "Learn to add numbers 0-10",
        [
            "Understand that addition means combining groups",
            "Start with small numbers",
            "Count on your fingers if needed",
            "Practice until you know them by heart",
        ],
        [
            {
                "title": "Example",
                "content": "3 + 4 = 7. Think: 3 items + 4 more items = 7 items total",
            }
        ],
        "builtin",
        None,
        1,
    )
    add_practice_problem(
        lesson_id,
        "5 + 3 = ?",
        "8",
        ["Start at 5", "Count up 3 more", "Answer: 8"],
        ["Use your fingers", "Count carefully"],
        "easy",
        1,
    )
    add_practice_problem(
        lesson_id,
        "7 + 6 = ?",
        "13",
        ["Start at 7", "Add 6 more", "Answer: 13"],
        ["You can split 6 into 3 + 3", "Make 10 first"],
        "medium",
        2,
    )

    # Subtraction
    lesson_id = add_lesson(
        subtraction_id,
        "Subtracting Single Digits",
        "Learn to subtract numbers",
        [
            "Subtraction means taking away",
            "Start with the larger number",
            "Count backwards or take away",
            "Practice with objects",
        ],
        [
            {
                "title": "Example",
                "content": "8 - 3 = 5. Start with 8, take away 3, you have 5 left",
            }
        ],
        "builtin",
        None,
        1,
    )
    add_practice_problem(
        lesson_id,
        "9 - 4 = ?",
        "5",
        ["Start at 9", "Take away 4", "Answer: 5"],
        ["Count backwards", "Use counters"],
        "easy",
        1,
    )

    # Multiplication
    lesson_id = add_lesson(
        multiplication_id,
        "Multiplication Tables",
        "Master multiplication facts",
        [
            "Multiplication is repeated addition",
            "3 × 4 means '3 groups of 4'",
            "Learn your times tables",
            "Practice daily",
        ],
        [
            {
                "title": "Example",
                "content": "5 × 6 = 30. Five groups of six: 6+6+6+6+6 = 30",
            }
        ],
        "builtin",
        None,
        1,
    )
    add_practice_problem(
        lesson_id,
        "7 × 8 = ?",
        "56",
        ["Think: 7 groups of 8", "Or 8 groups of 7", "Answer: 56"],
        ["Use arrays", "Practice facts"],
        "medium",
        1,
    )

    # Fractions
    lesson_id = add_lesson(
        fractions_id,
        "Understanding Fractions",
        "Learn what fractions represent",
        [
            "A fraction represents part of a whole",
            "The bottom number (denominator) tells how many equal parts",
            "The top number (numerator) tells how many parts you have",
            "Practice with visual models",
        ],
        [{"title": "Example", "content": "3/4 means 3 out of 4 equal parts"}],
        "builtin",
        None,
        1,
    )
    add_practice_problem(
        lesson_id,
        "What is 1/2 of 10?",
        "5",
        ["1/2 means divide by 2", "10 ÷ 2 = 5", "Answer: 5"],
        ["Half means 2 equal parts", "Divide evenly"],
        "easy",
        1,
    )

    # Decimals
    lesson_id = add_lesson(
        decimals_id,
        "Introduction to Decimals",
        "Understand decimal place value",
        [
            "Decimals are another way to write fractions",
            "The decimal point separates whole numbers from parts",
            "Each place to the right is 10 times smaller",
            "Practice reading and writing decimals",
        ],
        [{"title": "Example", "content": "0.5 = 5/10 = 1/2"}],
        "builtin",
        None,
        1,
    )
    add_practice_problem(
        lesson_id,
        "Write three tenths as a decimal",
        "0.3",
        ["Three tenths = 3/10", "In decimal form: 0.3", "Answer: 0.3"],
        ["Count the places after the decimal"],
        "easy",
        1,
    )

    # Geometry
    lesson_id = add_lesson(
        geometry_id,
        "Basic Shapes",
        "Identify and describe shapes",
        [
            "Learn names of common shapes",
            "Count sides and corners",
            "Recognize shapes in the world around you",
            "Draw and label shapes",
        ],
        [{"title": "Example", "content": "A triangle has 3 sides and 3 corners"}],
        "builtin",
        None,
        1,
    )
    add_practice_problem(
        lesson_id,
        "How many sides does a rectangle have?",
        "4",
        ["Count the sides", "A rectangle has 4 sides", "Answer: 4"],
        ["Draw it out", "Count carefully"],
        "easy",
        1,
    )


def seed_ela(subject_id):
    """Seed MASSIVE English Language Arts curriculum with grade levels."""

    # GRADE LEVEL TOPICS
    # Kindergarten
    k_phonics_id = add_topic(
        subject_id, "K - Phonics & Letter Sounds", "Learn letters and their sounds", 1
    )
    k_reading_id = add_topic(
        subject_id, "K - Beginning Reading", "Start reading simple words", 2
    )
    k_writing_id = add_topic(
        subject_id, "K - Pre-Writing Skills", "Learn to write letters and words", 3
    )
    k_speaking_id = add_topic(
        subject_id, "K - Speaking & Listening", "Talk and listen to others", 4
    )

    # Grade 1
    g1_phonics_id = add_topic(
        subject_id, "1st - Advanced Phonics", "Master letter sounds and blends", 5
    )
    g1_reading_id = add_topic(
        subject_id, "1st - Reading Fluency", "Read smoothly and with expression", 6
    )
    g1_writing_id = add_topic(
        subject_id, "1st - Sentence Writing", "Write complete sentences", 7
    )
    g1_grammar_id = add_topic(
        subject_id, "1st - Basic Grammar", "Learn nouns, verbs, and adjectives", 8
    )

    # Grade 2
    g2_phonics_id = add_topic(
        subject_id, "2nd - Complex Phonics", "Learn digraphs and diphthongs", 9
    )
    g2_reading_id = add_topic(
        subject_id, "2nd - Reading Comprehension", "Understand what you read", 10
    )
    g2_writing_id = add_topic(
        subject_id, "2nd - Paragraph Writing", "Write organized paragraphs", 11
    )
    g2_grammar_id = add_topic(
        subject_id, "2nd - Grammar Rules", "Master punctuation and capitalization", 12
    )

    # Grade 3
    g3_reading_id = add_topic(
        subject_id, "3rd - Advanced Reading", "Read chapter books and analyze text", 13
    )
    g3_writing_id = add_topic(
        subject_id, "3rd - Multi-Paragraph Writing", "Write essays and stories", 14
    )
    g3_grammar_id = add_topic(
        subject_id, "3rd - Complex Grammar", "Learn advanced grammar rules", 15
    )
    g3_vocab_id = add_topic(
        subject_id, "3rd - Vocabulary Building", "Expand your word knowledge", 16
    )

    # Grade 4
    g4_reading_id = add_topic(
        subject_id, "4th - Literary Analysis", "Analyze characters, plot, and theme", 17
    )
    g4_writing_id = add_topic(
        subject_id, "4th - Essay Writing", "Write persuasive and informative essays", 18
    )
    g4_grammar_id = add_topic(
        subject_id, "4th - Advanced Grammar", "Master complex sentence structures", 19
    )
    g4_vocab_id = add_topic(
        subject_id, "4th - Advanced Vocabulary", "Learn sophisticated words", 20
    )

    # Grade 5
    g5_reading_id = add_topic(
        subject_id, "5th - Critical Reading", "Think critically about what you read", 21
    )
    g5_writing_id = add_topic(
        subject_id, "5th - Research Writing", "Research and write reports", 22
    )
    g5_grammar_id = add_topic(
        subject_id, "5th - Grammar Mastery", "Perfect your grammar skills", 23
    )
    g5_vocab_id = add_topic(
        subject_id, "5th - Academic Vocabulary", "Learn subject-specific words", 24
    )

    # Grade 6
    g6_reading_id = add_topic(
        subject_id, "6th - Literature Study", "Study classic and modern literature", 25
    )
    g6_writing_id = add_topic(
        subject_id, "6th - Creative Writing", "Write stories, poems, and scripts", 26
    )
    g6_grammar_id = add_topic(
        subject_id, "6th - Style & Voice", "Develop your writing style", 27
    )
    g6_vocab_id = add_topic(
        subject_id, "6th - Etymology", "Learn word origins and roots", 28
    )

    # Grade 7
    g7_reading_id = add_topic(
        subject_id, "7th - Advanced Literature", "Analyze complex texts and themes", 29
    )
    g7_writing_id = add_topic(
        subject_id, "7th - Argumentative Writing", "Write convincing arguments", 30
    )
    g7_grammar_id = add_topic(
        subject_id, "7th - Rhetorical Devices", "Use literary techniques", 31
    )
    g7_vocab_id = add_topic(
        subject_id, "7th - SAT Vocabulary", "Prepare for standardized tests", 32
    )

    # Grade 8
    g8_reading_id = add_topic(
        subject_id, "8th - College Prep Reading", "Prepare for high school reading", 33
    )
    g8_writing_id = add_topic(
        subject_id, "8th - Research Papers", "Write formal research papers", 34
    )
    g8_grammar_id = add_topic(
        subject_id, "8th - Advanced Style", "Master sophisticated writing", 35
    )
    g8_vocab_id = add_topic(
        subject_id, "8th - Academic Language", "Master academic vocabulary", 36
    )

    # SPECIALIZED TOPICS
    poetry_id = add_topic(
        subject_id, "Poetry & Creative Writing", "Write and analyze poetry", 37
    )
    drama_id = add_topic(
        subject_id, "Drama & Performance", "Act, direct, and write plays", 38
    )
    media_id = add_topic(
        subject_id, "Media Literacy", "Analyze news, ads, and digital content", 39
    )
    public_speaking_id = add_topic(
        subject_id, "Public Speaking", "Present with confidence", 40
    )
    debate_id = add_topic(
        subject_id, "Debate & Discussion", "Argue persuasively and respectfully", 41
    )
    journalism_id = add_topic(
        subject_id, "Journalism & News Writing", "Write news articles and reports", 42
    )
    technical_writing_id = add_topic(
        subject_id, "Technical Writing", "Write instructions and manuals", 43
    )
    business_writing_id = add_topic(
        subject_id, "Business Writing", "Write emails, letters, and proposals", 44
    )

    # KINDERGARTEN LESSONS
    # Phonics & Letter Sounds
    lesson_id = add_lesson(
        k_phonics_id,
        "Letter A - Sound and Recognition",
        "Learn the letter A and its sound",
        [
            "A is the first letter of the alphabet",
            "A makes the 'a' sound like in 'apple'",
            "A can be uppercase A or lowercase a",
            "Practice writing A: big line down, little line across",
            "Find A in words: apple, ant, alligator",
        ],
        [
            {
                "title": "Examples",
                "content": "A words: apple, ant, alligator, airplane, art",
            }
        ],
        "builtin",
        None,
        1,
    )
    add_practice_problem(
        lesson_id,
        "What sound does the letter A make?",
        "a",
        [
            "Think of the word 'apple'",
            "What sound do you hear at the beginning?",
            "A makes the 'a' sound",
        ],
        ["Say 'apple' out loud"],
        "easy",
        1,
    )

    lesson_id = add_lesson(
        comprehension_id,
        "Main Idea",
        "Find the main idea of a passage",
        [
            "The main idea is what the passage is mostly about",
            "Ask: What is the author mostly telling me?",
            "Look for repeated words or themes",
            "The main idea is usually a sentence, not just one word",
            "Details support the main idea",
        ],
        [
            {
                "title": "Example",
                "content": "Passage about dogs being good pets. Main idea: Dogs make wonderful pets for families.",
            }
        ],
        "builtin",
        None,
        1,
    )

    lesson_id = add_lesson(
        writing_id,
        "Writing Complete Sentences",
        "Learn to write clear, complete sentences",
        [
            "A sentence expresses a complete thought",
            "It has a subject (who or what)",
            "It has a predicate (what they do)",
            "Start with a capital letter",
            "End with punctuation (. ! ?)",
        ],
        [
            {
                "title": "Example",
                "content": "The dog runs. (Subject: dog, Predicate: runs)",
            }
        ],
        "builtin",
        None,
        1,
    )

    lesson_id = add_lesson(
        grammar_id,
        "Nouns",
        "Identify and use nouns",
        [
            "A noun is a person, place, thing, or idea",
            "Person: teacher, boy, Sarah",
            "Place: school, park, Chicago",
            "Thing: book, car, apple",
            "Idea: love, freedom, happiness",
        ],
        [
            {
                "title": "Example",
                "content": "In 'The cat sat on the mat,' the nouns are: cat, mat",
            }
        ],
        "builtin",
        None,
        1,
    )

    lesson_id = add_lesson(
        vocabulary_id,
        "Context Clues",
        "Use context to figure out new words",
        [
            "When you see an unfamiliar word, don't panic!",
            "Look at the words around it (context)",
            "Ask: What would make sense here?",
            "Look for definitions, examples, or synonyms nearby",
            "Try substituting a word you know",
        ],
        [
            {
                "title": "Example",
                "content": "'The enormous elephant was huge.' Context tells us enormous means very big.",
            }
        ],
        "builtin",
        None,
        1,
    )


def seed_science(subject_id):
    """Seed Science curriculum."""

    life_sci = add_topic(
        subject_id, "Life Science", "Plants, animals, and living things", 1
    )
    physical_sci = add_topic(
        subject_id, "Physical Science", "Matter, energy, and forces", 2
    )
    earth_sci = add_topic(
        subject_id, "Earth Science", "Weather, rocks, and our planet", 3
    )
    space_sci = add_topic(subject_id, "Space Science", "Astronomy and the universe", 4)
    sci_method = add_topic(
        subject_id, "Scientific Method", "How scientists investigate", 5
    )

    lesson_id = add_lesson(
        life_sci,
        "Plant Life Cycle",
        "How plants grow and reproduce",
        [
            "Plants start as seeds",
            "With water and sunlight, seeds germinate (sprout)",
            "The plant grows roots, stems, and leaves",
            "The plant matures and produces flowers",
            "Flowers make seeds",
            "The cycle repeats!",
        ],
        [
            {
                "title": "Example",
                "content": "A sunflower: seed → sprout → grows tall → flowers → makes new seeds",
            }
        ],
        "builtin",
        None,
        1,
    )

    lesson_id = add_lesson(
        physical_sci,
        "States of Matter",
        "Solids, liquids, and gases",
        [
            "Matter exists in three states: solid, liquid, gas",
            "Solids have a definite shape (like ice)",
            "Liquids take the shape of their container (like water)",
            "Gases spread out to fill their container (like air)",
            "Heating and cooling can change states",
        ],
        [
            {
                "title": "Example",
                "content": "Water: ice (solid) → water (liquid) → steam (gas)",
            }
        ],
        "builtin",
        None,
        1,
    )

    lesson_id = add_lesson(
        earth_sci,
        "Water Cycle",
        "How water moves through our environment",
        [
            "The sun heats water (oceans, lakes, rivers)",
            "Water evaporates into the air as vapor (gas)",
            "Vapor rises and cools, forming clouds (condensation)",
            "Clouds release water as precipitation (rain, snow)",
            "Water returns to earth and the cycle repeats",
        ],
        [
            {
                "title": "Example",
                "content": "Rain falls → runs into rivers → flows to ocean → evaporates → forms clouds → rain again",
            }
        ],
        "builtin",
        None,
        1,
    )

    lesson_id = add_lesson(
        space_sci,
        "The Solar System",
        "Our sun and the planets",
        [
            "The Solar System has the Sun at the center",
            "Eight planets orbit the Sun",
            "Inner planets (Mercury, Venus, Earth, Mars) are rocky",
            "Outer planets (Jupiter, Saturn, Uranus, Neptune) are gas giants",
            "Earth is the only planet we know with life",
        ],
        [
            {
                "title": "Example",
                "content": "Order: Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune",
            }
        ],
        "builtin",
        None,
        1,
    )

    lesson_id = add_lesson(
        sci_method,
        "The Scientific Method",
        "Steps scientists use to investigate",
        [
            "Step 1: Ask a question or identify a problem",
            "Step 2: Research and gather information",
            "Step 3: Form a hypothesis (an educated guess)",
            "Step 4: Conduct an experiment to test the hypothesis",
            "Step 5: Analyze the results",
            "Step 6: Draw a conclusion",
            "Step 7: Share your findings",
        ],
        [
            {
                "title": "Example",
                "content": "Question: Do plants need light to grow? Hypothesis: Yes, plants need light. Experiment: Grow two plants, one in light, one in dark. Result: Plant in light grew, plant in dark didn't. Conclusion: Plants need light.",
            }
        ],
        "builtin",
        None,
        1,
    )


def seed_social_studies(subject_id):
    """Seed Social Studies curriculum."""

    us_history = add_topic(subject_id, "U.S. History", "American history and events", 1)
    world_history = add_topic(
        subject_id, "World History", "Ancient civilizations and world events", 2
    )
    geography = add_topic(subject_id, "Geography", "Maps, places, and cultures", 3)
    civics = add_topic(subject_id, "Civics & Government", "How government works", 4)
    economics = add_topic(subject_id, "Economics", "Money, trade, and resources", 5)

    lesson_id = add_lesson(
        us_history,
        "The American Revolution",
        "How America gained independence",
        [
            "In the 1700s, America was ruled by Great Britain",
            "Colonists were unhappy with British taxes and rules",
            "The colonists decided to fight for independence",
            "Key events: Boston Tea Party, Declaration of Independence, battles",
            "America won the war and became independent in 1783",
        ],
        [
            {
                "title": "Key Date",
                "content": "July 4, 1776: Declaration of Independence signed",
            }
        ],
        "builtin",
        None,
        1,
    )

    lesson_id = add_lesson(
        world_history,
        "Ancient Egypt",
        "One of the world's first great civilizations",
        [
            "Ancient Egypt existed over 3,000 years ago",
            "Located along the Nile River in Africa",
            "Egyptians built pyramids as tombs for pharaohs (kings)",
            "They developed hieroglyphics (picture writing)",
            "Egyptian civilization lasted thousands of years",
        ],
        [{"title": "Famous Monument", "content": "The Great Pyramid of Giza"}],
        "builtin",
        None,
        1,
    )

    lesson_id = add_lesson(
        geography,
        "Reading Maps",
        "Understand maps and their features",
        [
            "Maps show places from above",
            "Title tells you what the map shows",
            "Compass rose shows directions (N, S, E, W)",
            "Legend/key explains symbols",
            "Scale shows distance",
        ],
        [
            {
                "title": "Example",
                "content": "A map of your town might show streets (lines), parks (green), and buildings (shapes)",
            }
        ],
        "builtin",
        None,
        1,
    )

    lesson_id = add_lesson(
        civics,
        "Three Branches of Government",
        "How the U.S. government is organized",
        [
            "The U.S. government has three branches",
            "Legislative Branch (Congress): Makes laws",
            "Executive Branch (President): Enforces laws",
            "Judicial Branch (Courts): Interprets laws",
            "Each branch has different powers",
            "This system provides checks and balances",
        ],
        [
            {
                "title": "Example",
                "content": "Congress passes a law, President signs it, Courts make sure it's constitutional",
            }
        ],
        "builtin",
        None,
        1,
    )

    lesson_id = add_lesson(
        economics,
        "Needs vs. Wants",
        "Understanding the difference",
        [
            "Needs are things you must have to survive",
            "Examples: food, water, shelter, clothing",
            "Wants are things you would like but don't need",
            "Examples: toys, candy, video games",
            "We have limited money, so we must make choices",
            "Prioritize needs first, then wants",
        ],
        [{"title": "Example", "content": "A coat (need) vs. a toy (want)"}],
        "builtin",
        None,
        1,
    )


def seed_arts(subject_id):
    """Seed Arts curriculum."""

    visual_arts = add_topic(
        subject_id, "Visual Arts", "Drawing, painting, and sculpture", 1
    )
    music = add_topic(
        subject_id, "Music", "Rhythm, melody, and musical appreciation", 2
    )

    lesson_id = add_lesson(
        visual_arts,
        "Elements of Art",
        "The building blocks of art",
        [
            "Line: A mark made by a moving point",
            "Shape: A flat, enclosed area (circle, square, etc.)",
            "Color: What we see when light reflects",
            "Texture: How something feels or looks like it feels",
            "Space: The area around and between objects",
            "Form: Three-dimensional shapes",
            "Value: Lightness or darkness of a color",
        ],
        [
            {
                "title": "Example",
                "content": "A painting uses lines to create shapes, colors to make it interesting, and space to show depth",
            }
        ],
        "builtin",
        None,
        1,
    )

    lesson_id = add_lesson(
        music,
        "Rhythm and Beat",
        "Understanding the pulse of music",
        [
            "Rhythm is the pattern of sounds in time",
            "Beat is the steady pulse you can clap to",
            "Notes can be long or short",
            "Rests are moments of silence",
            "Tempo is how fast or slow the beat is",
        ],
        [
            {
                "title": "Example",
                "content": "Clap along to a song - that steady clap is the beat. The melody on top is the rhythm.",
            }
        ],
        "builtin",
        None,
        1,
    )


def seed_languages(subject_id):
    """Seed World Languages curriculum."""

    spanish = add_topic(subject_id, "Spanish", "Learn basic Spanish", 1)
    french = add_topic(subject_id, "French", "Learn basic French", 2)
    esl = add_topic(subject_id, "ESL Support", "English as a Second Language", 3)

    lesson_id = add_lesson(
        spanish,
        "Spanish Greetings",
        "Say hello in Spanish",
        [
            "Hola = Hello",
            "Buenos días = Good morning",
            "Buenas tardes = Good afternoon",
            "Buenas noches = Good evening/night",
            "¿Cómo estás? = How are you?",
            "Muy bien = Very well",
            "Gracias = Thank you",
            "Adiós = Goodbye",
        ],
        [
            {
                "title": "Conversation",
                "content": "Person 1: ¡Hola! ¿Cómo estás? Person 2: Muy bien, gracias. ¿Y tú?",
            }
        ],
        "builtin",
        None,
        1,
    )

    lesson_id = add_lesson(
        french,
        "French Greetings",
        "Say hello in French",
        [
            "Bonjour = Hello/Good day",
            "Bonsoir = Good evening",
            "Comment allez-vous? = How are you? (formal)",
            "Ça va? = How are you? (informal)",
            "Je vais bien = I'm well",
            "Merci = Thank you",
            "Au revoir = Goodbye",
        ],
        [
            {
                "title": "Conversation",
                "content": "Person 1: Bonjour! Ça va? Person 2: Ça va bien, merci!",
            }
        ],
        "builtin",
        None,
        1,
    )


def seed_technology(subject_id):
    """Seed Technology & STEAM curriculum."""

    coding = add_topic(subject_id, "Coding Basics", "Introduction to programming", 1)
    media_lit = add_topic(
        subject_id, "Media Literacy", "Understanding digital media", 2
    )
    steam = add_topic(
        subject_id, "STEAM Projects", "Science, Technology, Engineering, Art, Math", 3
    )

    lesson_id = add_lesson(
        coding,
        "What is Code?",
        "Understanding computer programming",
        [
            "Code is instructions for a computer",
            "Computers follow instructions exactly",
            "Coding languages include: JavaScript, Python, Scratch",
            "Programs are made of sequences of commands",
            "Debugging means fixing errors in code",
        ],
        [
            {
                "title": "Example",
                "content": "A simple instruction: 'Move forward 10 steps' or 'Repeat 5 times: say Hello'",
            }
        ],
        "builtin",
        None,
        1,
    )

    lesson_id = add_lesson(
        media_lit,
        "Evaluating Online Information",
        "How to tell if information is reliable",
        [
            "Not everything on the internet is true",
            "Check the source: Who created it?",
            "Look for evidence and facts",
            "Compare information from multiple sources",
            "Be careful with personal information online",
        ],
        [
            {
                "title": "Example",
                "content": "A news article from a known newspaper is more reliable than an anonymous blog post",
            }
        ],
        "builtin",
        None,
        1,
    )


def seed_pe_health(subject_id):
    """Seed PE & Health curriculum."""

    fitness = add_topic(
        subject_id, "Fitness & Exercise", "Staying active and healthy", 1
    )
    nutrition = add_topic(subject_id, "Nutrition", "Eating healthy foods", 2)

    lesson_id = add_lesson(
        fitness,
        "Importance of Exercise",
        "Why we need to stay active",
        [
            "Exercise makes your body strong",
            "It helps your heart and lungs",
            "Exercise improves mood and energy",
            "Aim for at least 60 minutes of activity each day",
            "Activities: running, swimming, biking, dancing, sports",
        ],
        [{"title": "Example", "content": "Playing tag at recess counts as exercise!"}],
        "builtin",
        None,
        1,
    )

    lesson_id = add_lesson(
        nutrition,
        "Healthy Eating",
        "Choosing nutritious foods",
        [
            "Eat a variety of foods from all food groups",
            "Fruits and vegetables are important",
            "Protein builds muscles (meat, beans, eggs)",
            "Whole grains give you energy",
            "Drink plenty of water",
            "Limit sugar and junk food",
        ],
        [
            {
                "title": "Example",
                "content": "A balanced meal: chicken, broccoli, brown rice, and milk",
            }
        ],
        "builtin",
        None,
        1,
    )


def seed_life_skills(subject_id):
    """Seed Life & Study Skills curriculum."""

    study_skills = add_topic(subject_id, "Study Skills", "How to study effectively", 1)
    test_prep = add_topic(
        subject_id, "Test Preparation", "Strategies for taking tests", 2
    )

    lesson_id = add_lesson(
        study_skills,
        "Taking Good Notes",
        "How to write helpful notes",
        [
            "Listen carefully to the teacher",
            "Write down key points, not every word",
            "Use abbreviations to save time",
            "Organize notes with headings and bullets",
            "Review notes after class",
            "Add drawings or diagrams if helpful",
        ],
        [
            {
                "title": "Example",
                "content": "During a science lesson, write: 'Water cycle: evap → condense → precip'",
            }
        ],
        "builtin",
        None,
        1,
    )

    lesson_id = add_lesson(
        test_prep,
        "Test-Taking Strategies",
        "Tips for doing your best on tests",
        [
            "Get a good night's sleep before the test",
            "Eat a healthy breakfast",
            "Read directions carefully",
            "Answer easy questions first",
            "Check your work if you have time",
            "Stay calm and do your best",
        ],
        [
            {
                "title": "Example",
                "content": "If you don't know an answer, skip it and come back later",
            }
        ],
        "builtin",
        None,
        1,
    )
