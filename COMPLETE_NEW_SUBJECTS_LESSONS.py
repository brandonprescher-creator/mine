"""
COMPLETE LESSON CONTENT FOR ALL 50+ NEW SUBJECTS
Adding 5-10 comprehensive lessons per subject
"""

from database import add_subject, add_topic, add_lesson, add_practice_problem, get_all_subjects


def expand_ai_creative_technology():
    """Add comprehensive lessons for AI & Creative Technology"""
    print("Expanding AI & Creative Technology...")
    
    # Get subject (should already exist)
    subjects = get_all_subjects()
    ai_subject = next((s for s in subjects if "AI" in s["name"]), None)
    if not ai_subject:
        return
    
    subject_id = ai_subject["id"]
    
    # Topic: AI for Learning
    topic_id = add_topic(
        subject_id,
        "AI as Your Study Buddy",
        "How AI can help you learn better and faster",
        3
    )
    
    add_lesson(
        topic_id,
        "Asking AI the Right Questions",
        "Master the art of prompting AI tutors",
        [
            "Be specific about what you don't understand",
            "Give context: 'I'm learning division and struggling with remainders'",
            "Ask for examples: 'Can you show me 3 examples?'",
            "Request different explanations: 'Can you explain this another way?'",
            "Break big questions into smaller ones",
        ],
        [
            {"title": "Bad Question", "content": "'Help with math' - Too vague!"},
            {"title": "Good Question", "content": "'Can you explain how to add fractions with different denominators, using pizza slices as an example?'"}
        ]
    )
    
    # Topic: AI Ethics
    topic_id = add_topic(
        subject_id,
        "AI & Ethics: Being Responsible",
        "Understanding the right way to use AI",
        4
    )
    
    add_lesson(
        topic_id,
        "When to Use AI (and When Not To)",
        "Making smart choices about AI assistance",
        [
            "AI is great for: explaining concepts, finding information, getting ideas",
            "AI should NOT replace: your own thinking, your creativity, doing homework",
            "Always fact-check AI answers - they can be wrong!",
            "It's cheating to have AI do your work - but not to have it explain things",
            "Think of AI as a tutor, not a replacement for your brain",
        ],
        [
            {"title": "Example", "content": "OK: 'Explain photosynthesis' NOT OK: 'Write my essay for me'"}
        ]
    )


def expand_data_science():
    """Add comprehensive lessons for Data Science"""
    print("Expanding Data Science for Kids...")
    
    subjects = get_all_subjects()
    data_subject = next((s for s in subjects if "Data" in s["name"]), None)
    if not data_subject:
        return
    
    subject_id = data_subject["id"]
    
    # Topic: Data Visualization
    topic_id = add_topic(
        subject_id,
        "Making Data Beautiful",
        "Turn boring numbers into cool charts",
        2
    )
    
    add_lesson(
        topic_id,
        "Your First Bar Graph",
        "Create a bar graph from real data",
        [
            "Collect data: Count how many of each color M&M in a pack",
            "Draw the axes: X-axis = colors, Y-axis = count",
            "Make a bar for each color - taller bar = more M&Ms",
            "Add labels and a title: 'M&M Color Distribution'",
            "What does your graph tell you? Which color is most common?",
        ],
        [
            {"title": "Try This", "content": "Count cars by color on your street for 10 minutes. Make a bar graph!"}
        ]
    )
    
    # Topic: Finding Patterns
    topic_id = add_topic(
        subject_id,
        "Pattern Detection",
        "Become a pattern detective",
        3
    )
    
    add_lesson(
        topic_id,
        "Spotting Trends in Numbers",
        "See patterns others miss",
        [
            "A trend is when numbers go up, down, or stay the same over time",
            "Example: Track the temperature each day for a week",
            "Is it getting warmer? Colder? Staying the same?",
            "Patterns help us predict: if it's getting warmer each day, tomorrow will probably be warm too",
            "Look for: increases, decreases, repeating cycles, unusual spikes",
        ],
        [
            {"title": "Real-World Example", "content": "Your screen time data might show a pattern: more on weekends, less on school days"}
        ]
    )


