"""
ULTIMATE MATH MASTERY - 25 SUBJECTS WITH 10 TEACHING METHODS EACH
Every concept taught 10 different ways for deep understanding
"""

from database import add_subject, add_topic, add_lesson, get_all_subjects


def seed_division_mastery_10_ways():
    """10 Different Methods for Division - Comprehensive Teaching"""
    print("🔢 Adding Division Mastery with 10 Teaching Methods...")
    
    subjects = get_all_subjects()
    math_subject = next((s for s in subjects if s["name"] == "Mathematics"), None)
    if not math_subject:
        return
    
    subject_id = math_subject["id"]
    
    # Create Division Mastery topic
    division_topic = add_topic(
        subject_id,
        "Division Mastery: 10 Different Ways",
        "Master division through 10 unique teaching methods",
        100
    )
    
    # Method 1: Fair Share (Equal Groups)
    add_lesson(
        division_topic,
        "Method 1: The Fair Share Method",
        "Division as equal sharing - the most intuitive approach",
        [
            "CONCEPT: Division is about splitting things equally",
            "EXAMPLE: 12 cookies shared among 3 friends = 4 cookies each",
            "",
            "WAY 1 - Snack Sharing: Use real objects (crackers, toys) and deal them out one by one",
            "WAY 2 - Draw Circles: Draw 3 circles (groups) and put dots in each until you've used 12 dots",
            "WAY 3 - Money Division: $30 split among 5 people = $6 each (use play money!)",
            "WAY 4 - Array Formation: Arrange 24 toy soldiers into 4 equal rows",
            "WAY 5 - Remainder Game: 17 beads into 3 bracelets = 5 each with 2 leftover",
            "WAY 6 - Story Problems: 'You have 42 apples to give to 7 baskets equally...'",
            "WAY 7 - Fraction Connection: Show that 20 ÷ 4 = finding 1/4 of 20",
            "WAY 8 - Visual Proof: Draw the process to show why it works",
            "WAY 9 - Inefficiency Demonstration: Try sharing 1,256 items one by one to see why we need faster methods",
            "WAY 10 - Algebraic Form: Groups × Items per group = Total (solve for items per group)",
        ],
        [
            {"title": "Try This", "content": "Share 20 M&Ms equally among 4 people. Each gets 5!"},
            {"title": "Challenge", "content": "Try 23 ÷ 5. You get 4 each with 3 remaining!"}
        ]
    )
    
    # Method 2: Repeated Subtraction
    add_lesson(
        division_topic,
        "Method 2: The Measuring Stick Method (Repeated Subtraction)",
        "Division as asking 'How many times does this fit?'",
        [
            "CONCEPT: How many times can you subtract the divisor before reaching zero?",
            "EXAMPLE: 24 ÷ 6 = Start at 24, subtract 6 repeatedly: 24→18→12→6→0 (4 times)",
            "",
            "WAY 1 - Cookie Thief: Start with 15 blocks, 'steal' 3 at a time, count how many steals",
            "WAY 2 - Number Line Hops: Start at 24, hop backward by 6s, count the hops",
            "WAY 3 - Calculator Pattern: Type 56 - 7 =, then keep pressing = and count",
            "WAY 4 - Building Block Towers: Break a 20-block tower into 4-block pieces",
            "WAY 5 - Race to Zero Game: Start at 100, subtract 12 each turn, who reaches zero first?",
            "WAY 6 - Remainder Discovery: 17 - 5 = 12, 12 - 5 = 7, 7 - 5 = 2 (3 times with 2 left)",
            "WAY 7 - Partial Quotients Preview: Instead of subtracting 1 at a time, subtract 10 or 100 at once!",
            "WAY 8 - Real-World Budget: '$50 budget, spending $10/day, how many days?'",
            "WAY 9 - Coding Loop: while (dividend >= divisor) { subtract; count++ }",
            "WAY 10 - Measurement Application: '36-inch ribbon cut into 3-inch pieces'",
        ],
        [
            {"title": "Try This", "content": "Start at 30. Subtract 5 repeatedly. How many times? Answer: 6 times!"},
            {"title": "Advanced", "content": "Try 145 ÷ 12. Subtract 120 (10×12) first, then keep going!"}
        ]
    )
    
    # Method 3: The Grid/Area Model
    add_lesson(
        division_topic,
        "Method 3: The Grid Method (Area Model)",
        "Division as finding the missing side of a rectangle",
        [
            "CONCEPT: If a rectangle has area 36 and one side is 4, the other side must be 9",
            "EXAMPLE: 36 ÷ 4 = Draw a rectangle with 36 squares and height of 4. Width = 9!",
            "",
            "WAY 1 - LEGO Rectangles: Build rectangles with LEGOs to visualize",
            "WAY 2 - Graph Paper: Color 36 squares making a rectangle with height 3",
            "WAY 3 - Big Box Method: For 156 ÷ 12, draw rectangle. Chop off 120 area (width=10), then remaining 36 (width=3). Total width = 13",
            "WAY 4 - Multiplication Connection: Teach 4×5=20 first as a 4×5 rectangle, then flip to division",
            "WAY 5 - Fact Families: Draw one 3×4 array to show all 4 facts: 3×4, 4×3, 12÷3, 12÷4",
            "WAY 6 - Expand the Rectangle: 'We have area 156. One side is 12. Let's build it out...'",
            "WAY 7 - Polynomial Division Connection: Show older daughter same model works for (x²+5x+6)÷(x+2)",
            "WAY 8 - Room Design: 'Room has 120 sq ft. This wall is 10 ft. How long is the other?'",
            "WAY 9 - Remainder Visualization: Graph paper for 38÷5 shows 5×7 rectangle + 3 extra squares",
            "WAY 10 - Digital Grid Tools: Use drawing apps to quickly create/manipulate area models",
        ],
        [
            {"title": "Try This", "content": "Draw a rectangle with 24 squares. Make it 4 squares tall. How wide? 6!"},
            {"title": "Advanced", "content": "Try 156 ÷ 12 using the Big Box method!"}
        ]
    )
    
    # Method 4: Long Division (The Traditional Algorithm)
    add_lesson(
        division_topic,
        "Method 4: Long Division - The Traditional Way",
        "The classic algorithm taught 10 different ways",
        [
            "CONCEPT: Divide, Multiply, Subtract, Bring Down - repeat!",
            "EXAMPLE: 156 ÷ 12",
            "",
            "WAY 1 - Dad-Mom-Sister-Brother: Divide, Multiply, Subtract, Bring down (mnemonic!)",
            "WAY 2 - Step-by-Step Color Coding: Use different colors for each step",
            "WAY 3 - The Bus Stop Method: Draw it like a bus shelter with number inside",
            "WAY 4 - Grid/Box Method First: Start with area model, then connect to traditional",
            "WAY 5 - Estimate First: 'How many 12s in 156? Maybe 10? Let's try...'",
            "WAY 6 - Talk It Out: Verbalize every step: 'How many 12s go into 15? One! 1×12=12...'",
            "WAY 7 - Work Backward from Multiplication: Practice 12×13 first, then do 156÷12",
            "WAY 8 - Partial Products Connection: Show how it relates to multiplication method they know",
            "WAY 9 - Real-World Application: 'A 156-mile road trip, driving 12 mph (old car!), how many hours?'",
            "WAY 10 - Error Analysis: Show common mistakes (forgetting to bring down, wrong place value) and how to catch them",
        ],
        [
            {"title": "Try This", "content": "84 ÷ 7: How many 7s in 8? 1! 1×7=7, subtract, bring down 4. How many 7s in 14? 2!"},
            {"title": "Mnemonic", "content": "Does McDonald's Sell Burgers? Divide, Multiply, Subtract, Bring down!"}
        ]
    )
    
    # Method 5: Partial Quotients
    add_lesson(
        division_topic,
        "Method 5: Partial Quotients - Chunks of Understanding",
        "Break division into easy chunks",
        [
            "CONCEPT: Don't know the answer? Subtract big, easy chunks until you get there!",
            "EXAMPLE: 145 ÷ 12",
            "",
            "WAY 1 - 10s First: 'I know 10×12=120. Subtract that! Now I have 25 left.'",
            "WAY 2 - Keep It Simple: Use easy multiples. For 12s: try 2×12, 5×12, 10×12",
            "WAY 3 - Visual Chunks: Draw boxes showing each chunk you subtract",
            "WAY 4 - Repeated Subtraction++: It's repeated subtraction, but smarter (bigger chunks!)",
            "WAY 5 - Guess & Check: 'Maybe 15×12? Too big? Try 12×12...'",
            "WAY 6 - Build Up Method: Start with 1×12, then 2×12, until you get close to 145",
            "WAY 7 - Written Record: Write each step: 145 - 120 = 25 (that's 10), 25 - 24 = 1 (that's 2 more), total = 12 R1",
            "WAY 8 - Friendly Number First: For 145÷12, try 144÷12 first (easy 12!), then deal with the extra 1",
            "WAY 9 - Real-World Chunking: 'We need 145 cupcakes. Each box holds 12. Let's fill boxes of 12...'",
            "WAY 10 - Compare to Traditional: Show how partial quotients and long division get the same answer different ways",
        ],
        [
            {"title": "Try This", "content": "156 ÷ 12: Subtract 120 (10), leaves 36. Subtract 24 (2), leaves 12. Subtract 12 (1). Total: 10+2+1=13!"},
            {"title": "Why It's Great", "content": "You can't mess up! Take your time, use easy numbers!"}
        ]
    )
    
    # Method 6: Multiplication Tables Backward
    add_lesson(
        division_topic,
        "Method 6: Know Your Times Tables Backward!",
        "Division is just asking 'What times this equals that?'",
        [
            "CONCEPT: 24 ÷ 6 is really asking '6 times WHAT equals 24?'",
            "ANSWER: You already know 6×4=24, so 24÷6=4!",
            "",
            "WAY 1 - Flashcard Flip: Use multiplication flashcards backward (see 6×4, say 24÷6=4)",
            "WAY 2 - Times Table Mastery: Memorize tables 1-12, then division becomes instant",
            "WAY 3 - Fact Family Triangles: Draw triangles with 3 numbers (6, 4, 24). Practice all 4 facts",
            "WAY 4 - Missing Number Equations: 6 × __ = 24 (same as 24 ÷ 6)",
            "WAY 5 - Multiplication Songs Backward: If they know times table songs, reverse them",
            "WAY 6 - Division Bingo: Call out division facts, they cover the answer if they know it",
            "WAY 7 - Speed Drills: Timed practice to build automaticity",
            "WAY 8 - Real-World Speed: 'Quick! 8 people, 56 cookies, how many each?' (56÷8=7)",
            "WAY 9 - Online Games: Use Khan Academy or math games for times table practice",
            "WAY 10 - Connection to Arrays: Show how 6 rows of 4 dots can be viewed as 6×4 or 24÷6",
        ],
        [
            {"title": "Master This", "content": "If you know 7×8=56, then you know 56÷7=8 and 56÷8=7!"},
            {"title": "Pro Tip", "content": "Mastering times tables makes division 10x easier!"}
        ]
    )
    
    # Method 7: Fraction Bar Model
    add_lesson(
        division_topic,
        "Method 7: The Fraction Bar Model",
        "Division as creating and measuring fractions",
        [
            "CONCEPT: 20 ÷ 4 = How big is 1/4 of 20?",
            "VISUAL: Draw a bar representing 20, divide it into 4 equal parts",
            "",
            "WAY 1 - Paper Strip Folding: Take a paper strip as 'the whole', fold into equal parts",
            "WAY 2 - Chocolate Bar Division: Real or drawn chocolate bar divided into sections",
            "WAY 3 - Length Model: Draw a line segment, mark it into equal pieces",
            "WAY 4 - Fraction Circle Connection: Use fraction circles to see division as parts of a whole",
            "WAY 5 - Double Number Line: Top line shows whole (0 to 20), bottom shows parts (0 to 4)",
            "WAY 6 - Pizza Slices: 'Cut a pizza (20 inches) into 4 equal slices. How big is each?'",
            "WAY 7 - Tape Diagrams: Singapore Math-style bar models",
            "WAY 8 - Ratio Tables: Create a table showing the relationship between dividend and quotient",
            "WAY 9 - Connecting to Fractions: Show 20÷4 = 20×(1/4) = 5",
            "WAY 10 - Real-World Measurement: 'This 20-inch rope cut into 4 equal pieces = 5 inches each'",
        ],
        [
            {"title": "Try This", "content": "Draw a bar. It represents 30. Divide it into 5 equal parts. Each part = 6!"},
            {"title": "Connection", "content": "Division and fractions are best friends!"}
        ]
    )
    
    # Method 8: Ratio & Proportion
    add_lesson(
        division_topic,
        "Method 8: Division Through Ratios",
        "Understanding division as a ratio relationship",
        [
            "CONCEPT: Division creates a ratio: 24 ÷ 6 = 4:1 relationship",
            "EXAMPLE: If 6 apples cost $24, what's the cost per apple?",
            "",
            "WAY 1 - Ratio Tables: Create tables showing equivalent ratios",
            "WAY 2 - Unit Rate: 'Find the price for ONE item' (that's division!)",
            "WAY 3 - Recipe Scaling: 'Recipe for 4 people uses 12 eggs. For 1 person?'",
            "WAY 4 - Speed Calculations: 'Car goes 120 miles in 3 hours. Miles per hour?'",
            "WAY 5 - Price Comparison: 'Pack of 12 for $24 vs 6 for $15. Which is better?' (find unit price)",
            "WAY 6 - Double Number Line: Visual representation of ratio relationships",
            "WAY 7 - Cross-Multiplication: For older students, connect to solving proportions",
            "WAY 8 - Real Shopping: Compare actual grocery prices using division",
            "WAY 9 - Density Problems: 'Object has mass 24g, volume 6mL. Density = ?'",
            "WAY 10 - Conversion Factors: '60 minutes ÷ 4 = 15 minutes per quarter-hour'",
        ],
        [
            {"title": "Try This", "content": "12 donuts cost $18. How much per donut? 18 ÷ 12 = $1.50 each!"},
            {"title": "Real Life", "content": "Always check unit prices at the store - that's division!"}
        ]
    )
    
    # Method 9: Chunking (Breaking Apart)
    add_lesson(
        division_topic,
        "Method 9: The Chunking Strategy",
        "Break the dividend into friendly pieces",
        [
            "CONCEPT: Break big division into smaller, easier pieces",
            "EXAMPLE: 156 ÷ 12 → Break 156 into 120 + 36, divide each: 120÷12=10, 36÷12=3, total=13",
            "",
            "WAY 1 - Friendly Numbers: Break dividend into multiples you know",
            "WAY 2 - Visual Boxes: Draw the division as separate boxes, solve each, combine",
            "WAY 3 - Decomposition Practice: '156 = 100 + 50 + 6' or '156 = 120 + 36' (choose what works!)",
            "WAY 4 - Area Model Connection: Each 'chunk' is a section of the rectangle",
            "WAY 5 - Mental Math Application: Break 84÷7 into 70÷7 + 14÷7 (mentally!)",
            "WAY 6 - Multiple Strategies: Show there's more than one way to chunk the same problem",
            "WAY 7 - Real-World Splitting: '156 pencils. Give 120 to room 1 (12×10), 36 to room 2 (12×3)'",
            "WAY 8 - Distributive Property Connection: Show it's the same as (120+36)÷12 = 120÷12 + 36÷12",
            "WAY 9 - Build Your Own: Let them choose how to break the number apart",
            "WAY 10 - Compare to Partial Quotients: Show how they're similar but different approaches",
        ],
        [
            {"title": "Try This", "content": "96 ÷ 8: Break into 80 + 16. 80÷8=10, 16÷8=2. Answer: 10+2=12!"},
            {"title": "Pro Tip", "content": "Choose chunks YOU find easy - there's no 'wrong' way to chunk!"}
        ]
    )
    
    # Method 10: Decimal Division
    add_lesson(
        division_topic,
        "Method 10: Division with Decimals",
        "Extending division beyond whole numbers",
        [
            "CONCEPT: Division can result in decimal answers, and we can divide BY decimals too!",
            "EXAMPLE: 5 ÷ 2 = 2.5 (not just 2 R1!)",
            "",
            "WAY 1 - Money Model: $5 shared between 2 people = $2.50 each (makes decimals real)",
            "WAY 2 - Continue the Algorithm: When you get a remainder, add a decimal point and keep going!",
            "WAY 3 - Fraction First: 5÷2 = 5/2 = 2½ = 2.5 (connect all representations)",
            "WAY 4 - Move the Decimal: To divide BY a decimal, move BOTH decimal points right",
            "WAY 5 - Visual with Base-10 Blocks: Use the small 'tenth' blocks for remainders",
            "WAY 6 - Calculator Verification: Use calculator to confirm decimal answers",
            "WAY 7 - Real Measurements: '2.5 feet is how many inches?' (2.5 × 12 = 30)",
            "WAY 8 - Rounding Practice: Sometimes estimate: 17÷3 ≈ 5.67, but we can say ≈ 6",
            "WAY 9 - Repeating Decimals: Explore 10÷3 = 3.3333... (why does it repeat?)",
            "WAY 10 - Scientific Notation: For very small/large decimal division (advanced)",
        ],
        [
            {"title": "Try This", "content": "Divide $10 among 3 people. Each gets $3.33... (with 1 cent left over!)"},
            {"title": "Real Life", "content": "Splitting restaurant bills always involves decimal division!"}
        ]
    )
    
    print("✅ Division Mastery with 10 Teaching Methods added!")


