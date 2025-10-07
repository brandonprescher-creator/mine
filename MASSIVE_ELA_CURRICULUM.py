"""
MASSIVE English Language Arts Curriculum with Grade Levels
This creates a comprehensive ELA curriculum for K-8 with grade-specific topics and lessons.
"""

from database import (add_subject, add_topic, add_lesson, add_practice_problem, 
                      get_all_subjects, get_topics_by_subject)

def seed_massive_ela_curriculum():
    """Seed the database with MASSIVE ELA curriculum organized by grade levels."""
    
    # Check if already seeded
    existing_subjects = get_all_subjects()
    if existing_subjects and any(s['name'] == 'English Language Arts' for s in existing_subjects):
        print("English Language Arts curriculum already seeded.")
        return
    
    print("Seeding MASSIVE ELA curriculum...")
    
    # Create ELA subject
    ela_id = add_subject("English Language Arts", "Reading, writing, grammar, and vocabulary", "📚", 2)
    
    # KINDERGARTEN TOPICS
    k_phonics_id = add_topic(ela_id, "K - Phonics & Letter Sounds", "Learn letters and their sounds", 1)
    k_reading_id = add_topic(ela_id, "K - Beginning Reading", "Start reading simple words", 2)
    k_writing_id = add_topic(ela_id, "K - Pre-Writing Skills", "Learn to write letters and words", 3)
    k_speaking_id = add_topic(ela_id, "K - Speaking & Listening", "Talk and listen to others", 4)
    
    # GRADE 1 TOPICS
    g1_phonics_id = add_topic(ela_id, "1st - Advanced Phonics", "Master letter sounds and blends", 5)
    g1_reading_id = add_topic(ela_id, "1st - Reading Fluency", "Read smoothly and with expression", 6)
    g1_writing_id = add_topic(ela_id, "1st - Sentence Writing", "Write complete sentences", 7)
    g1_grammar_id = add_topic(ela_id, "1st - Basic Grammar", "Learn nouns, verbs, and adjectives", 8)
    
    # GRADE 2 TOPICS
    g2_phonics_id = add_topic(ela_id, "2nd - Complex Phonics", "Learn digraphs and diphthongs", 9)
    g2_reading_id = add_topic(ela_id, "2nd - Reading Comprehension", "Understand what you read", 10)
    g2_writing_id = add_topic(ela_id, "2nd - Paragraph Writing", "Write organized paragraphs", 11)
    g2_grammar_id = add_topic(ela_id, "2nd - Grammar Rules", "Master punctuation and capitalization", 12)
    
    # GRADE 3 TOPICS
    g3_reading_id = add_topic(ela_id, "3rd - Advanced Reading", "Read chapter books and analyze text", 13)
    g3_writing_id = add_topic(ela_id, "3rd - Multi-Paragraph Writing", "Write essays and stories", 14)
    g3_grammar_id = add_topic(ela_id, "3rd - Complex Grammar", "Learn advanced grammar rules", 15)
    g3_vocab_id = add_topic(ela_id, "3rd - Vocabulary Building", "Expand your word knowledge", 16)
    
    # GRADE 4 TOPICS
    g4_reading_id = add_topic(ela_id, "4th - Literary Analysis", "Analyze characters, plot, and theme", 17)
    g4_writing_id = add_topic(ela_id, "4th - Essay Writing", "Write persuasive and informative essays", 18)
    g4_grammar_id = add_topic(ela_id, "4th - Advanced Grammar", "Master complex sentence structures", 19)
    g4_vocab_id = add_topic(ela_id, "4th - Advanced Vocabulary", "Learn sophisticated words", 20)
    
    # GRADE 5 TOPICS
    g5_reading_id = add_topic(ela_id, "5th - Critical Reading", "Think critically about what you read", 21)
    g5_writing_id = add_topic(ela_id, "5th - Research Writing", "Research and write reports", 22)
    g5_grammar_id = add_topic(ela_id, "5th - Grammar Mastery", "Perfect your grammar skills", 23)
    g5_vocab_id = add_topic(ela_id, "5th - Academic Vocabulary", "Learn subject-specific words", 24)
    
    # GRADE 6 TOPICS
    g6_reading_id = add_topic(ela_id, "6th - Literature Study", "Study classic and modern literature", 25)
    g6_writing_id = add_topic(ela_id, "6th - Creative Writing", "Write stories, poems, and scripts", 26)
    g6_grammar_id = add_topic(ela_id, "6th - Style & Voice", "Develop your writing style", 27)
    g6_vocab_id = add_topic(ela_id, "6th - Etymology", "Learn word origins and roots", 28)
    
    # GRADE 7 TOPICS
    g7_reading_id = add_topic(ela_id, "7th - Advanced Literature", "Analyze complex texts and themes", 29)
    g7_writing_id = add_topic(ela_id, "7th - Argumentative Writing", "Write convincing arguments", 30)
    g7_grammar_id = add_topic(ela_id, "7th - Rhetorical Devices", "Use literary techniques", 31)
    g7_vocab_id = add_topic(ela_id, "7th - SAT Vocabulary", "Prepare for standardized tests", 32)
    
    # GRADE 8 TOPICS
    g8_reading_id = add_topic(ela_id, "8th - College Prep Reading", "Prepare for high school reading", 33)
    g8_writing_id = add_topic(ela_id, "8th - Research Papers", "Write formal research papers", 34)
    g8_grammar_id = add_topic(ela_id, "8th - Advanced Style", "Master sophisticated writing", 35)
    g8_vocab_id = add_topic(ela_id, "8th - Academic Language", "Master academic vocabulary", 36)
    
    # SPECIALIZED TOPICS
    poetry_id = add_topic(ela_id, "Poetry & Creative Writing", "Write and analyze poetry", 37)
    drama_id = add_topic(ela_id, "Drama & Performance", "Act, direct, and write plays", 38)
    media_id = add_topic(ela_id, "Media Literacy", "Analyze news, ads, and digital content", 39)
    public_speaking_id = add_topic(ela_id, "Public Speaking", "Present with confidence", 40)
    debate_id = add_topic(ela_id, "Debate & Discussion", "Argue persuasively and respectfully", 41)
    journalism_id = add_topic(ela_id, "Journalism & News Writing", "Write news articles and reports", 42)
    technical_writing_id = add_topic(ela_id, "Technical Writing", "Write instructions and manuals", 43)
    business_writing_id = add_topic(ela_id, "Business Writing", "Write emails, letters, and proposals", 44)
    
    # KINDERGARTEN LESSONS
    seed_kindergarten_lessons(k_phonics_id, k_reading_id, k_writing_id, k_speaking_id)
    
    # GRADE 1 LESSONS
    seed_grade1_lessons(g1_phonics_id, g1_reading_id, g1_writing_id, g1_grammar_id)
    
    # GRADE 2 LESSONS
    seed_grade2_lessons(g2_phonics_id, g2_reading_id, g2_writing_id, g2_grammar_id)
    
    # GRADE 3 LESSONS
    seed_grade3_lessons(g3_reading_id, g3_writing_id, g3_grammar_id, g3_vocab_id)
    
    # GRADE 4 LESSONS
    seed_grade4_lessons(g4_reading_id, g4_writing_id, g4_grammar_id, g4_vocab_id)
    
    # GRADE 5 LESSONS
    seed_grade5_lessons(g5_reading_id, g5_writing_id, g5_grammar_id, g5_vocab_id)
    
    # GRADE 6 LESSONS
    seed_grade6_lessons(g6_reading_id, g6_writing_id, g6_grammar_id, g6_vocab_id)
    
    # GRADE 7 LESSONS
    seed_grade7_lessons(g7_reading_id, g7_writing_id, g7_grammar_id, g7_vocab_id)
    
    # GRADE 8 LESSONS
    seed_grade8_lessons(g8_reading_id, g8_writing_id, g8_grammar_id, g8_vocab_id)
    
    # SPECIALIZED LESSONS
    seed_specialized_lessons(poetry_id, drama_id, media_id, public_speaking_id, 
                           debate_id, journalism_id, technical_writing_id, business_writing_id)
    
    print("MASSIVE ELA curriculum seeded successfully!")

