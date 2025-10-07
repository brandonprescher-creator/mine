"""
GENERATE PRACTICE PROBLEMS FOR ALL LESSONS
Ensure every lesson has 5-10 practice problems
"""

from database import get_connection, add_practice_problem
import random


def generate_practice_for_all_lessons():
    """Generate practice problems for every lesson that doesn't have enough"""
    conn = get_connection()
    cursor = conn.cursor()
    
    # Get all lessons
    cursor.execute("SELECT id, title, description FROM lessons")
    lessons = cursor.fetchall()
    
    print(f"Found {len(lessons)} total lessons")
    print("Generating practice problems...\n")
    
    problems_added = 0
    
    for lesson in lessons:
        lesson_id = lesson["id"]
        lesson_title = lesson["title"]
        
        # Check how many practice problems this lesson already has
        cursor.execute(
            "SELECT COUNT(*) as count FROM practice_problems WHERE lesson_id = ?",
            (lesson_id,)
        )
        current_count = cursor.fetchone()["count"]
        
        # Generate problems if less than 5
        if current_count < 5:
            needed = 5 - current_count
            
            for i in range(needed):
                # Generate contextual practice problems based on lesson title
                problem = generate_contextual_problem(lesson_title, i + current_count + 1)
                
                add_practice_problem(
                    lesson_id=lesson_id,
                    question=problem["question"],
                    answer=problem["answer"],
                    steps=problem["explanation"],  # Changed from 'explanation' to 'steps'
                    hints=problem["hints"],
                    difficulty="Medium",
                    display_order=current_count + i + 1
                )
                
                problems_added += 1
            
            print(f"Added {needed} problems to: {lesson_title}")
    
    conn.close()
    
    print(f"\nSUCCESS! Added {problems_added} practice problems!")
    print(f"All lessons now have at least 5 practice problems!")


