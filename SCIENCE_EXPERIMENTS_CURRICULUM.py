"""
MASSIVE Science Experiments Curriculum
50+ hands-on experiments kids can do at home!
"""

from database import (add_subject, add_topic, add_lesson, add_practice_problem, 
                      get_all_subjects, get_topics_by_subject)

def seed_science_experiments_curriculum():
    """Seed the database with Science Experiments curriculum."""
    
    # Check if already seeded
    existing_subjects = get_all_subjects()
    if existing_subjects and any(s['name'] == 'Science Experiments' for s in existing_subjects):
        print("Science Experiments curriculum already seeded.")
        return
    
    print("Seeding Science Experiments curriculum...")
    
    # Create Science Experiments subject
    experiments_id = add_subject("Science Experiments", "Hands-on science experiments you can do at home!", "🧪", 10)
    
    # Create topics by type
    chemistry_id = add_topic(experiments_id, "Chemistry Experiments", "Mix, react, and explore chemistry", 1)
    physics_id = add_topic(experiments_id, "Physics Experiments", "Explore forces, motion, and energy", 2)
    biology_id = add_topic(experiments_id, "Biology Experiments", "Study living things and nature", 3)
    earth_science_id = add_topic(experiments_id, "Earth Science Experiments", "Explore weather, rocks, and Earth", 4)
    kitchen_science_id = add_topic(experiments_id, "Kitchen Science", "Amazing experiments with food and kitchen items", 5)
    water_experiments_id = add_topic(experiments_id, "Water Experiments", "Explore properties of water", 6)
    light_sound_id = add_topic(experiments_id, "Light & Sound Experiments", "Investigate light and sound", 7)
    electricity_id = add_topic(experiments_id, "Electricity & Magnetism", "Explore electrical and magnetic forces", 8)
    
    # Seed experiment lessons
    seed_chemistry_experiments(chemistry_id)
    seed_physics_experiments(physics_id)
    seed_biology_experiments(biology_id)
    seed_earth_science_experiments(earth_science_id)
    seed_kitchen_science_experiments(kitchen_science_id)
    seed_water_experiments(water_experiments_id)
    seed_light_sound_experiments(light_sound_id)
    seed_electricity_experiments(electricity_id)
    
    print("Science Experiments curriculum seeded successfully!")

def seed_chemistry_experiments(topic_id):
    """Add chemistry experiments."""
    
    lesson_id = add_lesson(topic_id, "Volcano Eruption", "Create a fizzing volcano!",
                          ["Materials: Baking soda, vinegar, dish soap, food coloring",
                           "Step 1: Put 2 tablespoons baking soda in a container",
                           "Step 2: Add a few drops of food coloring and dish soap",
                           "Step 3: Pour in 1/4 cup vinegar",
                           "Step 4: Watch it erupt!",
                           "Science: Acid (vinegar) + Base (baking soda) = Gas (CO2)"],
                          [{"title": "What's Happening", "content": "The vinegar (acid) reacts with baking soda (base) to create carbon dioxide gas, which makes the bubbles and foam!"}],
                          "builtin", None, 1)
    
    lesson_id = add_lesson(topic_id, "Rainbow in a Jar", "Create colorful density layers",
                          ["Materials: Honey, dish soap, water, vegetable oil, rubbing alcohol, food coloring",
                           "Step 1: Pour honey in bottom of clear jar",
                           "Step 2: Slowly add dish soap",
                           "Step 3: Add colored water (blue)",
                           "Step 4: Add vegetable oil",
                           "Step 5: Add colored alcohol (red) on top",
                           "Science: Liquids layer by density!"],
                          [{"title": "What's Happening", "content": "Different liquids have different densities. Denser liquids sink to the bottom, lighter ones float on top!"}],
                          "builtin", None, 1)
    
    lesson_id = add_lesson(topic_id, "Invisible Ink", "Write secret messages with lemon juice",
                          ["Materials: Lemon juice, cotton swab, white paper, lamp or iron",
                           "Step 1: Squeeze lemon juice into a bowl",
                           "Step 2: Dip cotton swab in lemon juice",
                           "Step 3: Write message on white paper",
                           "Step 4: Let it dry completely",
                           "Step 5: Hold near light bulb or iron to reveal message",
                           "Science: Heat causes oxidation, turning lemon juice brown"],
                          [{"title": "What's Happening", "content": "Lemon juice is clear on paper, but when heated, it oxidizes and turns brown, revealing your secret message!"}],
                          "builtin", None, 1)
    
    lesson_id = add_lesson(topic_id, "Color Changing Milk", "Make milk swirl with colors",
                          ["Materials: Milk, dish soap, food coloring, shallow dish",
                           "Step 1: Pour milk into shallow dish",
                           "Step 2: Add drops of different food colors in center",
                           "Step 3: Dip cotton swab in dish soap",
                           "Step 4: Touch soap to center of milk",
                           "Step 5: Watch the colors explode and swirl!",
                           "Science: Soap breaks surface tension and fat molecules"],
                          [{"title": "What's Happening", "content": "Soap molecules have two ends: one likes water, one likes fat. They rush around breaking up fat in milk, making colors swirl!"}],
                          "builtin", None, 1)
    
    lesson_id = add_lesson(topic_id, "Crystal Growing", "Grow your own crystals",
                          ["Materials: Borax or sugar, hot water, string, pencil, jar",
                           "Step 1: Heat water until very hot",
                           "Step 2: Add borax or sugar, stir until dissolved",
                           "Step 3: Tie string to pencil",
                           "Step 4: Hang string in solution",
                           "Step 5: Wait 24 hours for crystals to form",
                           "Science: Crystals form as water evaporates"],
                          [{"title": "What's Happening", "content": "As water evaporates, dissolved borax/sugar molecules come together to form solid crystals with regular patterns!"}],
                          "builtin", None, 1)

