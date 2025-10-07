"""
MASSIVE Arts & Music Curriculum with Grade Levels
This creates a comprehensive Arts curriculum for K-8 with grade-specific topics and lessons.
"""

from database import (
    add_subject,
    add_topic,
    add_lesson,
    add_practice_problem,
    get_all_subjects,
    get_topics_by_subject,
)


def seed_massive_arts_curriculum():
    """Seed the database with MASSIVE Arts curriculum organized by grade levels."""

    # Check if already seeded
    existing_subjects = get_all_subjects()
    if existing_subjects and any(
        s["name"] == "Arts & Music" for s in existing_subjects
    ):
        print("Arts & Music curriculum already seeded.")
        return

    print("Seeding MASSIVE Arts & Music curriculum...")

    # Create Arts subject
    arts_id = add_subject(
        "Arts & Music", "Visual arts, music, drama, and creative expression", "🎨", 5
    )

    # VISUAL ARTS TOPICS
    k_art_id = add_topic(
        arts_id, "K - Art Basics", "Learn colors, shapes, and basic art skills", 1
    )
    g1_art_id = add_topic(
        arts_id, "1st - Drawing & Painting", "Learn to draw and paint", 2
    )
    g2_art_id = add_topic(
        arts_id, "2nd - Art Materials", "Explore different art materials", 3
    )
    g3_art_id = add_topic(
        arts_id, "3rd - Art Elements", "Learn line, shape, color, texture", 4
    )
    g4_art_id = add_topic(
        arts_id, "4th - Art Techniques", "Master drawing and painting techniques", 5
    )
    g5_art_id = add_topic(
        arts_id, "5th - Art History", "Learn about famous artists and art movements", 6
    )
    g6_art_id = add_topic(
        arts_id, "6th - Advanced Drawing", "Develop advanced drawing skills", 7
    )
    g7_art_id = add_topic(
        arts_id, "7th - Painting Styles", "Explore different painting styles", 8
    )
    g8_art_id = add_topic(
        arts_id, "8th - Mixed Media", "Combine different art forms", 9
    )

    # MUSIC TOPICS
    k_music_id = add_topic(
        arts_id, "K - Music Basics", "Learn rhythm, sounds, and singing", 10
    )
    g1_music_id = add_topic(
        arts_id, "1st - Musical Instruments", "Learn about different instruments", 11
    )
    g2_music_id = add_topic(
        arts_id, "2nd - Reading Music", "Learn to read basic music notation", 12
    )
    g3_music_id = add_topic(
        arts_id, "3rd - Melody & Harmony", "Understand melody and harmony", 13
    )
    g4_music_id = add_topic(
        arts_id, "4th - Music Theory", "Learn basic music theory", 14
    )
    g5_music_id = add_topic(
        arts_id, "5th - Music History", "Study famous composers and music eras", 15
    )
    g6_music_id = add_topic(
        arts_id, "6th - Playing Instruments", "Learn to play an instrument", 16
    )
    g7_music_id = add_topic(arts_id, "7th - Songwriting", "Create your own music", 17)
    g8_music_id = add_topic(
        arts_id, "8th - Music Production", "Learn recording and production", 18
    )

    # DRAMA & THEATER TOPICS
    drama_basics_id = add_topic(
        arts_id, "Drama Basics", "Learn acting and theater skills", 19
    )
    theater_production_id = add_topic(
        arts_id, "Theater Production", "Learn about putting on a show", 20
    )

    # DANCE TOPICS
    dance_basics_id = add_topic(
        arts_id, "Dance Basics", "Learn basic dance moves and styles", 21
    )
    choreography_id = add_topic(arts_id, "Choreography", "Create dance routines", 22)

    # CREATIVE ARTS TOPICS
    photography_id = add_topic(arts_id, "Photography", "Learn to take great photos", 23)
    digital_art_id = add_topic(
        arts_id, "Digital Art", "Create art using technology", 24
    )
    crafts_id = add_topic(arts_id, "Crafts & DIY", "Make cool crafts and projects", 25)

    # Seed lessons
    seed_visual_arts_lessons(
        k_art_id,
        g1_art_id,
        g2_art_id,
        g3_art_id,
        g4_art_id,
        g5_art_id,
        g6_art_id,
        g7_art_id,
        g8_art_id,
    )
    seed_music_lessons(
        k_music_id,
        g1_music_id,
        g2_music_id,
        g3_music_id,
        g4_music_id,
        g5_music_id,
        g6_music_id,
        g7_music_id,
        g8_music_id,
    )
    seed_drama_dance_lessons(
        drama_basics_id, theater_production_id, dance_basics_id, choreography_id
    )
    seed_creative_arts_lessons(photography_id, digital_art_id, crafts_id)

    print("MASSIVE Arts & Music curriculum seeded successfully!")