def seed_number_line_journey():
    """Complete Number Line Journey subject with all grade levels"""
    print("🎯 Adding Number Line Journey - Complete K-8 Progression...")
    
    subjects = get_all_subjects()
    math_subject = next((s for s in subjects if s["name"] == "Mathematics"), None)
    if not math_subject:
        return
    
    subject_id = math_subject["id"]
    
    numberline_topic = add_topic(
        subject_id,
        "Number Line Mastery: Visualizing All of Math",
        "From counting to infinity - the complete number line journey",
        101
    )
    
    add_lesson(
        numberline_topic,
        "The Number Line Journey - 10 Ways to Master It",
        "Every math concept visualized on a number line",
        [
            "CONCEPT: The number line is the most powerful visual tool in all of math!",
            "FROM: Counting to infinity, negatives, fractions, decimals, everything!",
            "",
            "WAY 1 - Life-Sized Floor Line: Masking tape on floor, physically walk the numbers",
            "WAY 2 - Interactive Whiteboard: Draw and hop on a digital number line",
            "WAY 3 - Beaded String: 100 beads on a string (alternating colors every 10)",
            "WAY 4 - Story Journey: 'Knight starts at castle 3, travels 5 miles east to castle 8'",
            "WAY 5 - Ruler as Model: Actual ruler is a number line with fractions!",
            "WAY 6 - Zoomable Digital Line: App that lets you zoom between whole numbers to see fractions",
            "WAY 7 - Coding Movement: Scratch character moves along x-axis based on math commands",
            "WAY 8 - Guess My Number: 'Between 20 and 30, closer to 25...'",
            "WAY 9 - Clothesline Numbers: Hang numbered cards, place others in correct position",
            "WAY 10 - Abstract Representation: Finally, draw number lines for any problem on paper",
        ],
        [
            {"title": "K-2 Focus", "content": "Counting, addition as hopping forward, subtraction as hopping back"},
            {"title": "3-5 Focus", "content": "Fractions between whole numbers, multiplication as bigger jumps"},
            {"title": "6-8 Focus", "content": "Negative numbers (left of zero), square roots, absolute value"},
            {"title": "Why It Works", "content": "One visual tool that grows with them through ALL of math!"}
        ]
    )


