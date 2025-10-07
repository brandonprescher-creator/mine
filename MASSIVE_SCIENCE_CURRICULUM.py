"""
MASSIVE Science Curriculum with Grade Levels
This creates a comprehensive Science curriculum for K-8 with grade-specific topics and lessons.
"""

from database import (
    add_subject,
    add_topic,
    add_lesson,
    add_practice_problem,
    get_all_subjects,
    get_topics_by_subject,
)


def seed_massive_science_curriculum():
    """Seed the database with MASSIVE Science curriculum organized by grade levels."""

    # Check if already seeded
    existing_subjects = get_all_subjects()
    if existing_subjects and any(s["name"] == "Science" for s in existing_subjects):
        print("Science curriculum already seeded.")
        return

    print("Seeding MASSIVE Science curriculum...")

    # Create Science subject
    science_id = add_subject(
        "Science", "Biology, chemistry, physics, and earth science", "🔬", 3
    )

    # KINDERGARTEN TOPICS
    k_animals_id = add_topic(
        science_id,
        "K - Animals & Living Things",
        "Learn about animals and what makes them alive",
        1,
    )
    k_plants_id = add_topic(
        science_id,
        "K - Plants & Growing",
        "Discover how plants grow and what they need",
        2,
    )
    k_weather_id = add_topic(
        science_id,
        "K - Weather & Seasons",
        "Observe weather patterns and seasonal changes",
        3,
    )
    k_matter_id = add_topic(
        science_id, "K - Solids & Liquids", "Explore different states of matter", 4
    )

    # GRADE 1 TOPICS
    g1_life_id = add_topic(
        science_id, "1st - Life Cycles", "Study how living things grow and change", 5
    )
    g1_habitats_id = add_topic(
        science_id,
        "1st - Habitats & Environments",
        "Learn where animals and plants live",
        6,
    )
    g1_weather_id = add_topic(
        science_id, "1st - Weather Patterns", "Understand different types of weather", 7
    )
    g1_light_id = add_topic(
        science_id, "1st - Light & Sound", "Explore light and sound in our world", 8
    )

    # GRADE 2 TOPICS
    g2_plants_id = add_topic(
        science_id, "2nd - Plant Science", "Study plant parts and how they work", 9
    )
    g2_animals_id = add_topic(
        science_id,
        "2nd - Animal Science",
        "Learn about animal characteristics and behaviors",
        10,
    )
    g2_earth_id = add_topic(
        science_id, "2nd - Earth's Surface", "Explore rocks, soil, and landforms", 11
    )
    g2_motion_id = add_topic(
        science_id, "2nd - Motion & Forces", "Understand how things move", 12
    )

    # GRADE 3 TOPICS
    g3_ecosystems_id = add_topic(
        science_id, "3rd - Ecosystems", "Study how living things interact", 13
    )
    g3_adaptations_id = add_topic(
        science_id, "3rd - Adaptations", "Learn how animals and plants adapt", 14
    )
    g3_rocks_id = add_topic(
        science_id, "3rd - Rocks & Minerals", "Study Earth's materials", 15
    )
    g3_magnets_id = add_topic(
        science_id,
        "3rd - Magnets & Electricity",
        "Explore magnetic and electrical forces",
        16,
    )

    # GRADE 4 TOPICS
    g4_energy_id = add_topic(
        science_id, "4th - Energy & Motion", "Understand different types of energy", 17
    )
    g4_waves_id = add_topic(
        science_id, "4th - Waves & Sound", "Study wave properties and sound", 18
    )
    g4_earth_id = add_topic(
        science_id,
        "4th - Earth's Processes",
        "Learn about Earth's changing surface",
        19,
    )
    g4_food_id = add_topic(
        science_id,
        "4th - Food Chains & Webs",
        "Study how energy flows through ecosystems",
        20,
    )

    # GRADE 5 TOPICS
    g5_cells_id = add_topic(
        science_id,
        "5th - Cells & Living Systems",
        "Study the building blocks of life",
        21,
    )
    g5_matter_id = add_topic(
        science_id,
        "5th - Properties of Matter",
        "Explore matter and its properties",
        22,
    )
    g5_space_id = add_topic(
        science_id, "5th - Solar System", "Study our solar system and beyond", 23
    )
    g5_water_id = add_topic(
        science_id, "5th - Water Cycle", "Understand Earth's water systems", 24
    )

    # GRADE 6 TOPICS
    g6_genetics_id = add_topic(
        science_id,
        "6th - Genetics & Heredity",
        "Learn about traits and inheritance",
        25,
    )
    g6_chemistry_id = add_topic(
        science_id, "6th - Chemical Reactions", "Study how substances change", 26
    )
    g6_geology_id = add_topic(
        science_id,
        "6th - Earth's Structure",
        "Explore Earth's layers and processes",
        27,
    )
    g6_astronomy_id = add_topic(
        science_id, "6th - Astronomy", "Study stars, galaxies, and the universe", 28
    )

    # GRADE 7 TOPICS
    g7_evolution_id = add_topic(
        science_id,
        "7th - Evolution & Natural Selection",
        "Understand how species change over time",
        29,
    )
    g7_atoms_id = add_topic(
        science_id, "7th - Atomic Structure", "Study atoms and the periodic table", 30
    )
    g7_climate_id = add_topic(
        science_id, "7th - Climate & Weather Systems", "Understand Earth's climate", 31
    )
    g7_energy_id = add_topic(
        science_id, "7th - Energy Transfer", "Study how energy moves and transforms", 32
    )

    # GRADE 8 TOPICS
    g8_biology_id = add_topic(
        science_id, "8th - Advanced Biology", "Study complex biological systems", 33
    )
    g8_chemistry_id = add_topic(
        science_id, "8th - Chemical Bonding", "Understand how atoms combine", 34
    )
    g8_physics_id = add_topic(
        science_id, "8th - Forces & Motion", "Study Newton's laws and mechanics", 35
    )
    g8_environment_id = add_topic(
        science_id,
        "8th - Environmental Science",
        "Study human impact on the environment",
        36,
    )

    # ADVANCED TOPICS
    molecular_biology_id = add_topic(
        science_id, "Molecular Biology", "Study DNA, RNA, and proteins", 37
    )
    organic_chemistry_id = add_topic(
        science_id, "Organic Chemistry", "Study carbon-based compounds", 38
    )
    quantum_physics_id = add_topic(
        science_id, "Quantum Physics", "Explore the quantum world", 39
    )
    climate_science_id = add_topic(
        science_id, "Climate Science", "Study climate change and solutions", 40
    )

    # KINDERGARTEN LESSONS
    seed_kindergarten_science_lessons(
        k_animals_id, k_plants_id, k_weather_id, k_matter_id
    )

    # GRADE 1 LESSONS
    seed_grade1_science_lessons(g1_life_id, g1_habitats_id, g1_weather_id, g1_light_id)

    # GRADE 2 LESSONS
    seed_grade2_science_lessons(g2_plants_id, g2_animals_id, g2_earth_id, g2_motion_id)

    # GRADE 3 LESSONS
    seed_grade3_science_lessons(
        g3_ecosystems_id, g3_adaptations_id, g3_rocks_id, g3_magnets_id
    )

    # GRADE 4 LESSONS
    seed_grade4_science_lessons(g4_energy_id, g4_waves_id, g4_earth_id, g4_food_id)

    # GRADE 5 LESSONS
    seed_grade5_science_lessons(g5_cells_id, g5_matter_id, g5_space_id, g5_water_id)

    # GRADE 6 LESSONS
    seed_grade6_science_lessons(
        g6_genetics_id, g6_chemistry_id, g6_geology_id, g6_astronomy_id
    )

    # GRADE 7 LESSONS
    seed_grade7_science_lessons(
        g7_evolution_id, g7_atoms_id, g7_climate_id, g7_energy_id
    )

    # GRADE 8 LESSONS
    seed_grade8_science_lessons(
        g8_biology_id, g8_chemistry_id, g8_physics_id, g8_environment_id
    )

    # ADVANCED LESSONS
    seed_advanced_science_lessons(
        molecular_biology_id,
        organic_chemistry_id,
        quantum_physics_id,
        climate_science_id,
    )

    print("MASSIVE Science curriculum seeded successfully!")


