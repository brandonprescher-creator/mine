"""
INTEREST-BASED LESSON THEMING
Dynamically personalize lesson content based on student interests
"""

import random
from typing import Dict, List


class InterestThemer:
    """Theme lessons based on student interests"""
    
    def __init__(self):
        self.interest_themes = {
            "horses": {
                "math_contexts": [
                    "A horse stable has {a} horses. {b} more arrive. How many total?",
                    "A horse eats {a} pounds of hay per day. How much in {b} days?",
                    "A rider practices {a} hours per week. How many hours in {b} weeks?",
                    "A horse runs at {a} mph. How far in {b} hours?",
                ],
                "science_examples": [
                    "Horses are herbivores - they only eat plants",
                    "A horse's heart weighs about 10 pounds!",
                    "Horses can sleep standing up using a special leg mechanism",
                ],
                "reading_prompts": [
                    "Write about a magical horse adventure",
                    "Describe your dream horse stable",
                    "Research a famous racehorse",
                ]
            },
            "space": {
                "math_contexts": [
                    "A rocket travels {a} miles per second. How far in {b} seconds?",
                    "Mars is {a} million miles away. Earth is {b} million. Difference?",
                    "A space station orbits {a} times per day. How many in {b} days?",
                    "An astronaut weighs {a} lbs on Earth, but only {b} lbs on the Moon!",
                ],
                "science_examples": [
                    "In space, there's no air, so sound can't travel",
                    "The Sun is 93 million miles away - light takes 8 minutes to reach us!",
                    "Black holes have gravity so strong, even light can't escape",
                ],
                "reading_prompts": [
                    "Write about discovering a new planet",
                    "Describe what life would be like on Mars",
                    "Research the Apollo moon landings",
                ]
            },
            "art": {
                "math_contexts": [
                    "You mix {a} parts blue paint with {b} parts yellow. What color?",
                    "A canvas is {a} inches wide and {b} inches tall. What's the area?",
                    "You need {a} colors for your palette. You have {b}. How many more?",
                    "A painting takes {a} hours. You work {b} hours per day. How many days?",
                ],
                "science_examples": [
                    "Colors are different wavelengths of light!",
                    "Mixing all colors of light makes white, but mixing all paints makes brown",
                    "Your eye has 3 types of color sensors: red, green, and blue",
                ],
                "reading_prompts": [
                    "Describe a famous painting in detail",
                    "Write about creating your masterpiece",
                    "Research your favorite artist's life",
                ]
            },
            "coding": {
                "math_contexts": [
                    "A program runs {a} calculations per second for {b} seconds. How many total?",
                    "You have {a} lines of code. You write {b} more. Total lines?",
                    "A game has {a} levels. Each takes {b} minutes to code. Total time?",
                ],
                "science_examples": [
                    "Computers use binary (1s and 0s) for everything!",
                    "A modern processor can do billions of calculations per second",
                    "The first computer filled an entire room!",
                ],
                "reading_prompts": [
                    "Write instructions for making a sandwich (learn algorithms!)",
                    "Describe how your favorite app works",
                    "Research famous programmers",
                ]
            },
            "reading": {
                "math_contexts": [
                    "A book has {a} chapters. You read {b} per day. Days to finish?",
                    "You read {a} pages per hour. How many pages in {b} hours?",
                    "A library has {a} books. You've read {b}. How many left?",
                ],
                "science_examples": [
                    "Reading activates many parts of your brain at once",
                    "Speed reading techniques can triple your reading speed",
                    "Your brain creates mental images when you read",
                ],
                "reading_prompts": [
                    "Write a book review of your favorite book",
                    "Create an alternate ending to a story",
                    "Interview a character from your book",
                ]
            },
            "minecraft": {
                "math_contexts": [
                    "You need {a} blocks for a wall. Each is {b} units. Total length?",
                    "A Minecraft world is {a} by {a} blocks. What's the area?",
                    "You mine {a} diamonds per hour. How many in {b} hours?",
                ],
                "science_examples": [
                    "Redstone in Minecraft simulates electrical circuits!",
                    "Building in Minecraft teaches 3D spatial reasoning",
                    "The Minecraft world is made of cubes - a lesson in geometry",
                ],
                "reading_prompts": [
                    "Write about your greatest Minecraft creation",
                    "Describe a survival adventure in Minecraft",
                    "Create a guide for new Minecraft players",
                ]
            },
            "animals": {
                "math_contexts": [
                    "A zoo has {a} lions and {b} tigers. How many big cats total?",
                    "A bird flies {a} miles per hour. How far in {b} hours?",
                    "A puppy grows {a} pounds per month for {b} months. Total weight gain?",
                ],
                "science_examples": [
                    "Dolphins sleep with half their brain at a time!",
                    "Octopuses have 3 hearts and blue blood",
                    "Some animals can regenerate body parts (like starfish)",
                ],
                "reading_prompts": [
                    "Write about your favorite animal",
                    "Describe a day in the life of a wild animal",
                    "Research an endangered species",
                ]
            }
        }
    
    def theme_math_problem(self, base_problem: str, interests: List[str]) -> str:
        """Theme a math problem based on interests"""
        if not interests:
            return base_problem
        
        # Pick a random interest
        interest = random.choice(interests)
        
        if interest.lower() in self.interest_themes:
            theme = self.interest_themes[interest.lower()]
            if theme["math_contexts"]:
                context_template = random.choice(theme["math_contexts"])
                # Replace {a} and {b} with numbers from the original problem
                # This is a simplified version - in reality, you'd parse the original problem
                themed = context_template.format(a=random.randint(5, 20), b=random.randint(2, 10))
                return themed
        
        return base_problem
    
    def theme_science_example(self, base_example: str, interests: List[str]) -> str:
        """Theme a science example based on interests"""
        if not interests:
            return base_example
        
        interest = random.choice(interests)
        
        if interest.lower() in self.interest_themes:
            theme = self.interest_themes[interest.lower()]
            if theme["science_examples"]:
                return random.choice(theme["science_examples"])
        
        return base_example
    
    def get_themed_writing_prompt(self, interests: List[str]) -> str:
        """Get a writing prompt based on interests"""
        if not interests:
            return "Write about something that interests you"
        
        interest = random.choice(interests)
        
        if interest.lower() in self.interest_themes:
            theme = self.interest_themes[interest.lower()]
            if theme["reading_prompts"]:
                return random.choice(theme["reading_prompts"])
        
        return f"Write about {interest}"
    
    def get_interest_connection(self, lesson_title: str, interests: List[str]) -> str:
        """Find connections between a lesson and student interests"""
        connections = []
        
        for interest in interests:
            if interest.lower() == "horses":
                if "velocity" in lesson_title.lower() or "speed" in lesson_title.lower():
                    connections.append("Did you know a horse can gallop at 30 mph? Let's calculate using horses!")
                elif "biology" in lesson_title.lower():
                    connections.append("Let's learn this using horses as our example!")
            
            elif interest.lower() == "space":
                if "gravity" in lesson_title.lower():
                    connections.append("On the Moon, you'd weigh only 1/6 of what you weigh on Earth!")
                elif "distance" in lesson_title.lower():
                    connections.append("Let's measure distances in space!")
            
            elif interest.lower() == "art":
                if "geometry" in lesson_title.lower():
                    connections.append("Artists use geometry to create perspective in paintings!")
                elif "ratio" in lesson_title.lower():
                    connections.append("Let's learn about color mixing ratios!")
        
        if connections:
            return random.choice(connections)
        
        return ""


# Global instance
interest_themer = InterestThemer()


def theme_lesson_for_student(lesson: Dict, interests: List[str]) -> Dict:
    """Apply interest-based theming to a lesson"""
    themed_lesson = lesson.copy()
    
    # Add interest connection if available
    connection = interest_themer.get_interest_connection(lesson["title"], interests)
    if connection:
        themed_lesson["interest_connection"] = connection
    
    # Theme examples if they exist
    if "examples" in lesson and lesson["examples"]:
        for example in themed_lesson["examples"]:
            if "content" in example:
                example["content"] = interest_themer.theme_science_example(
                    example["content"], interests
                )
    
    return themed_lesson


if __name__ == "__main__":
    # Test interest theming
    themer = InterestThemer()
    
    print("Testing Interest Theming...")
    print("\nHorse-themed math problem:")
    print(themer.theme_math_problem("Word problem here", ["horses"]))
    
    print("\nSpace-themed science example:")
    print(themer.theme_science_example("Science fact here", ["space"]))
    
    print("\nArt-themed writing prompt:")
    print(themer.get_themed_writing_prompt(["art"]))
    
    print("\n✅ Interest theming working!")