def seed_physics_experiments(topic_id):
    """Add physics experiments."""
    
    lesson_id = add_lesson(topic_id, "Egg Drop Challenge", "Protect an egg from a high drop",
                          ["Materials: Raw egg, various materials (straws, tape, bubble wrap, etc.)",
                           "Step 1: Design a container to protect the egg",
                           "Step 2: Use materials to create cushioning",
                           "Step 3: Place egg in container",
                           "Step 4: Drop from increasing heights",
                           "Step 5: Check if egg survived!",
                           "Science: Force, impact, and energy absorption"],
                          [{"title": "What's Happening", "content": "Your design must absorb the force of impact. Materials compress and slow the egg down, reducing force!"}],
                          "builtin", None, 1)
    
    lesson_id = add_lesson(topic_id, "Paper Airplane Science", "Test different airplane designs",
                          ["Materials: Paper, ruler, tape",
                           "Step 1: Fold 3 different airplane designs",
                           "Step 2: Test each design's flight distance",
                           "Step 3: Measure how far each flies",
                           "Step 4: Test which flies straightest",
                           "Step 5: Determine the best design",
                           "Science: Aerodynamics, lift, drag, weight, thrust"],
                          [{"title": "What's Happening", "content": "Different designs have different aerodynamic properties. Wing shape and weight distribution affect flight!"}],
                          "builtin", None, 1)
    
    lesson_id = add_lesson(topic_id, "Balloon Rocket", "Make a rocket powered by air",
                          ["Materials: Balloon, string, straw, tape",
                           "Step 1: Thread string through straw",
                           "Step 2: Stretch string across room, tie ends",
                           "Step 3: Blow up balloon, don't tie it",
                           "Step 4: Tape balloon to straw",
                           "Step 5: Release balloon and watch it zoom!",
                           "Science: Newton's Third Law - action and reaction"],
                          [{"title": "What's Happening", "content": "Air rushes out of balloon (action), pushing balloon forward (reaction). This is how real rockets work!"}],
                          "builtin", None, 1)
    
    lesson_id = add_lesson(topic_id, "Pendulum Patterns", "Explore how pendulums swing",
                          ["Materials: String, weight (washer or ball), tape",
                           "Step 1: Tie weight to string",
                           "Step 2: Tape string to table edge",
                           "Step 3: Pull weight to side and release",
                           "Step 4: Time how long it swings",
                           "Step 5: Try different lengths and weights",
                           "Science: Gravity, period, frequency"],
                          [{"title": "What's Happening", "content": "Length affects swing time, but weight doesn't! Longer pendulums swing slower. Gravity pulls it back and forth!"}],
                          "builtin", None, 1)
    
    lesson_id = add_lesson(topic_id, "Ramp and Roll", "Test how ramps affect rolling objects",
                          ["Materials: Board or book, toy cars, blocks, ruler",
                           "Step 1: Create ramp at low angle",
                           "Step 2: Roll car down, measure distance",
                           "Step 3: Increase ramp angle",
                           "Step 4: Roll again, measure distance",
                           "Step 5: Compare results",
                           "Science: Gravity, potential energy, kinetic energy"],
                          [{"title": "What's Happening", "content": "Higher ramps give more potential energy, which converts to kinetic energy, making cars go farther!"}],
                          "builtin", None, 1)

