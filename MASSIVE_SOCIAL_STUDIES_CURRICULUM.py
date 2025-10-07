"""
MASSIVE Social Studies Curriculum with Grade Levels
This creates a comprehensive Social Studies curriculum for K-8 with grade-specific topics and lessons.
"""

from database import (
    add_subject,
    add_topic,
    add_lesson,
    add_practice_problem,
    get_all_subjects,
    get_topics_by_subject,
)


def seed_massive_social_studies_curriculum():
    """Seed the database with MASSIVE Social Studies curriculum organized by grade levels."""

    # Check if already seeded
    existing_subjects = get_all_subjects()
    if existing_subjects and any(
        s["name"] == "Social Studies" for s in existing_subjects
    ):
        print("Social Studies curriculum already seeded.")
        return

    print("Seeding MASSIVE Social Studies curriculum...")

    # Create Social Studies subject
    social_id = add_subject(
        "Social Studies", "History, geography, civics, and economics", "🌍", 4
    )

    # KINDERGARTEN TOPICS
    k_family_id = add_topic(
        social_id, "K - Family & Community", "Learn about families and communities", 1
    )
    k_helpers_id = add_topic(
        social_id, "K - Community Helpers", "Meet people who help in our community", 2
    )
    k_holidays_id = add_topic(
        social_id,
        "K - Holidays & Traditions",
        "Celebrate different holidays and traditions",
        3,
    )
    k_maps_id = add_topic(
        social_id, "K - Maps & Places", "Learn about maps and different places", 4
    )

    # GRADE 1 TOPICS
    g1_neighborhood_id = add_topic(
        social_id, "1st - Neighborhoods", "Explore different types of neighborhoods", 5
    )
    g1_rules_id = add_topic(
        social_id, "1st - Rules & Laws", "Learn about rules and why we need them", 6
    )
    g1_culture_id = add_topic(
        social_id,
        "1st - Different Cultures",
        "Learn about cultures around the world",
        7,
    )
    g1_time_id = add_topic(
        social_id, "1st - Past & Present", "Compare life in the past and present", 8
    )

    # GRADE 2 TOPICS
    g2_geography_id = add_topic(
        social_id,
        "2nd - World Geography",
        "Learn about continents, oceans, and countries",
        9,
    )
    g2_government_id = add_topic(
        social_id, "2nd - Local Government", "Understand how local government works", 10
    )
    g2_economics_id = add_topic(
        social_id, "2nd - Needs & Wants", "Learn about needs, wants, and money", 11
    )
    g2_history_id = add_topic(
        social_id,
        "2nd - American History",
        "Learn about important events in American history",
        12,
    )

    # GRADE 3 TOPICS
    g3_communities_id = add_topic(
        social_id,
        "3rd - Types of Communities",
        "Study urban, suburban, and rural communities",
        13,
    )
    g3_immigration_id = add_topic(
        social_id,
        "3rd - Immigration & Diversity",
        "Learn about people coming to America",
        14,
    )
    g3_native_id = add_topic(
        social_id,
        "3rd - Native American Cultures",
        "Study Native American history and culture",
        15,
    )
    g3_environment_id = add_topic(
        social_id,
        "3rd - Human-Environment Interaction",
        "Learn how people affect their environment",
        16,
    )

    # GRADE 4 TOPICS
    g4_states_id = add_topic(
        social_id,
        "4th - United States Geography",
        "Study the 50 states and their features",
        17,
    )
    g4_colonization_id = add_topic(
        social_id, "4th - Colonial America", "Learn about the 13 colonies", 18
    )
    g4_revolution_id = add_topic(
        social_id, "4th - American Revolution", "Study the fight for independence", 19
    )
    g4_constitution_id = add_topic(
        social_id,
        "4th - Constitution & Government",
        "Learn about the founding documents",
        20,
    )

    # GRADE 5 TOPICS
    g5_westward_id = add_topic(
        social_id,
        "5th - Westward Expansion",
        "Study the growth of America westward",
        21,
    )
    g5_civil_war_id = add_topic(
        social_id,
        "5th - Civil War & Reconstruction",
        "Learn about the Civil War and its aftermath",
        22,
    )
    g5_industrial_id = add_topic(
        social_id,
        "5th - Industrial Revolution",
        "Study the growth of industry and cities",
        23,
    )
    g5_immigration_id = add_topic(
        social_id,
        "5th - Immigration & Urbanization",
        "Learn about waves of immigration",
        24,
    )

    # GRADE 6 TOPICS
    g6_ancient_id = add_topic(
        social_id,
        "6th - Ancient Civilizations",
        "Study ancient Egypt, Greece, and Rome",
        25,
    )
    g6_medieval_id = add_topic(
        social_id, "6th - Medieval Times", "Learn about the Middle Ages", 26
    )
    g6_renaissance_id = add_topic(
        social_id,
        "6th - Renaissance & Exploration",
        "Study the Renaissance and Age of Exploration",
        27,
    )
    g6_economics_id = add_topic(
        social_id,
        "6th - Economics & Trade",
        "Learn about economic systems and trade",
        28,
    )

    # GRADE 7 TOPICS
    g7_world_war_id = add_topic(
        social_id, "7th - World Wars", "Study World War I and World War II", 29
    )
    g7_cold_war_id = add_topic(
        social_id, "7th - Cold War Era", "Learn about the Cold War and its effects", 30
    )
    g7_civil_rights_id = add_topic(
        social_id, "7th - Civil Rights Movement", "Study the fight for equality", 31
    )
    g7_global_id = add_topic(
        social_id, "7th - Globalization", "Learn about our connected world", 32
    )

    # GRADE 8 TOPICS
    g8_government_id = add_topic(
        social_id,
        "8th - American Government",
        "Study the three branches of government",
        33,
    )
    g8_civics_id = add_topic(
        social_id,
        "8th - Civics & Citizenship",
        "Learn about rights, responsibilities, and voting",
        34,
    )
    g8_economics_id = add_topic(
        social_id,
        "8th - Economics & Personal Finance",
        "Study economic principles and money management",
        35,
    )
    g8_current_id = add_topic(
        social_id, "8th - Current Events", "Analyze current events and their impact", 36
    )

    # ADVANCED TOPICS
    world_history_id = add_topic(
        social_id, "World History", "Study major events in world history", 37
    )
    political_science_id = add_topic(
        social_id, "Political Science", "Study government and political systems", 38
    )
    sociology_id = add_topic(
        social_id, "Sociology", "Study human society and social behavior", 39
    )
    anthropology_id = add_topic(
        social_id, "Anthropology", "Study human cultures and societies", 40
    )

    # KINDERGARTEN LESSONS
    seed_kindergarten_social_lessons(
        k_family_id, k_helpers_id, k_holidays_id, k_maps_id
    )

    # GRADE 1 LESSONS
    seed_grade1_social_lessons(
        g1_neighborhood_id, g1_rules_id, g1_culture_id, g1_time_id
    )

    # GRADE 2 LESSONS
    seed_grade2_social_lessons(
        g2_geography_id, g2_government_id, g2_economics_id, g2_history_id
    )

    # GRADE 3 LESSONS
    seed_grade3_social_lessons(
        g3_communities_id, g3_immigration_id, g3_native_id, g3_environment_id
    )

    # GRADE 4 LESSONS
    seed_grade4_social_lessons(
        g4_states_id, g4_colonization_id, g4_revolution_id, g4_constitution_id
    )

    # GRADE 5 LESSONS
    seed_grade5_social_lessons(
        g5_westward_id, g5_civil_war_id, g5_industrial_id, g5_immigration_id
    )

    # GRADE 6 LESSONS
    seed_grade6_social_lessons(
        g6_ancient_id, g6_medieval_id, g6_renaissance_id, g6_economics_id
    )

    # GRADE 7 LESSONS
    seed_grade7_social_lessons(
        g7_world_war_id, g7_cold_war_id, g7_civil_rights_id, g7_global_id
    )

    # GRADE 8 LESSONS
    seed_grade8_social_lessons(
        g8_government_id, g8_civics_id, g8_economics_id, g8_current_id
    )

    # ADVANCED LESSONS
    seed_advanced_social_lessons(
        world_history_id, political_science_id, sociology_id, anthropology_id
    )

    print("MASSIVE Social Studies curriculum seeded successfully!")


