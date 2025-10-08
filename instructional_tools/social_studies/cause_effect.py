"""
Cause & Effect Chain Builder
Visualize historical causation and consequences
"""
from typing import Dict, List, Any, Optional


class CauseEffectLink:
    """A link between cause and effect"""
    def __init__(self, id: int, cause: str, effect: str, explanation: str):
        self.id = id
        self.cause = cause
        self.effect = effect
        self.explanation = explanation
    
    def to_dict(self) -> Dict[str, Any]:
        return {'id': self.id, 'cause': self.cause, 'effect': self.effect, 'explanation': self.explanation}


class CauseEffectChain:
    """Build chains of historical causation"""
    
    def __init__(self, event_title: str):
        self.event_title = event_title
        self.links: List[CauseEffectLink] = []
        self.link_id_counter = 0
    
    def add_link(self, cause: str, effect: str, explanation: str) -> CauseEffectLink:
        """Add a cause-effect link"""
        link = CauseEffectLink(self.link_id_counter, cause, effect, explanation)
        self.links.append(link)
        self.link_id_counter += 1
        return link
    
    def get_chain_visualization(self) -> List[Dict[str, Any]]:
        """Get data for visualizing the chain"""
        return [{'step': i+1, 'link': link.to_dict()} for i, link in enumerate(self.links)]
    
    def validate_chain(self) -> tuple[bool, List[str]]:
        """Validate cause-effect chain"""
        errors = []
        
        if len(self.links) < 2:
            errors.append('Need at least 2 cause-effect links')
        
        # Check that effects lead to next causes
        for i in range(len(self.links) - 1):
            if self.links[i].effect.lower() not in self.links[i+1].cause.lower():
                errors.append(f'Link {i+1} effect should connect to link {i+2} cause')
        
        return len(errors) == 0, errors
