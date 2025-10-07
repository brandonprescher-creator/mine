"""
🎓 NEW SUBJECTS CURRICULUM - 50+ Revolutionary Learning Topics
Complete curriculum expansion for ultimate homeschool experience
"""

from database import add_subject, add_topic, add_lesson, add_practice_problem


def seed_future_ready_tech_subjects():
    """Category 1: Future-Ready & Technology Skills (10 Subjects)"""
    print("🚀 Seeding Future-Ready & Technology subjects...")

    # Subject 1: AI & Me: The Creative Partner
    ai_subject = add_subject(
        "AI & Creative Technology",
        "Learn to use AI as a creative partner and problem-solving tool",
        "🤖",
        100,
    )

    ai_topic1 = add_topic(
        ai_subject,
        "Understanding AI Basics",
        "What is AI and how does it work?",
        1,
    )
    add_lesson(
        ai_topic1,
        "What is Artificial Intelligence?",
        "Discover what AI is and how it's changing our world",
        [
            "AI is when computers can think and learn like humans",
            "AI powers things like Siri, Alexa, and recommendation systems",
            "AI can help us solve problems, create art, and learn new things",
            "AI is a tool - it helps us do things better and faster",
        ],
        [
            {
                "title": "AI in Your Life",
                "content": "Think about apps you use: Netflix recommendations, spell-check, voice assistants - that's all AI!",
            }
        ],
    )

    ai_topic2 = add_topic(
        ai_subject, "AI for Creativity", "Use AI to create amazing things", 2
    )
    add_lesson(
        ai_topic2,
        "Writing Prompts for AI Art",
        "Learn to describe what you want AI to create",
        [
            "Be specific about what you want to see",
            "Describe colors, mood, and style",
            "Add details about setting and atmosphere",
            "Experiment with different words to get better results",
        ],
        [
            {
                "title": "Good Prompt Example",
                "content": "Instead of 'a cat', try 'a fluffy orange cat sitting on a rainbow in the clouds at sunset, digital art style'",
            }
        ],
    )

    # Subject 2: Data Detectives
    data_subject = add_subject(
        "Data Science for Kids",
        "Become a data detective and find patterns in numbers",
        "🔍",
        101,
    )

    data_topic1 = add_topic(
        data_subject, "Collecting Data", "Learn to gather and organize information", 1
    )
    add_lesson(
        data_topic1,
        "What is Data?",
        "Understanding information and how to collect it",
        [
            "Data is information we collect about the world",
            "We can collect data by counting, measuring, and observing",
            "Data helps us answer questions and make decisions",
            "Good data collection requires a plan and careful recording",
        ],
        [
            {
                "title": "Real-World Example",
                "content": "Track the weather for a week: temperature, rain, sunny/cloudy. You're collecting data!",
            }
        ],
    )

    # Subject 3: Cybersecurity
    cyber_subject = add_subject(
        "Digital Safety & Cybersecurity",
        "Learn to protect yourself and your information online",
        "🔒",
        102,
    )

    cyber_topic1 = add_topic(
        cyber_subject, "Password Power", "Create unbreakable passwords", 1
    )
    add_lesson(
        cyber_topic1,
        "Making Super Strong Passwords",
        "Learn the secrets of password security",
        [
            "Use at least 12 characters",
            "Mix uppercase, lowercase, numbers, and symbols",
            "Never use personal information (birthdays, pet names)",
            "Use a different password for each important account",
            "Consider using a passphrase: 'BlueDog$Loves#Pizza99!'",
        ],
        [
            {
                "title": "Password Strength Test",
                "content": "Weak: 'password123' Strong: 'MyC@t&2Sisters!Love#Pizza'",
            }
        ],
    )

    # Subject 4: Computer Fundamentals
    computer_subject = add_subject(
        "How Computers Think",
        "Understand the magic inside every computer",
        "💻",
        103,
    )

    # Subject 5: Digital Storytelling
    storytelling_subject = add_subject(
        "Digital Media Creation",
        "Create videos, podcasts, and digital stories",
        "🎬",
        104,
    )

    # Subject 6: 3D Modeling
    modeling_subject = add_subject(
        "3D Design & Printing",
        "Design three-dimensional objects for the real world",
        "🎨",
        105,
    )

    # Subject 7: Game Design
    game_subject = add_subject(
        "Game Design Fundamentals",
        "Learn to create your own video games",
        "🎮",
        106,
    )

    # Subject 8: Smart Home
    iot_subject = add_subject(
        "Smart Home Technology",
        "Understand how automated devices work together",
        "🏠",
        107,
    )

    # Subject 9: Digital Ethics
    ethics_subject = add_subject(
        "Digital Ethics & Citizenship",
        "Be a responsible and thoughtful online citizen",
        "⚖️",
        108,
    )

    # Subject 10: Personal Branding
    brand_subject = add_subject(
        "Your Digital Footprint",
        "Build a positive online presence",
        "👤",
        109,
    )

    print("✅ Future-Ready & Technology subjects added!")