def seed_kindergarten_lessons(phonics_id, reading_id, writing_id, speaking_id):
    """Seed Kindergarten lessons."""
    
    # Phonics lessons
    lesson_id = add_lesson(phonics_id, "Letter A - Sound and Recognition", "Learn the letter A and its sound",
                          ["A is the first letter of the alphabet",
                           "A makes the 'a' sound like in 'apple'",
                           "A can be uppercase A or lowercase a",
                           "Practice writing A: big line down, little line across",
                           "Find A in words: apple, ant, alligator"],
                          [{"title": "Examples", "content": "A words: apple, ant, alligator, airplane, art"}],
                          "builtin", None, 1)
    add_practice_problem(lesson_id, "What sound does the letter A make?", "a",
                        ["Think of the word 'apple'", "What sound do you hear at the beginning?", "A makes the 'a' sound"],
                        ["Say 'apple' out loud"], "easy", 1)
    
    lesson_id = add_lesson(phonics_id, "Letter B - Sound and Recognition", "Learn the letter B and its sound",
                          ["B makes the 'b' sound like in 'ball'",
                           "B can be uppercase B or lowercase b",
                           "Practice writing B: big line down, two bumps",
                           "Find B in words: ball, bear, book"],
                          [{"title": "Examples", "content": "B words: ball, bear, book, baby, blue"}],
                          "builtin", None, 1)
    
    lesson_id = add_lesson(phonics_id, "Letter C - Sound and Recognition", "Learn the letter C and its sound",
                          ["C makes the 'c' sound like in 'cat'",
                           "C can be uppercase C or lowercase c",
                           "Practice writing C: curve around like a moon",
                           "Find C in words: cat, car, cake"],
                          [{"title": "Examples", "content": "C words: cat, car, cake, cow, cup"}],
                          "builtin", None, 1)
    
    # Reading lessons
    lesson_id = add_lesson(reading_id, "Sight Words - I, Can, See", "Learn your first sight words",
                          ["Sight words are words you know by sight",
                           "I - means yourself",
                           "Can - means able to do something",
                           "See - means to look at something",
                           "Practice reading: I can see"],
                          [{"title": "Example", "content": "I can see the cat. I can see the dog."}],
                          "builtin", None, 1)
    
    lesson_id = add_lesson(reading_id, "Sight Words - The, A, An", "Learn more important sight words",
                          ["The - points to something specific",
                           "A - points to one thing (before consonant sounds)",
                           "An - points to one thing (before vowel sounds)",
                           "Practice reading: The cat. A dog. An apple"],
                          [{"title": "Examples", "content": "The book. A car. An elephant."}],
                          "builtin", None, 1)
    
    # Writing lessons
    lesson_id = add_lesson(writing_id, "Writing Your Name", "Learn to write your own name",
                          ["Your name is special and unique",
                           "Start with a capital letter",
                           "Use lowercase letters for the rest",
                           "Practice writing your name many times",
                           "Make sure all letters are clear and neat"],
                          [{"title": "Example", "content": "If your name is Sarah, write: Sarah"}],
                          "builtin", None, 1)
    
    # Speaking lessons
    lesson_id = add_lesson(speaking_id, "Speaking Clearly", "Learn to speak so others can understand",
                          ["Speak slowly and clearly",
                           "Look at the person you're talking to",
                           "Use your inside voice in the classroom",
                           "Take turns when talking in a group",
                           "Listen when others are speaking"],
                          [{"title": "Example", "content": "When sharing news, say: 'I want to tell you about...'"}],
                          "builtin", None, 1)