def seed_visual_arts_lessons(
    k_art_id,
    g1_art_id,
    g2_art_id,
    g3_art_id,
    g4_art_id,
    g5_art_id,
    g6_art_id,
    g7_art_id,
    g8_art_id,
):
    """Seed visual arts lessons."""

    # Kindergarten Art
    lesson_id = add_lesson(
        k_art_id,
        "Primary Colors",
        "Learn about red, yellow, and blue",
        [
            "Primary colors are red, yellow, and blue",
            "These colors cannot be made by mixing other colors",
            "All other colors come from mixing primary colors",
            "Practice painting with primary colors",
            "Try mixing colors to see what happens",
        ],
        [
            {
                "title": "Examples",
                "content": "Red + Yellow = Orange, Blue + Yellow = Green, Red + Blue = Purple",
            }
        ],
        "builtin",
        None,
        1,
    )

    lesson_id = add_lesson(
        k_art_id,
        "Drawing Basic Shapes",
        "Learn to draw circles, squares, and triangles",
        [
            "Start with simple shapes: circles, squares, triangles",
            "Practice drawing these shapes over and over",
            "Shapes are the building blocks of all drawings",
            "Combine shapes to make pictures",
            "Have fun creating with shapes",
        ],
        [
            {
                "title": "Examples",
                "content": "Circle = sun, face, ball. Square = house, box, window. Triangle = roof, mountain, tree",
            }
        ],
        "builtin",
        None,
        1,
    )

    # Grade 1 Art
    lesson_id = add_lesson(
        g1_art_id,
        "Drawing People",
        "Learn to draw simple figures",
        [
            "Start with a circle for the head",
            "Add a rectangle or oval for the body",
            "Draw stick arms and legs",
            "Add details: eyes, nose, mouth, hair",
            "Practice drawing your family and friends",
        ],
        [
            {
                "title": "Example",
                "content": "Circle head + oval body + stick arms and legs + details = person",
            }
        ],
        "builtin",
        None,
        1,
    )

    lesson_id = add_lesson(
        g1_art_id,
        "Painting with Watercolors",
        "Learn basic watercolor techniques",
        [
            "Watercolors are paints you mix with water",
            "Use a brush to apply paint to paper",
            "More water makes lighter colors",
            "Less water makes darker colors",
            "Let layers dry before adding more",
        ],
        [
            {
                "title": "Examples",
                "content": "Wet-on-wet: paint on wet paper for soft effects. Wet-on-dry: paint on dry paper for sharp edges",
            }
        ],
        "builtin",
        None,
        1,
    )

    # Grade 2 Art
    lesson_id = add_lesson(
        g2_art_id,
        "Clay and Sculpture",
        "Learn to work with clay",
        [
            "Clay is a soft material you can shape",
            "Basic techniques: rolling, pinching, coiling",
            "Make simple sculptures like bowls, animals, figures",
            "Clay can be dried or baked to harden",
            "Paint your clay creations when dry",
        ],
        [
            {
                "title": "Examples",
                "content": "Roll clay into a ball, pinch to make a bowl. Roll clay into coils, stack to make a pot",
            }
        ],
        "builtin",
        None,
        1,
    )

    # Grade 3 Art
    lesson_id = add_lesson(
        g3_art_id,
        "Line in Art",
        "Learn about different types of lines",
        [
            "Lines are the foundation of art",
            "Types: straight, curved, zigzag, wavy, dotted",
            "Lines can show movement, emotion, texture",
            "Thick lines are bold, thin lines are delicate",
            "Practice creating art using only lines",
        ],
        [
            {
                "title": "Examples",
                "content": "Straight lines: buildings, fences. Curved lines: waves, flowers. Zigzag: lightning, mountains",
            }
        ],
        "builtin",
        None,
        1,
    )

    lesson_id = add_lesson(
        g3_art_id,
        "Color Theory",
        "Learn how colors work together",
        [
            "Color wheel: shows how colors relate",
            "Warm colors: red, orange, yellow (feel warm)",
            "Cool colors: blue, green, purple (feel cool)",
            "Complementary colors: opposite on wheel, look great together",
            "Use color to create mood in your art",
        ],
        [
            {
                "title": "Examples",
                "content": "Warm: sunset, fire, summer. Cool: ocean, winter, sky. Complementary: red/green, blue/orange, yellow/purple",
            }
        ],
        "builtin",
        None,
        1,
    )

    # Grade 4 Art
    lesson_id = add_lesson(
        g4_art_id,
        "Perspective Drawing",
        "Learn to draw in 3D",
        [
            "Perspective makes drawings look 3D",
            "One-point perspective: lines go to one vanishing point",
            "Objects look smaller as they go farther away",
            "Use perspective to draw buildings, roads, rooms",
            "Practice with simple shapes first",
        ],
        [
            {
                "title": "Example",
                "content": "Draw a road: sides get closer together as they go back, meet at vanishing point on horizon",
            }
        ],
        "builtin",
        None,
        1,
    )

    # Grade 5 Art
    lesson_id = add_lesson(
        g5_art_id,
        "Famous Artists",
        "Learn about great artists in history",
        [
            "Leonardo da Vinci: Renaissance artist, painted Mona Lisa",
            "Vincent van Gogh: Post-Impressionist, painted Starry Night",
            "Pablo Picasso: Cubist, created unique abstract art",
            "Frida Kahlo: Mexican artist, painted self-portraits",
            "Study their techniques and try their styles",
        ],
        [
            {
                "title": "Examples",
                "content": "Da Vinci: realistic, detailed. Van Gogh: thick paint, swirly. Picasso: geometric shapes. Kahlo: colorful, personal",
            }
        ],
        "builtin",
        None,
        1,
    )

    # Grade 6 Art
    lesson_id = add_lesson(
        g6_art_id,
        "Portrait Drawing",
        "Learn to draw realistic faces",
        [
            "Face proportions: eyes are in the middle",
            "Eyes are one eye-width apart",
            "Nose is halfway between eyes and chin",
            "Mouth is halfway between nose and chin",
            "Practice drawing from photos",
        ],
        [
            {
                "title": "Example",
                "content": "Draw oval, divide in half horizontally for eyes, divide lower half for nose and mouth",
            }
        ],
        "builtin",
        None,
        1,
    )

    # Grade 7 Art
    lesson_id = add_lesson(
        g7_art_id,
        "Impressionism",
        "Learn the Impressionist painting style",
        [
            "Impressionism: art movement from 1800s",
            "Focus on light and color rather than details",
            "Paint with visible brushstrokes",
            "Capture a moment or impression",
            "Famous Impressionists: Monet, Renoir, Degas",
        ],
        [
            {
                "title": "Examples",
                "content": "Monet: Water Lilies, haystacks. Characteristics: soft edges, bright colors, outdoor scenes",
            }
        ],
        "builtin",
        None,
        1,
    )

    # Grade 8 Art
    lesson_id = add_lesson(
        g8_art_id,
        "Collage and Mixed Media",
        "Combine different materials in art",
        [
            "Mixed media: using multiple materials in one artwork",
            "Can include: paper, fabric, paint, photos, found objects",
            "Collage: gluing different materials onto a surface",
            "Experiment with textures and layers",
            "Create unique, personal artworks",
        ],
        [
            {
                "title": "Examples",
                "content": "Magazine collage, texture collage, photo montage, assemblage with objects",
            }
        ],
        "builtin",
        None,
        1,
    )