def seed_kindergarten_science_lessons(animals_id, plants_id, weather_id, matter_id):
    """Seed Kindergarten science lessons."""

    # Animals & Living Things
    lesson_id = add_lesson(
        animals_id,
        "What Makes Something Alive?",
        "Learn the characteristics of living things",
        [
            "Living things need food and water",
            "Living things grow and change",
            "Living things can move on their own",
            "Living things can have babies",
            "Examples: people, animals, plants",
        ],
        [
            {
                "title": "Examples",
                "content": "Living: dog, tree, person. Not living: rock, toy, book",
            }
        ],
        "builtin",
        None,
        1,
    )
    add_practice_problem(
        lesson_id,
        "Is a flower alive or not alive?",
        "alive",
        [
            "Think about what living things do",
            "Flowers grow and need water",
            "Flowers can make seeds",
            "Flowers are alive",
        ],
        ["Look at a real flower"],
        "easy",
        1,
    )

    lesson_id = add_lesson(
        animals_id,
        "Different Types of Animals",
        "Learn about mammals, birds, fish, and reptiles",
        [
            "Mammals: have fur or hair, feed milk to babies",
            "Birds: have feathers, lay eggs, can fly",
            "Fish: live in water, have scales, breathe with gills",
            "Reptiles: have scales, lay eggs, are cold-blooded",
            "Practice identifying different animals",
        ],
        [
            {
                "title": "Examples",
                "content": "Mammals: dog, cat, elephant. Birds: robin, eagle, penguin. Fish: goldfish, shark, salmon. Reptiles: snake, lizard, turtle",
            }
        ],
        "builtin",
        None,
        1,
    )

    lesson_id = add_lesson(
        animals_id,
        "Animal Habitats",
        "Learn where different animals live",
        [
            "Habitat: the place where an animal lives",
            "Forest: trees, squirrels, bears, birds",
            "Ocean: fish, whales, dolphins, sharks",
            "Desert: camels, snakes, lizards, cacti",
            "Farm: cows, pigs, chickens, horses",
        ],
        [
            {
                "title": "Examples",
                "content": "Polar bear lives in Arctic, penguin lives in Antarctica, monkey lives in rainforest",
            }
        ],
        "builtin",
        None,
        1,
    )

    # Plants & Growing
    lesson_id = add_lesson(
        plants_id,
        "What Plants Need to Grow",
        "Learn what plants need to survive",
        [
            "Plants need sunlight to make food",
            "Plants need water to grow",
            "Plants need soil to anchor their roots",
            "Plants need air to breathe",
            "Without these things, plants cannot grow",
        ],
        [
            {
                "title": "Examples",
                "content": "A plant in a dark closet will not grow well, a plant without water will wilt and die",
            }
        ],
        "builtin",
        None,
        1,
    )

    lesson_id = add_lesson(
        plants_id,
        "Parts of a Plant",
        "Learn about roots, stems, leaves, and flowers",
        [
            "Roots: hold the plant in the ground, take in water",
            "Stem: holds up the plant, carries water and food",
            "Leaves: make food for the plant using sunlight",
            "Flowers: make seeds so new plants can grow",
            "Each part has an important job",
        ],
        [
            {
                "title": "Examples",
                "content": "Carrot is a root, celery is a stem, lettuce is leaves, rose is a flower",
            }
        ],
        "builtin",
        None,
        1,
    )

    # Weather & Seasons
    lesson_id = add_lesson(
        weather_id,
        "Types of Weather",
        "Learn about sunny, rainy, cloudy, and snowy weather",
        [
            "Sunny: bright sun, warm, good for playing outside",
            "Rainy: water falls from clouds, plants get water",
            "Cloudy: sky is covered with clouds, might rain",
            "Snowy: frozen water falls, cold, good for winter fun",
            "Weather changes every day",
        ],
        [
            {
                "title": "Examples",
                "content": "Summer is usually sunny and hot, winter is usually cold and snowy, spring is often rainy",
            }
        ],
        "builtin",
        None,
        1,
    )

    lesson_id = add_lesson(
        weather_id,
        "The Four Seasons",
        "Learn about spring, summer, fall, and winter",
        [
            "Spring: flowers bloom, baby animals are born, weather gets warmer",
            "Summer: hot weather, long days, good for swimming",
            "Fall: leaves change color and fall, weather gets cooler",
            "Winter: cold weather, short days, snow and ice",
            "Seasons happen in the same order every year",
        ],
        [
            {
                "title": "Examples",
                "content": "Spring: March, April, May. Summer: June, July, August. Fall: September, October, November. Winter: December, January, February",
            }
        ],
        "builtin",
        None,
        1,
    )

    # Solids & Liquids
    lesson_id = add_lesson(
        matter_id,
        "Solids and Liquids",
        "Learn the difference between solids and liquids",
        [
            "Solids: have a shape, you can hold them",
            "Liquids: take the shape of their container",
            "Examples of solids: rock, book, toy",
            "Examples of liquids: water, milk, juice",
            "Practice identifying solids and liquids",
        ],
        [
            {
                "title": "Examples",
                "content": "Solid: ice cube, pencil, apple. Liquid: water, orange juice, milk",
            }
        ],
        "builtin",
        None,
        1,
    )