def seed_grade1_lessons(phonics_id, reading_id, writing_id, grammar_id):
    """Seed Grade 1 lessons."""
    
    # Phonics lessons
    lesson_id = add_lesson(phonics_id, "Short Vowel Sounds", "Master the five short vowel sounds",
                          ["Short 'a' sounds like in 'cat'",
                           "Short 'e' sounds like in 'bed'",
                           "Short 'i' sounds like in 'sit'",
                           "Short 'o' sounds like in 'hot'",
                           "Short 'u' sounds like in 'cup'",
                           "Practice reading CVC words (consonant-vowel-consonant)"],
                          [{"title": "Examples", "content": "cat, bed, sit, hot, cup - each has a short vowel sound"}],
                          "builtin", None, 1)
    
    lesson_id = add_lesson(phonics_id, "Consonant Blends", "Learn to blend consonant sounds",
                          ["Blends are two consonants that make two sounds",
                           "bl - like in 'black'",
                           "cl - like in 'clap'",
                           "fl - like in 'flag'",
                           "gl - like in 'glad'",
                           "pl - like in 'play'",
                           "sl - like in 'slide'"],
                          [{"title": "Examples", "content": "black, clap, flag, glad, play, slide"}],
                          "builtin", None, 1)
    
    # Reading lessons
    lesson_id = add_lesson(reading_id, "Reading with Expression", "Read smoothly and with feeling",
                          ["Reading with expression makes stories more interesting",
                           "Change your voice for different characters",
                           "Pause at periods and commas",
                           "Make your voice go up for questions",
                           "Show excitement with exclamation points"],
                          [{"title": "Example", "content": "'Hello!' said the happy cat. 'How are you?'"}],
                          "builtin", None, 1)
    
    # Writing lessons
    lesson_id = add_lesson(writing_id, "Writing Complete Sentences", "Learn to write clear, complete sentences",
                          ["A sentence expresses a complete thought",
                           "It has a subject (who or what)",
                           "It has a predicate (what they do)",
                           "Start with a capital letter",
                           "End with punctuation (. ! ?)"],
                          [{"title": "Example", "content": "The dog runs. (Subject: dog, Predicate: runs)"}],
                          "builtin", None, 1)
    
    # Grammar lessons
    lesson_id = add_lesson(grammar_id, "Nouns", "Identify and use nouns",
                          ["A noun is a person, place, thing, or idea",
                           "Person: teacher, boy, Sarah",
                           "Place: school, park, Chicago",
                           "Thing: book, car, apple",
                           "Idea: love, freedom, happiness"],
                          [{"title": "Example", "content": "In 'The cat sat on the mat,' the nouns are: cat, mat"}],
                          "builtin", None, 1)