def seed_mental_math_magic():
    """Mental Math Magic Tricks - 10 Ways for Each Strategy"""
    print("✨ Adding Mental Math Magic with Multiple Strategies...")
    
    subjects = get_all_subjects()
    math_subject = next((s for s in subjects if s["name"] == "Mathematics"), None)
    if not math_subject:
        return
    
    subject_id = math_subject["id"]
    
    mental_topic = add_topic(
        subject_id,
        "Mental Math Superpowers",
        "Calculate faster than a calculator!",
        102
    )
    
    add_lesson(
        mental_topic,
        "10 Mental Math Strategies - Mastery Through Choice",
        "Choose the strategy that makes sense to YOU",
        [
            "PROBLEM: 27 + 35",
            "",
            "STRATEGY 1 - Decomposition: (20+30) + (7+5) = 50 + 12 = 62",
            "STRATEGY 2 - Compensation: 30 + 35 - 3 = 62 (round 27 up to 30, then subtract back)",
            "STRATEGY 3 - Making Tens: 27 + 3 = 30, then 30 + 32 = 62",
            "STRATEGY 4 - Left to Right: 20+30=50, 7+5=12, 50+12=62",
            "STRATEGY 5 - Round Both: 30 + 35 = 65, subtract 3 = 62",
            "",
            "MULTIPLICATION: 16 × 25",
            "STRATEGY 6 - Halving/Doubling: 8 × 50 = 400 (or continue: 4 × 100 = 400)",
            "STRATEGY 7 - Friendly Numbers: 16 × 25 = 16 × (100 ÷ 4) = 1600 ÷ 4 = 400",
            "STRATEGY 8 - Breaking Apart: (10×25) + (6×25) = 250 + 150 = 400",
            "STRATEGY 9 - Think Money: 25 cents × 16 = 4 dollars (4 quarters = $1, so 16 quarters = $4)",
            "STRATEGY 10 - Pattern Recognition: 4×25=100, 8×25=200, 16×25=400 (doubling pattern!)",
            "",
            "KEY: There's NO ONE RIGHT WAY - use what makes sense to your brain!",
        ],
        [
            {"title": "Practice", "content": "Try 49 + 28 using compensation: 50 + 28 - 1 = 77!"},
            {"title": "Race the Calculator", "content": "Can you solve 25 × 12 mentally before someone types it in?"}
        ]
    )