def seed_music_lessons(
    k_music_id,
    g1_music_id,
    g2_music_id,
    g3_music_id,
    g4_music_id,
    g5_music_id,
    g6_music_id,
    g7_music_id,
    g8_music_id,
):
    """Seed music lessons."""

    # Kindergarten Music
    lesson_id = add_lesson(
        k_music_id,
        "Rhythm and Beat",
        "Learn about rhythm in music",
        [
            "Beat: steady pulse in music",
            "Rhythm: pattern of long and short sounds",
            "Clap along to songs to feel the beat",
            "Practice simple rhythms by clapping",
            "Music is made of patterns of sounds",
        ],
        [
            {
                "title": "Examples",
                "content": "Beat: clap steady like a clock. Rhythm: clap-clap-pause-clap, clap-pause-pause-clap",
            }
        ],
        "builtin",
        None,
        1,
    )

    lesson_id = add_lesson(
        k_music_id,
        "High and Low Sounds",
        "Learn about pitch in music",
        [
            "Pitch: how high or low a sound is",
            "High sounds: small animals, small instruments",
            "Low sounds: big animals, big instruments",
            "Practice singing high and low notes",
            "Music uses both high and low sounds",
        ],
        [
            {
                "title": "Examples",
                "content": "High: bird chirping, whistle, piccolo. Low: lion roaring, drum, tuba",
            }
        ],
        "builtin",
        None,
        1,
    )

    # Grade 1 Music
    lesson_id = add_lesson(
        g1_music_id,
        "Instrument Families",
        "Learn about different types of instruments",
        [
            "String instruments: violin, guitar, harp (pluck or bow strings)",
            "Wind instruments: flute, trumpet, clarinet (blow air)",
            "Percussion instruments: drums, xylophone, tambourine (hit or shake)",
            "Keyboard instruments: piano, organ (press keys)",
            "Each family makes sound in a different way",
        ],
        [
            {
                "title": "Examples",
                "content": "Strings: violin, guitar, cello. Winds: flute, trumpet, saxophone. Percussion: drums, cymbals, triangle",
            }
        ],
        "builtin",
        None,
        1,
    )

    # Grade 2 Music
    lesson_id = add_lesson(
        g2_music_id,
        "Musical Notes",
        "Learn to read basic music notation",
        [
            "Notes: symbols that represent sounds",
            "Staff: five lines where notes are written",
            "Notes on lines and spaces have different pitches",
            "Quarter note: one beat, half note: two beats, whole note: four beats",
            "Practice reading simple melodies",
        ],
        [
            {
                "title": "Examples",
                "content": "Quarter note looks like filled circle with stem. Half note has hollow circle. Whole note has no stem",
            }
        ],
        "builtin",
        None,
        1,
    )

    # Grade 3 Music
    lesson_id = add_lesson(
        g3_music_id,
        "Melody",
        "Learn about melody in music",
        [
            "Melody: the main tune you sing or hum",
            "Made up of notes at different pitches",
            "Melodies go up and down",
            "Some melodies are smooth, others are jumpy",
            "Practice singing simple melodies",
        ],
        [
            {
                "title": "Examples",
                "content": "Twinkle Twinkle: smooth melody. Happy Birthday: familiar melody. Every song has a melody",
            }
        ],
        "builtin",
        None,
        1,
    )

    lesson_id = add_lesson(
        g3_music_id,
        "Harmony",
        "Learn about harmony in music",
        [
            "Harmony: two or more notes played together",
            "Harmony supports the melody",
            "Chords: groups of notes played together",
            "Harmony makes music fuller and richer",
            "Try singing in harmony with others",
        ],
        [
            {
                "title": "Examples",
                "content": "Row Your Boat: rounds create harmony. Guitar chords accompany singing. Choir parts create harmony",
            }
        ],
        "builtin",
        None,
        1,
    )

    # Grade 4 Music
    lesson_id = add_lesson(
        g4_music_id,
        "Music Scales",
        "Learn about musical scales",
        [
            "Scale: sequence of notes going up or down",
            "Major scale: sounds happy and bright",
            "Minor scale: sounds sad or serious",
            "Scales are the foundation of melodies",
            "Practice singing and playing scales",
        ],
        [
            {
                "title": "Examples",
                "content": "C major scale: C-D-E-F-G-A-B-C (do-re-mi-fa-sol-la-ti-do)",
            }
        ],
        "builtin",
        None,
        1,
    )

    # Grade 5 Music
    lesson_id = add_lesson(
        g5_music_id,
        "Famous Composers",
        "Learn about great composers in history",
        [
            "Wolfgang Amadeus Mozart: Classical composer, child prodigy",
            "Ludwig van Beethoven: composed while deaf",
            "Johann Sebastian Bach: Baroque composer, organ master",
            "Pyotr Tchaikovsky: composed ballets like Nutcracker",
            "Listen to their music and learn their stories",
        ],
        [
            {
                "title": "Examples",
                "content": "Mozart: Eine Kleine Nachtmusik. Beethoven: Symphony No. 5. Bach: Toccata and Fugue",
            }
        ],
        "builtin",
        None,
        1,
    )

    # Grade 6 Music
    lesson_id = add_lesson(
        g6_music_id,
        "Playing Piano Basics",
        "Learn basic piano skills",
        [
            "Piano has white and black keys",
            "White keys: C-D-E-F-G-A-B",
            "Black keys: sharps and flats",
            "Right hand plays melody, left hand plays chords",
            "Practice simple songs with both hands",
        ],
        [
            {
                "title": "Examples",
                "content": "C is to the left of two black keys. Start with simple songs like Ode to Joy, Mary Had a Little Lamb",
            }
        ],
        "builtin",
        None,
        1,
    )

    # Grade 7 Music
    lesson_id = add_lesson(
        g7_music_id,
        "Writing Songs",
        "Learn to create your own music",
        [
            "Start with lyrics: write about your feelings or experiences",
            "Create a melody that fits the lyrics",
            "Add chords to support the melody",
            "Think about song structure: verse, chorus, bridge",
            "Record your songs to share with others",
        ],
        [
            {
                "title": "Example",
                "content": "Song structure: Verse 1 - Chorus - Verse 2 - Chorus - Bridge - Chorus",
            }
        ],
        "builtin",
        None,
        1,
    )

    # Grade 8 Music
    lesson_id = add_lesson(
        g8_music_id,
        "Music Technology",
        "Learn about recording and production",
        [
            "Digital Audio Workstation (DAW): software for recording",
            "Recording: capture sounds with microphone",
            "Editing: cut, copy, and arrange recordings",
            "Mixing: balance levels of different tracks",
            "Modern music is created using technology",
        ],
        [
            {
                "title": "Examples",
                "content": "DAWs: GarageBand, Audacity, FL Studio. Can record vocals, instruments, create electronic music",
            }
        ],
        "builtin",
        None,
        1,
    )


