"""
MASSIVE Mathematics Curriculum with Grade Levels
This creates a comprehensive Math curriculum for K-8 with grade-specific topics and lessons.
"""

from database import (add_subject, add_topic, add_lesson, add_practice_problem, 
                      get_all_subjects, get_topics_by_subject)

def seed_massive_math_curriculum():
    """Seed the database with MASSIVE Math curriculum organized by grade levels."""
    
    # Check if already seeded
    existing_subjects = get_all_subjects()
    if existing_subjects and any(s['name'] == 'Mathematics' for s in existing_subjects):
        print("Mathematics curriculum already seeded.")
        return
    
    print("Seeding MASSIVE Math curriculum...")
    
    # Create Math subject
    math_id = add_subject("Mathematics", "Numbers, operations, algebra, geometry, and more", "🔢", 1)
    
    # KINDERGARTEN TOPICS
    k_numbers_id = add_topic(math_id, "K - Numbers & Counting", "Learn to count and recognize numbers", 1)
    k_shapes_id = add_topic(math_id, "K - Shapes & Patterns", "Identify shapes and create patterns", 2)
    k_measurement_id = add_topic(math_id, "K - Basic Measurement", "Compare sizes and learn measurement", 3)
    k_addition_id = add_topic(math_id, "K - Simple Addition", "Add small numbers together", 4)
    
    # GRADE 1 TOPICS
    g1_numbers_id = add_topic(math_id, "1st - Number Sense", "Understand numbers 1-100", 5)
    g1_addition_id = add_topic(math_id, "1st - Addition Facts", "Master addition within 20", 6)
    g1_subtraction_id = add_topic(math_id, "1st - Subtraction Facts", "Master subtraction within 20", 7)
    g1_geometry_id = add_topic(math_id, "1st - 2D & 3D Shapes", "Explore geometric shapes", 8)
    
    # GRADE 2 TOPICS
    g2_place_value_id = add_topic(math_id, "2nd - Place Value", "Understand hundreds, tens, and ones", 9)
    g2_addition_id = add_topic(math_id, "2nd - Multi-Digit Addition", "Add 2 and 3 digit numbers", 10)
    g2_subtraction_id = add_topic(math_id, "2nd - Multi-Digit Subtraction", "Subtract 2 and 3 digit numbers", 11)
    g2_money_id = add_topic(math_id, "2nd - Money & Time", "Count money and tell time", 12)
    
    # GRADE 3 TOPICS
    g3_multiplication_id = add_topic(math_id, "3rd - Multiplication", "Learn multiplication facts", 13)
    g3_division_id = add_topic(math_id, "3rd - Division", "Learn division facts", 14)
    g3_fractions_id = add_topic(math_id, "3rd - Introduction to Fractions", "Understand basic fractions", 15)
    g3_measurement_id = add_topic(math_id, "3rd - Measurement", "Measure length, weight, and capacity", 16)
    
    # GRADE 4 TOPICS
    g4_multiplication_id = add_topic(math_id, "4th - Multi-Digit Multiplication", "Multiply large numbers", 17)
    g4_division_id = add_topic(math_id, "4th - Long Division", "Divide large numbers", 18)
    g4_fractions_id = add_topic(math_id, "4th - Fractions & Decimals", "Work with fractions and decimals", 19)
    g4_geometry_id = add_topic(math_id, "4th - Angles & Lines", "Understand angles and geometric lines", 20)
    
    # GRADE 5 TOPICS
    g5_fractions_id = add_topic(math_id, "5th - Fraction Operations", "Add, subtract, multiply, and divide fractions", 21)
    g5_decimals_id = add_topic(math_id, "5th - Decimal Operations", "Work with decimal numbers", 22)
    g5_geometry_id = add_topic(math_id, "5th - Area & Perimeter", "Calculate area and perimeter", 23)
    g5_algebra_id = add_topic(math_id, "5th - Introduction to Algebra", "Solve simple equations", 24)
    
    # GRADE 6 TOPICS
    g6_ratios_id = add_topic(math_id, "6th - Ratios & Proportions", "Understand ratios and proportions", 25)
    g6_percentages_id = add_topic(math_id, "6th - Percentages", "Work with percentages", 26)
    g6_geometry_id = add_topic(math_id, "6th - Volume & Surface Area", "Calculate volume and surface area", 27)
    g6_statistics_id = add_topic(math_id, "6th - Statistics & Data", "Analyze data and create graphs", 28)
    
    # GRADE 7 TOPICS
    g7_algebra_id = add_topic(math_id, "7th - Pre-Algebra", "Solve equations and inequalities", 29)
    g7_geometry_id = add_topic(math_id, "7th - Geometry", "Study angles, triangles, and circles", 30)
    g7_probability_id = add_topic(math_id, "7th - Probability", "Understand probability and chance", 31)
    g7_ratios_id = add_topic(math_id, "7th - Proportional Relationships", "Work with proportional relationships", 32)
    
    # GRADE 8 TOPICS
    g8_algebra_id = add_topic(math_id, "8th - Algebra I", "Master algebraic concepts", 33)
    g8_geometry_id = add_topic(math_id, "8th - Advanced Geometry", "Study transformations and congruence", 34)
    g8_functions_id = add_topic(math_id, "8th - Functions", "Understand linear functions", 35)
    g8_systems_id = add_topic(math_id, "8th - Systems of Equations", "Solve systems of equations", 36)
    
    # ADVANCED TOPICS
    calculus_id = add_topic(math_id, "Calculus", "Limits, derivatives, and integrals", 37)
    trigonometry_id = add_topic(math_id, "Trigonometry", "Sine, cosine, and tangent", 38)
    statistics_id = add_topic(math_id, "Advanced Statistics", "Statistical analysis and inference", 39)
    discrete_math_id = add_topic(math_id, "Discrete Mathematics", "Logic, sets, and combinatorics", 40)
    
    # KINDERGARTEN LESSONS
    seed_kindergarten_math_lessons(k_numbers_id, k_shapes_id, k_measurement_id, k_addition_id)
    
    # GRADE 1 LESSONS
    seed_grade1_math_lessons(g1_numbers_id, g1_addition_id, g1_subtraction_id, g1_geometry_id)
    
    # GRADE 2 LESSONS
    seed_grade2_math_lessons(g2_place_value_id, g2_addition_id, g2_subtraction_id, g2_money_id)
    
    # GRADE 3 LESSONS
    seed_grade3_math_lessons(g3_multiplication_id, g3_division_id, g3_fractions_id, g3_measurement_id)
    
    # GRADE 4 LESSONS
    seed_grade4_math_lessons(g4_multiplication_id, g4_division_id, g4_fractions_id, g4_geometry_id)
    
    # GRADE 5 LESSONS
    seed_grade5_math_lessons(g5_fractions_id, g5_decimals_id, g5_geometry_id, g5_algebra_id)
    
    # GRADE 6 LESSONS
    seed_grade6_math_lessons(g6_ratios_id, g6_percentages_id, g6_geometry_id, g6_statistics_id)
    
    # GRADE 7 LESSONS
    seed_grade7_math_lessons(g7_algebra_id, g7_geometry_id, g7_probability_id, g7_ratios_id)
    
    # GRADE 8 LESSONS
    seed_grade8_math_lessons(g8_algebra_id, g8_geometry_id, g8_functions_id, g8_systems_id)
    
    # ADVANCED LESSONS
    seed_advanced_math_lessons(calculus_id, trigonometry_id, statistics_id, discrete_math_id)
    
    print("MASSIVE Math curriculum seeded successfully!")