def seed_kindergarten_social_lessons(family_id, helpers_id, holidays_id, maps_id):
    """Seed Kindergarten social studies lessons."""

    # Family & Community
    lesson_id = add_lesson(
        family_id,
        "What is a Family?",
        "Learn about different types of families",
        [
            "Family: people who love and care for each other",
            "Families can be big or small",
            "Some families have parents, children, grandparents",
            "All families are special and unique",
            "Families help each other and spend time together",
        ],
        [
            {
                "title": "Examples",
                "content": "Nuclear family: parents and children. Extended family: grandparents, aunts, uncles, cousins",
            }
        ],
        "builtin",
        None,
        1,
    )
    add_practice_problem(
        lesson_id,
        "Who are the people in your family?",
        "Answers will vary",
        [
            "Think about who lives with you",
            "Think about who you see often",
            "Family members love and care for each other",
        ],
        ["Draw a picture of your family"],
        "easy",
        1,
    )

    lesson_id = add_lesson(
        family_id,
        "Family Traditions",
        "Learn about special things families do together",
        [
            "Tradition: something special a family does regularly",
            "Traditions help families feel connected",
            "Examples: holiday celebrations, family meals, bedtime stories",
            "Traditions can be passed down from generation to generation",
            "Every family has their own special traditions",
        ],
        [
            {
                "title": "Examples",
                "content": "Holiday traditions: decorating Christmas tree, lighting Hanukkah candles. Daily traditions: family dinner, bedtime stories",
            }
        ],
        "builtin",
        None,
        1,
    )

    lesson_id = add_lesson(
        family_id,
        "Community Helpers",
        "Learn about people who help in our community",
        [
            "Community: the place where we live and work",
            "Community helpers: people who work to help others",
            "Examples: teachers, doctors, firefighters, police officers",
            "Each helper has a special job to do",
            "We should respect and thank our community helpers",
        ],
        [
            {
                "title": "Examples",
                "content": "Teacher: helps us learn. Doctor: helps us stay healthy. Firefighter: helps put out fires. Police officer: helps keep us safe",
            }
        ],
        "builtin",
        None,
        1,
    )

    # Community Helpers
    lesson_id = add_lesson(
        helpers_id,
        "Teachers and School Helpers",
        "Learn about people who work at school",
        [
            "Teachers: help us learn new things",
            "Principal: leads the school and helps everyone",
            "Librarian: helps us find books and learn to read",
            "Nurse: helps us when we're sick or hurt",
            "Custodian: keeps our school clean and safe",
        ],
        [
            {
                "title": "Examples",
                "content": "Teacher: teaches reading and math. Principal: makes school rules. Librarian: organizes books. Nurse: takes care of sick students",
            }
        ],
        "builtin",
        None,
        1,
    )

    lesson_id = add_lesson(
        helpers_id,
        "Safety Helpers",
        "Learn about people who keep us safe",
        [
            "Police officers: help keep our community safe",
            "Firefighters: put out fires and help in emergencies",
            "Paramedics: help people who are hurt or sick",
            "These helpers work hard to protect us",
            "We should always be respectful to safety helpers",
        ],
        [
            {
                "title": "Examples",
                "content": "Police officer: stops bad guys, helps lost children. Firefighter: puts out fires, rescues people. Paramedic: gives first aid, takes people to hospital",
            }
        ],
        "builtin",
        None,
        1,
    )

    # Holidays & Traditions
    lesson_id = add_lesson(
        holidays_id,
        "American Holidays",
        "Learn about important American holidays",
        [
            "Holiday: a special day that we celebrate",
            "Independence Day: celebrates America's freedom",
            "Thanksgiving: celebrates being thankful",
            "Christmas: celebrates giving and family",
            "Each holiday has special traditions and meanings",
        ],
        [
            {
                "title": "Examples",
                "content": "Independence Day: fireworks, parades, red-white-blue. Thanksgiving: turkey dinner, family gathering, being thankful",
            }
        ],
        "builtin",
        None,
        1,
    )

    lesson_id = add_lesson(
        holidays_id,
        "Cultural Celebrations",
        "Learn about different cultural holidays",
        [
            "Different cultures celebrate different holidays",
            "Hanukkah: Jewish holiday of lights",
            "Kwanzaa: African American celebration of heritage",
            "Diwali: Hindu festival of lights",
            "Learning about different celebrations helps us understand each other",
        ],
        [
            {
                "title": "Examples",
                "content": "Hanukkah: menorah, dreidel, latkes. Kwanzaa: kinara, seven principles, family unity. Diwali: lamps, fireworks, sweets",
            }
        ],
        "builtin",
        None,
        1,
    )

    # Maps & Places
    lesson_id = add_lesson(
        maps_id,
        "What is a Map?",
        "Learn about maps and how to use them",
        [
            "Map: a picture that shows places and how to get there",
            "Maps help us find our way",
            "Maps show where things are located",
            "We can use maps to plan trips",
            "Maps use symbols to represent real things",
        ],
        [
            {
                "title": "Examples",
                "content": "Road map: shows streets and highways. School map: shows classrooms and offices. World map: shows countries and oceans",
            }
        ],
        "builtin",
        None,
        1,
    )

    lesson_id = add_lesson(
        maps_id,
        "Our School and Neighborhood",
        "Learn about places near us",
        [
            "School: where we go to learn",
            "Neighborhood: the area around our school and home",
            "Places in our neighborhood: stores, parks, houses",
            "We can walk or ride to places in our neighborhood",
            "Our neighborhood is part of our community",
        ],
        [
            {
                "title": "Examples",
                "content": "School: classrooms, playground, library. Neighborhood: grocery store, park, houses, fire station",
            }
        ],
        "builtin",
        None,
        1,
    )