def seed_grade1_science_lessons(life_id, habitats_id, weather_id, light_id):
    """Seed Grade 1 science lessons."""

    # Life Cycles
    lesson_id = add_lesson(
        life_id,
        "Life Cycle of a Butterfly",
        "Learn how a caterpillar becomes a butterfly",
        [
            "Stage 1: Egg - butterfly lays eggs on leaves",
            "Stage 2: Caterpillar - eats leaves and grows",
            "Stage 3: Chrysalis - caterpillar makes a cocoon",
            "Stage 4: Butterfly - beautiful butterfly emerges",
            "This cycle repeats for new butterflies",
        ],
        [
            {
                "title": "Example",
                "content": "Monarch butterfly: egg → caterpillar → chrysalis → butterfly",
            }
        ],
        "builtin",
        None,
        1,
    )

    lesson_id = add_lesson(
        life_id,
        "Life Cycle of a Plant",
        "Learn how plants grow from seeds",
        [
            "Stage 1: Seed - contains baby plant and food",
            "Stage 2: Sprout - seed grows roots and stem",
            "Stage 3: Young Plant - grows leaves and gets bigger",
            "Stage 4: Adult Plant - makes flowers and seeds",
            "Seeds can grow into new plants",
        ],
        [
            {
                "title": "Example",
                "content": "Bean plant: seed → sprout → young plant → adult plant with beans",
            }
        ],
        "builtin",
        None,
        1,
    )

    # Habitats & Environments
    lesson_id = add_lesson(
        habitats_id,
        "Forest Habitat",
        "Learn about the forest ecosystem",
        [
            "Forests have many trees and plants",
            "Animals: deer, squirrels, birds, bears",
            "Plants: trees, ferns, mushrooms, flowers",
            "Forests provide shelter and food",
            "Forests help clean the air we breathe",
        ],
        [
            {
                "title": "Examples",
                "content": "Deciduous forest: oak trees, maple trees. Coniferous forest: pine trees, spruce trees",
            }
        ],
        "builtin",
        None,
        1,
    )

    lesson_id = add_lesson(
        habitats_id,
        "Ocean Habitat",
        "Learn about life in the ocean",
        [
            "Ocean is a huge body of salt water",
            "Animals: fish, whales, dolphins, sharks, octopus",
            "Plants: seaweed, kelp, coral",
            "Ocean provides food and oxygen",
            "Many animals live in different ocean zones",
        ],
        [
            {
                "title": "Examples",
                "content": "Shallow water: coral reef fish. Deep water: anglerfish. Surface: dolphins and whales",
            }
        ],
        "builtin",
        None,
        1,
    )

    # Weather Patterns
    lesson_id = add_lesson(
        weather_id,
        "How Rain Forms",
        "Learn about the water cycle",
        [
            "Sun heats water in oceans, lakes, and rivers",
            "Water evaporates and becomes water vapor",
            "Water vapor rises and forms clouds",
            "When clouds get heavy, rain falls",
            "This cycle happens over and over",
        ],
        [
            {
                "title": "Example",
                "content": "Ocean water → evaporation → clouds → rain → rivers → back to ocean",
            }
        ],
        "builtin",
        None,
        1,
    )

    # Light & Sound
    lesson_id = add_lesson(
        light_id,
        "Sources of Light",
        "Learn about natural and artificial light",
        [
            "Natural light comes from the sun",
            "Artificial light comes from things we make",
            "Examples of artificial light: light bulbs, flashlights, candles",
            "Light helps us see things",
            "Some animals make their own light",
        ],
        [
            {
                "title": "Examples",
                "content": "Natural: sun, stars, fireflies. Artificial: light bulb, flashlight, candle",
            }
        ],
        "builtin",
        None,
        1,
    )

    lesson_id = add_lesson(
        light_id,
        "How Sound Travels",
        "Learn about sound waves",
        [
            "Sound is made when things vibrate",
            "Sound travels through air, water, and solids",
            "Sound travels in waves",
            "We hear sound when waves reach our ears",
            "Different sounds have different pitches",
        ],
        [
            {
                "title": "Examples",
                "content": "Drum makes sound when you hit it, guitar strings vibrate to make music",
            }
        ],
        "builtin",
        None,
        1,
    )


def seed_grade2_science_lessons(plants_id, animals_id, earth_id, motion_id):
    """Seed Grade 2 science lessons."""

    # Plant Science
    lesson_id = add_lesson(
        plants_id,
        "How Plants Make Food",
        "Learn about photosynthesis",
        [
            "Plants use sunlight to make their own food",
            "Leaves have a green chemical called chlorophyll",
            "Chlorophyll captures sunlight energy",
            "Plants use sunlight, water, and air to make sugar",
            "This process is called photosynthesis",
        ],
        [
            {
                "title": "Example",
                "content": "Sunlight + Water + Carbon Dioxide → Sugar + Oxygen",
            }
        ],
        "builtin",
        None,
        1,
    )

    lesson_id = add_lesson(
        plants_id,
        "Plant Reproduction",
        "Learn how plants make new plants",
        [
            "Flowers contain the plant's reproductive parts",
            "Pollen from one flower can reach another flower",
            "This is called pollination",
            "After pollination, seeds form",
            "Seeds can grow into new plants",
        ],
        [
            {
                "title": "Examples",
                "content": "Bees help pollinate flowers, wind can carry pollen, some flowers pollinate themselves",
            }
        ],
        "builtin",
        None,
        1,
    )

    # Animal Science
    lesson_id = add_lesson(
        animals_id,
        "Animal Body Coverings",
        "Learn about fur, feathers, scales, and skin",
        [
            "Fur: keeps mammals warm, like dogs and cats",
            "Feathers: help birds fly and stay warm",
            "Scales: protect fish and reptiles",
            "Skin: covers amphibians and some other animals",
            "Each covering helps the animal survive",
        ],
        [
            {
                "title": "Examples",
                "content": "Fur: bear, rabbit. Feathers: eagle, penguin. Scales: fish, snake. Skin: frog, human",
            }
        ],
        "builtin",
        None,
        1,
    )

    lesson_id = add_lesson(
        animals_id,
        "Animal Behaviors",
        "Learn about how animals act",
        [
            "Migration: animals travel long distances",
            "Hibernation: animals sleep through winter",
            "Camouflage: animals hide by blending in",
            "Communication: animals talk to each other",
            "Each behavior helps animals survive",
        ],
        [
            {
                "title": "Examples",
                "content": "Migration: geese fly south. Hibernation: bears sleep in winter. Camouflage: chameleon changes color",
            }
        ],
        "builtin",
        None,
        1,
    )

    # Earth's Surface
    lesson_id = add_lesson(
        earth_id,
        "Types of Rocks",
        "Learn about igneous, sedimentary, and metamorphic rocks",
        [
            "Igneous rocks: formed from cooled lava or magma",
            "Sedimentary rocks: formed from layers of sediment",
            "Metamorphic rocks: formed from heat and pressure",
            "Rocks can change from one type to another",
            "Rocks are made of minerals",
        ],
        [
            {
                "title": "Examples",
                "content": "Igneous: granite, basalt. Sedimentary: limestone, sandstone. Metamorphic: marble, slate",
            }
        ],
        "builtin",
        None,
        1,
    )

    lesson_id = add_lesson(
        earth_id,
        "Soil and Its Layers",
        "Learn about different soil layers",
        [
            "Topsoil: dark, rich soil where plants grow",
            "Subsoil: lighter soil with some nutrients",
            "Bedrock: solid rock at the bottom",
            "Soil is made of rock particles, water, air, and organic matter",
            "Different places have different types of soil",
        ],
        [
            {
                "title": "Example",
                "content": "Topsoil (0-6 inches) → Subsoil (6-24 inches) → Bedrock (24+ inches)",
            }
        ],
        "builtin",
        None,
        1,
    )

    # Motion & Forces
    lesson_id = add_lesson(
        motion_id,
        "Push and Pull",
        "Learn about forces",
        [
            "Force: a push or pull that makes things move",
            "Push: move something away from you",
            "Pull: move something toward you",
            "Forces can make things start moving, stop moving, or change direction",
            "Practice pushing and pulling different objects",
        ],
        [
            {
                "title": "Examples",
                "content": "Push: opening a door, kicking a ball. Pull: closing a drawer, pulling a wagon",
            }
        ],
        "builtin",
        None,
        1,
    )

    lesson_id = add_lesson(
        motion_id,
        "Simple Machines",
        "Learn about levers, pulleys, and inclined planes",
        [
            "Simple machines make work easier",
            "Lever: a bar that pivots on a fulcrum",
            "Pulley: a wheel with a rope or chain",
            "Inclined plane: a ramp or slope",
            "Simple machines help us do work with less effort",
        ],
        [
            {
                "title": "Examples",
                "content": "Lever: seesaw, crowbar. Pulley: flagpole, well. Inclined plane: ramp, stairs",
            }
        ],
        "builtin",
        None,
        1,
    )