def seed_kindergarten_math_lessons(numbers_id, shapes_id, measurement_id, addition_id):
    """Seed Kindergarten math lessons."""
    
    # Numbers & Counting
    lesson_id = add_lesson(numbers_id, "Counting 1-10", "Learn to count from 1 to 10",
                          ["Numbers help us count things",
                           "Start with 1 and count up to 10",
                           "Practice counting objects around you",
                           "Each number has a name: one, two, three, four, five",
                           "Count with your fingers to help you remember"],
                          [{"title": "Examples", "content": "Count: 1 apple, 2 cars, 3 balls, 4 cats, 5 dogs"}],
                          "builtin", None, 1)
    add_practice_problem(lesson_id, "How many fingers do you have on one hand?", "5",
                        ["Count your fingers", "One, two, three, four, five", "You have 5 fingers on one hand"],
                        ["Use your fingers to count"], "easy", 1)
    
    lesson_id = add_lesson(numbers_id, "Number Recognition", "Recognize numbers 1-10",
                          ["Numbers look different from letters",
                           "Each number has a special shape",
                           "Practice writing numbers 1-10",
                           "Find numbers in books and signs",
                           "Numbers help us tell how many things we have"],
                          [{"title": "Examples", "content": "1 looks like a stick, 2 looks like a swan, 3 looks like a snake"}],
                          "builtin", None, 1)
    
    lesson_id = add_lesson(numbers_id, "Counting Objects", "Count groups of objects",
                          ["When you count, touch each object once",
                           "Say the number as you touch each object",
                           "The last number you say is how many you have",
                           "Practice counting toys, books, and other things",
                           "Make sure you count each object only once"],
                          [{"title": "Example", "content": "Count 3 blocks: Touch first block and say '1', touch second block and say '2', touch third block and say '3'. You have 3 blocks."}],
                          "builtin", None, 1)
    
    # Shapes & Patterns
    lesson_id = add_lesson(shapes_id, "Basic Shapes", "Learn about circles, squares, triangles, and rectangles",
                          ["Shapes are all around us",
                           "Circle: round like a ball or wheel",
                           "Square: has 4 equal sides",
                           "Triangle: has 3 sides",
                           "Rectangle: has 4 sides, but not all equal"],
                          [{"title": "Examples", "content": "Circle: pizza, wheel. Square: window, book. Triangle: roof, slice of pizza. Rectangle: door, paper."}],
                          "builtin", None, 1)
    
    lesson_id = add_lesson(shapes_id, "Creating Patterns", "Make and continue patterns",
                          ["Patterns repeat in a special order",
                           "Look for what comes next in the pattern",
                           "Patterns can be made with colors, shapes, or objects",
                           "Practice making your own patterns",
                           "Patterns help us predict what comes next"],
                          [{"title": "Example", "content": "Red, blue, red, blue, red, blue... What comes next? Blue!"}],
                          "builtin", None, 1)
    
    # Basic Measurement
    lesson_id = add_lesson(measurement_id, "Big and Small", "Compare sizes of objects",
                          ["Some things are big, some are small",
                           "Big means larger or takes up more space",
                           "Small means smaller or takes up less space",
                           "Compare objects to see which is bigger",
                           "Practice using the words big and small"],
                          [{"title": "Examples", "content": "An elephant is big, a mouse is small. A house is big, a toy is small."}],
                          "builtin", None, 1)
    
    # Simple Addition
    lesson_id = add_lesson(addition_id, "Adding with Objects", "Add small numbers using objects",
                          ["Addition means putting things together",
                           "Use objects like blocks or toys to help you add",
                           "Start with a small number, then add more",
                           "Count all the objects to find the answer",
                           "Practice adding 1, 2, or 3 to numbers"],
                          [{"title": "Example", "content": "2 blocks + 1 block = 3 blocks. Count: 1, 2, then 3."}],
                          "builtin", None, 1)