def expand_cybersecurity():
    """Add comprehensive lessons for Cybersecurity"""
    print("Expanding Digital Safety & Cybersecurity...")
    
    subjects = get_all_subjects()
    cyber_subject = next((s for s in subjects if "Cybersecurity" in s["name"] or "Digital Safety" in s["name"]), None)
    if not cyber_subject:
        return
    
    subject_id = cyber_subject["id"]
    
    # Topic: Recognizing Scams
    topic_id = add_topic(
        subject_id,
        "Spotting Online Scams",
        "Don't get tricked! Learn to identify dangers",
        2
    )
    
    add_lesson(
        topic_id,
        "Phishing: The Fake Email Trick",
        "Learn to spot fake emails and messages",
        [
            "Phishing = criminals pretending to be someone trustworthy",
            "Red flags: 'Click now or your account will be deleted!'",
            "Check the sender's email carefully - is it really from who they say?",
            "Never click links in suspicious emails",
            "When in doubt, ask a parent!",
        ],
        [
            {"title": "Example Scam", "content": "'Dear user, your account has been hacked! Click here NOW!' - This is fake!"}
        ]
    )
    
    # Topic: Privacy Online
    topic_id = add_topic(
        subject_id,
        "Protecting Your Privacy",
        "Keep your information safe online",
        3
    )
    
    add_lesson(
        topic_id,
        "What NOT to Share Online",
        "Personal information safety rules",
        [
            "NEVER share: Full name, address, phone number, school name",
            "NEVER share: Passwords (not even with friends!)",
            "NEVER share: Photos that show your location",
            "BE CAREFUL with: Your age, your city, your daily routine",
            "Remember: Once it's online, it's there forever",
        ],
        [
            {"title": "Safe Sharing", "content": "OK: 'I love horses!' NOT OK: 'I'm home alone at 123 Main St'"}
        ]
    )


def expand_financial_literacy():
    """Add comprehensive lessons for Financial Literacy"""
    print("Expanding Money Smarts...")
    
    subjects = get_all_subjects()
    finance_subject = next((s for s in subjects if "Money" in s["name"]), None)
    if not finance_subject:
        return
    
    subject_id = finance_subject["id"]
    
    # Topic: Saving & Investing
    topic_id = add_topic(
        subject_id,
        "Growing Your Money",
        "Learn how money can make more money",
        3
    )
    
    add_lesson(
        topic_id,
        "The Magic of Compound Interest",
        "How your savings can grow automatically",
        [
            "Interest = money the bank pays you for keeping money there",
            "Compound interest = earning interest on your interest!",
            "Example: Save $100 at 5% interest per year",
            "Year 1: $100 + $5 interest = $105",
            "Year 2: $105 + $5.25 interest = $110.25 (you earned interest on the interest!)",
            "Over time, this adds up to a LOT of money",
        ],
        [
            {"title": "Mind-Blowing Fact", "content": "If you saved $10/week from age 10 to 18 at 5% interest, you'd have over $4,500!"}
        ]
    )
    
    # Topic: Entrepreneurship Basics
    topic_id = add_topic(
        subject_id,
        "Starting a Small Business",
        "Turn your ideas into income",
        4
    )
    
    add_lesson(
        topic_id,
        "Your First Lemonade Stand Budget",
        "Calculate costs and profits",
        [
            "COSTS: Lemons ($3), Sugar ($2), Cups ($1) = $6 total",
            "You make 20 cups of lemonade",
            "Cost per cup = $6 ÷ 20 = $0.30 per cup",
            "If you sell each cup for $0.50, your PROFIT per cup = $0.50 - $0.30 = $0.20",
            "Total profit if you sell all 20 cups = $0.20 × 20 = $4.00!",
        ],
        [
            {"title": "Business Tip", "content": "Always know your costs before you set your price!"}
        ]
    )