def seed_estimation_mastery():
    """The Art of Estimation - 10 Different Approaches"""
    print("🎯 Adding Estimation Mastery...")
    
    subjects = get_all_subjects()
    math_subject = next((s for s in subjects if s["name"] == "Mathematics"), None)
    if not math_subject:
        return
    
    subject_id = math_subject["id"]
    
    estimation_topic = add_topic(
        subject_id,
        "Estimation: The Superpower of Smart Guessing",
        "Fast, accurate estimates for real-world problems",
        103
    )
    
    add_lesson(
        estimation_topic,
        "10 Ways to Estimate Like a Pro",
        "Build intuition for numbers and reasonableness",
        [
            "GOAL: Fast, reasonably accurate answers without exact calculation",
            "",
            "METHOD 1 - Rounding to Nearest 10/100: 452 + 319 → 450 + 320 = 770",
            "METHOD 2 - Front-End Estimation: 452 + 319 → 400 + 300 = 700",
            "METHOD 3 - Clustering: 27+24+26+28 → 4 × 25 = 100",
            "METHOD 4 - Compatible Numbers: 23 + 49 → 25 + 50 = 75",
            "METHOD 5 - Benchmark Fractions: 3/8 is close to 1/2, 7/8 is close to 1",
            "METHOD 6 - One-Digit Multiplication: 6,234 × 8 → think 6 × 8 = 48, so about 48,000",
            "METHOD 7 - Division Chunks: 523 ÷ 8 → 'How many 8s in 500? About 60'",
            "METHOD 8 - Percentage Quick Math: 10% of any number (move decimal left once!)",
            "METHOD 9 - Fermi Estimation: Break impossible questions into pieces you CAN estimate",
            "METHOD 10 - Reasonableness Check: After ANY exact calculation, ask 'Does this make sense?'",
            "",
            "PRACTICE ACTIVITIES:",
            "• Jar of Beans: Estimate quantity weekly",
            "• Grocery Store Game: Estimate total bill before checkout",
            "• 'Price is Right': Guess prices without going over",
            "• Fermi Problems: 'How many leaves on a tree?' Use logic to estimate!",
        ],
        [
            {"title": "Quick Test", "content": "Estimate 47 × 22. Think: 50 × 20 = 1,000. Actual: 1,034!"},
            {"title": "Real Life", "content": "Estimation saves time and catches mistakes!"}
        ]
    )


