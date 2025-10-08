"""
Vocabulary Flashcards
Auto-generated from texts with spaced repetition
"""
from typing import Dict, List, Any, Optional
from datetime import datetime, timedelta
import random
import re

from ..base.activity_base import LiteracyActivity, ActivityType


class FlashCard:
    """A single vocabulary flashcard"""
    
    def __init__(
        self,
        word: str,
        definition: str,
        context_sentence: Optional[str] = None,
        synonyms: Optional[List[str]] = None,
        antonyms: Optional[List[str]] = None,
        part_of_speech: Optional[str] = None
    ):
        self.word = word
        self.definition = definition
        self.context_sentence = context_sentence
        self.synonyms = synonyms or []
        self.antonyms = antonyms or []
        self.part_of_speech = part_of_speech
        
        # Spaced repetition tracking
        self.times_seen = 0
        self.times_correct = 0
        self.last_seen = None
        self.next_review = datetime.utcnow()
        self.mastery_level = 0  # 0-5
    
    def record_attempt(self, correct: bool):
        """Record a practice attempt"""
        self.times_seen += 1
        if correct:
            self.times_correct += 1
            self.mastery_level = min(5, self.mastery_level + 1)
        else:
            self.mastery_level = max(0, self.mastery_level - 1)
        
        self.last_seen = datetime.utcnow()
        self._calculate_next_review()
    
    def _calculate_next_review(self):
        """Calculate when card should be reviewed next (spaced repetition)"""
        intervals = {
            0: timedelta(minutes=10),   # New/struggling
            1: timedelta(hours=1),       # Learning
            2: timedelta(days=1),        # Getting it
            3: timedelta(days=3),        # Confident
            4: timedelta(days=7),        # Strong
            5: timedelta(days=14)        # Mastered
        }
        
        self.next_review = datetime.utcnow() + intervals.get(self.mastery_level, timedelta(days=1))
    
    @property
    def accuracy(self) -> float:
        """Get accuracy percentage"""
        return (self.times_correct / self.times_seen * 100) if self.times_seen > 0 else 0
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        return {
            'word': self.word,
            'definition': self.definition,
            'context_sentence': self.context_sentence,
            'synonyms': self.synonyms,
            'antonyms': self.antonyms,
            'part_of_speech': self.part_of_speech,
            'times_seen': self.times_seen,
            'times_correct': self.times_correct,
            'accuracy': round(self.accuracy, 1),
            'mastery_level': self.mastery_level,
            'next_review': self.next_review.isoformat() if self.next_review else None
        }