def seed_grade1_social_lessons(neighborhood_id, rules_id, culture_id, time_id):
    """Seed Grade 1 social studies lessons."""

    # Neighborhoods
    lesson_id = add_lesson(
        neighborhood_id,
        "Types of Neighborhoods",
        "Learn about different places people live",
        [
            "Urban: city with tall buildings and many people",
            "Suburban: area outside the city with houses and yards",
            "Rural: countryside with farms and open spaces",
            "Each type of neighborhood has different features",
            "People choose where to live based on their needs",
        ],
        [
            {
                "title": "Examples",
                "content": "Urban: New York City, tall buildings, subways. Suburban: houses with yards, shopping centers. Rural: farms, open fields, small towns",
            }
        ],
        "builtin",
        None,
        1,
    )

    lesson_id = add_lesson(
        neighborhood_id,
        "Neighborhood Services",
        "Learn about services in our community",
        [
            "Service: something that helps people",
            "Examples: grocery stores, hospitals, libraries",
            "Services make our lives easier and better",
            "Different neighborhoods have different services",
            "We should appreciate the services in our community",
        ],
        [
            {
                "title": "Examples",
                "content": "Grocery store: sells food. Hospital: treats sick people. Library: lends books. Post office: delivers mail",
            }
        ],
        "builtin",
        None,
        1,
    )

    # Rules & Laws
    lesson_id = add_lesson(
        rules_id,
        "Why We Have Rules",
        "Learn about the importance of rules",
        [
            "Rule: something we must or must not do",
            "Rules help keep us safe and happy",
            "Rules help us get along with others",
            "Examples: look both ways before crossing, raise your hand to speak",
            "Following rules makes our community better",
        ],
        [
            {
                "title": "Examples",
                "content": "School rules: be kind, listen to teacher, walk in hallways. Home rules: clean up toys, be respectful",
            }
        ],
        "builtin",
        None,
        1,
    )

    lesson_id = add_lesson(
        rules_id,
        "Laws in Our Community",
        "Learn about laws and why we need them",
        [
            "Law: a rule that everyone must follow",
            "Laws are made by government leaders",
            "Laws help keep our community safe and fair",
            "Examples: don't steal, don't hurt others, follow traffic signs",
            "Breaking laws can have serious consequences",
        ],
        [
            {
                "title": "Examples",
                "content": "Traffic laws: stop at red lights, wear seatbelts. Safety laws: don't play with matches, don't talk to strangers",
            }
        ],
        "builtin",
        None,
        1,
    )

    # Different Cultures
    lesson_id = add_lesson(
        culture_id,
        "What is Culture?",
        "Learn about different ways of life",
        [
            "Culture: the way a group of people live",
            "Culture includes: food, clothing, language, traditions",
            "Different places have different cultures",
            "Learning about other cultures helps us understand the world",
            "We should respect all cultures",
        ],
        [
            {
                "title": "Examples",
                "content": "Food: pizza (Italy), tacos (Mexico), sushi (Japan). Clothing: kimono (Japan), sari (India), lederhosen (Germany)",
            }
        ],
        "builtin",
        None,
        1,
    )

    lesson_id = add_lesson(
        culture_id,
        "Languages Around the World",
        "Learn about different languages",
        [
            "Language: how people communicate with words",
            "Different countries speak different languages",
            "Examples: English, Spanish, French, Chinese, Arabic",
            "Learning other languages helps us connect with more people",
            "Many people speak more than one language",
        ],
        [
            {
                "title": "Examples",
                "content": "English: United States, United Kingdom. Spanish: Mexico, Spain. French: France, Canada. Chinese: China",
            }
        ],
        "builtin",
        None,
        1,
    )

    # Past & Present
    lesson_id = add_lesson(
        time_id,
        "Life Long Ago",
        "Learn about how people lived in the past",
        [
            "Past: time that has already happened",
            "People long ago lived differently than we do today",
            "Examples: no electricity, no cars, no computers",
            "People had to work harder to do everyday things",
            "We can learn from how people lived in the past",
        ],
        [
            {
                "title": "Examples",
                "content": "Transportation: horses and wagons instead of cars. Communication: letters instead of phones. Entertainment: books and games instead of TV",
            }
        ],
        "builtin",
        None,
        1,
    )

    lesson_id = add_lesson(
        time_id,
        "How Things Have Changed",
        "Compare life in the past and present",
        [
            "Present: time right now",
            "Many things have changed over time",
            "Technology has made life easier in many ways",
            "Some things stay the same: family, friends, learning",
            "Change can be good and help us grow",
        ],
        [
            {
                "title": "Examples",
                "content": "Past: wash clothes by hand. Present: washing machine. Past: send letters. Present: email and text messages",
            }
        ],
        "builtin",
        None,
        1,
    )


def seed_grade2_social_lessons(geography_id, government_id, economics_id, history_id):
    """Seed Grade 2 social studies lessons."""

    # World Geography
    lesson_id = add_lesson(
        geography_id,
        "Continents and Oceans",
        "Learn about Earth's major land and water features",
        [
            "Continent: large landmass on Earth",
            "There are 7 continents: North America, South America, Europe, Asia, Africa, Australia, Antarctica",
            "Ocean: large body of salt water",
            "There are 5 oceans: Pacific, Atlantic, Indian, Arctic, Southern",
            "Continents and oceans help us understand where places are located",
        ],
        [
            {
                "title": "Examples",
                "content": "North America: United States, Canada, Mexico. Asia: China, India, Japan. Pacific Ocean: largest ocean",
            }
        ],
        "builtin",
        None,
        1,
    )

    lesson_id = add_lesson(
        geography_id,
        "Countries and Capitals",
        "Learn about different countries and their capitals",
        [
            "Country: a nation with its own government",
            "Capital: the main city where government is located",
            "Examples: United States (Washington D.C.), France (Paris), Japan (Tokyo)",
            "Each country has its own flag, language, and culture",
            "Learning about countries helps us understand the world",
        ],
        [
            {
                "title": "Examples",
                "content": "United States: Washington D.C. France: Paris. Japan: Tokyo. Brazil: Brasília. Australia: Canberra",
            }
        ],
        "builtin",
        None,
        1,
    )

    # Local Government
    lesson_id = add_lesson(
        government_id,
        "What is Government?",
        "Learn about how government works",
        [
            "Government: group of people who make rules and decisions for a community",
            "Government helps keep people safe and provides services",
            "Examples of government services: schools, roads, police, fire department",
            "Government leaders are chosen by the people",
            "We all have a role in our government",
        ],
        [
            {
                "title": "Examples",
                "content": "Local government: mayor, city council. State government: governor, state legislature. National government: president, Congress",
            }
        ],
        "builtin",
        None,
        1,
    )

    lesson_id = add_lesson(
        government_id,
        "Local Leaders",
        "Learn about leaders in our community",
        [
            "Mayor: leader of a city or town",
            "City Council: group that makes laws for the city",
            "School Board: group that makes decisions about schools",
            "These leaders work to help our community",
            "We can vote for leaders when we grow up",
        ],
        [
            {
                "title": "Examples",
                "content": "Mayor: runs the city, makes speeches, meets with people. City Council: votes on laws, decides how to spend money",
            }
        ],
        "builtin",
        None,
        1,
    )

    # Needs & Wants
    lesson_id = add_lesson(
        economics_id,
        "Needs vs Wants",
        "Learn the difference between needs and wants",
        [
            "Need: something we must have to survive",
            "Want: something we would like to have",
            "Examples of needs: food, water, shelter, clothing",
            "Examples of wants: toys, games, candy, movies",
            "We should focus on needs first, then wants",
        ],
        [
            {
                "title": "Examples",
                "content": "Needs: healthy food, clean water, safe home, warm clothes. Wants: video games, ice cream, new toys, fancy clothes",
            }
        ],
        "builtin",
        None,
        1,
    )

    lesson_id = add_lesson(
        economics_id,
        "Money and Jobs",
        "Learn about earning and spending money",
        [
            "Money: what we use to buy things",
            "Job: work that people do to earn money",
            "Examples of jobs: teacher, doctor, firefighter, store clerk",
            "People work to earn money to buy things they need and want",
            "It's important to save money for the future",
        ],
        [
            {
                "title": "Examples",
                "content": "Jobs: teacher (helps students learn), doctor (helps sick people), firefighter (puts out fires), store clerk (helps customers)",
            }
        ],
        "builtin",
        None,
        1,
    )

    # American History
    lesson_id = add_lesson(
        history_id,
        "Native Americans",
        "Learn about the first people in America",
        [
            "Native Americans: first people to live in America",
            "They lived here for thousands of years before Europeans came",
            "Different tribes lived in different parts of America",
            "They had their own languages, cultures, and ways of life",
            "We should respect and learn from Native American culture",
        ],
        [
            {
                "title": "Examples",
                "content": "Plains tribes: lived in tipis, hunted buffalo. Southwest tribes: lived in pueblos, farmed corn. Northeast tribes: lived in longhouses, fished",
            }
        ],
        "builtin",
        None,
        1,
    )

    lesson_id = add_lesson(
        history_id,
        "Explorers and Settlers",
        "Learn about people who came to America",
        [
            "Explorer: person who travels to discover new places",
            "Settler: person who moves to a new place to live",
            "Christopher Columbus: famous explorer who sailed to America",
            "Many people came to America looking for new opportunities",
            "These people helped build the country we have today",
        ],
        [
            {
                "title": "Examples",
                "content": "Christopher Columbus: sailed in 1492. Pilgrims: came on Mayflower in 1620. Other settlers: came from many different countries",
            }
        ],
        "builtin",
        None,
        1,
    )