def seed_drama_dance_lessons(
    drama_basics_id, theater_production_id, dance_basics_id, choreography_id
):
    """Seed drama and dance lessons."""

    # Drama
    lesson_id = add_lesson(
        drama_basics_id,
        "Acting Basics",
        "Learn fundamental acting skills",
        [
            "Acting is pretending to be someone else",
            "Use your voice, body, and emotions",
            "Stay in character throughout the scene",
            "React to what other actors do",
            "Practice makes you a better actor",
        ],
        [
            {
                "title": "Examples",
                "content": "Voice: loud and clear, different voices for different characters. Body: use gestures, facial expressions. Emotions: happy, sad, angry, scared",
            }
        ],
        "builtin",
        None,
        1,
    )

    lesson_id = add_lesson(
        theater_production_id,
        "Putting on a Play",
        "Learn about theater production",
        [
            "Script: the written words of the play",
            "Director: leads rehearsals and makes decisions",
            "Actors: perform the characters",
            "Stage crew: handles lights, sound, scenery",
            "Everyone works together to create a show",
        ],
        [
            {
                "title": "Examples",
                "content": "Jobs: actor, director, stage manager, lighting, sound, costumes, props, set design",
            }
        ],
        "builtin",
        None,
        1,
    )

    # Dance
    lesson_id = add_lesson(
        dance_basics_id,
        "Basic Dance Moves",
        "Learn fundamental dance steps",
        [
            "Ballet: graceful, pointed toes, positions",
            "Jazz: energetic, sharp movements",
            "Hip hop: urban, freestyle, creative",
            "Tap: rhythmic, metal taps on shoes",
            "Start with basic steps and build from there",
        ],
        [
            {
                "title": "Examples",
                "content": "Ballet: plié, tendu, relevé. Jazz: kicks, turns, leaps. Hip hop: popping, locking, breaking",
            }
        ],
        "builtin",
        None,
        1,
    )

    lesson_id = add_lesson(
        choreography_id,
        "Creating Dance Routines",
        "Learn to choreograph dances",
        [
            "Choreography: creating dance movements",
            "Match movements to the music",
            "Create patterns and formations",
            "Think about levels: high, medium, low",
            "Tell a story through dance",
        ],
        [
            {
                "title": "Examples",
                "content": "Start with 8-count: match moves to music beats. Combine steps: turn + kick + jump. Practice and refine",
            }
        ],
        "builtin",
        None,
        1,
    )