def seed_life_practical_skills():
    """Category 2: Life & Practical Skills (12 Subjects)"""
    print("🏡 Seeding Life & Practical Skills subjects...")

    # Subject 1: Financial Literacy
    finance_subject = add_subject(
        "Money Smarts",
        "Master the basics of money management",
        "💰",
        110,
    )

    finance_topic1 = add_topic(
        finance_subject, "What is Money?", "Understanding currency and value", 1
    )
    add_lesson(
        finance_topic1,
        "The History of Money",
        "How money evolved from bartering to digital payment",
        [
            "Long ago, people traded goods (barter system)",
            "Coins and paper money made trading easier",
            "Today we have credit cards and digital money",
            "Money represents value and allows us to exchange goods and services",
        ],
        [
            {
                "title": "Barter Example",
                "content": "If you trade 2 cookies for your friend's apple, that's bartering!",
            }
        ],
    )

    finance_topic2 = add_topic(
        finance_subject, "Budgeting Basics", "Learn to plan your spending", 2
    )
    add_lesson(
        finance_topic2,
        "Making Your First Budget",
        "How to track income and expenses",
        [
            "Income is money you receive (allowance, gifts, earnings)",
            "Expenses are things you spend money on",
            "A budget helps you plan: Income - Expenses = Savings",
            "Save some, spend some, give some!",
        ],
        [
            {
                "title": "Budget Example",
                "content": "Allowance: $10/week. Save: $3, Spend: $5, Give: $2",
            }
        ],
    )

    # Subject 2: Architecture & Design
    arch_subject = add_subject(
        "Home & Space Design",
        "Learn to design beautiful and functional spaces",
        "🏛️",
        111,
    )

    # Subject 3: Kitchen Chemistry
    kitchen_subject = add_subject(
        "Kitchen Chemistry",
        "Cooking is science! Learn the chemistry of food",
        "🧪",
        112,
    )

    kitchen_topic1 = add_topic(
        kitchen_subject, "Baking Science", "The chemistry behind baking", 1
    )
    add_lesson(
        kitchen_topic1,
        "Why Baking Soda Makes Things Rise",
        "The science of leavening agents",
        [
            "Baking soda is a base that creates bubbles",
            "When mixed with acid (vinegar, lemon juice), it creates CO2 gas",
            "These bubbles make baked goods fluffy and light",
            "Too much = bitter taste, too little = flat cookies",
        ],
        [
            {
                "title": "Try This Experiment",
                "content": "Mix baking soda with vinegar in a cup - watch it fizz!",
            }
        ],
    )

    # Subject 4: Debate Skills
    debate_subject = add_subject(
        "Debate & Public Speaking",
        "Express your ideas with confidence and logic",
        "🎤",
        113,
    )

    # Subject 5: Home Maintenance
    maintenance_subject = add_subject(
        "Home & Auto Basics",
        "Practical skills for maintaining your home and car",
        "🔧",
        114,
    )

    # Subject 6: Entrepreneurship
    business_subject = add_subject(
        "Young Entrepreneurs",
        "Turn your ideas into real businesses",
        "💼",
        115,
    )

    business_topic1 = add_topic(
        business_subject, "Business Ideas", "Finding problems to solve", 1
    )
    add_lesson(
        business_topic1,
        "What Makes a Good Business Idea?",
        "Identifying opportunities and solutions",
        [
            "A good business solves a problem people have",
            "Look for things that frustrate you or others",
            "Think about what you're good at and enjoy",
            "Start small and test your idea",
        ],
        [
            {
                "title": "Example",
                "content": "Problem: Neighbors need help with yard work. Solution: Start a lawn-mowing service!",
            }
        ],
    )

    # Subject 7: Gardening
    garden_subject = add_subject(
        "Gardening & Urban Farming",
        "Grow your own food and understand plant science",
        "🌱",
        116,
    )

    # Subject 8: First Aid
    firstaid_subject = add_subject(
        "First Aid & Emergency Prep",
        "Essential skills for helping in emergencies",
        "🚑",
        117,
    )

    # Subject 9: Navigation
    nav_subject = add_subject(
        "Maps & Navigation",
        "Master the art of finding your way",
        "🗺️",
        118,
    )

    # Subject 10: Productivity
    productivity_subject = add_subject(
        "Time Management & Productivity",
        "Get more done and stress less",
        "⏰",
        119,
    )

    # Subject 11: DIY & Maker
    diy_subject = add_subject(
        "DIY & Maker Skills",
        "Build, create, and fix things yourself",
        "🛠️",
        120,
    )

    # Subject 12: Mental Wellness
    wellness_subject = add_subject(
        "Mental Health & Mindfulness",
        "Take care of your mind and emotions",
        "🧘",
        121,
    )

    wellness_topic1 = add_topic(
        wellness_subject,
        "Understanding Emotions",
        "Learning to recognize and express feelings",
        1,
    )
    add_lesson(
        wellness_topic1,
        "The Feelings Wheel",
        "Identifying and naming your emotions",
        [
            "Everyone has many different feelings every day",
            "Basic emotions: happy, sad, angry, scared, surprised, disgusted",
            "Each basic emotion has many shades (sad can be disappointed, lonely, hurt)",
            "Naming your feelings helps you understand and manage them",
        ],
        [
            {
                "title": "Practice",
                "content": "When you feel bad, try to name the exact feeling. 'I feel frustrated' is more helpful than 'I feel bad'.",
            }
        ],
    )

    print("✅ Life & Practical Skills subjects added!")