def seed_grade1_math_lessons(numbers_id, addition_id, subtraction_id, geometry_id):
    """Seed Grade 1 math lessons."""
    
    # Number Sense
    lesson_id = add_lesson(numbers_id, "Numbers 1-100", "Count and recognize numbers up to 100",
                          ["Numbers go from 1 to 100 and beyond",
                           "Practice counting by 1s, 2s, 5s, and 10s",
                           "Learn to read and write numbers up to 100",
                           "Understand that 10 ones make 1 ten",
                           "Practice counting objects up to 100"],
                          [{"title": "Examples", "content": "Count by 10s: 10, 20, 30, 40, 50, 60, 70, 80, 90, 100"}],
                          "builtin", None, 1)
    
    lesson_id = add_lesson(numbers_id, "Comparing Numbers", "Compare numbers using greater than, less than, and equal to",
                          ["Use symbols to compare numbers",
                           "> means greater than (bigger)",
                           "< means less than (smaller)",
                           "= means equal to (same)",
                           "Practice comparing different numbers"],
                          [{"title": "Examples", "content": "5 > 3 (5 is greater than 3), 2 < 7 (2 is less than 7), 4 = 4 (4 equals 4)"}],
                          "builtin", None, 1)
    
    # Addition Facts
    lesson_id = add_lesson(addition_id, "Addition Facts to 10", "Master addition facts within 10",
                          ["Memorize addition facts to make math easier",
                           "Practice: 1+1=2, 1+2=3, 2+2=4, etc.",
                           "Use strategies like counting on or using doubles",
                           "Practice with flashcards and games",
                           "The more you practice, the faster you'll get"],
                          [{"title": "Examples", "content": "Doubles: 1+1=2, 2+2=4, 3+3=6, 4+4=8, 5+5=10"}],
                          "builtin", None, 1)
    
    lesson_id = add_lesson(addition_id, "Addition Facts to 20", "Master addition facts within 20",
                          ["Learn addition facts up to 20",
                           "Use strategies like making 10 or using known facts",
                           "Practice: 6+7=13, 8+9=17, 9+9=18, etc.",
                           "Practice with games and activities",
                           "Speed and accuracy are both important"],
                          [{"title": "Examples", "content": "Making 10: 7+5 = 7+3+2 = 10+2 = 12"}],
                          "builtin", None, 1)
    
    # Subtraction Facts
    lesson_id = add_lesson(subtraction_id, "Subtraction Facts to 10", "Master subtraction facts within 10",
                          ["Subtraction means taking away",
                           "Practice: 5-2=3, 7-3=4, 9-4=5, etc.",
                           "Use addition to help with subtraction",
                           "Practice with objects and pictures",
                           "Memorize the facts for speed"],
                          [{"title": "Examples", "content": "If 3+4=7, then 7-4=3 and 7-3=4"}],
                          "builtin", None, 1)
    
    # 2D & 3D Shapes
    lesson_id = add_lesson(geometry_id, "2D Shapes", "Learn about flat shapes",
                          ["2D shapes are flat and have length and width",
                           "Learn about circles, squares, triangles, rectangles, hexagons",
                           "Count the sides and corners of each shape",
                           "Find 2D shapes in the world around you",
                           "Practice drawing and identifying shapes"],
                          [{"title": "Examples", "content": "Triangle: 3 sides, 3 corners. Square: 4 equal sides, 4 corners. Circle: no sides, no corners."}],
                          "builtin", None, 1)
    
    lesson_id = add_lesson(geometry_id, "3D Shapes", "Learn about solid shapes",
                          ["3D shapes are solid and have length, width, and height",
                           "Learn about cubes, spheres, cylinders, cones, pyramids",
                           "3D shapes can be held and have faces, edges, and vertices",
                           "Find 3D shapes in everyday objects",
                           "Practice identifying and describing 3D shapes"],
                          [{"title": "Examples", "content": "Cube: like a box, 6 square faces. Sphere: like a ball, round all over. Cylinder: like a can, round on top and bottom."}],
                          "builtin", None, 1)