def seed_grade3_social_lessons(
    communities_id, immigration_id, native_id, environment_id
):
    """Seed Grade 3 social studies lessons."""

    # Types of Communities
    lesson_id = add_lesson(
        communities_id,
        "Urban Communities",
        "Learn about city life",
        [
            "Urban: city with many people and tall buildings",
            "Features: skyscrapers, subways, busy streets, many jobs",
            "Advantages: many services, entertainment, jobs",
            "Challenges: traffic, noise, expensive housing",
            "Examples: New York City, Los Angeles, Chicago",
        ],
        [
            {
                "title": "Examples",
                "content": "Urban features: apartment buildings, office towers, public transportation, museums, theaters, restaurants",
            }
        ],
        "builtin",
        None,
        1,
    )

    lesson_id = add_lesson(
        communities_id,
        "Suburban Communities",
        "Learn about life outside the city",
        [
            "Suburban: area between city and countryside",
            "Features: houses with yards, shopping centers, schools",
            "Advantages: more space, quieter, good schools",
            "Challenges: need to drive everywhere, less public transportation",
            "Many families choose to live in suburbs",
        ],
        [
            {
                "title": "Examples",
                "content": "Suburban features: single-family homes, driveways, shopping malls, parks, good schools, less traffic",
            }
        ],
        "builtin",
        None,
        1,
    )

    lesson_id = add_lesson(
        communities_id,
        "Rural Communities",
        "Learn about country life",
        [
            "Rural: countryside with farms and open spaces",
            "Features: farms, small towns, wide open spaces",
            "Advantages: peaceful, close to nature, less pollution",
            "Challenges: fewer services, need to travel for shopping",
            "Examples: farming communities, small towns",
        ],
        [
            {
                "title": "Examples",
                "content": "Rural features: farms, barns, tractors, small schools, general stores, wide open fields",
            }
        ],
        "builtin",
        None,
        1,
    )

    # Immigration & Diversity
    lesson_id = add_lesson(
        immigration_id,
        "Why People Immigrate",
        "Learn about reasons people come to America",
        [
            "Immigration: moving to a new country to live",
            "Reasons: better opportunities, freedom, family, safety",
            "America is called 'melting pot' because of all the different cultures",
            "Immigrants bring their traditions and skills",
            "Immigration has made America stronger and more diverse",
        ],
        [
            {
                "title": "Examples",
                "content": "Reasons: better jobs, religious freedom, escaping war, joining family, better education for children",
            }
        ],
        "builtin",
        None,
        1,
    )

    lesson_id = add_lesson(
        immigration_id,
        "Ellis Island",
        "Learn about the gateway to America",
        [
            "Ellis Island: place where many immigrants entered America",
            "Located in New York Harbor",
            "Millions of people passed through Ellis Island",
            "Immigrants were checked for health and documents",
            "Ellis Island represents hope and new beginnings",
        ],
        [
            {
                "title": "Examples",
                "content": "Process: ship arrives, health inspection, document check, questions, either admitted or sent back",
            }
        ],
        "builtin",
        None,
        1,
    )

    # Native American Cultures
    lesson_id = add_lesson(
        native_id,
        "Native American Tribes",
        "Learn about different Native American groups",
        [
            "Many different tribes lived across America",
            "Each tribe had its own culture, language, and traditions",
            "Examples: Cherokee, Sioux, Navajo, Iroquois",
            "Tribes adapted to their environment",
            "We should respect and honor Native American heritage",
        ],
        [
            {
                "title": "Examples",
                "content": "Cherokee: lived in Southeast, farmed corn. Sioux: lived on Plains, hunted buffalo. Navajo: lived in Southwest, raised sheep",
            }
        ],
        "builtin",
        None,
        1,
    )

    lesson_id = add_lesson(
        native_id,
        "Native American Contributions",
        "Learn about what Native Americans gave us",
        [
            "Native Americans taught settlers many important things",
            "Examples: farming techniques, food, medicine, art",
            "Foods: corn, potatoes, tomatoes, chocolate",
            "We should appreciate and remember these contributions",
            "Native American culture is still alive today",
        ],
        [
            {
                "title": "Examples",
                "content": "Food: corn, beans, squash, potatoes, tomatoes. Medicine: herbal remedies, healing practices. Art: pottery, weaving, jewelry",
            }
        ],
        "builtin",
        None,
        1,
    )

    # Human-Environment Interaction
    lesson_id = add_lesson(
        environment_id,
        "How People Use Land",
        "Learn about how humans change the environment",
        [
            "People change the environment to meet their needs",
            "Examples: building cities, farming, mining",
            "Some changes are good, some can cause problems",
            "We need to think about how our actions affect the environment",
            "We should try to protect the environment for future generations",
        ],
        [
            {
                "title": "Examples",
                "content": "Good changes: planting trees, building parks, recycling. Problems: pollution, cutting down forests, building on wetlands",
            }
        ],
        "builtin",
        None,
        1,
    )

    lesson_id = add_lesson(
        environment_id,
        "Natural Resources",
        "Learn about Earth's gifts to us",
        [
            "Natural resource: something from nature that people use",
            "Examples: water, trees, minerals, oil, soil",
            "Some resources are renewable, others are not",
            "We need to use resources wisely",
            "Conservation: using resources carefully so they don't run out",
        ],
        [
            {
                "title": "Examples",
                "content": "Renewable: trees, water, wind, solar energy. Nonrenewable: oil, coal, natural gas, minerals",
            }
        ],
        "builtin",
        None,
        1,
    )