def seed_creative_critical_thinking():
    """Category 3: Creative & Critical Thinking (10 Subjects)"""
    print("🎨 Seeding Creative & Critical Thinking subjects...")

    # Subject 1: Philosophy for Kids
    philosophy_subject = add_subject(
        "Philosophy: The Big Questions",
        "Think deeply about life's most interesting questions",
        "🤔",
        122,
    )

    phil_topic1 = add_topic(
        philosophy_subject, "What is Fair?", "Exploring justice and fairness", 1
    )
    add_lesson(
        phil_topic1,
        "The Cookie Dilemma",
        "Exploring different ideas of fairness",
        [
            "Imagine: You and your sister get cookies. Is it fair if you both get the same amount?",
            "What if your sister is older and hungrier - should she get more?",
            "What if you helped bake them - should you get more?",
            "Fairness can mean different things in different situations",
        ],
        [
            {
                "title": "Think About It",
                "content": "Is equal always fair? Is fair always equal?",
            }
        ],
    )

    # Subject 2: Invention Lab
    invention_subject = add_subject(
        "Invention & Problem Solving",
        "Design creative solutions to real problems",
        "💡",
        123,
    )

    # Subject 3: World Mythology
    mythology_subject = add_subject(
        "Mythology & Modern Stories",
        "Connect ancient myths to today's tales",
        "📚",
        124,
    )

    # Subject 4: Logic Puzzles
    logic_subject = add_subject(
        "Logic Puzzles & Brain Teasers",
        "Exercise your brain with challenging puzzles",
        "🧩",
        125,
    )

    # Subject 5: World-Building
    worldbuilding_subject = add_subject(
        "Creative Writing: World-Building",
        "Create entire fictional worlds from scratch",
        "🌍",
        126,
    )

    # Subject 6: Critical Thinking
    critical_subject = add_subject(
        "Spotting Misinformation",
        "Learn to think critically and check facts",
        "🕵️",
        127,
    )

    # Subject 7: Symbology
    symbol_subject = add_subject(
        "Symbols & Their Meanings",
        "Decode the hidden language of symbols",
        "🔣",
        128,
    )

    # Subject 8: Futures Studies
    futures_subject = add_subject(
        "Imagining Tomorrow",
        "Predict and design the future",
        "🔮",
        129,
    )

    # Subject 9: Storyboarding
    storyboard_subject = add_subject(
        "Visual Storytelling",
        "Plan stories with pictures and sequences",
        "🎬",
        130,
    )

    # Subject 10: Psychology
    psychology_subject = add_subject(
        "Understanding People",
        "Learn why people think and act the way they do",
        "🧠",
        131,
    )

    print("✅ Creative & Critical Thinking subjects added!")


