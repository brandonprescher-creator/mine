"""
Summarize & Paraphrase Practice
Teach original expression and avoid plagiarism
"""
from typing import Dict, List, Any, Optional


class SummarizeParaphraseTrainer:
    """
    Summarize & Paraphrase Tool
    
    Features:
    - Text comparison
    - Originality checking
    - Key points identification
    - Guided rewriting
    """
    
    def __init__(self, original_text: str):
        self.original_text = original_text
        self.student_summary = ''
        self.student_paraphrase = ''
    
    def check_originality(self, student_text: str) -> Dict[str, Any]:
        """Check if student used own words (simplified)"""
        original_words = set(self.original_text.lower().split())
        student_words = set(student_text.lower().split())
        
        # Calculate overlap (simplified - real version would use n-grams)
        common_words = original_words & student_words
        overlap_percentage = (len(common_words) / len(original_words) * 100) if original_words else 0
        
        # Filter out common words
        common_english = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with'}
        significant_overlap = common_words - common_english
        
        is_original = overlap_percentage < 70 and len(significant_overlap) < len(original_words) * 0.5
        
        feedback = []
        if is_original:
            feedback.append('✅ Good use of your own words!')
        else:
            feedback.append('⚠️ Try using more of your own words')
            if overlap_percentage > 80:
                feedback.append('Too much copying from the original')
        
        return {'is_original': is_original, 'overlap_percentage': round(overlap_percentage, 1), 'feedback': ' '.join(feedback)}
    
    def identify_key_points(self) -> List[str]:
        """Identify key points from original text (simplified)"""
        sentences = [s.strip() for s in self.original_text.split('.') if s.strip()]
        # In production, would use NLP to identify topic sentences
        return sentences[:3] if len(sentences) >= 3 else sentences
    
    def get_paraphrase_tips(self) -> List[str]:
        """Get tips for paraphrasing"""
        return [
            'Read the original text carefully and understand it',
            'Put the text away and write from memory',
            'Use synonyms for key words',
            'Change sentence structure',
            'Keep the same meaning but use your own voice',
            'Cite the source even when paraphrasing'
        ]
    
    def validate_summary(self, summary: str, max_words: Optional[int] = None) -> tuple[bool, List[str]]:
        """Validate a summary"""
        errors = []
        
        if not summary.strip():
            errors.append('Summary cannot be empty')
        
        word_count = len(summary.split())
        original_word_count = len(self.original_text.split())
        
        if word_count > original_word_count * 0.8:
            errors.append('Summary should be much shorter than original')
        
        if max_words and word_count > max_words:
            errors.append(f'Summary exceeds maximum length ({word_count}/{max_words} words)')
        
        # Check originality
        originality = self.check_originality(summary)
        if not originality['is_original']:
            errors.append('Use more of your own words')
        
        return len(errors) == 0, errors