def seed_grade2_math_lessons(place_value_id, addition_id, subtraction_id, money_id):
    """Seed Grade 2 math lessons."""
    
    # Place Value
    lesson_id = add_lesson(place_value_id, "Hundreds, Tens, and Ones", "Understand place value up to 999",
                          ["Place value tells us what each digit means",
                           "Ones place: 0-9 (like counting objects)",
                           "Tens place: 10, 20, 30... (like counting groups of 10)",
                           "Hundreds place: 100, 200, 300... (like counting groups of 100)",
                           "Practice reading and writing 3-digit numbers"],
                          [{"title": "Example", "content": "In 247: 2 is in hundreds place (200), 4 is in tens place (40), 7 is in ones place (7)"}],
                          "builtin", None, 1)
    
    lesson_id = add_lesson(place_value_id, "Expanded Form", "Write numbers in expanded form",
                          ["Expanded form shows the value of each digit",
                           "Break apart numbers to show place value",
                           "Example: 247 = 200 + 40 + 7",
                           "Practice writing numbers in expanded form",
                           "This helps you understand what each digit means"],
                          [{"title": "Examples", "content": "156 = 100 + 50 + 6, 384 = 300 + 80 + 4"}],
                          "builtin", None, 1)
    
    # Multi-Digit Addition
    lesson_id = add_lesson(addition_id, "Adding 2-Digit Numbers", "Add numbers with regrouping",
                          ["When adding 2-digit numbers, add ones first, then tens",
                           "If ones add up to 10 or more, regroup to tens",
                           "Example: 27 + 35 = 62",
                           "Practice with and without regrouping",
                           "Use base-10 blocks to help visualize"],
                          [{"title": "Example", "content": "27 + 35: 7+5=12 (write 2, carry 1), 2+3+1=6, answer: 62"}],
                          "builtin", None, 1)
    
    lesson_id = add_lesson(addition_id, "Adding 3-Digit Numbers", "Add larger numbers with regrouping",
                          ["Add hundreds, tens, and ones separately",
                           "Regroup when any column adds up to 10 or more",
                           "Example: 247 + 158 = 405",
                           "Practice with different combinations",
                           "Check your work by adding in reverse"],
                          [{"title": "Example", "content": "247 + 158: 7+8=15 (write 5, carry 1), 4+5+1=10 (write 0, carry 1), 2+1+1=4, answer: 405"}],
                          "builtin", None, 1)
    
    # Multi-Digit Subtraction
    lesson_id = add_lesson(subtraction_id, "Subtracting 2-Digit Numbers", "Subtract with regrouping",
                          ["When subtracting, start with ones, then tens",
                           "If you can't subtract, borrow from the next column",
                           "Example: 52 - 27 = 25",
                           "Practice with and without borrowing",
                           "Use base-10 blocks to help understand"],
                          [{"title": "Example", "content": "52 - 27: Can't do 2-7, so borrow 1 ten, making it 12-7=5, then 4-2=2, answer: 25"}],
                          "builtin", None, 1)
    
    # Money & Time
    lesson_id = add_lesson(money_id, "Counting Money", "Count coins and bills",
                          ["Learn the value of pennies, nickels, dimes, quarters",
                           "Practice counting different combinations of coins",
                           "Learn about dollar bills",
                           "Practice making change",
                           "Use real money or play money to practice"],
                          [{"title": "Examples", "content": "Penny = 1¢, Nickel = 5¢, Dime = 10¢, Quarter = 25¢, Dollar = 100¢"}],
                          "builtin", None, 1)
    
    lesson_id = add_lesson(money_id, "Telling Time", "Read analog and digital clocks",
                          ["Learn to tell time to the hour and half hour",
                           "Hour hand points to the hour",
                           "Minute hand points to the minutes",
                           "Practice reading both analog and digital clocks",
                           "Learn about AM and PM"],
                          [{"title": "Examples", "content": "3:00 = three o'clock, 3:30 = three thirty or half past three"}],
                          "builtin", None, 1)

def seed_grade3_math_lessons(multiplication_id, division_id, fractions_id, measurement_id):
    """Seed Grade 3 math lessons."""
    
    # Multiplication
    lesson_id = add_lesson(multiplication_id, "Multiplication Basics", "Understand what multiplication means",
                          ["Multiplication is repeated addition",
                           "3 × 4 means 3 groups of 4, or 4 + 4 + 4 = 12",
                           "Learn multiplication vocabulary: factors and product",
                           "Practice with arrays and groups",
                           "Start with multiplication facts 0-5"],
                          [{"title": "Examples", "content": "2 × 3 = 2 + 2 + 2 = 6, or 3 groups of 2 objects each"}],
                          "builtin", None, 1)
    
    lesson_id = add_lesson(multiplication_id, "Multiplication Facts 0-10", "Master multiplication tables",
                          ["Memorize multiplication facts for speed",
                           "Practice: 0×0=0, 1×1=1, 2×2=4, 3×3=9, etc.",
                           "Use strategies like skip counting and patterns",
                           "Practice with games and flashcards",
                           "Focus on accuracy first, then speed"],
                          [{"title": "Examples", "content": "Skip counting by 3s: 3, 6, 9, 12, 15, 18, 21, 24, 27, 30"}],
                          "builtin", None, 1)
    
    # Division
    lesson_id = add_lesson(division_id, "Division Basics", "Understand what division means",
                          ["Division is the opposite of multiplication",
                           "12 ÷ 3 means 'how many groups of 3 make 12?'",
                           "Learn division vocabulary: dividend, divisor, quotient",
                           "Practice with sharing and grouping",
                           "Start with division facts 1-10"],
                          [{"title": "Examples", "content": "12 ÷ 3 = 4 because 3 × 4 = 12, or 12 objects shared equally among 3 people"}],
                          "builtin", None, 1)
    
    # Introduction to Fractions
    lesson_id = add_lesson(fractions_id, "Understanding Fractions", "Learn what fractions represent",
                          ["Fractions show parts of a whole",
                           "The top number (numerator) tells how many parts",
                           "The bottom number (denominator) tells how many equal parts",
                           "Start with halves, thirds, and fourths",
                           "Practice with pictures and objects"],
                          [{"title": "Examples", "content": "1/2 means 1 out of 2 equal parts, 2/3 means 2 out of 3 equal parts"}],
                          "builtin", None, 1)
    
    lesson_id = add_lesson(fractions_id, "Comparing Fractions", "Compare fractions with the same denominator",
                          ["When denominators are the same, compare numerators",
                           "The larger numerator means the larger fraction",
                           "Example: 3/4 > 1/4 because 3 > 1",
                           "Practice with visual models",
                           "Use fraction strips or circles to help"],
                          [{"title": "Examples", "content": "2/5 < 4/5, 1/3 < 2/3, 3/8 > 1/8"}],
                          "builtin", None, 1)
    
    # Measurement
    lesson_id = add_lesson(measurement_id, "Length and Distance", "Measure length using inches, feet, and yards",
                          ["Use rulers to measure length",
                           "12 inches = 1 foot, 3 feet = 1 yard",
                           "Practice measuring objects around you",
                           "Learn to estimate lengths",
                           "Compare lengths using <, >, and ="],
                          [{"title": "Examples", "content": "A pencil is about 6 inches, a door is about 7 feet, a football field is 100 yards"}],
                          "builtin", None, 1)
    
    lesson_id = add_lesson(measurement_id, "Weight and Capacity", "Measure weight and capacity",
                          ["Weight tells how heavy something is",
                           "Capacity tells how much something can hold",
                           "Practice with scales and measuring cups",
                           "Learn about ounces, pounds, cups, pints, quarts",
                           "Compare weights and capacities"],
                          [{"title": "Examples", "content": "16 ounces = 1 pound, 2 cups = 1 pint, 4 quarts = 1 gallon"}],
                          "builtin", None, 1)