def seed_interdisciplinary_units():
    """Category 4: Interdisciplinary & Thematic Units (8 Subjects)"""
    print("🌐 Seeding Interdisciplinary & Thematic subjects...")

    # Subject 1: The Silk Road
    silkroad_subject = add_subject(
        "The Silk Road Journey",
        "Travel through history along the world's greatest trade route",
        "🐫",
        132,
    )

    silk_topic1 = add_topic(
        silkroad_subject, "The Route", "Mapping the Silk Road", 1
    )
    add_lesson(
        silk_topic1,
        "From China to Rome: The Silk Road Map",
        "Geography and civilizations along the route",
        [
            "The Silk Road wasn't one road - it was many routes across Asia",
            "Started in China, crossed deserts and mountains to reach Europe",
            "Connected three major continents: Asia, Europe, and Africa",
            "Cities like Samarkand and Baghdad became wealthy trading centers",
        ],
        [
            {
                "title": "Fun Fact",
                "content": "The Silk Road was over 4,000 miles long - that's like driving from NYC to LA and back!",
            }
        ],
    )

    # Subject 2: Science of Sports
    sports_science_subject = add_subject(
        "The Science of Sports",
        "Physics, biology, and mathematics in athletics",
        "⚽",
        133,
    )

    # Subject 3: Utah Farm Life
    farm_subject = add_subject(
        "A Year on a Utah Farm",
        "Experience farming through the seasons in Utah",
        "🚜",
        134,
    )

    # Subject 4: Architecture Worldwide
    world_arch_subject = add_subject(
        "World Architecture",
        "Explore famous structures and their engineering",
        "🗼",
        135,
    )

    # Subject 5: Body as Machine
    body_subject = add_subject(
        "The Human Body Machine",
        "How your body works like an amazing machine",
        "🤖",
        136,
    )

    # Subject 6: Story of Food
    food_subject = add_subject(
        "The Journey of Food",
        "Follow food from farm to table through history",
        "🍎",
        137,
    )

    # Subject 7: Codes & Ciphers
    codes_subject = add_subject(
        "Secret Codes & Ciphers",
        "The history and mathematics of secret messages",
        "🔐",
        138,
    )

    codes_topic1 = add_topic(codes_subject, "Simple Ciphers", "Basic code-breaking", 1)
    add_lesson(
        codes_topic1,
        "The Caesar Cipher",
        "Learn Julius Caesar's secret code",
        [
            "The Caesar Cipher shifts each letter by a fixed number",
            "Example: Shift by 3 means A becomes D, B becomes E, etc.",
            "To decode, shift backward by the same number",
            "Julius Caesar used this to send secret military messages",
        ],
        [
            {
                "title": "Try It",
                "content": "Encode 'HELLO' with a shift of 3: KHOOR",
            }
        ],
    )

    # Subject 8: Deep Sea Exploration
    ocean_subject = add_subject(
        "Exploring the Deep Sea",
        "Discover the mysteries of Earth's final frontier",
        "🌊",
        139,
    )

    print("✅ Interdisciplinary & Thematic subjects added!")