def seed_grade2_lessons(phonics_id, reading_id, writing_id, grammar_id):
    """Seed Grade 2 lessons."""
    
    # Phonics lessons
    lesson_id = add_lesson(phonics_id, "Digraphs - sh, ch, th, wh", "Learn consonant digraphs",
                          ["Digraphs are two letters that make one sound",
                           "sh - like in 'ship'",
                           "ch - like in 'chair'",
                           "th - like in 'think'",
                           "wh - like in 'what'",
                           "Practice reading words with digraphs"],
                          [{"title": "Examples", "content": "ship, chair, think, what, fish, much, bath, when"}],
                          "builtin", None, 1)
    
    lesson_id = add_lesson(phonics_id, "Long Vowel Sounds", "Learn when vowels say their name",
                          ["Long vowels say their name: a, e, i, o, u",
                           "Magic e makes the vowel say its name: cake, bike, home",
                           "Two vowels together: rain, feet, boat",
                           "Practice reading long vowel words"],
                          [{"title": "Examples", "content": "cake, bike, home, rain, feet, boat"}],
                          "builtin", None, 1)
    
    # Reading lessons
    lesson_id = add_lesson(reading_id, "Finding the Main Idea", "Understand what stories are about",
                          ["The main idea is what the story is mostly about",
                           "Ask: What is the author mostly telling me?",
                           "Look for repeated words or themes",
                           "The main idea is usually a sentence, not just one word",
                           "Details support the main idea"],
                          [{"title": "Example", "content": "Story about dogs being good pets. Main idea: Dogs make wonderful pets for families."}],
                          "builtin", None, 1)
    
    # Writing lessons
    lesson_id = add_lesson(writing_id, "Writing a Paragraph", "Learn to organize your ideas",
                          ["A paragraph has a main idea",
                           "Start with a topic sentence",
                           "Add supporting details",
                           "End with a closing sentence",
                           "All sentences should be about the same topic"],
                          [{"title": "Example", "content": "Topic: My Pet. Topic sentence: I have a wonderful dog named Max. Details: He is brown, he likes to play, he is very friendly. Closing: Max is the best pet ever."}],
                          "builtin", None, 1)
    
    # Grammar lessons
    lesson_id = add_lesson(grammar_id, "Verbs", "Identify and use action words",
                          ["A verb is an action word",
                           "Verbs tell what someone or something does",
                           "Examples: run, jump, eat, sleep, read",
                           "Verbs can be in the past, present, or future",
                           "Practice finding verbs in sentences"],
                          [{"title": "Example", "content": "In 'The cat runs fast,' the verb is 'runs'"}],
                          "builtin", None, 1)

def seed_grade3_lessons(reading_id, writing_id, grammar_id, vocab_id):
    """Seed Grade 3 lessons."""
    
    # Reading lessons
    lesson_id = add_lesson(reading_id, "Character Analysis", "Understand characters in stories",
                          ["Characters are the people or animals in stories",
                           "Think about what characters look like",
                           "Think about what characters do and say",
                           "Think about how characters feel",
                           "Characters can change throughout the story"],
                          [{"title": "Example", "content": "In 'The Three Little Pigs,' the wolf is mean and tricky, but the pigs are smart and hardworking."}],
                          "builtin", None, 1)
    
    lesson_id = add_lesson(reading_id, "Plot Structure", "Understand how stories are organized",
                          ["Every story has a beginning, middle, and end",
                           "Beginning: introduces characters and setting",
                           "Middle: the problem or conflict happens",
                           "End: the problem is solved",
                           "Look for these parts in every story"],
                          [{"title": "Example", "content": "Beginning: Three pigs build houses. Middle: Wolf tries to blow them down. End: Pigs are safe in brick house."}],
                          "builtin", None, 1)
    
    # Writing lessons
    lesson_id = add_lesson(writing_id, "Writing a Story", "Create your own narrative",
                          ["Stories have characters, setting, and plot",
                           "Start with an interesting beginning",
                           "Include a problem or conflict",
                           "Show how the problem is solved",
                           "End with a satisfying conclusion"],
                          [{"title": "Example", "content": "Once upon a time, a brave knight went on a quest to save the princess from a dragon."}],
                          "builtin", None, 1)
    
    # Grammar lessons
    lesson_id = add_lesson(grammar_id, "Adjectives", "Describe nouns with adjectives",
                          ["Adjectives describe or tell about nouns",
                           "They tell what kind, how many, or which one",
                           "Examples: big, red, three, happy, fast",
                           "Adjectives make your writing more interesting",
                           "Practice using adjectives in your sentences"],
                          [{"title": "Example", "content": "The big, red car drove fast down the street."}],
                          "builtin", None, 1)
    
    # Vocabulary lessons
    lesson_id = add_lesson(vocab_id, "Context Clues", "Use context to figure out new words",
                          ["When you see an unfamiliar word, don't panic!",
                           "Look at the words around it (context)",
                           "Ask: What would make sense here?",
                           "Look for definitions, examples, or synonyms nearby",
                           "Try substituting a word you know"],
                          [{"title": "Example", "content": "'The enormous elephant was huge.' Context tells us enormous means very big."}],
                          "builtin", None, 1)

