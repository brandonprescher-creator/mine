"""
Government & Civics Simulations
Interactive simulations for understanding government processes
"""
from typing import Dict, List, Any, Optional


class BillSimulation:
    """Simulate the legislative process"""
    
    BILL_STAGES = ['draft', 'committee', 'house_vote', 'senate_vote', 'presidential_action', 'law']
    
    def __init__(self, bill_title: str, sponsor: str):
        self.bill_title = bill_title
        self.sponsor = sponsor
        self.bill_text = ''
        self.current_stage = 'draft'
        self.votes_for = 0
        self.votes_against = 0
        self.amendments = []
        self.passed = False
    
    def advance_stage(self, vote_result: Optional[Dict[str, int]] = None):
        """Advance bill to next stage"""
        current_index = self.BILL_STAGES.index(self.current_stage)
        
        if vote_result:
            self.votes_for = vote_result.get('for', 0)
            self.votes_against = vote_result.get('against', 0)
            
            if self.votes_for <= self.votes_against:
                self.passed = False
                return
        
        if current_index < len(self.BILL_STAGES) - 1:
            self.current_stage = self.BILL_STAGES[current_index + 1]
        
        if self.current_stage == 'law':
            self.passed = True
    
    def to_dict(self) -> Dict[str, Any]:
        return {'title': self.bill_title, 'sponsor': self.sponsor, 'stage': self.current_stage, 'votes_for': self.votes_for, 'votes_against': self.votes_against, 'passed': self.passed}