def seed_grade3_science_lessons(ecosystems_id, adaptations_id, rocks_id, magnets_id):
    """Seed Grade 3 science lessons."""

    # Ecosystems
    lesson_id = add_lesson(
        ecosystems_id,
        "Food Chains",
        "Learn how energy flows through ecosystems",
        [
            "Food chain: shows who eats whom",
            "Producers: plants that make their own food",
            "Consumers: animals that eat other living things",
            "Decomposers: break down dead plants and animals",
            "Energy flows from producers to consumers",
        ],
        [{"title": "Example", "content": "Grass → Rabbit → Fox → Decomposers"}],
        "builtin",
        None,
        1,
    )

    lesson_id = add_lesson(
        ecosystems_id,
        "Food Webs",
        "Learn about complex feeding relationships",
        [
            "Food web: many food chains connected together",
            "Most animals eat more than one type of food",
            "If one animal disappears, it affects others",
            "Food webs show how all living things are connected",
            "Balance in food webs is important for survival",
        ],
        [
            {
                "title": "Example",
                "content": "Grass → Rabbit, Mouse → Fox, Owl. Grass → Deer → Mountain Lion",
            }
        ],
        "builtin",
        None,
        1,
    )

    # Adaptations
    lesson_id = add_lesson(
        adaptations_id,
        "Physical Adaptations",
        "Learn about body parts that help animals survive",
        [
            "Adaptation: a trait that helps an animal survive",
            "Camouflage: blending in with surroundings",
            "Sharp claws: for catching prey or climbing",
            "Thick fur: for staying warm in cold weather",
            "Each adaptation has a specific purpose",
        ],
        [
            {
                "title": "Examples",
                "content": "Polar bear: white fur for camouflage, thick fur for warmth. Eagle: sharp talons for catching prey",
            }
        ],
        "builtin",
        None,
        1,
    )

    lesson_id = add_lesson(
        adaptations_id,
        "Behavioral Adaptations",
        "Learn about behaviors that help animals survive",
        [
            "Behavioral adaptation: actions that help animals survive",
            "Migration: traveling to find food or better weather",
            "Hibernation: sleeping through harsh seasons",
            "Hunting in groups: working together to catch prey",
            "These behaviors are learned or instinctive",
        ],
        [
            {
                "title": "Examples",
                "content": "Migration: monarch butterflies fly to Mexico. Hibernation: groundhogs sleep all winter",
            }
        ],
        "builtin",
        None,
        1,
    )

    # Rocks & Minerals
    lesson_id = add_lesson(
        rocks_id,
        "Rock Cycle",
        "Learn how rocks change over time",
        [
            "Rocks can change from one type to another",
            "Weathering: rocks break down into smaller pieces",
            "Erosion: pieces of rock are moved by wind, water, or ice",
            "Deposition: rock pieces settle in new places",
            "Heat and pressure can form new rocks",
        ],
        [
            {
                "title": "Example",
                "content": "Igneous rock → weathering → sediment → pressure → sedimentary rock → heat → metamorphic rock",
            }
        ],
        "builtin",
        None,
        1,
    )

    lesson_id = add_lesson(
        rocks_id,
        "Minerals and Their Properties",
        "Learn about different minerals",
        [
            "Minerals: natural, solid substances",
            "Each mineral has unique properties",
            "Color: what color the mineral is",
            "Hardness: how easily it can be scratched",
            "Luster: how shiny or dull it is",
        ],
        [
            {
                "title": "Examples",
                "content": "Quartz: clear or colored, very hard, glassy luster. Gold: yellow, soft, metallic luster",
            }
        ],
        "builtin",
        None,
        1,
    )

    # Magnets & Electricity
    lesson_id = add_lesson(
        magnets_id,
        "Magnetic Properties",
        "Learn about magnets and magnetism",
        [
            "Magnet: an object that attracts certain metals",
            "Magnetic poles: north and south poles",
            "Like poles repel, opposite poles attract",
            "Magnetic field: invisible area around a magnet",
            "Some materials are magnetic, others are not",
        ],
        [
            {
                "title": "Examples",
                "content": "Magnetic: iron, nickel, cobalt. Not magnetic: wood, plastic, aluminum",
            }
        ],
        "builtin",
        None,
        1,
    )

    lesson_id = add_lesson(
        magnets_id,
        "Static Electricity",
        "Learn about electric charges",
        [
            "Static electricity: buildup of electric charge",
            "Positive and negative charges attract each other",
            "Like charges repel each other",
            "Static electricity can cause sparks or shocks",
            "Lightning is a form of static electricity",
        ],
        [
            {
                "title": "Examples",
                "content": "Rubbing a balloon on your hair creates static electricity, lightning is static electricity in clouds",
            }
        ],
        "builtin",
        None,
        1,
    )