def seed_grade4_lessons(reading_id, writing_id, grammar_id, vocab_id):
    """Seed Grade 4 lessons."""
    
    # Reading lessons
    lesson_id = add_lesson(reading_id, "Theme and Message", "Find the deeper meaning in stories",
                          ["Theme is the main message or lesson of a story",
                           "Ask: What does the author want me to learn?",
                           "Themes are often about friendship, courage, or kindness",
                           "Look for clues in what characters do and say",
                           "Themes are not usually stated directly"],
                          [{"title": "Example", "content": "In 'The Tortoise and the Hare,' the theme is that slow and steady wins the race."}],
                          "builtin", None, 1)
    
    lesson_id = add_lesson(reading_id, "Making Predictions", "Guess what will happen next",
                          ["Predictions are educated guesses about what will happen",
                           "Use clues from the story",
                           "Think about what you already know",
                           "Make predictions as you read",
                           "Check if your predictions were correct"],
                          [{"title": "Example", "content": "If a character is walking toward a dark forest, you might predict something scary will happen."}],
                          "builtin", None, 1)
    
    # Writing lessons
    lesson_id = add_lesson(writing_id, "Persuasive Writing", "Convince others with your words",
                          ["Persuasive writing tries to convince someone to agree with you",
                           "Start with your opinion or claim",
                           "Give reasons to support your opinion",
                           "Use facts and examples as evidence",
                           "End with a strong conclusion"],
                          [{"title": "Example", "content": "I think students should have longer recess because it helps them focus better in class."}],
                          "builtin", None, 1)
    
    # Grammar lessons
    lesson_id = add_lesson(grammar_id, "Complex Sentences", "Combine ideas with conjunctions",
                          ["Complex sentences have two parts joined by a conjunction",
                           "Use words like because, since, when, if, although",
                           "One part can stand alone, the other cannot",
                           "Complex sentences make your writing more interesting",
                           "Practice combining simple sentences"],
                          [{"title": "Example", "content": "I went to the store because I needed milk."}],
                          "builtin", None, 1)
    
    # Vocabulary lessons
    lesson_id = add_lesson(vocab_id, "Word Families", "Learn related words",
                          ["Word families are groups of words with the same root",
                           "Example: happy, happiness, happily, unhappiness",
                           "Learning word families helps you understand new words",
                           "Look for common prefixes and suffixes",
                           "Practice using different forms of words"],
                          [{"title": "Example", "content": "Friend: friendly, friendship, unfriendly, befriend"}],
                          "builtin", None, 1)