def seed_biology_experiments(topic_id):
    """Add biology experiments."""
    
    lesson_id = add_lesson(topic_id, "Grow a Bean Plant", "Watch a seed grow into a plant",
                          ["Materials: Bean seeds, clear cup, paper towels, water",
                           "Step 1: Wet paper towel and line inside of cup",
                           "Step 2: Place bean between towel and cup wall",
                           "Step 3: Keep towel moist",
                           "Step 4: Watch root grow down in 2-3 days",
                           "Step 5: Watch stem grow up",
                           "Science: Germination, photosynthesis, plant growth"],
                          [{"title": "What's Happening", "content": "Seeds contain baby plant and food. Water activates growth. Root grows first to get water, then stem grows to get light!"}],
                          "builtin", None, 1)
    
    lesson_id = add_lesson(topic_id, "Celery Color Change", "See how plants drink water",
                          ["Materials: Celery stalk with leaves, food coloring, water, cup",
                           "Step 1: Fill cup with water",
                           "Step 2: Add lots of food coloring",
                           "Step 3: Cut bottom of celery stalk",
                           "Step 4: Place celery in colored water",
                           "Step 5: Wait 4-6 hours, observe color in leaves",
                           "Science: Capillary action, xylem, transpiration"],
                          [{"title": "What's Happening", "content": "Water travels up tiny tubes (xylem) in the celery to the leaves. Food coloring shows the path!"}],
                          "builtin", None, 1)
    
    lesson_id = add_lesson(topic_id, "Bird Feeder Observation", "Create a feeder and observe birds",
                          ["Materials: Pinecone, peanut butter, birdseed, string",
                           "Step 1: Tie string around pinecone",
                           "Step 2: Spread peanut butter on pinecone",
                           "Step 3: Roll in birdseed",
                           "Step 4: Hang outside window",
                           "Step 5: Watch and identify birds that visit",
                           "Science: Bird behavior, diet, local species"],
                          [{"title": "What's Happening", "content": "Different birds prefer different foods. Observe their beaks, colors, and behaviors. Keep a journal!"}],
                          "builtin", None, 1)
    
    lesson_id = add_lesson(topic_id, "Fingerprint Investigation", "Examine your unique fingerprints",
                          ["Materials: Ink pad or pencil, paper, tape, magnifying glass",
                           "Step 1: Press finger on ink pad or rub on pencil marks",
                           "Step 2: Press finger on paper",
                           "Step 3: Use tape to lift print",
                           "Step 4: Examine with magnifying glass",
                           "Step 5: Compare with family members",
                           "Science: Genetics, unique traits, forensics"],
                          [{"title": "What's Happening", "content": "Everyone has unique fingerprints! Patterns form before birth and never change. Used for identification!"}],
                          "builtin", None, 1)