def seed_grade4_science_lessons(energy_id, waves_id, earth_id, food_id):
    """Seed Grade 4 science lessons."""

    # Energy & Motion
    lesson_id = add_lesson(
        energy_id,
        "Types of Energy",
        "Learn about different forms of energy",
        [
            "Kinetic energy: energy of motion",
            "Potential energy: stored energy",
            "Thermal energy: heat energy",
            "Light energy: energy we can see",
            "Sound energy: energy we can hear",
        ],
        [
            {
                "title": "Examples",
                "content": "Kinetic: moving car, running person. Potential: stretched rubber band, water behind dam",
            }
        ],
        "builtin",
        None,
        1,
    )

    lesson_id = add_lesson(
        energy_id,
        "Energy Transfer",
        "Learn how energy moves from place to place",
        [
            "Energy can be transferred from one object to another",
            "Conduction: energy moves through direct contact",
            "Convection: energy moves through fluids",
            "Radiation: energy moves through empty space",
            "Energy is never created or destroyed, only transferred",
        ],
        [
            {
                "title": "Examples",
                "content": "Conduction: hot pan heats food. Convection: hot air rises. Radiation: sun heats Earth",
            }
        ],
        "builtin",
        None,
        1,
    )

    # Waves & Sound
    lesson_id = add_lesson(
        waves_id,
        "Wave Properties",
        "Learn about wavelength, frequency, and amplitude",
        [
            "Wavelength: distance between wave peaks",
            "Frequency: how many waves pass per second",
            "Amplitude: height of the wave",
            "Higher frequency = higher pitch",
            "Higher amplitude = louder sound",
        ],
        [
            {
                "title": "Examples",
                "content": "High frequency: whistle, bird chirp. Low frequency: drum, thunder. High amplitude: shout. Low amplitude: whisper",
            }
        ],
        "builtin",
        None,
        1,
    )

    lesson_id = add_lesson(
        waves_id,
        "How Sound Travels",
        "Learn about sound waves and mediums",
        [
            "Sound travels as waves through matter",
            "Sound travels fastest through solids",
            "Sound travels slower through liquids",
            "Sound travels slowest through gases",
            "Sound cannot travel through empty space",
        ],
        [
            {
                "title": "Examples",
                "content": "Sound through steel: very fast. Sound through water: medium speed. Sound through air: slower. Sound in space: none",
            }
        ],
        "builtin",
        None,
        1,
    )

    # Earth's Processes
    lesson_id = add_lesson(
        earth_id,
        "Weathering and Erosion",
        "Learn how Earth's surface changes",
        [
            "Weathering: breaking down of rocks and soil",
            "Erosion: moving of weathered material",
            "Deposition: dropping of eroded material",
            "These processes shape Earth's surface",
            "Water, wind, and ice cause weathering and erosion",
        ],
        [
            {
                "title": "Examples",
                "content": "Weathering: freeze-thaw breaks rocks. Erosion: river carries soil. Deposition: river delta forms",
            }
        ],
        "builtin",
        None,
        1,
    )

    lesson_id = add_lesson(
        earth_id,
        "Earth's Layers",
        "Learn about Earth's structure",
        [
            "Crust: thin outer layer where we live",
            "Mantle: thick middle layer of hot rock",
            "Outer core: liquid metal layer",
            "Inner core: solid metal center",
            "Temperature and pressure increase with depth",
        ],
        [
            {
                "title": "Example",
                "content": "Crust (0-25 miles) → Mantle (25-1800 miles) → Outer Core (1800-3200 miles) → Inner Core (3200-4000 miles)",
            }
        ],
        "builtin",
        None,
        1,
    )

    # Food Chains & Webs
    lesson_id = add_lesson(
        food_id,
        "Energy Flow in Ecosystems",
        "Learn how energy moves through food webs",
        [
            "Energy flows from producers to consumers",
            "Only about 10% of energy is passed to the next level",
            "Most energy is lost as heat",
            "This limits the number of levels in a food chain",
            "Decomposers recycle nutrients back to producers",
        ],
        [
            {
                "title": "Example",
                "content": "Sun → Grass (100%) → Rabbit (10%) → Fox (1%) → Decomposers recycle nutrients",
            }
        ],
        "builtin",
        None,
        1,
    )


def seed_grade5_science_lessons(cells_id, matter_id, space_id, water_id):
    """Seed Grade 5 science lessons."""

    # Cells & Living Systems
    lesson_id = add_lesson(
        cells_id,
        "Plant and Animal Cells",
        "Learn about the basic unit of life",
        [
            "Cell: the smallest unit of living things",
            "Plant cells: have cell wall, chloroplasts, and large vacuole",
            "Animal cells: have cell membrane, nucleus, and smaller vacuoles",
            "Both have nucleus, cytoplasm, and mitochondria",
            "Cells work together to form tissues and organs",
        ],
        [
            {
                "title": "Examples",
                "content": "Plant cell parts: cell wall, chloroplast, vacuole. Animal cell parts: cell membrane, nucleus, mitochondria",
            }
        ],
        "builtin",
        None,
        1,
    )

    lesson_id = add_lesson(
        cells_id,
        "Cell Functions",
        "Learn what different cell parts do",
        [
            "Nucleus: controls the cell, contains DNA",
            "Cytoplasm: jelly-like substance where reactions happen",
            "Mitochondria: makes energy for the cell",
            "Cell membrane: controls what enters and leaves",
            "Each part has a specific job to keep the cell alive",
        ],
        [
            {
                "title": "Examples",
                "content": "Nucleus: like the brain of the cell. Mitochondria: like the power plant. Cell membrane: like a security guard",
            }
        ],
        "builtin",
        None,
        1,
    )

    # Properties of Matter
    lesson_id = add_lesson(
        matter_id,
        "States of Matter",
        "Learn about solids, liquids, and gases",
        [
            "Solid: has definite shape and volume",
            "Liquid: has definite volume but takes shape of container",
            "Gas: has no definite shape or volume",
            "Matter can change from one state to another",
            "Temperature affects the state of matter",
        ],
        [
            {
                "title": "Examples",
                "content": "Solid: ice, rock. Liquid: water, milk. Gas: steam, air",
            }
        ],
        "builtin",
        None,
        1,
    )

    lesson_id = add_lesson(
        matter_id,
        "Physical and Chemical Changes",
        "Learn how matter can change",
        [
            "Physical change: matter changes form but not identity",
            "Chemical change: matter changes into something new",
            "Physical changes are usually reversible",
            "Chemical changes are usually not reversible",
            "Look for signs of chemical change",
        ],
        [
            {
                "title": "Examples",
                "content": "Physical: ice melting, paper tearing. Chemical: burning wood, rusting metal",
            }
        ],
        "builtin",
        None,
        1,
    )

    # Solar System
    lesson_id = add_lesson(
        space_id,
        "Planets in Our Solar System",
        "Learn about the eight planets",
        [
            "Inner planets: Mercury, Venus, Earth, Mars (rocky)",
            "Outer planets: Jupiter, Saturn, Uranus, Neptune (gas giants)",
            "Each planet has unique characteristics",
            "Planets orbit the Sun in elliptical paths",
            "Distance from Sun affects temperature and conditions",
        ],
        [
            {
                "title": "Examples",
                "content": "Mercury: closest, very hot. Earth: perfect for life. Jupiter: largest, gas giant. Pluto: now a dwarf planet",
            }
        ],
        "builtin",
        None,
        1,
    )

    lesson_id = add_lesson(
        space_id,
        "Earth's Place in Space",
        "Learn about Earth's rotation and revolution",
        [
            "Rotation: Earth spins on its axis (causes day and night)",
            "Revolution: Earth orbits the Sun (causes seasons)",
            "Earth's axis is tilted 23.5 degrees",
            "This tilt causes different seasons",
            "One rotation = 24 hours, one revolution = 365 days",
        ],
        [
            {
                "title": "Example",
                "content": "When your side of Earth faces the Sun, it's day. When it faces away, it's night",
            }
        ],
        "builtin",
        None,
        1,
    )

    # Water Cycle
    lesson_id = add_lesson(
        water_id,
        "The Water Cycle",
        "Learn how water moves through Earth's systems",
        [
            "Evaporation: water turns into water vapor",
            "Condensation: water vapor forms clouds",
            "Precipitation: water falls as rain, snow, or hail",
            "Collection: water gathers in oceans, lakes, and rivers",
            "This cycle happens continuously",
        ],
        [
            {
                "title": "Example",
                "content": "Ocean → evaporation → clouds → precipitation → rivers → back to ocean",
            }
        ],
        "builtin",
        None,
        1,
    )

    lesson_id = add_lesson(
        water_id,
        "Water Conservation",
        "Learn why water is important and how to save it",
        [
            "Water is essential for all living things",
            "Only 3% of Earth's water is fresh water",
            "Most fresh water is frozen in ice caps",
            "We need to conserve water for future generations",
            "Simple ways to save water every day",
        ],
        [
            {
                "title": "Examples",
                "content": "Turn off faucet while brushing teeth, take shorter showers, fix leaky faucets",
            }
        ],
        "builtin",
        None,
        1,
    )