def seed_grade4_math_lessons(multiplication_id, division_id, fractions_id, geometry_id):
    """Seed Grade 4 math lessons."""
    
    # Multi-Digit Multiplication
    lesson_id = add_lesson(multiplication_id, "Multiplying 2-Digit by 1-Digit", "Multiply larger numbers",
                          ["Use the distributive property to break apart numbers",
                           "Example: 23 × 4 = (20 × 4) + (3 × 4) = 80 + 12 = 92",
                           "Practice with different combinations",
                           "Use area models to visualize",
                           "Check your work by estimating"],
                          [{"title": "Example", "content": "34 × 5: 30×5=150, 4×5=20, 150+20=170"}],
                          "builtin", None, 1)
    
    lesson_id = add_lesson(multiplication_id, "Multiplying 2-Digit by 2-Digit", "Master 2-digit multiplication",
                          ["Use the standard algorithm for 2-digit multiplication",
                           "Example: 24 × 13 = 312",
                           "Multiply by ones first, then by tens",
                           "Add the partial products",
                           "Practice with different combinations"],
                          [{"title": "Example", "content": "24 × 13: 24×3=72, 24×10=240, 72+240=312"}],
                          "builtin", None, 1)
    
    # Long Division
    lesson_id = add_lesson(division_id, "Long Division with Remainders", "Divide larger numbers",
                          ["Use the standard long division algorithm",
                           "Divide, multiply, subtract, bring down",
                           "Example: 127 ÷ 4 = 31 R3",
                           "Practice with and without remainders",
                           "Check your work by multiplying"],
                          [{"title": "Example", "content": "127 ÷ 4: 4 goes into 12 three times (3), 4×3=12, 12-12=0, bring down 7, 4 goes into 7 one time (1), 4×1=4, 7-4=3, remainder 3"}],
                          "builtin", None, 1)
    
    # Fractions & Decimals
    lesson_id = add_lesson(fractions_id, "Equivalent Fractions", "Find fractions that are equal",
                          ["Equivalent fractions represent the same amount",
                           "Multiply or divide numerator and denominator by the same number",
                           "Example: 1/2 = 2/4 = 4/8",
                           "Use fraction strips to visualize",
                           "Practice finding equivalent fractions"],
                          [{"title": "Examples", "content": "1/3 = 2/6 = 3/9, 2/5 = 4/10 = 6/15"}],
                          "builtin", None, 1)
    
    lesson_id = add_lesson(fractions_id, "Adding and Subtracting Fractions", "Add and subtract fractions with like denominators",
                          ["When denominators are the same, add or subtract numerators",
                           "Keep the denominator the same",
                           "Example: 3/8 + 2/8 = 5/8",
                           "Simplify your answer if possible",
                           "Practice with different fractions"],
                          [{"title": "Examples", "content": "5/6 - 2/6 = 3/6 = 1/2, 4/7 + 1/7 = 5/7"}],
                          "builtin", None, 1)
    
    lesson_id = add_lesson(fractions_id, "Introduction to Decimals", "Understand decimal numbers",
                          ["Decimals are another way to write fractions",
                           "The decimal point separates whole numbers from parts",
                           "Example: 0.5 = 1/2, 0.25 = 1/4",
                           "Practice reading and writing decimals",
                           "Compare decimals using <, >, and ="],
                          [{"title": "Examples", "content": "0.3 = 3/10, 0.75 = 75/100 = 3/4, 2.5 = 2 and 5/10"}],
                          "builtin", None, 1)
    
    # Angles & Lines
    lesson_id = add_lesson(geometry_id, "Types of Angles", "Learn about different angles",
                          ["Right angle: exactly 90 degrees",
                           "Acute angle: less than 90 degrees",
                           "Obtuse angle: more than 90 degrees",
                           "Straight angle: exactly 180 degrees",
                           "Practice identifying angles"],
                          [{"title": "Examples", "content": "Corner of a book = right angle, tip of a slice of pizza = acute angle"}],
                          "builtin", None, 1)
    
    lesson_id = add_lesson(geometry_id, "Lines and Line Segments", "Understand different types of lines",
                          ["Line: goes on forever in both directions",
                           "Line segment: has two endpoints",
                           "Ray: has one endpoint and goes on forever",
                           "Parallel lines: never meet",
                           "Perpendicular lines: meet at right angles"],
                          [{"title": "Examples", "content": "Railroad tracks = parallel lines, corner of a room = perpendicular lines"}],
                          "builtin", None, 1)

