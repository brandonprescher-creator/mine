"""
Writing Prompts Library
Curated prompts by grade level and genre
"""
from typing import Dict, List, Any, Optional
import random


class WritingPrompt:
    """A single writing prompt"""
    def __init__(self, id: int, prompt_text: str, genre: str, grade_level: int, image_url: Optional[str] = None, video_url: Optional[str] = None):
        self.id = id
        self.prompt_text = prompt_text
        self.genre = genre
        self.grade_level = grade_level
        self.image_url = image_url
        self.video_url = video_url
    
    def to_dict(self) -> Dict[str, Any]:
        return {'id': self.id, 'prompt': self.prompt_text, 'genre': self.genre, 'grade_level': self.grade_level, 'image_url': self.image_url, 'video_url': self.video_url}


class WritingPromptsLibrary:
    """Collection of writing prompts"""
    
    GENRES = ['narrative', 'expository', 'persuasive', 'descriptive', 'creative', 'research', 'poetry']
    
    def __init__(self):
        self.prompts: List[WritingPrompt] = []
        self._load_default_prompts()
    
    def _load_default_prompts(self):
        """Load default prompt library"""
        default_prompts = [
            (1, "Write about a time when you learned something important.", "narrative", 3),
            (2, "Explain how to make your favorite food.", "expository", 4),
            (3, "Should students have homework? Take a position and defend it.", "persuasive", 5),
            (4, "Describe your perfect day from morning to night.", "descriptive", 3),
            (5, "Write a story that begins: 'The door slowly creaked open...'", "creative", 4),
            (6, "Research and explain how plants make food.", "research", 5),
            (7, "Write a poem about your favorite season.", "poetry", 3),
            (8, "Tell about a challenge you overcame.", "narrative", 6),
            (9, "Compare and contrast two historical figures.", "expository", 7),
            (10, "Should schools ban junk food? Argue your position.", "persuasive", 6)
        ]
        
        for id, text, genre, grade in default_prompts:
            self.prompts.append(WritingPrompt(id, text, genre, grade))
    
    def get_by_grade(self, grade_level: int) -> List[WritingPrompt]:
        """Get prompts for a grade level"""
        return [p for p in self.prompts if abs(p.grade_level - grade_level) <= 1]
    
    def get_by_genre(self, genre: str) -> List[WritingPrompt]:
        """Get prompts by genre"""
        return [p for p in self.prompts if p.genre == genre]
    
    def get_random(self, count: int = 3) -> List[WritingPrompt]:
        """Get random prompts"""
        return random.sample(self.prompts, min(count, len(self.prompts)))