def seed_grade4_social_lessons(
    states_id, colonization_id, revolution_id, constitution_id
):
    """Seed Grade 4 social studies lessons."""

    # United States Geography
    lesson_id = add_lesson(
        states_id,
        "The 50 States",
        "Learn about all the states in America",
        [
            "United States has 50 states",
            "Each state has its own government and capital",
            "States are grouped into regions: Northeast, Southeast, Midwest, Southwest, West",
            "Each state has unique features: geography, history, culture",
            "Learning about states helps us understand our country",
        ],
        [
            {
                "title": "Examples",
                "content": "Northeast: New York, Massachusetts, Maine. Southeast: Florida, Georgia, Texas. Midwest: Illinois, Ohio, Michigan",
            }
        ],
        "builtin",
        None,
        1,
    )

    lesson_id = add_lesson(
        states_id,
        "State Capitals and Features",
        "Learn about state capitals and landmarks",
        [
            "Capital: main city where state government is located",
            "Each state has important landmarks and features",
            "Examples: Grand Canyon (Arizona), Statue of Liberty (New York)",
            "States have different climates, geography, and resources",
            "These differences make each state special",
        ],
        [
            {
                "title": "Examples",
                "content": "California: Sacramento (capital), Hollywood, Silicon Valley. Texas: Austin (capital), oil, cattle. Florida: Tallahassee (capital), beaches, oranges",
            }
        ],
        "builtin",
        None,
        1,
    )

    # Colonial America
    lesson_id = add_lesson(
        colonization_id,
        "The 13 Colonies",
        "Learn about the original American colonies",
        [
            "Colony: settlement in a new land controlled by another country",
            "13 colonies were established by England",
            "Colonies were divided into three regions: New England, Middle, Southern",
            "Each region had different geography, economy, and culture",
            "Colonies were the beginning of what became the United States",
        ],
        [
            {
                "title": "Examples",
                "content": "New England: Massachusetts, New Hampshire, Connecticut (fishing, shipbuilding). Middle: New York, Pennsylvania, New Jersey (farming, trade). Southern: Virginia, Georgia, South Carolina (plantations, slavery)",
            }
        ],
        "builtin",
        None,
        1,
    )

    lesson_id = add_lesson(
        colonization_id,
        "Life in the Colonies",
        "Learn about daily life in colonial times",
        [
            "Colonial life was very different from today",
            "Most people were farmers",
            "Children had to work hard and help their families",
            "Education was limited, especially for girls",
            "People made most things by hand",
        ],
        [
            {
                "title": "Examples",
                "content": "Work: farming, blacksmithing, weaving, carpentry. Education: boys learned reading, writing, arithmetic. Girls learned household skills",
            }
        ],
        "builtin",
        None,
        1,
    )

    # American Revolution
    lesson_id = add_lesson(
        revolution_id,
        "Causes of the Revolution",
        "Learn why the colonies wanted independence",
        [
            "Revolution: when people fight to change their government",
            "Colonists were angry about British taxes and laws",
            "No taxation without representation: colonists wanted a say in government",
            "Important events: Boston Tea Party, Boston Massacre",
            "These events led to the Revolutionary War",
        ],
        [
            {
                "title": "Examples",
                "content": "Taxes: Stamp Act, Tea Act, Townshend Acts. Protests: Boston Tea Party (1773), Boston Massacre (1770)",
            }
        ],
        "builtin",
        None,
        1,
    )

    lesson_id = add_lesson(
        revolution_id,
        "Key People of the Revolution",
        "Learn about important leaders",
        [
            "George Washington: leader of the Continental Army",
            "Thomas Jefferson: wrote the Declaration of Independence",
            "Benjamin Franklin: inventor and diplomat",
            "Paul Revere: warned about British attack",
            "These leaders helped America win independence",
        ],
        [
            {
                "title": "Examples",
                "content": "George Washington: first president, led army. Thomas Jefferson: wrote Declaration, third president. Benjamin Franklin: lightning rod, helped with Constitution",
            }
        ],
        "builtin",
        None,
        1,
    )

    # Constitution & Government
    lesson_id = add_lesson(
        constitution_id,
        "The Constitution",
        "Learn about America's founding document",
        [
            "Constitution: the plan for how our government works",
            "Written in 1787, it's still used today",
            "Sets up three branches of government",
            "Includes the Bill of Rights (first 10 amendments)",
            "The Constitution protects our freedoms",
        ],
        [
            {
                "title": "Examples",
                "content": "Three branches: Executive (President), Legislative (Congress), Judicial (Courts). Bill of Rights: freedom of speech, religion, press",
            }
        ],
        "builtin",
        None,
        1,
    )

    lesson_id = add_lesson(
        constitution_id,
        "Three Branches of Government",
        "Learn how government is organized",
        [
            "Executive Branch: led by the President, enforces laws",
            "Legislative Branch: Congress makes laws",
            "Judicial Branch: courts interpret laws",
            "Each branch has different powers",
            "This system prevents any one branch from becoming too powerful",
        ],
        [
            {
                "title": "Examples",
                "content": "Executive: President, Vice President, Cabinet. Legislative: House of Representatives, Senate. Judicial: Supreme Court, federal courts",
            }
        ],
        "builtin",
        None,
        1,
    )