def generate_contextual_problem(lesson_title, problem_number):
    """Generate a contextual practice problem based on lesson title"""
    
    # Math problems
    if any(word in lesson_title.lower() for word in ["addition", "add", "sum", "plus"]):
        a, b = random.randint(1, 50), random.randint(1, 50)
        return {
            "question": f"What is {a} + {b}?",
            "answer": str(a + b),
            "explanation": [
                f"Start with {a}",
                f"Add {b} more",
                f"Count up to get {a + b}",
                f"Answer: {a + b}"
            ],
            "hints": [
                f"Try counting on your fingers",
                f"Break it into smaller parts: {a} + {b//2} + {b - b//2}"
            ]
        }
    
    elif any(word in lesson_title.lower() for word in ["subtraction", "subtract", "minus", "difference"]):
        a = random.randint(20, 100)
        b = random.randint(1, a)
        return {
            "question": f"What is {a} - {b}?",
            "answer": str(a - b),
            "explanation": [
                f"Start with {a}",
                f"Take away {b}",
                f"Count down to get {a - b}",
                f"Answer: {a - b}"
            ],
            "hints": [
                "Count backward",
                f"Think: {a} minus {b} equals what?"
            ]
        }
    
    elif any(word in lesson_title.lower() for word in ["multiplication", "multiply", "times", "product"]):
        a, b = random.randint(2, 12), random.randint(2, 12)
        return {
            "question": f"What is {a} × {b}?",
            "answer": str(a * b),
            "explanation": [
                f"{a} groups of {b}",
                f"Or {b} groups of {a}",
                f"Add {a} repeatedly {b} times: " + " + ".join([str(a)] * min(b, 5)),
                f"Answer: {a * b}"
            ],
            "hints": [
                f"Use skip counting: count by {a}s, {b} times",
                f"Or use your times tables!"
            ]
        }
    
    elif any(word in lesson_title.lower() for word in ["division", "divide", "quotient", "shared"]):
        b = random.randint(2, 12)
        quotient = random.randint(2, 12)
        a = b * quotient
        return {
            "question": f"What is {a} ÷ {b}?",
            "answer": str(quotient),
            "explanation": [
                f"How many {b}s fit into {a}?",
                f"Or: {a} split into {b} equal groups",
                f"Think: {b} × ? = {a}",
                f"Answer: {quotient} (because {b} × {quotient} = {a})"
            ],
            "hints": [
                f"What times {b} equals {a}?",
                "Use your multiplication tables backward!"
            ]
        }
    
    elif any(word in lesson_title.lower() for word in ["fraction", "half", "third", "quarter"]):
        return {
            "question": "What is 1/2 + 1/4?",
            "answer": "3/4",
            "explanation": [
                "Find common denominator: 4",
                "Convert 1/2 to 2/4",
                "Now add: 2/4 + 1/4 = 3/4",
                "Answer: 3/4"
            ],
            "hints": [
                "Convert 1/2 to fourths first",
                "2/4 + 1/4 = ?"
            ]
        }
    
    # Reading/ELA problems
    elif any(word in lesson_title.lower() for word in ["letter", "alphabet", "sound", "phonics"]):
        letters = ["A", "B", "C", "D", "E"]
        sounds = ["a (apple)", "b (ball)", "c (cat)", "d (dog)", "e (egg)"]
        idx = random.randint(0, 4)
        return {
            "question": f"What sound does the letter {letters[idx]} make?",
            "answer": sounds[idx].split()[0],
            "explanation": [
                f"The letter {letters[idx]} makes the '{sounds[idx].split()[0]}' sound",
                f"Like in the word {sounds[idx].split()[1].strip('()')}",
                "Say it out loud a few times!"
            ],
            "hints": [
                f"Think of the word {sounds[idx].split()[1].strip('()')}",
                "Say the word slowly"
            ]
        }
    
    elif any(word in lesson_title.lower() for word in ["reading", "comprehension", "story"]):
        return {
            "question": "What is the main idea of a story?",
            "answer": "What the story is mostly about",
            "explanation": [
                "The main idea is the most important point",
                "It's what the whole story is about",
                "Details support the main idea",
                "Ask: What is this story mostly teaching me?"
            ],
            "hints": [
                "What is the story mostly about?",
                "Look at the title for clues"
            ]
        }
    
    # Science problems
    elif any(word in lesson_title.lower() for word in ["science", "biology", "chemistry", "physics"]):
        return {
            "question": "What is the scientific method's first step?",
            "answer": "Ask a question or make an observation",
            "explanation": [
                "Science starts with curiosity",
                "First: Ask a question or observe something interesting",
                "Then: Make a hypothesis (educated guess)",
                "Then: Test it with an experiment"
            ],
            "hints": [
                "What do scientists do first?",
                "It starts with being curious!"
            ]
        }
    
    # History/Social Studies
    elif any(word in lesson_title.lower() for word in ["history", "pioneer", "ancient", "geography"]):
        return {
            "question": "Why do we study history?",
            "answer": "To learn from the past and understand the present",
            "explanation": [
                "History helps us learn from past mistakes",
                "It shows us how we got to where we are today",
                "Understanding the past helps us make better decisions",
                "History connects us to people who came before us"
            ],
            "hints": [
                "Think about why knowing the past matters",
                "How does history affect us today?"
            ]
        }
    
    # Generic practice problem for any other lesson
    else:
        return {
            "question": f"What is the most important thing you learned in this lesson about {lesson_title}?",
            "answer": "Review the key steps and main concepts from the lesson",
            "explanation": [
                "Think about what surprised you or seemed most important",
                "Review the step-by-step teaching points",
                "Identify what you'll remember tomorrow",
                "This is about reflection and understanding"
            ],
            "hints": [
                "Look back at the teaching steps",
                "What was the main point?"
            ]
        }


if __name__ == "__main__":
    print("="*70)
    print("GENERATING PRACTICE PROBLEMS FOR ALL LESSONS")
    print("="*70 + "\n")
    
    generate_practice_for_all_lessons()
    
    print("\n" + "="*70)
    print("COMPLETE! Every lesson now has practice problems!")
    print("="*70)

