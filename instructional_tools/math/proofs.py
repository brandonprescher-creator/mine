"""
Scaffolded Proof Builder
Geometry and algebraic proofs with support
"""
from typing import Dict, List, Any, Optional


class ProofStatement:
    """A single statement in a proof"""
    def __init__(self, statement: str, reason: str):
        self.statement = statement
        self.reason = reason
    
    def to_dict(self) -> Dict[str, Any]:
        return {'statement': self.statement, 'reason': self.reason}


class ProofBuilder:
    """Build and validate mathematical proofs"""
    
    PROOF_TYPES = ['geometry', 'algebra', 'number_theory']
    
    COMMON_REASONS = [
        'Given',
        'Definition of...',
        'Reflexive Property',
        'Symmetric Property',
        'Transitive Property',
        'Addition Property of Equality',
        'Subtraction Property of Equality',
        'Multiplication Property of Equality',
        'Division Property of Equality',
        'Distributive Property',
        'Substitution',
        'Angle Addition Postulate',
        'Segment Addition Postulate',
        'Corresponding Angles',
        'Alternate Interior Angles',
        'Vertical Angles',
        'Triangle Sum Theorem',
        'Pythagorean Theorem'
    ]
    
    def __init__(self, proof_type: str, given: List[str], prove: str):
        self.proof_type = proof_type
        self.given = given
        self.prove = prove
        self.statements: List[ProofStatement] = []
    
    def add_statement(self, statement: str, reason: str):
        """Add a statement to the proof"""
        self.statements.append(ProofStatement(statement, reason))
    
    def validate_proof(self) -> tuple[bool, List[str]]:
        """Validate logical flow of proof"""
        errors = []
        
        if not self.statements:
            errors.append('Proof must have at least one statement')
        
        # Check that proof starts with given
        if self.statements and self.statements[0].reason.lower() != 'given':
            errors.append('Proof should start with Given statements')
        
        # Check that last statement matches what we're trying to prove
        if self.statements:
            last_stmt = self.statements[-1].statement
            if self.prove.lower() not in last_stmt.lower():
                errors.append('Final statement should match what you\'re proving')
        
        return len(errors) == 0, errors
    
    def to_dict(self) -> Dict[str, Any]:
        return {'proof_type': self.proof_type, 'given': self.given, 'prove': self.prove, 'statements': [s.to_dict() for s in self.statements], 'is_valid': self.validate_proof()[0]}