def seed_advanced_specialized():
    """Category 5: Advanced & Specialized Academic Wings (10 Subjects)"""
    print("🎓 Seeding Advanced & Specialized subjects...")

    # Subject 1: Linguistics
    linguistics_subject = add_subject(
        "The Science of Language",
        "How languages work and evolve",
        "🗣️",
        140,
    )

    # Subject 2: Classical Rome
    rome_subject = add_subject(
        "Ancient Rome Deep Dive",
        "Politics, culture, and engineering of Rome",
        "🏛️",
        141,
    )

    # Subject 3: Cognitive Science
    cognitive_subject = add_subject(
        "How Your Brain Learns",
        "The science of thinking and learning",
        "🧠",
        142,
    )

    # Subject 4: Environmental Policy
    environment_subject = add_subject(
        "Environmental Science & Solutions",
        "Understanding and solving environmental challenges",
        "🌍",
        143,
    )

    # Subject 5: Formal Logic
    formal_logic_subject = add_subject(
        "Formal Logic & Reasoning",
        "The mathematical foundation of logical thinking",
        "➗",
        144,
    )

    # Subject 6: Art History
    art_history_subject = add_subject(
        "Art Through the Ages",
        "From Renaissance masterpieces to modern art",
        "🎨",
        145,
    )

    # Subject 7: Macroeconomics
    macro_subject = add_subject(
        "How Economies Work",
        "Understanding national and global economics",
        "📊",
        146,
    )

    # Subject 8: Astrobiology
    astrobio_subject = add_subject(
        "The Search for Alien Life",
        "Exploring life's possibilities beyond Earth",
        "👽",
        147,
    )

    astro_topic1 = add_topic(
        astrobio_subject, "What is Life?", "Defining life in the universe", 1
    )
    add_lesson(
        astro_topic1,
        "The 7 Characteristics of Life",
        "What makes something 'alive'?",
        [
            "All living things: grow, reproduce, respond to environment",
            "They use energy, maintain homeostasis, adapt, and are made of cells",
            "But could alien life be different? Silicon-based instead of carbon?",
            "Life might exist in places we never imagined - under ice, in clouds of gas",
        ],
        [
            {
                "title": "Mind-Blowing Fact",
                "content": "There are more stars in the universe than grains of sand on all Earth's beaches!",
            }
        ],
    )

    # Subject 9: Constitutional Law
    law_subject = add_subject(
        "Constitutional Law for Teens",
        "Your rights and how the Constitution works",
        "⚖️",
        148,
    )

    # Subject 10: Creative Non-Fiction
    nonfiction_subject = add_subject(
        "Writing True Stories",
        "The art of narrative non-fiction",
        "✍️",
        149,
    )

    print("✅ Advanced & Specialized subjects added!")


def seed_all_new_subjects():
    """Seed all 50+ new revolutionary subjects"""
    print("\n" + "=" * 60)
    print("🚀 STARTING MASSIVE CURRICULUM EXPANSION")
    print("Adding 50+ Revolutionary Learning Topics!")
    print("=" * 60 + "\n")

    seed_future_ready_tech_subjects()
    seed_life_practical_skills()
    seed_creative_critical_thinking()
    seed_interdisciplinary_units()
    seed_advanced_specialized()

    print("\n" + "=" * 60)
    print("🎉 SUCCESS! 50+ NEW SUBJECTS ADDED!")
    print("Your daughters now have access to:")
    print("  • 10 Future-Ready Technology subjects")
    print("  • 12 Life & Practical Skills subjects")
    print("  • 10 Creative & Critical Thinking subjects")
    print("  • 8 Interdisciplinary Thematic Units")
    print("  • 10 Advanced Specialized subjects")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    from database import init_database

    init_database()
    seed_all_new_subjects()