def seed_grade5_math_lessons(fractions_id, decimals_id, geometry_id, algebra_id):
    """Seed Grade 5 math lessons."""
    
    # Fraction Operations
    lesson_id = add_lesson(fractions_id, "Multiplying Fractions", "Multiply fractions",
                          ["Multiply numerators together and denominators together",
                           "Example: 2/3 × 3/4 = 6/12 = 1/2",
                           "Simplify your answer",
                           "Practice with different fractions",
                           "Use visual models to understand"],
                          [{"title": "Examples", "content": "1/2 × 1/3 = 1/6, 3/4 × 2/5 = 6/20 = 3/10"}],
                          "builtin", None, 1)
    
    lesson_id = add_lesson(fractions_id, "Dividing Fractions", "Divide fractions",
                          ["To divide fractions, multiply by the reciprocal",
                           "Example: 2/3 ÷ 1/4 = 2/3 × 4/1 = 8/3",
                           "The reciprocal flips the numerator and denominator",
                           "Practice with different fractions",
                           "Check your work by multiplying"],
                          [{"title": "Examples", "content": "3/4 ÷ 1/2 = 3/4 × 2/1 = 6/4 = 3/2, 5/6 ÷ 2/3 = 5/6 × 3/2 = 15/12 = 5/4"}],
                          "builtin", None, 1)
    
    # Decimal Operations
    lesson_id = add_lesson(decimals_id, "Adding and Subtracting Decimals", "Work with decimal numbers",
                          ["Line up decimal points when adding or subtracting",
                           "Add zeros if needed to make numbers the same length",
                           "Example: 2.45 + 1.3 = 3.75",
                           "Practice with different decimal numbers",
                           "Check your work by estimating"],
                          [{"title": "Examples", "content": "3.67 + 2.14 = 5.81, 7.8 - 2.35 = 5.45"}],
                          "builtin", None, 1)
    
    lesson_id = add_lesson(decimals_id, "Multiplying Decimals", "Multiply decimal numbers",
                          ["Multiply as if there were no decimal points",
                           "Count decimal places in both numbers",
                           "Put the decimal point in the answer",
                           "Example: 2.3 × 1.4 = 3.22",
                           "Practice with different combinations"],
                          [{"title": "Example", "content": "2.3 × 1.4: 23 × 14 = 322, 1 decimal place + 1 decimal place = 2 decimal places, so 3.22"}],
                          "builtin", None, 1)
    
    # Area & Perimeter
    lesson_id = add_lesson(geometry_id, "Area of Rectangles", "Calculate area",
                          ["Area = length × width",
                           "Area is measured in square units",
                           "Example: rectangle 5 units by 3 units has area 15 square units",
                           "Practice with different rectangles",
                           "Use graph paper to visualize"],
                          [{"title": "Examples", "content": "Rectangle 4×6 has area 24 square units, Rectangle 7×2 has area 14 square units"}],
                          "builtin", None, 1)
    
    lesson_id = add_lesson(geometry_id, "Perimeter of Polygons", "Calculate perimeter",
                          ["Perimeter is the distance around a shape",
                           "Add up all the side lengths",
                           "Example: rectangle 5×3 has perimeter 5+3+5+3 = 16 units",
                           "Practice with different shapes",
                           "Use rulers to measure sides"],
                          [{"title": "Examples", "content": "Square with side 4: perimeter = 4+4+4+4 = 16, Triangle with sides 3,4,5: perimeter = 3+4+5 = 12"}],
                          "builtin", None, 1)
    
    # Introduction to Algebra
    lesson_id = add_lesson(algebra_id, "Variables and Expressions", "Use variables in math",
                          ["Variables are letters that represent unknown numbers",
                           "Example: x + 5 = 12, where x = 7",
                           "Practice solving simple equations",
                           "Use mental math and guess-and-check",
                           "Learn to write expressions with variables"],
                          [{"title": "Examples", "content": "If x + 3 = 8, then x = 5. If 2y = 10, then y = 5."}],
                          "builtin", None, 1)

def seed_grade6_math_lessons(ratios_id, percentages_id, geometry_id, statistics_id):
    """Seed Grade 6 math lessons."""
    
    # Ratios & Proportions
    lesson_id = add_lesson(ratios_id, "Understanding Ratios", "Work with ratios",
                          ["A ratio compares two quantities",
                           "Example: 3:4 means 3 to 4",
                           "Ratios can be written as fractions: 3/4",
                           "Practice with different ratios",
                           "Use ratios to compare quantities"],
                          [{"title": "Examples", "content": "2:3 = 2/3, 5:2 = 5/2, 1:4 = 1/4"}],
                          "builtin", None, 1)
    
    lesson_id = add_lesson(ratios_id, "Solving Proportions", "Solve proportion problems",
                          ["Proportions are two equal ratios",
                           "Use cross multiplication to solve",
                           "Example: 2/3 = x/12, so 2×12 = 3×x, 24 = 3x, x = 8",
                           "Practice with different proportions",
                           "Check your answer by substituting back"],
                          [{"title": "Example", "content": "3/4 = 9/x: 3x = 36, x = 12"}],
                          "builtin", None, 1)
    
    # Percentages
    lesson_id = add_lesson(percentages_id, "Understanding Percentages", "Work with percentages",
                          ["Percent means 'out of 100'",
                           "Example: 25% = 25/100 = 1/4 = 0.25",
                           "Convert between percents, fractions, and decimals",
                           "Practice with different percentages",
                           "Use percentages in real-world problems"],
                          [{"title": "Examples", "content": "50% = 1/2 = 0.5, 75% = 3/4 = 0.75, 20% = 1/5 = 0.2"}],
                          "builtin", None, 1)
    
    lesson_id = add_lesson(percentages_id, "Calculating Percentages", "Find percentages of numbers",
                          ["To find a percentage of a number, multiply",
                           "Example: 20% of 50 = 0.20 × 50 = 10",
                           "Practice with different numbers and percentages",
                           "Use mental math when possible",
                           "Apply to real-world situations"],
                          [{"title": "Examples", "content": "15% of 80 = 12, 25% of 120 = 30, 10% of 250 = 25"}],
                          "builtin", None, 1)
    
    # Volume & Surface Area
    lesson_id = add_lesson(geometry_id, "Volume of Rectangular Prisms", "Calculate volume",
                          ["Volume = length × width × height",
                           "Volume is measured in cubic units",
                           "Example: box 4×3×2 has volume 24 cubic units",
                           "Practice with different rectangular prisms",
                           "Use unit cubes to visualize"],
                          [{"title": "Examples", "content": "Box 5×4×3 has volume 60 cubic units, Box 2×6×2 has volume 24 cubic units"}],
                          "builtin", None, 1)
    
    lesson_id = add_lesson(geometry_id, "Surface Area", "Calculate surface area",
                          ["Surface area is the total area of all faces",
                           "For rectangular prism: 2(lw + lh + wh)",
                           "Example: box 4×3×2 has surface area 2(12+8+6) = 52 square units",
                           "Practice with different shapes",
                           "Use nets to visualize faces"],
                          [{"title": "Example", "content": "Box 3×2×4: faces are 3×2, 3×2, 2×4, 2×4, 3×4, 3×4 = 6+6+8+8+12+12 = 52"}],
                          "builtin", None, 1)
    
    # Statistics & Data
    lesson_id = add_lesson(statistics_id, "Mean, Median, and Mode", "Find measures of center",
                          ["Mean: add all numbers and divide by count",
                           "Median: middle number when arranged in order",
                           "Mode: number that appears most often",
                           "Practice with different data sets",
                           "Understand when to use each measure"],
                          [{"title": "Example", "content": "Data: 2, 3, 3, 5, 7. Mean = 20/5 = 4, Median = 3, Mode = 3"}],
                          "builtin", None, 1)
    
    lesson_id = add_lesson(statistics_id, "Creating and Reading Graphs", "Work with different types of graphs",
                          ["Bar graphs: compare categories",
                           "Line graphs: show changes over time",
                           "Circle graphs: show parts of a whole",
                           "Practice creating and reading graphs",
                           "Choose the right graph for your data"],
                          [{"title": "Examples", "content": "Use bar graph to compare test scores, line graph to show temperature over time"}],
                          "builtin", None, 1)