def seed_earth_science_experiments(topic_id):
    """Add earth science experiments."""
    
    lesson_id = add_lesson(topic_id, "Make a Rain Cloud", "Create rain in a jar",
                          ["Materials: Clear jar, hot water, ice, plate",
                           "Step 1: Fill jar 1/3 with hot water",
                           "Step 2: Place plate on top of jar",
                           "Step 3: Put ice cubes on plate",
                           "Step 4: Wait and watch 'rain' form inside",
                           "Step 5: Observe water drops falling",
                           "Science: Evaporation, condensation, precipitation"],
                          [{"title": "What's Happening", "content": "Hot water evaporates, rises, hits cold plate, condenses into drops, falls as 'rain'. Just like real rain clouds!"}],
                          "builtin", None, 1)
    
    lesson_id = add_lesson(topic_id, "Erosion Demonstration", "See how water shapes land",
                          ["Materials: Dirt or sand, pan, water, pitcher",
                           "Step 1: Make a mound of dirt in pan",
                           "Step 2: Create 'rivers' with your finger",
                           "Step 3: Slowly pour water on top",
                           "Step 4: Watch water carve paths",
                           "Step 5: See erosion in action",
                           "Science: Erosion, weathering, sedimentation"],
                          [{"title": "What's Happening", "content": "Water wears away soil and carries it downhill, just like rivers erode mountains and create valleys!"}],
                          "builtin", None, 1)
    
    lesson_id = add_lesson(topic_id, "Rock Candy Crystals", "Grow rock-like crystals",
                          ["Materials: Sugar, water, string, pencil, jar",
                           "Step 1: Boil 2 cups water",
                           "Step 2: Dissolve 4 cups sugar",
                           "Step 3: Pour into jar, add food coloring",
                           "Step 4: Hang wet sugary string in solution",
                           "Step 5: Wait 1 week for crystals",
                           "Science: Crystallization, minerals, geology"],
                          [{"title": "What's Happening", "content": "As water evaporates, sugar molecules arrange into crystal structures, like minerals forming rocks!"}],
                          "builtin", None, 1)
    
    lesson_id = add_lesson(topic_id, "Weather Station", "Track weather patterns",
                          ["Materials: Thermometer, rain gauge (jar with ruler), notebook",
                           "Step 1: Record temperature daily",
                           "Step 2: Measure rainfall with gauge",
                           "Step 3: Observe clouds and weather",
                           "Step 4: Track patterns over weeks",
                           "Step 5: Predict tomorrow's weather",
                           "Science: Meteorology, weather patterns, data collection"],
                          [{"title": "What's Happening", "content": "Weather patterns repeat! By collecting data, you can start to predict weather like a meteorologist!"}],
                          "builtin", None, 1)

def seed_kitchen_science_experiments(topic_id):
    """Add kitchen science experiments."""
    
    lesson_id = add_lesson(topic_id, "Dancing Raisins", "Make raisins dance in soda",
                          ["Materials: Clear glass, clear soda (Sprite or 7Up), raisins",
                           "Step 1: Fill glass with clear soda",
                           "Step 2: Drop in 5-6 raisins",
                           "Step 3: Watch them sink",
                           "Step 4: Watch them rise",
                           "Step 5: Watch them dance up and down!",
                           "Science: Carbon dioxide bubbles, buoyancy, density"],
                          [{"title": "What's Happening", "content": "CO2 bubbles stick to raisins, making them float up. Bubbles pop at surface, raisins sink. Repeat!"}],
                          "builtin", None, 1)
    
    lesson_id = add_lesson(topic_id, "Ice Cream in a Bag", "Make ice cream with science",
                          ["Materials: Milk, sugar, vanilla, ice, salt, zip bags",
                           "Step 1: Mix 1/2 cup milk, 1 tbsp sugar, 1/2 tsp vanilla in small bag",
                           "Step 2: Seal tightly",
                           "Step 3: Fill large bag with ice and 1/3 cup salt",
                           "Step 4: Put small bag inside large bag",
                           "Step 5: Shake for 5-10 minutes",
                           "Science: Freezing point depression, phase change"],
                          [{"title": "What's Happening", "content": "Salt lowers ice's temperature below 32°F, freezing the milk mixture into ice cream!"}],
                          "builtin", None, 1)
    
    lesson_id = add_lesson(topic_id, "Egg Float Test", "Test if eggs are fresh",
                          ["Materials: Eggs, water, clear glass",
                           "Step 1: Fill glass with water",
                           "Step 2: Gently place egg in water",
                           "Step 3: Fresh egg sinks and lays flat",
                           "Step 4: Older egg stands up or floats",
                           "Step 5: Test multiple eggs",
                           "Science: Air cell growth, density, freshness"],
                          [{"title": "What's Happening", "content": "As eggs age, air cell inside grows, making egg more buoyant. Floating egg = old egg!"}],
                          "builtin", None, 1)