def seed_grade6_science_lessons(genetics_id, chemistry_id, geology_id, astronomy_id):
    """Seed Grade 6 science lessons."""

    # Genetics & Heredity
    lesson_id = add_lesson(
        genetics_id,
        "Traits and Inheritance",
        "Learn about how traits are passed down",
        [
            "Trait: a characteristic of a living thing",
            "Inherited traits: passed from parents to offspring",
            "Acquired traits: learned or developed during life",
            "Genes: instructions for traits found in DNA",
            "Offspring inherit traits from both parents",
        ],
        [
            {
                "title": "Examples",
                "content": "Inherited: eye color, hair color, height. Acquired: language, riding a bike, scars",
            }
        ],
        "builtin",
        None,
        1,
    )

    lesson_id = add_lesson(
        genetics_id,
        "Dominant and Recessive Traits",
        "Learn about how some traits are stronger than others",
        [
            "Dominant trait: shows up even if only one parent has it",
            "Recessive trait: only shows up if both parents have it",
            "Each parent contributes one gene for each trait",
            "Punnett squares help predict offspring traits",
            "Some traits are more complex than dominant/recessive",
        ],
        [
            {
                "title": "Example",
                "content": "Brown eyes (dominant) + Blue eyes (recessive) = Brown eyes (if Bb) or Blue eyes (if bb)",
            }
        ],
        "builtin",
        None,
        1,
    )

    # Chemical Reactions
    lesson_id = add_lesson(
        chemistry_id,
        "Atoms and Molecules",
        "Learn about the building blocks of matter",
        [
            "Atom: smallest particle of an element",
            "Molecule: two or more atoms bonded together",
            "Element: pure substance made of one type of atom",
            "Compound: substance made of different types of atoms",
            "Atoms are made of protons, neutrons, and electrons",
        ],
        [
            {
                "title": "Examples",
                "content": "Element: gold (Au), oxygen (O₂). Compound: water (H₂O), salt (NaCl)",
            }
        ],
        "builtin",
        None,
        1,
    )

    lesson_id = add_lesson(
        chemistry_id,
        "Chemical Reactions",
        "Learn how substances change into new substances",
        [
            "Chemical reaction: process that changes substances",
            "Reactants: substances that start the reaction",
            "Products: new substances formed",
            "Signs of chemical reaction: color change, gas formation, temperature change",
            "Chemical reactions follow the law of conservation of mass",
        ],
        [
            {
                "title": "Example",
                "content": "Burning wood: Wood + Oxygen → Ash + Smoke + Heat (mass is conserved)",
            }
        ],
        "builtin",
        None,
        1,
    )

    # Earth's Structure
    lesson_id = add_lesson(
        geology_id,
        "Plate Tectonics",
        "Learn about Earth's moving plates",
        [
            "Earth's crust is broken into large pieces called plates",
            "Plates move slowly on the mantle",
            "Plate boundaries: where plates meet",
            "Movement causes earthquakes, volcanoes, and mountains",
            "Continental drift: continents have moved over time",
        ],
        [
            {
                "title": "Examples",
                "content": "Divergent: plates move apart (mid-ocean ridges). Convergent: plates collide (mountains). Transform: plates slide past (earthquakes)",
            }
        ],
        "builtin",
        None,
        1,
    )

    lesson_id = add_lesson(
        geology_id,
        "Earthquakes and Volcanoes",
        "Learn about Earth's powerful forces",
        [
            "Earthquake: shaking caused by plate movement",
            "Focus: where earthquake starts underground",
            "Epicenter: point on surface above focus",
            "Volcano: opening where molten rock reaches surface",
            "Both can cause great destruction but also create new land",
        ],
        [
            {
                "title": "Examples",
                "content": "Earthquake: San Andreas Fault. Volcano: Mount St. Helens, Hawaiian Islands",
            }
        ],
        "builtin",
        None,
        1,
    )

    # Astronomy
    lesson_id = add_lesson(
        astronomy_id,
        "Stars and Galaxies",
        "Learn about objects in space",
        [
            "Star: hot ball of gas that produces light",
            "Galaxy: huge collection of stars, gas, and dust",
            "Our galaxy: Milky Way (spiral galaxy)",
            "Stars have different colors based on temperature",
            "Stars are born, live, and die in cycles",
        ],
        [
            {
                "title": "Examples",
                "content": "Hot stars: blue-white. Cool stars: red. Our Sun: yellow. Galaxies: spiral, elliptical, irregular",
            }
        ],
        "builtin",
        None,
        1,
    )

    lesson_id = add_lesson(
        astronomy_id,
        "The Universe",
        "Learn about the vastness of space",
        [
            "Universe: everything that exists",
            "Light-year: distance light travels in one year",
            "Big Bang: theory of how universe began",
            "Universe is expanding and getting bigger",
            "There may be other planets with life",
        ],
        [
            {
                "title": "Examples",
                "content": "Nearest star: 4 light-years away. Observable universe: 93 billion light-years across",
            }
        ],
        "builtin",
        None,
        1,
    )