def seed_grade5_social_lessons(
    westward_id, civil_war_id, industrial_id, immigration_id
):
    """Seed Grade 5 social studies lessons."""

    # Westward Expansion
    lesson_id = add_lesson(
        westward_id,
        "Manifest Destiny",
        "Learn about America's westward growth",
        [
            "Manifest Destiny: belief that America should expand to the Pacific",
            "Americans moved west for land, gold, and opportunity",
            "Important events: Louisiana Purchase, Lewis and Clark expedition",
            "Westward expansion changed America forever",
            "It also caused conflicts with Native Americans",
        ],
        [
            {
                "title": "Examples",
                "content": "Louisiana Purchase (1803): doubled size of America. Lewis and Clark (1804-1806): explored new territory. Gold Rush (1849): brought thousands to California",
            }
        ],
        "builtin",
        None,
        1,
    )

    lesson_id = add_lesson(
        westward_id,
        "Pioneers and Settlers",
        "Learn about people who moved west",
        [
            "Pioneer: person who is first to settle in a new area",
            "Settlers faced many challenges: harsh weather, disease, conflicts",
            "They traveled in covered wagons on trails like the Oregon Trail",
            "Pioneers had to be brave and resourceful",
            "Their courage helped build America",
        ],
        [
            {
                "title": "Examples",
                "content": "Oregon Trail: 2,000 miles, took 4-6 months. Challenges: river crossings, mountain passes, disease, Native American attacks",
            }
        ],
        "builtin",
        None,
        1,
    )

    # Civil War & Reconstruction
    lesson_id = add_lesson(
        civil_war_id,
        "Causes of the Civil War",
        "Learn why the Civil War happened",
        [
            "Civil War: war between the North and South (1861-1865)",
            "Main cause: disagreement about slavery",
            "North: wanted to end slavery",
            "South: wanted to keep slavery",
            "Other issues: states' rights, economic differences",
        ],
        [
            {
                "title": "Examples",
                "content": "Slavery: North (free states) vs South (slave states). States' rights: South wanted more power, North wanted stronger federal government",
            }
        ],
        "builtin",
        None,
        1,
    )

    lesson_id = add_lesson(
        civil_war_id,
        "Key Events of the Civil War",
        "Learn about important battles and people",
        [
            "Abraham Lincoln: President during the Civil War",
            "Important battles: Gettysburg, Antietam, Vicksburg",
            "Emancipation Proclamation: freed slaves in Confederate states",
            "War ended in 1865 with Union victory",
            "Over 600,000 people died in the war",
        ],
        [
            {
                "title": "Examples",
                "content": "Gettysburg (1863): turning point of war. Emancipation Proclamation (1863): freed slaves. Appomattox (1865): war ended",
            }
        ],
        "builtin",
        None,
        1,
    )

    # Industrial Revolution
    lesson_id = add_lesson(
        industrial_id,
        "Inventions and Technology",
        "Learn about new inventions that changed America",
        [
            "Industrial Revolution: time when machines changed how things were made",
            "Important inventions: steam engine, cotton gin, telegraph",
            "Factories: places where machines made goods",
            "These changes made goods cheaper and faster to produce",
            "Industrial Revolution changed how people lived and worked",
        ],
        [
            {
                "title": "Examples",
                "content": "Steam engine: powered trains and factories. Cotton gin: made cotton processing faster. Telegraph: allowed instant communication",
            }
        ],
        "builtin",
        None,
        1,
    )

    lesson_id = add_lesson(
        industrial_id,
        "Growth of Cities",
        "Learn about urbanization and its effects",
        [
            "Urbanization: growth of cities",
            "People moved from farms to cities for factory jobs",
            "Cities grew quickly but had problems: overcrowding, pollution",
            "New technologies: electricity, telephone, automobiles",
            "This period shaped modern America",
        ],
        [
            {
                "title": "Examples",
                "content": "Problems: tenement housing, child labor, unsafe working conditions. Solutions: labor unions, safety laws, public education",
            }
        ],
        "builtin",
        None,
        1,
    )

    # Immigration & Urbanization
    lesson_id = add_lesson(
        immigration_id,
        "Waves of Immigration",
        "Learn about different groups who came to America",
        [
            "First wave (1840s-1860s): Irish and German immigrants",
            "Second wave (1880s-1920s): Southern and Eastern Europeans",
            "Immigrants came for jobs, freedom, and opportunity",
            "They faced discrimination but helped build America",
            "Immigration laws changed over time",
        ],
        [
            {
                "title": "Examples",
                "content": "Irish: came during potato famine, worked on railroads. Italians: came for factory jobs, built cities. Jews: came escaping persecution, started businesses",
            }
        ],
        "builtin",
        None,
        1,
    )

    lesson_id = add_lesson(
        immigration_id,
        "Life in the Cities",
        "Learn about urban life during this period",
        [
            "Cities were crowded and busy",
            "Immigrants often lived in ethnic neighborhoods",
            "Problems: disease, crime, poor housing",
            "Solutions: settlement houses, public health, education",
            "Cities became centers of culture and opportunity",
        ],
        [
            {
                "title": "Examples",
                "content": "Neighborhoods: Little Italy, Chinatown, Jewish Quarter. Problems: tenements, disease, child labor. Solutions: Hull House, public schools, health departments",
            }
        ],
        "builtin",
        None,
        1,
    )


def seed_grade6_social_lessons(ancient_id, medieval_id, renaissance_id, economics_id):
    """Seed Grade 6 social studies lessons."""

    # Ancient Civilizations
    lesson_id = add_lesson(
        ancient_id,
        "Ancient Egypt",
        "Learn about the civilization along the Nile",
        [
            "Ancient Egypt: civilization that lasted 3,000 years",
            "Located along the Nile River in Africa",
            "Famous for: pyramids, pharaohs, hieroglyphics",
            "Achievements: mathematics, medicine, architecture",
            "Egyptian culture influenced many other civilizations",
        ],
        [
            {
                "title": "Examples",
                "content": "Pyramids: tombs for pharaohs, built with precise mathematics. Hieroglyphics: picture writing system. Pharaohs: god-kings who ruled Egypt",
            }
        ],
        "builtin",
        None,
        1,
    )

    lesson_id = add_lesson(
        ancient_id,
        "Ancient Greece",
        "Learn about the birthplace of democracy",
        [
            "Ancient Greece: civilization that influenced Western culture",
            "Located in southeastern Europe",
            "Famous for: democracy, philosophy, Olympics, architecture",
            "Important people: Socrates, Plato, Aristotle, Alexander the Great",
            "Greek ideas about government and philosophy still influence us today",
        ],
        [
            {
                "title": "Examples",
                "content": "Democracy: government by the people, started in Athens. Philosophy: love of wisdom, questioning everything. Olympics: athletic competitions every 4 years",
            }
        ],
        "builtin",
        None,
        1,
    )

    lesson_id = add_lesson(
        ancient_id,
        "Ancient Rome",
        "Learn about the empire that ruled the Mediterranean",
        [
            "Ancient Rome: empire that controlled much of Europe, Africa, and Asia",
            "Started as a city-state, grew into a huge empire",
            "Famous for: roads, aqueducts, law, military",
            "Roman law and government influenced many countries",
            "Empire fell in 476 AD, but its influence continues",
        ],
        [
            {
                "title": "Examples",
                "content": "Roads: connected empire, 'All roads lead to Rome'. Aqueducts: brought water to cities. Law: 'innocent until proven guilty'",
            }
        ],
        "builtin",
        None,
        1,
    )

    # Medieval Times
    lesson_id = add_lesson(
        medieval_id,
        "Feudalism and the Middle Ages",
        "Learn about life in medieval Europe",
        [
            "Middle Ages: period from 500-1500 AD",
            "Feudalism: system where lords owned land and peasants worked it",
            "Society was organized in a hierarchy: king, lords, knights, peasants",
            "Life was difficult for most people",
            "This period was between ancient times and modern times",
        ],
        [
            {
                "title": "Examples",
                "content": "King: ruled the kingdom. Lords: owned land, provided protection. Knights: fought for lords. Peasants: worked the land, paid taxes",
            }
        ],
        "builtin",
        None,
        1,
    )

    lesson_id = add_lesson(
        medieval_id,
        "The Crusades",
        "Learn about religious wars between Christians and Muslims",
        [
            "Crusades: series of wars between Christians and Muslims",
            "Fought over control of the Holy Land (Jerusalem)",
            "Lasted from 1095-1291",
            "Results: increased trade, cultural exchange, and conflict",
            "The Crusades connected Europe with the Middle East",
        ],
        [
            {
                "title": "Examples",
                "content": "First Crusade (1095-1099): captured Jerusalem. Effects: new foods, spices, and ideas brought to Europe",
            }
        ],
        "builtin",
        None,
        1,
    )

    # Renaissance & Exploration
    lesson_id = add_lesson(
        renaissance_id,
        "The Renaissance",
        "Learn about the rebirth of learning and art",
        [
            "Renaissance: period of renewed interest in learning and art",
            "Started in Italy around 1400",
            "Famous artists: Leonardo da Vinci, Michelangelo, Raphael",
            "New ideas about science, art, and human potential",
            "The Renaissance marked the beginning of modern times",
        ],
        [
            {
                "title": "Examples",
                "content": "Leonardo da Vinci: Mona Lisa, flying machines. Michelangelo: Sistine Chapel, David statue. Raphael: beautiful paintings",
            }
        ],
        "builtin",
        None,
        1,
    )

    lesson_id = add_lesson(
        renaissance_id,
        "Age of Exploration",
        "Learn about European exploration of the world",
        [
            "Age of Exploration: period when Europeans explored new lands",
            "Famous explorers: Columbus, Magellan, da Gama",
            "Motives: find new trade routes, spread Christianity, gain wealth",
            "Results: new lands discovered, cultures met, trade expanded",
            "Exploration connected all parts of the world",
        ],
        [
            {
                "title": "Examples",
                "content": "Columbus (1492): reached America. Magellan (1519-1522): first to sail around the world. da Gama (1498): found sea route to India",
            }
        ],
        "builtin",
        None,
        1,
    )

    # Economics & Trade
    lesson_id = add_lesson(
        economics_id,
        "Trade and Commerce",
        "Learn about how people exchange goods and services",
        [
            "Trade: exchange of goods and services",
            "Commerce: buying and selling of goods",
            "Trade routes: paths that traders used to move goods",
            "Examples: Silk Road, spice trade, triangular trade",
            "Trade has connected different cultures throughout history",
        ],
        [
            {
                "title": "Examples",
                "content": "Silk Road: connected China and Europe. Spice trade: brought spices from Asia to Europe. Triangular trade: connected Europe, Africa, and America",
            }
        ],
        "builtin",
        None,
        1,
    )

    lesson_id = add_lesson(
        economics_id,
        "Economic Systems",
        "Learn about different ways societies organize their economies",
        [
            "Economic system: how a society organizes production and distribution",
            "Traditional: based on customs and traditions",
            "Market: based on supply and demand",
            "Command: government controls the economy",
            "Mixed: combination of market and command systems",
        ],
        [
            {
                "title": "Examples",
                "content": "Traditional: farming communities, barter system. Market: United States, supply and demand. Command: former Soviet Union, government control",
            }
        ],
        "builtin",
        None,
        1,
    )