def seed_creative_arts_lessons(photography_id, digital_art_id, crafts_id):
    """Seed creative arts lessons."""

    # Photography
    lesson_id = add_lesson(
        photography_id,
        "Basic Photography",
        "Learn to take great photos",
        [
            "Composition: how you arrange elements in photo",
            "Rule of thirds: divide image into 9 parts",
            "Lighting: natural light is often best",
            "Focus: make sure subject is sharp",
            "Practice taking lots of photos",
        ],
        [
            {
                "title": "Examples",
                "content": "Rule of thirds: place subject at intersection points. Lighting: golden hour (sunrise/sunset). Focus: tap on subject on phone",
            }
        ],
        "builtin",
        None,
        1,
    )

    # Digital Art
    lesson_id = add_lesson(
        digital_art_id,
        "Digital Drawing",
        "Create art on computer or tablet",
        [
            "Digital art: creating art using technology",
            "Tools: drawing tablet, stylus, software",
            "Layers: separate elements you can edit independently",
            "Can easily undo mistakes",
            "Many professional artists use digital tools",
        ],
        [
            {
                "title": "Examples",
                "content": "Software: Procreate, Adobe Photoshop, GIMP. Start with simple drawings, use layers for colors",
            }
        ],
        "builtin",
        None,
        1,
    )

    # Crafts
    lesson_id = add_lesson(
        crafts_id,
        "Fun Crafts Projects",
        "Make cool things with your hands",
        [
            "Paper crafts: origami, cards, decorations",
            "Fabric crafts: sewing, knitting, tie-dye",
            "Recycled crafts: use old materials creatively",
            "Holiday crafts: make decorations and gifts",
            "Crafts are fun and useful",
        ],
        [
            {
                "title": "Examples",
                "content": "Origami: fold paper into shapes. Tie-dye: create colorful patterns on fabric. Recycled: make bird feeder from bottle",
            }
        ],
        "builtin",
        None,
        1,
    )


if __name__ == "__main__":
    seed_massive_arts_curriculum()