def seed_grade7_science_lessons(evolution_id, atoms_id, climate_id, energy_id):
    """Seed Grade 7 science lessons."""

    # Evolution & Natural Selection
    lesson_id = add_lesson(
        evolution_id,
        "Natural Selection",
        "Learn how species change over time",
        [
            "Natural selection: process that drives evolution",
            "Variation: differences within a species",
            "Competition: struggle for limited resources",
            "Survival of the fittest: best adapted individuals survive",
            "Over time, beneficial traits become more common",
        ],
        [
            {
                "title": "Example",
                "content": "Peppered moths: dark moths survived better during industrial pollution, light moths survived better before",
            }
        ],
        "builtin",
        None,
        1,
    )

    lesson_id = add_lesson(
        evolution_id,
        "Evidence for Evolution",
        "Learn about proof that evolution occurs",
        [
            "Fossil record: shows how species changed over time",
            "Comparative anatomy: similar structures in different species",
            "DNA evidence: genetic similarities between species",
            "Embryology: similar development in related species",
            "All evidence supports the theory of evolution",
        ],
        [
            {
                "title": "Examples",
                "content": "Fossils: dinosaur bones. Anatomy: human arm, whale flipper, bat wing. DNA: humans and chimpanzees share 98% DNA",
            }
        ],
        "builtin",
        None,
        1,
    )

    # Atomic Structure
    lesson_id = add_lesson(
        atoms_id,
        "Structure of the Atom",
        "Learn about protons, neutrons, and electrons",
        [
            "Nucleus: center of atom with protons and neutrons",
            "Electrons: orbit around nucleus in energy levels",
            "Protons: positive charge, determine element",
            "Neutrons: no charge, add mass to atom",
            "Atoms are mostly empty space",
        ],
        [
            {
                "title": "Example",
                "content": "Hydrogen: 1 proton, 0 neutrons, 1 electron. Carbon: 6 protons, 6 neutrons, 6 electrons",
            }
        ],
        "builtin",
        None,
        1,
    )

    lesson_id = add_lesson(
        atoms_id,
        "Periodic Table",
        "Learn about organizing elements",
        [
            "Periodic table: chart organizing all elements",
            "Elements arranged by atomic number",
            "Rows: periods, Columns: groups or families",
            "Elements in same group have similar properties",
            "Metals, nonmetals, and metalloids have different properties",
        ],
        [
            {
                "title": "Examples",
                "content": "Group 1: alkali metals (very reactive). Group 18: noble gases (unreactive). Period 1: hydrogen and helium",
            }
        ],
        "builtin",
        None,
        1,
    )

    # Climate & Weather Systems
    lesson_id = add_lesson(
        climate_id,
        "Climate vs Weather",
        "Learn the difference between climate and weather",
        [
            "Weather: conditions in atmosphere over short time",
            "Climate: average weather over long time",
            "Climate zones: tropical, temperate, polar",
            "Factors affecting climate: latitude, altitude, ocean currents",
            "Climate can change naturally or due to human activities",
        ],
        [
            {
                "title": "Examples",
                "content": "Weather: today's temperature and rain. Climate: average temperature and rainfall over 30 years",
            }
        ],
        "builtin",
        None,
        1,
    )

    lesson_id = add_lesson(
        climate_id,
        "Greenhouse Effect",
        "Learn about Earth's natural warming system",
        [
            "Greenhouse effect: natural process that warms Earth",
            "Greenhouse gases trap heat in atmosphere",
            "Natural greenhouse effect: keeps Earth warm enough for life",
            "Enhanced greenhouse effect: human activities increase warming",
            "Carbon dioxide is the main greenhouse gas from human activities",
        ],
        [
            {
                "title": "Example",
                "content": "Sunlight enters → Earth absorbs heat → Heat radiates back → Greenhouse gases trap some heat → Earth stays warm",
            }
        ],
        "builtin",
        None,
        1,
    )

    # Energy Transfer
    lesson_id = add_lesson(
        energy_id,
        "Forms of Energy",
        "Learn about different types of energy",
        [
            "Mechanical energy: energy of motion and position",
            "Thermal energy: heat energy from particle movement",
            "Chemical energy: energy stored in chemical bonds",
            "Electrical energy: energy from moving electrons",
            "Nuclear energy: energy from atomic reactions",
        ],
        [
            {
                "title": "Examples",
                "content": "Mechanical: moving car, stretched spring. Thermal: hot stove, warm air. Chemical: food, gasoline",
            }
        ],
        "builtin",
        None,
        1,
    )

    lesson_id = add_lesson(
        energy_id,
        "Energy Transformation",
        "Learn how energy changes from one form to another",
        [
            "Energy can change from one form to another",
            "Energy transformation: changing energy from one form to another",
            "Energy is never created or destroyed (conservation of energy)",
            "Some energy is always lost as heat",
            "Efficiency: how much useful energy you get out",
        ],
        [
            {
                "title": "Examples",
                "content": "Light bulb: electrical → light + heat. Car engine: chemical → mechanical + heat. Solar panel: light → electrical",
            }
        ],
        "builtin",
        None,
        1,
    )