def seed_grade7_social_lessons(world_war_id, cold_war_id, civil_rights_id, global_id):
    """Seed Grade 7 social studies lessons."""

    # World Wars
    lesson_id = add_lesson(
        world_war_id,
        "World War I",
        "Learn about the Great War",
        [
            "World War I: 1914-1918, called the Great War",
            "Causes: alliances, imperialism, militarism, nationalism",
            "Major powers: Allies vs Central Powers",
            "New weapons: machine guns, tanks, poison gas",
            "Results: millions died, empires fell, new countries formed",
        ],
        [
            {
                "title": "Examples",
                "content": "Allies: Britain, France, Russia, United States. Central Powers: Germany, Austria-Hungary, Ottoman Empire. New weapons: changed warfare forever",
            }
        ],
        "builtin",
        None,
        1,
    )

    lesson_id = add_lesson(
        world_war_id,
        "World War II",
        "Learn about the deadliest war in history",
        [
            "World War II: 1939-1945, involved most of the world",
            "Causes: Treaty of Versailles, rise of dictators, economic depression",
            "Major powers: Allies vs Axis",
            "Holocaust: systematic murder of 6 million Jews",
            "Results: United Nations formed, Cold War began",
        ],
        [
            {
                "title": "Examples",
                "content": "Allies: United States, Britain, Soviet Union. Axis: Germany, Japan, Italy. Holocaust: Nazi genocide of Jews and others",
            }
        ],
        "builtin",
        None,
        1,
    )

    # Cold War Era
    lesson_id = add_lesson(
        cold_war_id,
        "The Cold War",
        "Learn about the conflict between the US and Soviet Union",
        [
            "Cold War: tension between United States and Soviet Union (1945-1991)",
            "Not a shooting war, but competition and conflict",
            "US: democracy and capitalism",
            "Soviet Union: communism and command economy",
            "Both sides built nuclear weapons",
        ],
        [
            {
                "title": "Examples",
                "content": "Competition: space race, arms race, proxy wars. Events: Berlin Wall, Cuban Missile Crisis, Vietnam War",
            }
        ],
        "builtin",
        None,
        1,
    )

    lesson_id = add_lesson(
        cold_war_id,
        "Space Race and Technology",
        "Learn about competition in space and technology",
        [
            "Space Race: competition between US and Soviet Union in space",
            "Soviet Union: first satellite (Sputnik), first human in space",
            "United States: first human on moon",
            "Technology advances: computers, satellites, nuclear power",
            "Space exploration continues today",
        ],
        [
            {
                "title": "Examples",
                "content": "Sputnik (1957): first satellite. Yuri Gagarin (1961): first human in space. Apollo 11 (1969): first humans on moon",
            }
        ],
        "builtin",
        None,
        1,
    )

    # Civil Rights Movement
    lesson_id = add_lesson(
        civil_rights_id,
        "Segregation and Jim Crow",
        "Learn about racial discrimination in America",
        [
            "Segregation: separation of people by race",
            "Jim Crow laws: laws that enforced segregation",
            "Separate facilities: schools, restaurants, transportation",
            "African Americans were treated as second-class citizens",
            "This system was unfair and unconstitutional",
        ],
        [
            {
                "title": "Examples",
                "content": "Separate schools: white and black children couldn't go to same school. Separate transportation: blacks had to sit in back of bus",
            }
        ],
        "builtin",
        None,
        1,
    )

    lesson_id = add_lesson(
        civil_rights_id,
        "Civil Rights Leaders and Events",
        "Learn about the fight for equality",
        [
            "Civil Rights Movement: fight for equal rights for African Americans",
            "Key leaders: Martin Luther King Jr., Rosa Parks, Malcolm X",
            "Important events: Montgomery Bus Boycott, March on Washington",
            "Results: Civil Rights Act, Voting Rights Act",
            "The movement changed America forever",
        ],
        [
            {
                "title": "Examples",
                "content": "Rosa Parks (1955): refused to give up bus seat. MLK Jr.: 'I Have a Dream' speech. March on Washington (1963): 250,000 people",
            }
        ],
        "builtin",
        None,
        1,
    )

    # Globalization
    lesson_id = add_lesson(
        global_id,
        "Globalization",
        "Learn about our connected world",
        [
            "Globalization: increasing connection between countries",
            "Factors: technology, transportation, communication",
            "Effects: global trade, cultural exchange, international cooperation",
            "Benefits: more goods, cultural diversity, economic growth",
            "Challenges: environmental problems, economic inequality",
        ],
        [
            {
                "title": "Examples",
                "content": "Technology: internet, smartphones connect people worldwide. Trade: goods made in one country, sold in another. Culture: music, food, ideas spread globally",
            }
        ],
        "builtin",
        None,
        1,
    )

    lesson_id = add_lesson(
        global_id,
        "International Organizations",
        "Learn about groups that work together globally",
        [
            "International organization: group of countries working together",
            "United Nations: promotes peace and cooperation",
            "World Trade Organization: regulates international trade",
            "European Union: economic and political union in Europe",
            "These organizations help solve global problems",
        ],
        [
            {
                "title": "Examples",
                "content": "UN: peacekeeping, human rights, development. WTO: trade rules, dispute settlement. EU: common currency, free movement",
            }
        ],
        "builtin",
        None,
        1,
    )


