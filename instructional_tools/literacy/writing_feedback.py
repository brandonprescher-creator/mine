"""
Writing Feedback System
Automated clarity, structure, and readability analysis
"""
from typing import Dict, List, Any
import re


class WritingAnalyzer:
    """Analyze writing for clarity and structure"""
    
    def analyze_text(self, text: str) -> Dict[str, Any]:
        """Comprehensive text analysis"""
        words = text.split()
        sentences = re.split(r'[.!?]+', text)
        sentences = [s.strip() for s in sentences if s.strip()]
        
        return {
            'word_count': len(words),
            'sentence_count': len(sentences),
            'paragraph_count': text.count('\n\n') + 1,
            'avg_words_per_sentence': round(len(words) / len(sentences), 1) if sentences else 0,
            'readability': self._calculate_readability(words, sentences),
            'structure_score': self._analyze_structure(text),
            'clarity_score': self._analyze_clarity(text),
            'suggestions': self._generate_suggestions(text)
        }
    
    def _calculate_readability(self, words: List[str], sentences: List[str]) -> Dict[str, Any]:
        """Calculate readability metrics"""
        avg_word_length = sum(len(w) for w in words) / len(words) if words else 0
        avg_sentence_length = len(words) / len(sentences) if sentences else 0
        
        # Simplified Flesch-Kincaid grade level
        grade_level = 0.39 * avg_sentence_length + 11.8 * (avg_word_length / 6) - 15.59
        grade_level = max(1, min(12, grade_level))
        
        return {'grade_level': round(grade_level, 1), 'avg_word_length': round(avg_word_length, 1), 'avg_sentence_length': round(avg_sentence_length, 1)}
    
    def _analyze_structure(self, text: str) -> int:
        """Analyze organizational structure (0-100)"""
        score = 50  # Base score
        
        # Check for paragraphs
        if '\n\n' in text:
            score += 10
        
        # Check for varied sentence starts
        sentences = re.split(r'[.!?]+', text)
        first_words = [s.strip().split()[0].lower() for s in sentences if s.strip() and s.strip().split()]
        if len(set(first_words)) / len(first_words) > 0.5:
            score += 20
        
        # Check for transition words
        transitions = ['however', 'therefore', 'furthermore', 'meanwhile', 'consequently', 'additionally']
        if any(t in text.lower() for t in transitions):
            score += 20
        
        return min(100, score)
    
    def _analyze_clarity(self, text: str) -> int:
        """Analyze writing clarity (0-100)"""
        score = 60  # Base score
        
        # Check for excessive passive voice (simplified)
        passive_indicators = ['was', 'were', 'been', 'being']
        passive_count = sum(text.lower().count(p) for p in passive_indicators)
        if passive_count < len(text.split()) * 0.1:
            score += 20
        
        # Check sentence variety
        sentences = re.split(r'[.!?]+', text)
        sentence_lengths = [len(s.split()) for s in sentences if s.strip()]
        if sentence_lengths and max(sentence_lengths) - min(sentence_lengths) > 5:
            score += 20
        
        return min(100, score)
    
    def _generate_suggestions(self, text: str) -> List[str]:
        """Generate improvement suggestions"""
        suggestions = []
        
        sentences = re.split(r'[.!?]+', text)
        avg_length = sum(len(s.split()) for s in sentences if s.strip()) / len([s for s in sentences if s.strip()])
        
        if avg_length > 25:
            suggestions.append('Consider breaking up long sentences for better readability')
        elif avg_length < 10:
            suggestions.append('Try combining some short sentences for better flow')
        
        if not '\n\n' in text:
            suggestions.append('Break your writing into paragraphs for better organization')
        
        if text.count(',') < len(text.split()) * 0.05:
            suggestions.append('Consider using more commas to separate ideas')
        
        return suggestions