def seed_grade5_lessons(reading_id, writing_id, grammar_id, vocab_id):
    """Seed Grade 5 lessons."""
    
    # Reading lessons
    lesson_id = add_lesson(reading_id, "Making Inferences", "Read between the lines",
                          ["Inferences are conclusions you draw from clues in the text",
                           "Look for clues in what characters say and do",
                           "Think about what you already know",
                           "Combine clues with your knowledge to make inferences",
                           "Ask: What does this really mean?"],
                          [{"title": "Example", "content": "If a character is crying and holding a broken toy, you can infer they are sad about the toy."}],
                          "builtin", None, 1)
    
    lesson_id = add_lesson(reading_id, "Author's Purpose", "Understand why authors write",
                          ["Authors write for different reasons",
                           "To inform: give facts and information",
                           "To persuade: convince you to think or act a certain way",
                           "To entertain: tell an interesting story",
                           "To express: share feelings or opinions"],
                          [{"title": "Example", "content": "A news article informs, an advertisement persuades, a novel entertains."}],
                          "builtin", None, 1)
    
    # Writing lessons
    lesson_id = add_lesson(writing_id, "Research and Note-Taking", "Gather information for writing",
                          ["Research means finding information about a topic",
                           "Use books, websites, and other sources",
                           "Take notes on important information",
                           "Write down where you found each fact",
                           "Organize your notes before writing"],
                          [{"title": "Example", "content": "Topic: Dolphins. Notes: Dolphins are mammals, they live in oceans, they are very intelligent."}],
                          "builtin", None, 1)
    
    # Grammar lessons
    lesson_id = add_lesson(grammar_id, "Subject and Predicate", "Understand sentence parts",
                          ["Every sentence has a subject and predicate",
                           "Subject: who or what the sentence is about",
                           "Predicate: what the subject does or is",
                           "Simple subject: the main noun or pronoun",
                           "Simple predicate: the main verb"],
                          [{"title": "Example", "content": "The big dog runs fast. Subject: dog, Predicate: runs"}],
                          "builtin", None, 1)
    
    # Vocabulary lessons
    lesson_id = add_lesson(vocab_id, "Multiple Meaning Words", "Words that have different meanings",
                          ["Some words have more than one meaning",
                           "Use context to figure out which meaning is correct",
                           "Example: 'bat' can mean an animal or a sports equipment",
                           "Practice using words in different contexts",
                           "Look up words in the dictionary to see all meanings"],
                          [{"title": "Example", "content": "The bat flew overhead. (animal) vs. The player swung the bat. (sports equipment)"}],
                          "builtin", None, 1)

def seed_grade6_lessons(reading_id, writing_id, grammar_id, vocab_id):
    """Seed Grade 6 lessons."""
    
    # Reading lessons
    lesson_id = add_lesson(reading_id, "Literary Devices", "Recognize techniques authors use",
                          ["Authors use special techniques to make their writing interesting",
                           "Simile: compares two things using 'like' or 'as'",
                           "Metaphor: compares two things without 'like' or 'as'",
                           "Personification: gives human qualities to non-human things",
                           "Alliteration: words that start with the same sound"],
                          [{"title": "Examples", "content": "Simile: 'as brave as a lion.' Metaphor: 'the classroom was a zoo.' Personification: 'the wind whispered.'"}],
                          "builtin", None, 1)
    
    lesson_id = add_lesson(reading_id, "Point of View", "Understand who is telling the story",
                          ["Point of view is who is telling the story",
                           "First person: 'I' or 'we' - the narrator is in the story",
                           "Second person: 'you' - talking directly to the reader",
                           "Third person: 'he,' 'she,' 'they' - narrator is outside the story",
                           "Point of view affects how you understand the story"],
                          [{"title": "Example", "content": "First person: 'I walked to school.' Third person: 'She walked to school.'"}],
                          "builtin", None, 1)
    
    # Writing lessons
    lesson_id = add_lesson(writing_id, "Poetry Writing", "Express yourself through poetry",
                          ["Poetry uses words in special ways to create feelings",
                           "Poems can rhyme or not rhyme",
                           "Use descriptive words to create pictures",
                           "Poems can be short or long",
                           "Express your feelings and ideas"],
                          [{"title": "Example", "content": "The sun shines bright / Like a golden light / Making everything / Feel just right"}],
                          "builtin", None, 1)
    
    # Grammar lessons
    lesson_id = add_lesson(grammar_id, "Active and Passive Voice", "Understand how sentences work",
                          ["Active voice: the subject does the action",
                           "Passive voice: the subject receives the action",
                           "Active voice is usually clearer and more direct",
                           "Passive voice is sometimes necessary or preferred",
                           "Practice changing between active and passive voice"],
                          [{"title": "Example", "content": "Active: 'The dog chased the cat.' Passive: 'The cat was chased by the dog.'"}],
                          "builtin", None, 1)
    
    # Vocabulary lessons
    lesson_id = add_lesson(vocab_id, "Greek and Latin Roots", "Learn word origins",
                          ["Many English words come from Greek and Latin",
                           "Learning roots helps you understand new words",
                           "Example: 'bio' means life (biology, biography)",
                           "Example: 'graph' means write (photograph, autograph)",
                           "Practice identifying roots in words"],
                          [{"title": "Example", "content": "Telephone: 'tele' (far) + 'phone' (sound) = sound from far away"}],
                          "builtin", None, 1)