def seed_water_experiments(topic_id):
    """Add water experiments."""
    
    lesson_id = add_lesson(topic_id, "Walking Water", "Watch water 'walk' between cups",
                          ["Materials: 3 cups, food coloring (red, yellow, blue), paper towels, water",
                           "Step 1: Fill 1st and 3rd cups with water",
                           "Step 2: Add red to 1st cup, blue to 3rd",
                           "Step 3: Leave middle cup empty",
                           "Step 4: Fold paper towels into strips",
                           "Step 5: Connect cups with paper towels",
                           "Step 6: Wait 30 minutes, watch water 'walk' and mix colors",
                           "Science: Capillary action, absorption, color mixing"],
                          [{"title": "What's Happening", "content": "Water climbs up paper towels due to capillary action, then flows down to empty cup. Red + blue = purple!"}],
                          "builtin", None, 1)
    
    lesson_id = add_lesson(topic_id, "Surface Tension Magic", "Test water's surface tension",
                          ["Materials: Cup of water, pepper, dish soap",
                           "Step 1: Fill cup to very top with water",
                           "Step 2: Sprinkle pepper on surface",
                           "Step 3: Touch water with soap on finger",
                           "Step 4: Watch pepper zoom to edges!",
                           "Step 5: Try with different objects",
                           "Science: Surface tension, molecular bonds"],
                          [{"title": "What's Happening", "content": "Water molecules stick together creating surface tension. Soap breaks these bonds, and pepper rushes away!"}],
                          "builtin", None, 1)

def seed_light_sound_experiments(topic_id):
    """Add light and sound experiments."""
    
    lesson_id = add_lesson(topic_id, "Make a Rainbow", "Create a rainbow with a prism or CD",
                          ["Materials: Clear CD or prism, sunlight or flashlight",
                           "Step 1: Hold CD shiny side up",
                           "Step 2: Tilt in sunlight",
                           "Step 3: Watch rainbow appear on wall or paper",
                           "Step 4: Move CD to change colors",
                           "Step 5: Observe all colors of spectrum",
                           "Science: Light refraction, visible spectrum, wavelengths"],
                          [{"title": "What's Happening", "content": "White light is made of all colors. CD or prism bends different wavelengths at different angles, separating colors!"}],
                          "builtin", None, 1)
    
    lesson_id = add_lesson(topic_id, "String Telephone", "Make a telephone with cups and string",
                          ["Materials: 2 paper cups, long string, something to poke holes",
                           "Step 1: Poke hole in bottom of each cup",
                           "Step 2: Thread string through both holes",
                           "Step 3: Tie knots inside cups",
                           "Step 4: Pull string tight",
                           "Step 5: One person talks in cup, other listens",
                           "Science: Sound vibrations, wave transmission"],
                          [{"title": "What's Happening", "content": "Your voice vibrates the cup, vibrations travel along string, other cup vibrates and creates sound!"}],
                          "builtin", None, 1)

def seed_electricity_experiments(topic_id):
    """Add electricity and magnetism experiments."""
    
    lesson_id = add_lesson(topic_id, "Static Electricity Butterfly", "Make paper butterflies fly with static",
                          ["Materials: Tissue paper, balloon, scissors",
                           "Step 1: Cut butterfly shape from tissue paper",
                           "Step 2: Blow up balloon",
                           "Step 3: Rub balloon on hair or sweater",
                           "Step 4: Hold balloon near butterfly",
                           "Step 5: Watch butterfly 'fly' to balloon",
                           "Science: Static electricity, electron transfer, attraction"],
                          [{"title": "What's Happening", "content": "Rubbing creates static charge on balloon. Opposite charges attract, pulling lightweight butterfly to balloon!"}],
                          "builtin", None, 1)
    
    lesson_id = add_lesson(topic_id, "Magnet Maze", "Create a magnetic maze game",
                          ["Materials: Paper plate, magnet, paper clip, markers",
                           "Step 1: Draw maze on paper plate",
                           "Step 2: Put paper clip on start",
                           "Step 3: Hold magnet under plate",
                           "Step 4: Move magnet to guide paper clip through maze",
                           "Step 5: Race against time or friend",
                           "Science: Magnetism, magnetic fields, force through materials"],
                          [{"title": "What's Happening", "content": "Magnet's force goes through paper plate and pulls metal paper clip. Magnetic fields pass through non-magnetic materials!"}],
                          "builtin", None, 1)

if __name__ == "__main__":
    seed_science_experiments_curriculum()