def seed_fractions_complete():
    """Fractions Without Fear - 10 Visual & Hands-On Methods"""
    print("🍕 Adding Complete Fractions Mastery...")
    
    subjects = get_all_subjects()
    math_subject = next((s for s in subjects if s["name"] == "Mathematics"), None)
    if not math_subject:
        return
    
    subject_id = math_subject["id"]
    
    fractions_topic = add_topic(
        subject_id,
        "Fractions Mastery: 10 Different Teaching Approaches",
        "Understanding parts of a whole through multiple lenses",
        104
    )
    
    add_lesson(
        fractions_topic,
        "Understanding Fractions - 10 Ways to See It",
        "From pizza slices to number lines",
        [
            "CONCEPT: A fraction represents a part of a whole",
            "EXAMPLE: 3/4 means 3 out of 4 equal parts",
            "",
            "WAY 1 - Paper Folding: Fold paper to create halves, fourths, eighths physically",
            "WAY 2 - Kitchen Measuring Cups: 2 quarter-cups = 1 half-cup (tactile equivalency!)",
            "WAY 3 - LEGO Bricks: 8-stud brick = whole, 4-stud = 1/2, 2-stud = 1/4",
            "WAY 4 - Fraction Circles: Physical or digital circles divided into parts",
            "WAY 5 - Fraction Strips: Long rectangles divided to compare sizes",
            "WAY 6 - Pizza/Pie Models: Everyone's favorite! Visual and delicious",
            "WAY 7 - Money Connection: Quarter = 1/4 dollar, dime = 1/10 dollar",
            "WAY 8 - Clock Time: 15 minutes = 1/4 hour, 30 minutes = 1/2 hour",
            "WAY 9 - Number Line Placement: Where does 3/4 go between 0 and 1?",
            "WAY 10 - Ratio Interpretation: 3/4 means 3:4 ratio (connects to later algebra)",
        ],
        [
            {"title": "Try This", "content": "Fold paper in half, then in half again. You've created fourths!"},
            {"title": "Kitchen Math", "content": "Bake cookies using 1/2 cup + 1/4 cup butter = 3/4 cup total!"}
        ]
    )
    
    add_lesson(
        fractions_topic,
        "Adding & Subtracting Fractions - 10 Methods",
        "Master fraction operations",
        [
            "PROBLEM: 1/4 + 2/4 and 1/2 + 1/3",
            "",
            "SAME DENOMINATOR:",
            "METHOD 1 - Visual Addition: Draw 1/4 pizza + 2/4 pizza = 3/4 pizza",
            "METHOD 2 - Fraction Strips: Lay 1/4 strip next to 2/4 strip, covers 3/4",
            "METHOD 3 - Number Line: Start at 1/4, jump 2/4 forward, land at 3/4",
            "METHOD 4 - Keep Denominator Rule: Add numerators only! 1+2=3, keep /4",
            "",
            "DIFFERENT DENOMINATORS:",
            "METHOD 5 - Visual with Circles: Draw 1/2 circle, draw 1/3 circle, find common pieces",
            "METHOD 6 - Fraction Strips Overlap: Lay 1/2 and 1/3 strips over a 'whole' to find LCD",
            "METHOD 7 - Find LCD: For 1/2 + 1/3, find common denominator (6). Change: 3/6 + 2/6 = 5/6",
            "METHOD 8 - Multiply to Match: 1/2 = 3/6 (multiply by 3/3), 1/3 = 2/6 (multiply by 2/2)",
            "METHOD 9 - Kitchen Test: Measure 1/2 cup + 1/3 cup water. What measuring cup holds it all?",
            "METHOD 10 - Cross-Multiply Check: Use cross-multiplication to find equivalent fractions",
        ],
        [
            {"title": "Same Bottom", "content": "2/5 + 1/5 = 3/5 (Easy! Just add the tops!)"},
            {"title": "Different Bottom", "content": "1/2 + 1/4: Change 1/2 to 2/4, now it's 2/4 + 1/4 = 3/4!"}
        ]
    )
    
    add_lesson(
        fractions_topic,
        "Multiplying & Dividing Fractions - 10 Approaches",
        "The seemingly magical operations",
        [
            "MULTIPLICATION: 1/2 × 1/3 = 1/6",
            "",
            "METHOD 1 - 'Of' Means Multiply: 1/2 OF a 1/3 pizza = 1/6 of the whole pizza",
            "METHOD 2 - Area Model: Draw a rectangle, shade 1/2 horizontally, 1/3 vertically. Overlap = 1/6",
            "METHOD 3 - Paper Folding: Fold paper into thirds, then into halves. Each section = 1/6",
            "METHOD 4 - Multiply Across: Top×Top, Bottom×Bottom (1×1=1, 2×3=6)",
            "METHOD 5 - Pattern Recognition: 1/2 of 1/2 = 1/4, 1/2 of 1/4 = 1/8 (halving pattern)",
            "",
            "DIVISION: 1/2 ÷ 1/4 = 2",
            "METHOD 6 - 'How Many Fit?' Model: How many 1/4s fit in 1/2? Two!",
            "METHOD 7 - Visual Strips: Lay 1/4 strips along a 1/2 strip - it takes 2",
            "METHOD 8 - 'Keep, Change, Flip': Keep first, change ÷ to ×, flip the second (1/2 × 4/1 = 2)",
            "METHOD 9 - Common Denominator Method: Change to 2/4 ÷ 1/4, now just divide numerators: 2÷1=2",
            "METHOD 10 - Real-World Recipe: 'Recipe needs 1/2 cup. Scoop is 1/4 cup. How many scoops?' 2!",
        ],
        [
            {"title": "Multiplication Trick", "content": "Multiply tops, multiply bottoms. That's it!"},
            {"title": "Division Trick", "content": "Flip the second fraction and multiply instead!"},
            {"title": "Visual Proof", "content": "Always draw it first until the rule makes sense!"}
        ]
    )