def seed_grade7_lessons(reading_id, writing_id, grammar_id, vocab_id):
    """Seed Grade 7 lessons."""
    
    # Reading lessons
    lesson_id = add_lesson(reading_id, "Symbolism in Literature", "Find hidden meanings in stories",
                          ["Symbols are objects or ideas that represent something else",
                           "A dove might symbolize peace",
                           "A storm might symbolize trouble",
                           "Look for objects that appear repeatedly",
                           "Think about what these objects might mean"],
                          [{"title": "Example", "content": "In a story, a character always carries a key. The key might symbolize freedom or opportunity."}],
                          "builtin", None, 1)
    
    lesson_id = add_lesson(reading_id, "Irony and Sarcasm", "Understand when words mean the opposite",
                          ["Irony is when something happens that's the opposite of what you expect",
                           "Verbal irony: saying the opposite of what you mean",
                           "Situational irony: when the opposite of what you expect happens",
                           "Dramatic irony: when the audience knows something the characters don't",
                           "Sarcasm is a type of verbal irony that's meant to be hurtful"],
                          [{"title": "Example", "content": "It's ironic when a fire station burns down. It's sarcastic to say 'Great job!' when someone makes a mistake."}],
                          "builtin", None, 1)
    
    # Writing lessons
    lesson_id = add_lesson(writing_id, "Building Strong Arguments", "Make convincing arguments",
                          ["Arguments try to persuade others to agree with you",
                           "Start with a clear claim or position",
                           "Provide evidence to support your claim",
                           "Address counterarguments (opposing views)",
                           "Use logical reasoning and facts"],
                          [{"title": "Example", "content": "Claim: School should start later. Evidence: Students need more sleep. Counterargument: Later start means later dismissal."}],
                          "builtin", None, 1)
    
    # Grammar lessons
    lesson_id = add_lesson(grammar_id, "Misplaced and Dangling Modifiers", "Fix confusing sentences",
                          ["Modifiers are words that describe other words",
                           "Misplaced modifiers are in the wrong place",
                           "Dangling modifiers don't clearly describe anything",
                           "Place modifiers close to what they describe",
                           "Make sure modifiers clearly refer to something"],
                          [{"title": "Example", "content": "Misplaced: 'I saw a dog walking to school.' (Who was walking?) Fixed: 'Walking to school, I saw a dog.'"}],
                          "builtin", None, 1)
    
    # Vocabulary lessons
    lesson_id = add_lesson(vocab_id, "SAT Vocabulary Prep", "Learn words for standardized tests",
                          ["SAT vocabulary includes academic and sophisticated words",
                           "Learn words in context, not just definitions",
                           "Practice using new words in sentences",
                           "Look for word parts and roots",
                           "Use flashcards and practice tests"],
                          [{"title": "Example", "content": "Ubiquitous means everywhere. 'Smartphones are ubiquitous in modern society.'"}],
                          "builtin", None, 1)

def seed_grade8_lessons(reading_id, writing_id, grammar_id, vocab_id):
    """Seed Grade 8 lessons."""
    
    # Reading lessons
    lesson_id = add_lesson(reading_id, "Analyzing Complex Texts", "Understand difficult reading material",
                          ["Complex texts have many layers of meaning",
                           "Read slowly and carefully",
                           "Look up unfamiliar words",
                           "Think about the author's purpose",
                           "Consider different interpretations"],
                          [{"title": "Example", "content": "When reading a difficult passage, break it into smaller parts and understand each part before moving on."}],
                          "builtin", None, 1)
    
    lesson_id = add_lesson(reading_id, "Critical Reading Skills", "Think deeply about what you read",
                          ["Critical reading means thinking carefully about the text",
                           "Ask questions about the author's claims",
                           "Look for evidence and reasoning",
                           "Consider different perspectives",
                           "Evaluate the quality of the argument"],
                          [{"title": "Example", "content": "When reading an article, ask: What evidence supports this claim? Are there other viewpoints?"}],
                          "builtin", None, 1)
    
    # Writing lessons
    lesson_id = add_lesson(writing_id, "Formal Research Papers", "Write academic papers",
                          ["Research papers present information in a formal way",
                           "Start with a thesis statement",
                           "Use multiple reliable sources",
                           "Cite your sources properly",
                           "Write in a formal, academic style"],
                          [{"title": "Example", "content": "Thesis: Climate change is affecting polar bear populations. Support with facts from scientific studies."}],
                          "builtin", None, 1)
    
    # Grammar lessons
    lesson_id = add_lesson(grammar_id, "Parallel Structure", "Make your writing flow smoothly",
                          ["Parallel structure means using the same grammatical form",
                           "Lists should have items in the same form",
                           "Comparisons should be balanced",
                           "Parallel structure makes writing clearer",
                           "Practice identifying and fixing parallel structure errors"],
                          [{"title": "Example", "content": "Not parallel: 'I like reading, to write, and swimming.' Parallel: 'I like reading, writing, and swimming.'"}],
                          "builtin", None, 1)
    
    # Vocabulary lessons
    lesson_id = add_lesson(vocab_id, "Academic Language", "Master formal vocabulary",
                          ["Academic language is formal and precise",
                           "Use specific, technical terms when appropriate",
                           "Avoid slang and casual expressions",
                           "Choose words that convey exact meaning",
                           "Practice using academic vocabulary in writing"],
                          [{"title": "Example", "content": "Instead of 'big,' use 'substantial' or 'considerable' in academic writing."}],
                          "builtin", None, 1)

