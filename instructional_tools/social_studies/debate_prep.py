"""
Debate Prep Organizer
Organize claims, evidence, and rebuttals for debates
"""
from typing import Dict, List, Any, Optional


class Argument:
    """A single argument with claim and evidence"""
    def __init__(self, id: int, claim: str, evidence: List[str], reasoning: str):
        self.id = id
        self.claim = claim
        self.evidence = evidence
        self.reasoning = reasoning
    
    def to_dict(self) -> Dict[str, Any]:
        return {'id': self.id, 'claim': self.claim, 'evidence': self.evidence, 'reasoning': self.reasoning}


class Rebuttal:
    """A rebuttal to an opposing argument"""
    def __init__(self, id: int, opposing_claim: str, counter_argument: str, counter_evidence: List[str]):
        self.id = id
        self.opposing_claim = opposing_claim
        self.counter_argument = counter_argument
        self.counter_evidence = counter_evidence
    
    def to_dict(self) -> Dict[str, Any]:
        return {'id': self.id, 'opposing_claim': self.opposing_claim, 'counter_argument': self.counter_argument, 'counter_evidence': self.counter_evidence}


class DebateOrganizer:
    """Debate Preparation Organizer"""
    
    def __init__(self, topic: str, position: str):
        self.topic = topic
        self.position = position  # 'affirmative' or 'negative'
        self.opening_statement = ''
        self.arguments: List[Argument] = []
        self.rebuttals: List[Rebuttal] = []
        self.closing_statement = ''
        self.arg_id_counter = 0
        self.reb_id_counter = 0
    
    def add_argument(self, claim: str, evidence: List[str], reasoning: str) -> Argument:
        """Add an argument"""
        arg = Argument(self.arg_id_counter, claim, evidence, reasoning)
        self.arguments.append(arg)
        self.arg_id_counter += 1
        return arg
    
    def add_rebuttal(self, opposing_claim: str, counter_argument: str, counter_evidence: List[str]) -> Rebuttal:
        """Add a rebuttal"""
        reb = Rebuttal(self.reb_id_counter, opposing_claim, counter_argument, counter_evidence)
        self.rebuttals.append(reb)
        self.reb_id_counter += 1
        return reb
    
    def validate_prep(self) -> tuple[bool, List[str]]:
        """Validate debate preparation"""
        errors = []
        
        if not self.opening_statement:
            errors.append('Opening statement required')
        
        if len(self.arguments) < 2:
            errors.append('Need at least 2 arguments')
        
        if len(self.rebuttals) < 1:
            errors.append('Need at least 1 rebuttal')
        
        if not self.closing_statement:
            errors.append('Closing statement required')
        
        return len(errors) == 0, errors
    
    def to_dict(self) -> Dict[str, Any]:
        """Export debate prep"""
        return {'topic': self.topic, 'position': self.position, 'opening_statement': self.opening_statement, 'arguments': [a.to_dict() for a in self.arguments], 'rebuttals': [r.to_dict() for r in self.rebuttals], 'closing_statement': self.closing_statement, 'is_complete': self.validate_prep()[0]}