def seed_grade7_math_lessons(algebra_id, geometry_id, probability_id, ratios_id):
    """Seed Grade 7 math lessons."""
    
    # Pre-Algebra
    lesson_id = add_lesson(algebra_id, "Solving Equations", "Solve one-step and two-step equations",
                          ["Use inverse operations to solve equations",
                           "Example: x + 5 = 12, subtract 5 from both sides, x = 7",
                           "Example: 2x - 3 = 7, add 3 then divide by 2, x = 5",
                           "Practice with different equations",
                           "Check your answer by substituting back"],
                          [{"title": "Examples", "content": "3x = 15, x = 5. x - 4 = 8, x = 12. 2x + 1 = 9, x = 4."}],
                          "builtin", None, 1)
    
    lesson_id = add_lesson(algebra_id, "Inequalities", "Solve and graph inequalities",
                          ["Inequalities use <, >, ≤, ≥ instead of =",
                           "Solve inequalities the same way as equations",
                           "Graph solutions on a number line",
                           "Example: x > 3 means all numbers greater than 3",
                           "Practice with different inequalities"],
                          [{"title": "Examples", "content": "x < 5: all numbers less than 5, x ≥ -2: all numbers greater than or equal to -2"}],
                          "builtin", None, 1)
    
    # Geometry
    lesson_id = add_lesson(geometry_id, "Angles and Triangles", "Work with angles and triangles",
                          ["Sum of angles in a triangle = 180°",
                           "Types of triangles: equilateral, isosceles, scalene",
                           "Types of angles: acute, right, obtuse",
                           "Practice finding missing angles",
                           "Use angle relationships to solve problems"],
                          [{"title": "Examples", "content": "Triangle with angles 60°, 60°, 60° is equilateral. Triangle with angles 30°, 60°, 90° is right triangle."}],
                          "builtin", None, 1)
    
    lesson_id = add_lesson(geometry_id, "Circles", "Work with circles",
                          ["Radius: distance from center to edge",
                           "Diameter: distance across circle through center",
                           "Circumference: distance around circle",
                           "Area: space inside circle",
                           "Practice with circle formulas"],
                          [{"title": "Formulas", "content": "C = 2πr or C = πd, A = πr², d = 2r"}],
                          "builtin", None, 1)
    
    # Probability
    lesson_id = add_lesson(probability_id, "Basic Probability", "Understand probability",
                          ["Probability = favorable outcomes / total outcomes",
                           "Probability is between 0 and 1",
                           "0 = impossible, 1 = certain",
                           "Example: probability of rolling 3 on die = 1/6",
                           "Practice with different probability problems"],
                          [{"title": "Examples", "content": "P(rolling even number) = 3/6 = 1/2, P(drawing red card) = 26/52 = 1/2"}],
                          "builtin", None, 1)
    
    # Proportional Relationships
    lesson_id = add_lesson(ratios_id, "Proportional Relationships", "Work with proportional relationships",
                          ["Proportional relationships have constant ratio",
                           "Example: y = 2x means y is always 2 times x",
                           "Graph proportional relationships as straight lines",
                           "Practice with different relationships",
                           "Use tables, graphs, and equations"],
                          [{"title": "Example", "content": "If y = 3x, then when x = 1, y = 3; when x = 2, y = 6; when x = 3, y = 9"}],
                          "builtin", None, 1)