class VocabularyFlashcards(LiteracyActivity):
    """
    Vocabulary Flashcards Activity
    
    Auto-generates flashcards from texts and uses spaced repetition
    for optimal learning and retention.
    """
    
    def __init__(
        self,
        activity_id: int,
        title: str,
        description: str,
        lesson_id: Optional[int] = None,
        config: Optional[Dict[str, Any]] = None
    ):
        super().__init__(
            activity_id=activity_id,
            activity_type=ActivityType.VOCAB_CARDS,
            title=title,
            description=description,
            lesson_id=lesson_id,
            config=config
        )
        
        self.cards: List[FlashCard] = []
        self.study_mode = self.config.get('study_mode', 'flashcard')  # flashcard, quiz, matching
    
    def add_card(self, card: FlashCard):
        """Add a flashcard to the deck"""
        self.cards.append(card)
    
    def get_cards_for_review(self, limit: int = 20) -> List[FlashCard]:
        """Get cards that are due for review"""
        now = datetime.utcnow()
        due_cards = [c for c in self.cards if c.next_review <= now]
        
        # Sort by urgency (most overdue first) and mastery (struggling words first)
        due_cards.sort(key=lambda c: (c.next_review, c.mastery_level))
        
        return due_cards[:limit]
    
    def get_new_cards(self, limit: int = 10) -> List[FlashCard]:
        """Get cards that haven't been studied yet"""
        new_cards = [c for c in self.cards if c.times_seen == 0]
        return new_cards[:limit]
    
    def get_struggling_cards(self, limit: int = 10) -> List[FlashCard]:
        """Get cards with low accuracy"""
        struggling = [c for c in self.cards if c.times_seen > 0 and c.accuracy < 70]
        struggling.sort(key=lambda c: c.accuracy)
        return struggling[:limit]
    
    def get_mastered_cards(self) -> List[FlashCard]:
        """Get cards that are mastered"""
        return [c for c in self.cards if c.mastery_level >= 4]
    
    def generate_quiz(self, num_questions: int = 10) -> List[Dict[str, Any]]:
        """Generate a multiple choice quiz"""
        quiz_cards = random.sample(self.cards, min(num_questions, len(self.cards)))
        questions = []
        
        for card in quiz_cards:
            # Get wrong answer choices
            other_cards = [c for c in self.cards if c.word != card.word]
            wrong_choices = random.sample(other_cards, min(3, len(other_cards)))
            
            choices = [card.definition] + [c.definition for c in wrong_choices]
            random.shuffle(choices)
            
            questions.append({
                'word': card.word,
                'correct_definition': card.definition,
                'choices': choices,
                'context': card.context_sentence
            })
        
        return questions
    
    def generate_matching(self, num_pairs: int = 10) -> Dict[str, List[str]]:
        """Generate a matching activity"""
        match_cards = random.sample(self.cards, min(num_pairs, len(self.cards)))
        
        words = [c.word for c in match_cards]
        definitions = [c.definition for c in match_cards]
        random.shuffle(definitions)
        
        return {
            'words': words,
            'definitions': definitions,
            'correct_pairs': {c.word: c.definition for c in match_cards}
        }
    
    @staticmethod
    def extract_from_text(
        text: str,
        grade_level: int = 5,
        num_words: int = 20
    ) -> List[str]:
        """
        Extract vocabulary words from a text
        (In a real app, this would use NLP and vocabulary databases)
        """
        # Simple implementation - extract longer, less common words
        words = re.findall(r'\b[a-zA-Z]{6,}\b', text.lower())
        
        # Remove very common words (simplified)
        common_words = {'the', 'and', 'that', 'have', 'with', 'this', 'from', 'they', 'would', 'there', 'their', 'what', 'about', 'which', 'when', 'make', 'like', 'time', 'just', 'know', 'take', 'people', 'into', 'year', 'your', 'good', 'some', 'could', 'them', 'see', 'other', 'than', 'then', 'now', 'look', 'only', 'come', 'its', 'over', 'think', 'also', 'back', 'after', 'use', 'two', 'how', 'our', 'work', 'first', 'well', 'way', 'even', 'new', 'want', 'because', 'any', 'these', 'give', 'day', 'most', 'us'}
        
        unique_words = list(set(words) - common_words)
        return sorted(unique_words)[:num_words]
    
    def get_progress_stats(self) -> Dict[str, Any]:
        """Get overall progress statistics"""
        total = len(self.cards)
        if total == 0:
            return {'total': 0, 'studied': 0, 'mastered': 0, 'accuracy': 0}
        
        studied = len([c for c in self.cards if c.times_seen > 0])
        mastered = len(self.get_mastered_cards())
        
        total_attempts = sum(c.times_seen for c in self.cards)
        total_correct = sum(c.times_correct for c in self.cards)
        accuracy = (total_correct / total_attempts * 100) if total_attempts > 0 else 0
        
        return {
            'total': total,
            'studied': studied,
            'mastered': mastered,
            'new': total - studied,
            'accuracy': round(accuracy, 1),
            'mastery_distribution': self._get_mastery_distribution()
        }
    
    def _get_mastery_distribution(self) -> Dict[int, int]:
        """Get count of cards at each mastery level"""
        distribution = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
        for card in self.cards:
            distribution[card.mastery_level] += 1
        return distribution
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert entire deck to dictionary"""
        return {
            'activity_id': self.activity_id,
            'title': self.title,
            'description': self.description,
            'total_cards': len(self.cards),
            'cards': [c.to_dict() for c in self.cards],
            'progress': self.get_progress_stats()
        }
