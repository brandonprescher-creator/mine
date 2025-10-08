"""
CER Scaffold
Claim-Evidence-Reasoning framework for scientific arguments
"""
from typing import Dict, List, Any, Optional
from ..base.activity_base import ScienceActivity, ActivityType


class CERScaffold(ScienceActivity):
    """
    Claim-Evidence-Reasoning Scaffold
    
    Structure:
    - Claim: What is your answer?
    - Evidence: What data supports your claim?
    - Reasoning: Why does the evidence support your claim?
    """
    
    def __init__(self, activity_id: int, title: str, description: str, question: str, lesson_id: Optional[int] = None, config: Optional[Dict[str, Any]] = None):
        super().__init__(activity_id=activity_id, activity_type=ActivityType.CER_SCAFFOLD, title=title, description=description, lesson_id=lesson_id, config=config)
        self.question = question
        self.requires_claim = True
        self.requires_evidence = True
        self.requires_reasoning = True
        self.min_evidence_pieces = self.config.get('min_evidence', 2)
    
    def get_prompts(self) -> Dict[str, str]:
        """Get CER prompts"""
        return {
            'claim': 'What is your answer to the question? State it clearly in one sentence.',
            'evidence': f'What data or observations support your claim? Provide at least {self.min_evidence_pieces} pieces of evidence.',
            'reasoning': 'Explain HOW your evidence supports your claim. Connect the evidence to the claim using scientific principles.'
        }
    
    def validate_cer(self, claim: str, evidence: List[str], reasoning: str) -> tuple[bool, List[str]]:
        """Validate CER structure"""
        errors = []
        
        if not claim.strip():
            errors.append('Claim is required')
        
        if len(evidence) < self.min_evidence_pieces:
            errors.append(f'Need at least {self.min_evidence_pieces} pieces of evidence')
        
        if not reasoning.strip():
            errors.append('Reasoning is required')
        
        # Check that reasoning connects to claim
        if reasoning and claim and claim.lower() not in reasoning.lower():
            errors.append('Reasoning should reference your claim')
        
        return len(errors) == 0, errors
    
    def auto_grade(self, submission_data: Dict[str, Any]) -> Dict[str, Any]:
        """Grade CER submission"""
        claim = submission_data.get('claim', '')
        evidence = submission_data.get('evidence', [])
        reasoning = submission_data.get('reasoning', '')
        
        is_valid, errors = self.validate_cer(claim, evidence, reasoning)
        
        if not is_valid:
            return {'score': 0, 'feedback': 'Please complete all CER components:\n' + '\n'.join(errors), 'details': {'errors': errors}}
        
        score = 0
        feedback_parts = []
        
        # Score claim (30 points)
        if claim:
            score += 30
            feedback_parts.append('✅ Clear claim stated\n')
        
        # Score evidence (40 points)
        evidence_score = min(40, len(evidence) * 20)
        score += evidence_score
        feedback_parts.append(f'✅ {len(evidence)} pieces of evidence provided\n')
        
        # Score reasoning (30 points)
        reasoning_words = len(reasoning.split())
        if reasoning_words >= 50:
            score += 30
            feedback_parts.append('✅ Thorough reasoning provided\n')
        elif reasoning_words >= 25:
            score += 20
            feedback_parts.append('⚠️ Good reasoning, could be more detailed\n')
        else:
            score += 10
            feedback_parts.append('⚠️ Reasoning needs more detail\n')
        
        return {'score': score, 'feedback': ''.join(feedback_parts), 'details': {'claim_length': len(claim), 'evidence_count': len(evidence), 'reasoning_length': reasoning_words}}