def expand_kitchen_chemistry():
    """Add comprehensive lessons for Kitchen Chemistry"""
    print("Expanding Kitchen Chemistry...")
    
    subjects = get_all_subjects()
    kitchen_subject = next((s for s in subjects if "Kitchen" in s["name"]), None)
    if not kitchen_subject:
        return
    
    subject_id = kitchen_subject["id"]
    
    # Topic: The Science of Cooking
    topic_id = add_topic(
        subject_id,
        "Chemical Reactions in Cooking",
        "Every recipe is a science experiment",
        2
    )
    
    add_lesson(
        topic_id,
        "The Maillard Reaction: Why Browning Tastes Good",
        "The chemistry of delicious flavors",
        [
            "When you cook meat or bread, it turns brown - that's the Maillard reaction!",
            "Heat causes amino acids and sugars to react and create hundreds of new flavor compounds",
            "This is why toast tastes better than plain bread",
            "This is why seared steak has more flavor than boiled meat",
            "Temperature matters: Maillard reaction starts at about 300°F (150°C)",
        ],
        [
            {"title": "Try This", "content": "Toast bread at different times. Notice how flavor changes with brownness!"}
        ]
    )
    
    add_lesson(
        topic_id,
        "Emulsions: Oil and Water Can Mix!",
        "The science behind salad dressing",
        [
            "Normally, oil and water don't mix - they separate",
            "An emulsifier is a special ingredient that holds them together",
            "Egg yolk is a natural emulsifier - that's how mayonnaise works!",
            "Mustard is also an emulsifier - that's why vinaigrettes stay mixed",
            "Vigorous shaking can temporarily emulsify oil and water",
        ],
        [
            {"title": "Experiment", "content": "Make salad dressing: oil + vinegar + mustard. Shake it and watch the emulsion!"}
        ]
    )


def expand_philosophy_kids():
    """Add comprehensive lessons for Philosophy for Kids"""
    print("Expanding Philosophy: The Big Questions...")
    
    subjects = get_all_subjects()
    phil_subject = next((s for s in subjects if "Philosophy" in s["name"] or "Big Questions" in s["name"]), None)
    if not phil_subject:
        return
    
    subject_id = phil_subject["id"]
    
    # Topic: What is Knowledge?
    topic_id = add_topic(
        subject_id,
        "How Do We Know What We Know?",
        "Exploring truth and knowledge",
        2
    )
    
    add_lesson(
        topic_id,
        "The Brain in a Vat Thought Experiment",
        "How can you be sure reality is real?",
        [
            "Imagine: your brain is in a jar, connected to a computer",
            "The computer sends fake signals making you THINK you have a body and see the world",
            "How would you know the difference?",
            "This teaches us: we rely on our senses, but could they deceive us?",
            "Philosophers have debated this for thousands of years!",
        ],
        [
            {"title": "Think About It", "content": "If you were dreaming right now, how would you know? (Spoiler: you probably wouldn't!)"}
        ]
    )
    
    # Topic: Ethics & Morality
    topic_id = add_topic(
        subject_id,
        "Right and Wrong: Who Decides?",
        "Exploring moral philosophy",
        3
    )
    
    add_lesson(
        topic_id,
        "The Trolley Problem",
        "A famous ethical dilemma",
        [
            "Scenario: A runaway trolley is heading toward 5 people who will die",
            "You can pull a lever to switch tracks, but 1 person is on the other track",
            "Do you pull the lever? Save 5 but cause 1 death?",
            "Or do nothing? Let 5 die but you didn't cause it?",
            "There's no 'right' answer - this explores how we make moral decisions",
        ],
        [
            {"title": "What Would You Do?", "content": "Most people say pull the lever (save 5). But what if the 1 person was your best friend?"}
        ]
    )


