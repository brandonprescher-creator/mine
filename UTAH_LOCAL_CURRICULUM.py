"""
UTAH & COTTONWOOD HEIGHTS LOCAL CURRICULUM
Location-specific lessons for meaningful local connections
"""

from database import add_subject, add_topic, add_lesson


def seed_utah_curriculum():
    """Add Utah-specific educational content"""
    print("🏔️ Adding Utah & Cottonwood Heights local curriculum...")
    
    # Subject: Utah Studies
    utah_subject = add_subject(
        "Utah Studies",
        "Explore the geography, history, and culture of your home state",
        "🏔️",
        150
    )
    
    # Topic: Utah Geology
    geology_topic = add_topic(
        utah_subject,
        "Wasatch Mountain Geology",
        "The mountains in your backyard!",
        1
    )
    
    add_lesson(
        geology_topic,
        "How the Wasatch Mountains Formed",
        "The geological history of the mountains you see every day",
        [
            "The Wasatch Mountains are part of the Rocky Mountain chain",
            "They formed from tectonic uplift - the Earth's crust pushing up",
            "Little Cottonwood Canyon was carved by glaciers during the Ice Age",
            "The granite in the canyon is over 30 million years old!",
            "The fault line along the Wasatch Front is still active - this is earthquake country",
        ],
        [
            {"title": "See It Yourself", "content": "Drive up Little Cottonwood Canyon - look for the U-shaped valley carved by glaciers!"}
        ]
    )
    
    add_lesson(
        geology_topic,
        "Why Utah Has Dinosaur Fossils",
        "Utah's prehistoric past",
        [
            "Millions of years ago, Utah was a tropical swamp!",
            "Dinosaurs lived here: Allosaurus, Stegosaurus, Utahraptor",
            "When they died, they were buried in sediment that turned to rock",
            "Today, Utah has some of the best dinosaur fossil sites in the world",
            "Dinosaur National Monument is just a few hours from Cottonwood Heights",
        ],
        [
            {"title": "Utah's Dinosaur", "content": "Utahraptor was discovered in Utah and is the state's official state fossil!"}
        ]
    )
    
    # Topic: Great Salt Lake Science
    lake_topic = add_topic(
        utah_subject,
        "The Great Salt Lake Ecosystem",
        "Understanding Utah's unique inland sea",
        2
    )
    
    add_lesson(
        lake_topic,
        "Why the Great Salt Lake is So Salty",
        "The science of salt accumulation",
        [
            "The Great Salt Lake has no outlet - water flows in but doesn't flow out",
            "Water evaporates, but salt and minerals stay behind",
            "Over thousands of years, the salt has concentrated",
            "It's now 5-27% salt (ocean water is only 3.5% salt)",
            "It's one of the saltiest lakes in the world!",
        ],
        [
            {"title": "Fun Fact", "content": "The Great Salt Lake is saltier than the ocean - you float REALLY easily!"}
        ]
    )
    
    add_lesson(
        lake_topic,
        "Brine Shrimp: The Lake's Tiny Superstars",
        "The amazing ecosystem of hypersaline water",
        [
            "Brine shrimp are tiny creatures that thrive in super salty water",
            "They're one of the few organisms that can survive in the Great Salt Lake",
            "Billions of them live in the lake",
            "They're a crucial food source for millions of migrating birds",
            "Brine shrimp eggs can survive for years in dry conditions!",
        ],
        [
            {"title": "Cool Experiment", "content": "You can buy brine shrimp eggs (Sea-Monkeys!) and grow them at home!"}
        ]
    )
    
    # Topic: Utah Pioneer History
    history_topic = add_topic(
        utah_subject,
        "Pioneer History",
        "The settlement of the Salt Lake Valley",
        3
    )
    
    add_lesson(
        history_topic,
        "The Mormon Trail: Journey to Utah",
        "Understanding why and how pioneers came to Utah",
        [
            "In 1847, Brigham Young led pioneers to the Salt Lake Valley",
            "They traveled over 1,000 miles from Illinois",
            "The journey took 3-6 months by wagon",
            "They were seeking religious freedom and a new home",
            "When they arrived, Brigham Young said 'This is the place'",
        ],
        [
            {"title": "Imagine", "content": "The entire journey was done on foot or in wagons - no cars, no planes!"}
        ]
    )
    
    add_lesson(
        history_topic,
        "Cottonwood Heights: From Farms to Suburbs",
        "The history of your own community",
        [
            "Cottonwood Heights was originally farmland and orchards",
            "The area was named for the cottonwood trees that grew along the creek",
            "In the 1950s-60s, it transitioned from farms to suburban homes",
            "It officially became a city in 2005",
            "Today it's home to about 34,000 people",
        ],
        [
            {"title": "Local History", "content": "Your neighborhood might have been an apple orchard just 70 years ago!"}
        ]
    )
    
    # Topic: Utah's Unique Ecology
    ecology_topic = add_topic(
        utah_subject,
        "Utah's Diverse Ecosystems",
        "From deserts to mountains to salt lakes",
        4
    )
    
    add_lesson(
        ecology_topic,
        "Life Zones of the Wasatch",
        "How ecosystems change with elevation",
        [
            "Utah has 5 distinct life zones based on elevation",
            "Valley Floor (4,000-5,000 ft): Sagebrush and grass",
            "Foothills (5,000-7,000 ft): Scrub oak and maple",
            "Mountain (7,000-9,000 ft): Aspen and pine forests",
            "Subalpine (9,000-11,000 ft): Spruce and wildflowers",
            "Alpine (11,000+ ft): No trees, just rocks and tiny plants",
        ],
        [
            {"title": "Hike It", "content": "Take a hike up Big Cottonwood Canyon and count how many zones you pass through!"}
        ]
    )
    
    # Topic: Utah Weather & Climate
    weather_topic = add_topic(
        utah_subject,
        "Utah Weather Patterns",
        "Understanding our unique climate",
        5
    )
    
    add_lesson(
        weather_topic,
        "Why Utah Gets 'The Greatest Snow on Earth'",
        "The science behind Utah's famous powder snow",
        [
            "Utah's snow is special because it's very dry and light",
            "Storms come from the Pacific Ocean, losing moisture over Nevada",
            "By the time they reach Utah, the air is dry",
            "Dry air + cold temperatures = light, fluffy powder snow",
            "This makes Utah one of the best ski destinations in the world!",
        ],
        [
            {"title": "Local Fact", "content": "Utah's license plates say 'Greatest Snow on Earth' - it's not just bragging!"}
        ]
    )
    
    add_lesson(
        weather_topic,
        "Inversion: Why Salt Lake's Air Can Be Dirty",
        "Understanding temperature inversions",
        [
            "Normally, warm air rises and carries pollution away",
            "An inversion happens when cold air is trapped under warm air",
            "The cold air (and pollution) can't escape the valley",
            "The mountains create a bowl that traps the air",
            "Inversions are most common in winter",
        ],
        [
            {"title": "What You Can Do", "content": "On inversion days, drive less and stay indoors when possible"}
        ]
    )
    
    # Topic: Field Trip Ideas
    fieldtrip_topic = add_topic(
        utah_subject,
        "Utah Learning Adventures",
        "Amazing places to explore near home",
        6
    )
    
    add_lesson(
        fieldtrip_topic,
        "Local Museums & Learning Centers",
        "Educational destinations within 30 minutes",
        [
            "Natural History Museum of Utah: Dinosaurs, geology, Native American history",
            "Clark Planetarium: Space shows and interactive science exhibits",
            "Tracy Aviary: See birds from around the world",
            "This is the Place Heritage Park: Pioneer history",
            "Loveland Living Planet Aquarium: Ocean life (even though we're landlocked!)",
        ],
        [
            {"title": "Plan It", "content": "Many of these have free or discounted days for Utah residents!"}
        ]
    )
    
    add_lesson(
        fieldtrip_topic,
        "Hiking Adventures for Learning",
        "Turn hikes into science and history lessons",
        [
            "Bell Canyon Trail: Look for fossils and learn about glacial geology",
            "Big Cottonwood Canyon: Identify different tree species at different elevations",
            "City Creek Canyon: Easy access for bird watching and plant identification",
            "Ensign Peak: Learn about pioneer history with amazing valley views",
            "Red Butte Garden: Botanical education with labeled plants",
        ],
        [
            {"title": "Safety First", "content": "Always bring water, sun protection, and tell someone where you're going!"}
        ]
    )
    
    # Topic: Utah Scientists & Innovators
    innovators_topic = add_topic(
        utah_subject,
        "Utah Innovators",
        "Scientists and inventors from Utah",
        7
    )
    
    add_lesson(
        innovators_topic,
        "Philo Farnsworth: The Inventor of Television",
        "A Utah genius who changed the world",
        [
            "Philo Farnsworth grew up in Rigby, Idaho, but studied in Utah",
            "At age 14, he sketched the idea for electronic television",
            "In 1927, at age 21, he transmitted the first TV image",
            "He went to Brigham Young High School (now BYU)",
            "Today, TV technology is based on his inventions",
        ],
        [
            {"title": "Amazing", "content": "Farnsworth had the idea while plowing a potato field - the rows gave him the idea for scanning lines!"}
        ]
    )
    
    print("✅ Utah curriculum added with 10+ local lessons!")


if __name__ == "__main__":
    from database import init_database
    init_database()
    seed_utah_curriculum()