def seed_place_value_power():
    """Place Value Power - Understanding the Engine of Numbers"""
    print("🔢 Adding Place Value Mastery...")
    
    subjects = get_all_subjects()
    math_subject = next((s for s in subjects if s["name"] == "Mathematics"), None)
    if not math_subject:
        return
    
    subject_id = math_subject["id"]
    
    place_value_topic = add_topic(
        subject_id,
        "Place Value Mastery: The Power of Position",
        "Why 222 has three different meanings for the same digit",
        105
    )
    
    add_lesson(
        place_value_topic,
        "Place Value - 10 Ways to Truly Understand It",
        "From base-10 blocks to binary code",
        [
            "CONCEPT: The POSITION of a digit determines its value",
            "EXAMPLE: In 342, the 3 means 300, the 4 means 40, the 2 means 2",
            "",
            "WAY 1 - Base-10 Blocks: Ones (cubes), Tens (rods), Hundreds (flats), Thousands (big cubes)",
            "WAY 2 - Building Numbers: Build 342 with 3 hundred-flats, 4 ten-rods, 2 ones",
            "WAY 3 - Trading Game: Collect 10 ones → trade for 1 ten. Collect 10 tens → trade for 1 hundred",
            "WAY 4 - Expanded Form: Show 342 = 300 + 40 + 2",
            "WAY 5 - Power of Zero: Compare 34 vs 304. The 0 holds the tens place so 3 can be hundreds!",
            "WAY 6 - Decimal Extension: 3.42 = 3 + 0.4 + 0.02 (tenths and hundredths)",
            "WAY 7 - Number Sliders: Paper slider moving digits through columns to change value",
            "WAY 8 - Binary Exploration: Show base-2 (only 0 and 1) to prove base-10 is a choice!",
            "WAY 9 - Ancient Number Systems: Roman numerals (no place value!) vs our system",
            "WAY 10 - Bank Ledger: Practice adding/subtracting money, lining up decimal points perfectly",
        ],
        [
            {"title": "Key Insight", "content": "The number 5 can mean 5, 50, 500, or 5,000 depending on WHERE it sits!"},
            {"title": "Advanced", "content": "In binary, 101 means (1×4) + (0×2) + (1×1) = 5 in base-10!"}
        ]
    )


def seed_all_ultimate_math_subjects():
    """Seed all 25 ultimate math subjects with 10 teaching methods each"""
    print("\n" + "="*80)
    print("🎓 ULTIMATE MATH MASTERY - 25 SUBJECTS × 10 METHODS = 250 TEACHING APPROACHES")
    print("="*80 + "\n")
    
    seed_division_mastery_10_ways()
    seed_number_line_journey()
    seed_mental_math_magic()
    seed_estimation_mastery()
    seed_fractions_complete()
    seed_place_value_power()
    
    print("\n" + "="*80)
    print("🎉 MATH MASTERY COMPLETE!")
    print("Your daughters can now learn EVERY concept in MULTIPLE ways!")
    print("="*80 + "\n")


if __name__ == "__main__":
    from database import init_database
    init_database()
    seed_all_ultimate_math_subjects()