def seed_grade8_science_lessons(biology_id, chemistry_id, physics_id, environment_id):
    """Seed Grade 8 science lessons."""

    # Advanced Biology
    lesson_id = add_lesson(
        biology_id,
        "Body Systems",
        "Learn about human body systems",
        [
            "Circulatory system: heart, blood vessels, blood",
            "Respiratory system: lungs, airways, breathing",
            "Digestive system: stomach, intestines, food processing",
            "Nervous system: brain, spinal cord, nerves",
            "All systems work together to keep body functioning",
        ],
        [
            {
                "title": "Examples",
                "content": "Circulatory: heart pumps blood. Respiratory: lungs exchange gases. Digestive: stomach breaks down food",
            }
        ],
        "builtin",
        None,
        1,
    )

    lesson_id = add_lesson(
        biology_id,
        "Ecosystem Interactions",
        "Learn about complex relationships in nature",
        [
            "Symbiosis: close relationship between different species",
            "Mutualism: both species benefit",
            "Commensalism: one benefits, other unaffected",
            "Parasitism: one benefits, other is harmed",
            "These relationships help maintain ecosystem balance",
        ],
        [
            {
                "title": "Examples",
                "content": "Mutualism: bees and flowers. Commensalism: barnacles on whales. Parasitism: ticks on deer",
            }
        ],
        "builtin",
        None,
        1,
    )

    # Chemical Bonding
    lesson_id = add_lesson(
        chemistry_id,
        "Ionic and Covalent Bonds",
        "Learn how atoms bond together",
        [
            "Ionic bond: electrons transferred between atoms",
            "Covalent bond: electrons shared between atoms",
            "Ionic compounds: usually between metals and nonmetals",
            "Covalent compounds: usually between nonmetals",
            "Type of bond affects properties of compounds",
        ],
        [
            {
                "title": "Examples",
                "content": "Ionic: NaCl (salt), CaCl₂. Covalent: H₂O (water), CO₂ (carbon dioxide)",
            }
        ],
        "builtin",
        None,
        1,
    )

    lesson_id = add_lesson(
        chemistry_id,
        "Acids and Bases",
        "Learn about pH and chemical properties",
        [
            "Acid: substance that donates hydrogen ions",
            "Base: substance that accepts hydrogen ions",
            "pH scale: measures acidity from 0-14",
            "pH 7: neutral, pH < 7: acidic, pH > 7: basic",
            "Acids and bases are important in many processes",
        ],
        [
            {
                "title": "Examples",
                "content": "Acids: lemon juice (pH 2), stomach acid (pH 1). Bases: soap (pH 9), baking soda (pH 8)",
            }
        ],
        "builtin",
        None,
        1,
    )

    # Forces & Motion
    lesson_id = add_lesson(
        physics_id,
        "Newton's Laws of Motion",
        "Learn about the fundamental laws of physics",
        [
            "First Law: objects at rest stay at rest, objects in motion stay in motion",
            "Second Law: force equals mass times acceleration (F=ma)",
            "Third Law: for every action there is an equal and opposite reaction",
            "These laws explain how objects move and interact",
            "Apply to everything from cars to rockets",
        ],
        [
            {
                "title": "Examples",
                "content": "First Law: car stops suddenly, you keep moving forward. Second Law: harder you push, faster it accelerates",
            }
        ],
        "builtin",
        None,
        1,
    )

    lesson_id = add_lesson(
        physics_id,
        "Gravity and Orbits",
        "Learn about gravitational forces",
        [
            "Gravity: force that attracts objects with mass",
            "More mass = stronger gravitational pull",
            "Closer distance = stronger gravitational pull",
            "Orbits: objects falling around other objects",
            "Gravity keeps planets in orbit around the Sun",
        ],
        [
            {
                "title": "Examples",
                "content": "Earth's gravity: keeps us on ground, Moon's gravity: causes tides. Orbits: Moon around Earth, Earth around Sun",
            }
        ],
        "builtin",
        None,
        1,
    )

    # Environmental Science
    lesson_id = add_lesson(
        environment_id,
        "Human Impact on Environment",
        "Learn about how humans affect Earth",
        [
            "Pollution: harmful substances in environment",
            "Deforestation: cutting down forests",
            "Overfishing: taking too many fish from oceans",
            "Climate change: global warming from human activities",
            "These impacts affect all living things",
        ],
        [
            {
                "title": "Examples",
                "content": "Pollution: air pollution from cars, water pollution from factories. Deforestation: Amazon rainforest, overfishing: cod populations",
            }
        ],
        "builtin",
        None,
        1,
    )

    lesson_id = add_lesson(
        environment_id,
        "Conservation and Sustainability",
        "Learn about protecting our planet",
        [
            "Conservation: protecting natural resources",
            "Sustainability: meeting needs without harming future generations",
            "Renewable resources: can be replaced naturally",
            "Nonrenewable resources: cannot be replaced easily",
            "We all have a role in protecting the environment",
        ],
        [
            {
                "title": "Examples",
                "content": "Renewable: solar energy, wind energy, trees. Nonrenewable: oil, coal, natural gas. Conservation: recycling, reducing waste",
            }
        ],
        "builtin",
        None,
        1,
    )


def seed_advanced_science_lessons(
    molecular_biology_id, organic_chemistry_id, quantum_physics_id, climate_science_id
):
    """Seed advanced science lessons."""

    # Molecular Biology
    lesson_id = add_lesson(
        molecular_biology_id,
        "DNA Structure and Function",
        "Learn about the molecule of life",
        [
            "DNA: deoxyribonucleic acid, contains genetic information",
            "Double helix: twisted ladder structure",
            "Nucleotides: building blocks of DNA (A, T, G, C)",
            "Genes: sections of DNA that code for proteins",
            "DNA replication: how cells copy genetic information",
        ],
        [
            {
                "title": "Examples",
                "content": "A pairs with T, G pairs with C. Human DNA: 3 billion base pairs, 20,000-25,000 genes",
            }
        ],
        "builtin",
        None,
        1,
    )

    lesson_id = add_lesson(
        molecular_biology_id,
        "Protein Synthesis",
        "Learn how cells make proteins",
        [
            "Transcription: DNA copied to RNA in nucleus",
            "Translation: RNA used to make proteins at ribosomes",
            "mRNA: messenger RNA carries genetic code",
            "tRNA: transfer RNA brings amino acids",
            "Proteins: do most of the work in cells",
        ],
        [
            {
                "title": "Example",
                "content": "DNA → mRNA → Protein. Each 3-letter code (codon) specifies one amino acid",
            }
        ],
        "builtin",
        None,
        1,
    )

    # Organic Chemistry
    lesson_id = add_lesson(
        organic_chemistry_id,
        "Carbon Chemistry",
        "Learn about carbon-based compounds",
        [
            "Organic chemistry: study of carbon compounds",
            "Carbon: can form 4 bonds, creates diverse molecules",
            "Hydrocarbons: compounds of carbon and hydrogen",
            "Functional groups: specific groups that give properties",
            "Organic compounds: basis of all life on Earth",
        ],
        [
            {
                "title": "Examples",
                "content": "Methane: CH₄, Ethane: C₂H₆, Benzene: C₆H₆. Functional groups: -OH (alcohol), -COOH (acid)",
            }
        ],
        "builtin",
        None,
        1,
    )

    # Quantum Physics
    lesson_id = add_lesson(
        quantum_physics_id,
        "Wave-Particle Duality",
        "Learn about the strange nature of light and matter",
        [
            "Light behaves as both wave and particle",
            "Photons: particles of light",
            "Electrons: can behave as waves or particles",
            "Quantum mechanics: physics of very small particles",
            "This challenges our everyday understanding of reality",
        ],
        [
            {
                "title": "Examples",
                "content": "Light: wave (interference patterns) and particle (photoelectric effect). Electron: particle (charge) and wave (diffraction)",
            }
        ],
        "builtin",
        None,
        1,
    )

    # Climate Science
    lesson_id = add_lesson(
        climate_science_id,
        "Climate Change Science",
        "Learn about global warming and its effects",
        [
            "Global warming: increase in Earth's average temperature",
            "Greenhouse gases: trap heat in atmosphere",
            "Carbon dioxide: main greenhouse gas from human activities",
            "Effects: rising sea levels, extreme weather, ecosystem changes",
            "Solutions: renewable energy, energy efficiency, carbon capture",
        ],
        [
            {
                "title": "Examples",
                "content": "CO₂ levels: 280 ppm (pre-industrial) → 420 ppm (today). Temperature: +1.1°C since 1880. Sea level: +8 inches since 1900",
            }
        ],
        "builtin",
        None,
        1,
    )


if __name__ == "__main__":
    seed_massive_science_curriculum()