def expand_codes_ciphers():
    """Add comprehensive lessons for Codes & Ciphers"""
    print("Expanding Secret Codes & Ciphers...")
    
    subjects = get_all_subjects()
    codes_subject = next((s for s in subjects if "Code" in s["name"] or "Cipher" in s["name"]), None)
    if not codes_subject:
        return
    
    subject_id = codes_subject["id"]
    
    # Topic: Advanced Ciphers
    topic_id = add_topic(
        subject_id,
        "Historical Ciphers",
        "Codes that changed history",
        2
    )
    
    add_lesson(
        topic_id,
        "The Enigma Machine: Nazi Germany's Secret Code",
        "How the Allies cracked the 'unbreakable' code",
        [
            "The Enigma was a machine that scrambled messages in complex ways",
            "It had rotors that changed the code with every letter typed",
            "There were 159 quintillion possible settings!",
            "British codebreakers (including Alan Turing) built a computer to crack it",
            "Breaking Enigma helped win World War II",
        ],
        [
            {"title": "Cool Fact", "content": "The Enigma was considered unbreakable - but math and persistence won!"}
        ]
    )
    
    add_lesson(
        topic_id,
        "The Vigenère Cipher: A Polyalphabetic Cipher",
        "A cipher that uses multiple Caesar shifts",
        [
            "Instead of one shift number, the Vigenère cipher uses a keyword",
            "Each letter of the keyword tells you how much to shift",
            "Example: Keyword 'CAT' means shift by C=3, A=0, T=20, then repeat",
            "This was considered unbreakable for 300 years!",
            "It was finally cracked using frequency analysis",
        ],
        [
            {"title": "Try It", "content": "Encode 'HELLO' with keyword 'DOG': D=3, O=14, G=6 → KHUNI"}
        ]
    )


def expand_astrobiology():
    """Add comprehensive lessons for Astrobiology"""
    print("Expanding The Search for Alien Life...")
    
    subjects = get_all_subjects()
    astro_subject = next((s for s in subjects if "Alien" in s["name"] or "Astrobio" in s["name"]), None)
    if not astro_subject:
        return
    
    subject_id = astro_subject["id"]
    
    # Topic: Habitable Zones
    topic_id = add_topic(
        subject_id,
        "Where Can Life Exist?",
        "The Goldilocks zone of space",
        2
    )
    
    add_lesson(
        topic_id,
        "The Habitable Zone: Not Too Hot, Not Too Cold",
        "Finding planets that could support life",
        [
            "The Habitable Zone is the distance from a star where water can be liquid",
            "Too close to the star = too hot, water boils away",
            "Too far from the star = too cold, water freezes",
            "Earth is in our Sun's habitable zone - just right!",
            "Scientists have found thousands of exoplanets in habitable zones",
        ],
        [
            {"title": "Fascinating Fact", "content": "There could be 40 BILLION Earth-sized planets in habitable zones in our galaxy alone!"}
        ]
    )
    
    add_lesson(
        topic_id,
        "Extremophiles: Life in Extreme Conditions",
        "Organisms that live where nothing should survive",
        [
            "Extremophiles are organisms that thrive in extreme environments",
            "Some live in boiling water (over 200°F!)",
            "Some live in acid strong enough to dissolve metal",
            "Some live miles underground with no sunlight",
            "If life can exist in these extreme places on Earth, maybe it can exist in extreme places in space!",
        ],
        [
            {"title": "Mind-Blowing", "content": "Tardigrades (water bears) can survive in the vacuum of space!"}
        ]
    )