def seed_grade8_math_lessons(algebra_id, geometry_id, functions_id, systems_id):
    """Seed Grade 8 math lessons."""
    
    # Algebra I
    lesson_id = add_lesson(algebra_id, "Linear Equations", "Work with linear equations",
                          ["Linear equations graph as straight lines",
                           "Standard form: Ax + By = C",
                           "Slope-intercept form: y = mx + b",
                           "Practice graphing and solving",
                           "Understand slope and y-intercept"],
                          [{"title": "Examples", "content": "y = 2x + 3 has slope 2 and y-intercept 3, 3x + 2y = 6 is in standard form"}],
                          "builtin", None, 1)
    
    lesson_id = add_lesson(algebra_id, "Factoring", "Factor quadratic expressions",
                          ["Factoring means writing as product of factors",
                           "Example: x² + 5x + 6 = (x + 2)(x + 3)",
                           "Practice with different quadratics",
                           "Use FOIL to check your work",
                           "Look for common factors first"],
                          [{"title": "Examples", "content": "x² - 4 = (x + 2)(x - 2), x² + 7x + 12 = (x + 3)(x + 4)"}],
                          "builtin", None, 1)
    
    # Advanced Geometry
    lesson_id = add_lesson(geometry_id, "Transformations", "Understand geometric transformations",
                          ["Translation: slide a shape",
                           "Rotation: turn a shape around a point",
                           "Reflection: flip a shape over a line",
                           "Dilation: make a shape bigger or smaller",
                           "Practice with different transformations"],
                          [{"title": "Examples", "content": "Translate triangle 3 units right, rotate square 90° clockwise, reflect over y-axis"}],
                          "builtin", None, 1)
    
    lesson_id = add_lesson(geometry_id, "Congruence and Similarity", "Understand congruent and similar shapes",
                          ["Congruent: same shape and size",
                           "Similar: same shape, different size",
                           "Use transformations to show congruence",
                           "Practice with different shapes",
                           "Understand scale factors"],
                          [{"title": "Examples", "content": "Two triangles are congruent if all sides and angles match, similar if angles match and sides are proportional"}],
                          "builtin", None, 1)
    
    # Functions
    lesson_id = add_lesson(functions_id, "Linear Functions", "Work with linear functions",
                          ["Function: each input has exactly one output",
                           "Linear function: y = mx + b",
                           "Domain: all possible input values",
                           "Range: all possible output values",
                           "Practice with different functions"],
                          [{"title": "Examples", "content": "f(x) = 2x + 1, g(x) = -3x + 5, h(x) = x/2 - 2"}],
                          "builtin", None, 1)
    
    # Systems of Equations
    lesson_id = add_lesson(systems_id, "Solving Systems by Graphing", "Solve systems of equations",
                          ["System of equations: two or more equations",
                           "Solution: point where lines intersect",
                           "Graph both equations on same coordinate plane",
                           "Find intersection point",
                           "Practice with different systems"],
                          [{"title": "Example", "content": "y = 2x + 1 and y = -x + 4 intersect at (1, 3), so x = 1, y = 3"}],
                          "builtin", None, 1)
    
    lesson_id = add_lesson(systems_id, "Solving Systems by Substitution", "Use substitution method",
                          ["Solve one equation for one variable",
                           "Substitute into other equation",
                           "Solve for remaining variable",
                           "Substitute back to find other variable",
                           "Check your solution in both equations"],
                          [{"title": "Example", "content": "x + y = 5, x - y = 1. From first: x = 5 - y. Substitute: (5 - y) - y = 1, 5 - 2y = 1, y = 2, x = 3"}],
                          "builtin", None, 1)

def seed_advanced_math_lessons(calculus_id, trigonometry_id, statistics_id, discrete_math_id):
    """Seed advanced math lessons."""
    
    # Calculus
    lesson_id = add_lesson(calculus_id, "Introduction to Limits", "Understand the concept of limits",
                          ["Limit: what a function approaches as input approaches a value",
                           "Example: lim(x→2) x² = 4",
                           "Practice with different functions",
                           "Understand one-sided and two-sided limits",
                           "Use limit laws to evaluate limits"],
                          [{"title": "Examples", "content": "lim(x→0) sin(x)/x = 1, lim(x→∞) 1/x = 0"}],
                          "builtin", None, 1)
    
    lesson_id = add_lesson(calculus_id, "Derivatives", "Understand derivatives",
                          ["Derivative: rate of change of a function",
                           "Power rule: d/dx(xⁿ) = nxⁿ⁻¹",
                           "Practice with different functions",
                           "Understand applications of derivatives",
                           "Use derivatives to find slopes and rates"],
                          [{"title": "Examples", "content": "d/dx(x³) = 3x², d/dx(2x² + 3x + 1) = 4x + 3"}],
                          "builtin", None, 1)
    
    # Trigonometry
    lesson_id = add_lesson(trigonometry_id, "Right Triangle Trigonometry", "Work with sine, cosine, and tangent",
                          ["SOH CAH TOA: sin = opp/hyp, cos = adj/hyp, tan = opp/adj",
                           "Practice with different triangles",
                           "Use trigonometric ratios to find missing sides",
                           "Understand inverse trigonometric functions",
                           "Apply to real-world problems"],
                          [{"title": "Examples", "content": "In 30-60-90 triangle, sin(30°) = 1/2, cos(30°) = √3/2, tan(30°) = 1/√3"}],
                          "builtin", None, 1)
    
    # Advanced Statistics
    lesson_id = add_lesson(statistics_id, "Normal Distribution", "Understand normal distribution",
                          ["Normal distribution: bell-shaped curve",
                           "Mean, median, and mode are all equal",
                           "68-95-99.7 rule: percentages within standard deviations",
                           "Practice with different normal distributions",
                           "Use z-scores to find probabilities"],
                          [{"title": "Examples", "content": "68% of data within 1 standard deviation, 95% within 2, 99.7% within 3"}],
                          "builtin", None, 1)
    
    # Discrete Mathematics
    lesson_id = add_lesson(discrete_math_id, "Logic and Proofs", "Understand logical reasoning",
                          ["Proposition: statement that is true or false",
                           "Logical operators: AND, OR, NOT",
                           "Truth tables: show all possible combinations",
                           "Practice with different logical statements",
                           "Understand logical equivalence"],
                          [{"title": "Examples", "content": "p AND q is true only when both p and q are true, p OR q is true when at least one is true"}],
                          "builtin", None, 1)

if __name__ == "__main__":
    seed_massive_math_curriculum()