def seed_specialized_lessons(poetry_id, drama_id, media_id, public_speaking_id, 
                           debate_id, journalism_id, technical_writing_id, business_writing_id):
    """Seed specialized ELA lessons."""
    
    # Poetry lessons
    lesson_id = add_lesson(poetry_id, "Types of Poetry", "Explore different poetry forms",
                          ["Haiku: 3 lines, 5-7-5 syllables",
                           "Limerick: 5 lines, funny and rhyming",
                           "Free verse: no rules, just expression",
                           "Sonnet: 14 lines with specific rhyme scheme",
                           "Try writing different types of poetry"],
                          [{"title": "Example", "content": "Haiku: 'Green grass grows tall / In the warm summer sun / Nature's beauty shines'"}],
                          "builtin", None, 1)
    
    # Drama lessons
    lesson_id = add_lesson(drama_id, "Elements of Drama", "Understand how plays work",
                          ["Drama is a story performed by actors",
                           "Script: the written words of the play",
                           "Characters: the people in the play",
                           "Setting: where and when the play takes place",
                           "Dialogue: what characters say to each other"],
                          [{"title": "Example", "content": "In a play, characters speak their lines and move around the stage to tell the story."}],
                          "builtin", None, 1)
    
    # Media literacy lessons
    lesson_id = add_lesson(media_id, "Analyzing Advertisements", "Think critically about ads",
                          ["Advertisements try to persuade you to buy something",
                           "Look for emotional appeals",
                           "Check if claims are supported by evidence",
                           "Consider who created the ad and why",
                           "Ask: What is this ad really trying to sell?"],
                          [{"title": "Example", "content": "A toy commercial might show kids having fun, but it's really trying to sell the toy to parents."}],
                          "builtin", None, 1)
    
    # Public speaking lessons
    lesson_id = add_lesson(public_speaking_id, "Overcoming Stage Fright", "Speak confidently in front of others",
                          ["Everyone feels nervous before speaking",
                           "Practice your speech many times",
                           "Make eye contact with your audience",
                           "Speak slowly and clearly",
                           "Remember: your audience wants you to succeed"],
                          [{"title": "Example", "content": "Before giving a speech, take deep breaths and remind yourself that you know your topic well."}],
                          "builtin", None, 1)
    
    # Debate lessons
    lesson_id = add_lesson(debate_id, "Respectful Argumentation", "Argue without being mean",
                          ["Debate means discussing different sides of an issue",
                           "Listen carefully to other people's views",
                           "Use facts and evidence to support your points",
                           "Stay calm and respectful",
                           "Be willing to change your mind if you learn something new"],
                          [{"title": "Example", "content": "Instead of saying 'You're wrong,' say 'I see it differently because...'"}],
                          "builtin", None, 1)
    
    # Journalism lessons
    lesson_id = add_lesson(journalism_id, "The 5 W's of News", "Write clear news articles",
                          ["News articles answer five important questions",
                           "Who: Who is involved?",
                           "What: What happened?",
                           "When: When did it happen?",
                           "Where: Where did it happen?",
                           "Why: Why did it happen?"],
                          [{"title": "Example", "content": "Who: Local students. What: Won science fair. When: Last Saturday. Where: Community center. Why: Great project."}],
                          "builtin", None, 1)
    
    # Technical writing lessons
    lesson_id = add_lesson(technical_writing_id, "Writing Clear Instructions", "Help others follow directions",
                          ["Instructions tell people how to do something step by step",
                           "Use simple, clear language",
                           "Number the steps in order",
                           "Include all necessary information",
                           "Test your instructions to make sure they work"],
                          [{"title": "Example", "content": "How to make a sandwich: 1. Get two slices of bread. 2. Spread peanut butter on one slice. 3. Add jelly. 4. Put slices together."}],
                          "builtin", None, 1)
    
    # Business writing lessons
    lesson_id = add_lesson(business_writing_id, "Professional Emails", "Write effective business emails",
                          ["Business emails should be clear and professional",
                           "Use a clear subject line",
                           "Start with a greeting",
                           "Get to the point quickly",
                           "End with a polite closing"],
                          [{"title": "Example", "content": "Subject: Meeting Request. Dear Mr. Smith, I would like to schedule a meeting to discuss the project. Best regards, [Your name]"}],
                          "builtin", None, 1)

if __name__ == "__main__":
    seed_massive_ela_curriculum()