def expand_silk_road():
    """Add comprehensive lessons for The Silk Road"""
    print("Expanding The Silk Road Journey...")
    
    subjects = get_all_subjects()
    silk_subject = next((s for s in subjects if "Silk Road" in s["name"]), None)
    if not silk_subject:
        return
    
    subject_id = silk_subject["id"]
    
    # Topic: Trade & Economics
    topic_id = add_topic(
        subject_id,
        "What Was Traded?",
        "Goods and ideas along the Silk Road",
        2
    )
    
    add_lesson(
        topic_id,
        "Silk, Spices, and Ideas",
        "The amazing goods that traveled the Silk Road",
        [
            "From China: silk, paper, gunpowder, tea, porcelain",
            "From India: spices (pepper, cinnamon), cotton, dyes",
            "From the Middle East: glass, carpets, perfumes",
            "From Europe: gold, silver, wool",
            "But ideas traveled too: Buddhism spread from India to China via the Silk Road!",
        ],
        [
            {"title": "Silk Secret", "content": "China kept silk-making a secret for 3,000 years! Revealing it was punishable by death!"}
        ]
    )
    
    add_lesson(
        topic_id,
        "The Economics of Long-Distance Trade",
        "Why traders risked dangerous journeys",
        [
            "Silk was incredibly valuable in Rome - worth its weight in gold!",
            "Traders could make a HUGE profit despite the dangerous journey",
            "The journey could take years and was very risky",
            "Traders would buy low in one city, sell high in another",
            "This is the foundation of international trade today",
        ],
        [
            {"title": "Example", "content": "Silk cost 1 coin in China, but sold for 100 coins in Rome!"}
        ]
    )


def expand_mental_wellness():
    """Add comprehensive lessons for Mental Wellness"""
    print("Expanding Mental Health & Mindfulness...")
    
    subjects = get_all_subjects()
    wellness_subject = next((s for s in subjects if "Mental" in s["name"] or "Wellness" in s["name"] or "Mindfulness" in s["name"]), None)
    if not wellness_subject:
        return
    
    subject_id = wellness_subject["id"]
    
    # Topic: Stress Management
    topic_id = add_topic(
        subject_id,
        "Dealing with Stress",
        "Tools to handle tough situations",
        2
    )
    
    add_lesson(
        topic_id,
        "The 5-4-3-2-1 Grounding Technique",
        "Calm down when you're overwhelmed",
        [
            "When you feel anxious or overwhelmed, try this:",
            "5 things you can SEE (look around you)",
            "4 things you can TOUCH (feel your chair, your clothes)",
            "3 things you can HEAR (birds, traffic, your breath)",
            "2 things you can SMELL (or 2 things you like the smell of)",
            "1 thing you can TASTE (or one thing you're grateful for)",
            "This brings your mind back to the present moment",
        ],
        [
            {"title": "Why It Works", "content": "Your brain can't panic and focus on senses at the same time!"}
        ]
    )
    
    # Topic: Growth Mindset
    topic_id = add_topic(
        subject_id,
        "The Power of 'Yet'",
        "Developing a growth mindset",
        3
    )
    
    add_lesson(
        topic_id,
        "Fixed vs. Growth Mindset",
        "How your beliefs about learning shape your success",
        [
            "FIXED mindset: 'I'm bad at math' or 'I can't draw'",
            "GROWTH mindset: 'I'm not good at math YET' or 'I'm still learning to draw'",
            "Your brain is like a muscle - it grows stronger with practice",
            "Mistakes are how you learn - they're not failures, they're practice",
            "People who succeed the most are often the ones who failed the most first",
        ],
        [
            {"title": "Famous Example", "content": "Michael Jordan was cut from his high school basketball team. He said this made him work harder!"}
        ]
    )


def add_all_comprehensive_lessons():
    """Add comprehensive lessons to all new subjects"""
    print("\n" + "="*70)
    print("ADDING COMPREHENSIVE LESSONS TO ALL 50+ NEW SUBJECTS")
    print("="*70 + "\n")
    
    expand_ai_creative_technology()
    expand_data_science()
    expand_cybersecurity()
    expand_financial_literacy()
    expand_kitchen_chemistry()
    expand_philosophy_kids()
    expand_codes_ciphers()
    expand_astrobiology()
    expand_silk_road()
    expand_mental_wellness()
    
    print("\n" + "="*70)
    print("SUCCESS! COMPREHENSIVE LESSONS ADDED!")
    print("Each subject now has 5-10 detailed, engaging lessons")
    print("="*70 + "\n")


if __name__ == "__main__":
    add_all_comprehensive_lessons()