def seed_grade8_social_lessons(government_id, civics_id, economics_id, current_id):
    """Seed Grade 8 social studies lessons."""

    # American Government
    lesson_id = add_lesson(
        government_id,
        "The Constitution and Bill of Rights",
        "Learn about America's founding principles",
        [
            "Constitution: supreme law of the United States",
            "Bill of Rights: first 10 amendments protecting individual freedoms",
            "Separation of powers: three branches of government",
            "Checks and balances: each branch limits the others",
            "Federalism: power shared between national and state governments",
        ],
        [
            {
                "title": "Examples",
                "content": "Bill of Rights: freedom of speech, religion, press, assembly. Three branches: Executive (President), Legislative (Congress), Judicial (Courts)",
            }
        ],
        "builtin",
        None,
        1,
    )

    lesson_id = add_lesson(
        government_id,
        "How Laws Are Made",
        "Learn about the legislative process",
        [
            "Bill: proposed law",
            "Process: introduced in Congress, debated, voted on",
            "Both houses must pass the same version",
            "President can sign or veto the bill",
            "Supreme Court can declare laws unconstitutional",
        ],
        [
            {
                "title": "Example",
                "content": "Process: Bill introduced → Committee review → House vote → Senate vote → Conference committee → President signature → Law",
            }
        ],
        "builtin",
        None,
        1,
    )

    # Civics & Citizenship
    lesson_id = add_lesson(
        civics_id,
        "Rights and Responsibilities",
        "Learn about what it means to be a citizen",
        [
            "Rights: freedoms guaranteed to citizens",
            "Responsibilities: duties citizens should fulfill",
            "Examples of rights: vote, free speech, fair trial",
            "Examples of responsibilities: vote, pay taxes, serve on juries",
            "Good citizens participate in their community",
        ],
        [
            {
                "title": "Examples",
                "content": "Rights: vote, free speech, practice religion, fair trial. Responsibilities: vote, pay taxes, serve on jury, follow laws",
            }
        ],
        "builtin",
        None,
        1,
    )

    lesson_id = add_lesson(
        civics_id,
        "Voting and Elections",
        "Learn about how democracy works",
        [
            "Voting: way citizens choose their leaders",
            "Elections: process of choosing leaders",
            "Types: local, state, national elections",
            "Voting is a right and responsibility",
            "Every vote counts in a democracy",
        ],
        [
            {
                "title": "Examples",
                "content": "Local: mayor, city council, school board. State: governor, state legislature. National: president, Congress",
            }
        ],
        "builtin",
        None,
        1,
    )

    # Economics & Personal Finance
    lesson_id = add_lesson(
        economics_id,
        "Supply and Demand",
        "Learn about how prices are determined",
        [
            "Supply: how much of a product is available",
            "Demand: how much people want a product",
            "Price: determined by supply and demand",
            "High demand + low supply = high price",
            "Low demand + high supply = low price",
        ],
        [
            {
                "title": "Examples",
                "content": "High demand: new iPhone, concert tickets. High supply: basic food items, common books. Price changes: gas prices, housing prices",
            }
        ],
        "builtin",
        None,
        1,
    )

    lesson_id = add_lesson(
        economics_id,
        "Personal Finance",
        "Learn about managing money",
        [
            "Budget: plan for spending and saving money",
            "Income: money you earn",
            "Expenses: money you spend",
            "Savings: money you set aside for the future",
            "Good financial habits help you achieve your goals",
        ],
        [
            {
                "title": "Examples",
                "content": "Income: job, allowance, gifts. Expenses: food, housing, transportation, entertainment. Savings: emergency fund, college, retirement",
            }
        ],
        "builtin",
        None,
        1,
    )

    # Current Events
    lesson_id = add_lesson(
        current_id,
        "Analyzing Current Events",
        "Learn how to understand news and events",
        [
            "Current events: things happening in the world today",
            "News sources: newspapers, TV, internet, radio",
            "Important to get news from reliable sources",
            "Consider different perspectives on issues",
            "Being informed helps you be a good citizen",
        ],
        [
            {
                "title": "Examples",
                "content": "Reliable sources: major newspapers, public broadcasting, fact-checking websites. Different perspectives: read multiple sources, consider bias",
            }
        ],
        "builtin",
        None,
        1,
    )

    lesson_id = add_lesson(
        current_id,
        "Global Issues",
        "Learn about challenges facing the world today",
        [
            "Global issues: problems that affect many countries",
            "Examples: climate change, poverty, disease, conflict",
            "These problems require international cooperation",
            "Young people can help solve these problems",
            "Understanding global issues makes you a better citizen",
        ],
        [
            {
                "title": "Examples",
                "content": "Climate change: global warming, rising sea levels. Poverty: lack of basic needs, education, healthcare. Disease: pandemics, access to medicine",
            }
        ],
        "builtin",
        None,
        1,
    )


def seed_advanced_social_lessons(
    world_history_id, political_science_id, sociology_id, anthropology_id
):
    """Seed advanced social studies lessons."""

    # World History
    lesson_id = add_lesson(
        world_history_id,
        "Major Historical Periods",
        "Study the major eras of world history",
        [
            "Prehistory: before written records",
            "Ancient: early civilizations (3000 BC - 500 AD)",
            "Medieval: Middle Ages (500 - 1500 AD)",
            "Modern: Renaissance to present (1500 - present)",
            "Each period had unique characteristics and developments",
        ],
        [
            {
                "title": "Examples",
                "content": "Prehistory: Stone Age, Bronze Age. Ancient: Egypt, Greece, Rome. Medieval: feudalism, Crusades. Modern: Renaissance, Industrial Revolution",
            }
        ],
        "builtin",
        None,
        1,
    )

    # Political Science
    lesson_id = add_lesson(
        political_science_id,
        "Political Systems",
        "Study different types of government",
        [
            "Democracy: government by the people",
            "Monarchy: government by a king or queen",
            "Dictatorship: government by one person with absolute power",
            "Republic: government where people elect representatives",
            "Each system has advantages and disadvantages",
        ],
        [
            {
                "title": "Examples",
                "content": "Democracy: United States, United Kingdom. Monarchy: Saudi Arabia, United Kingdom. Dictatorship: North Korea, former Nazi Germany",
            }
        ],
        "builtin",
        None,
        1,
    )

    # Sociology
    lesson_id = add_lesson(
        sociology_id,
        "Social Groups and Institutions",
        "Study how people organize in society",
        [
            "Social group: collection of people who interact",
            "Institution: established organization in society",
            "Examples: family, education, religion, government",
            "These institutions help society function",
            "Sociology helps us understand human behavior",
        ],
        [
            {
                "title": "Examples",
                "content": "Family: basic unit of society. Education: schools, universities. Religion: churches, temples, mosques. Government: laws, services",
            }
        ],
        "builtin",
        None,
        1,
    )

    # Anthropology
    lesson_id = add_lesson(
        anthropology_id,
        "Human Cultures and Societies",
        "Study human diversity and development",
        [
            "Anthropology: study of human cultures and societies",
            "Cultural anthropology: study of different cultures",
            "Physical anthropology: study of human evolution",
            "Archaeology: study of past human cultures",
            "Anthropology helps us understand human diversity",
        ],
        [
            {
                "title": "Examples",
                "content": "Cultural: study of different societies, customs, beliefs. Physical: human evolution, genetics, fossils. Archaeology: ancient civilizations, artifacts",
            }
        ],
        "builtin",
        None,
        1,
    )


if __name__ == "__main__":
    seed_massive_social_studies_curriculum()
