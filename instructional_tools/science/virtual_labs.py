"""
Virtual Labs Integration
Connect to PhET, NASA, CK-12 virtual labs
"""
from typing import Dict, List, Any, Optional


class VirtualLab:
    """A virtual lab simulation"""
    def __init__(self, id: str, title: str, url: str, provider: str, subject: str, grade_range: tuple):
        self.id = id
        self.title = title
        self.url = url
        self.provider = provider  # 'PhET', 'NASA', 'CK-12', 'etc.'
        self.subject = subject
        self.grade_range = grade_range
        self.description = ''
    
    def to_dict(self) -> Dict[str, Any]:
        return {'id': self.id, 'title': self.title, 'url': self.url, 'provider': self.provider, 'subject': self.subject, 'grade_range': list(self.grade_range), 'description': self.description}


class VirtualLabLibrary:
    """Library of virtual lab resources"""
    
    def __init__(self):
        self.labs: List[VirtualLab] = []
        self._load_popular_labs()
    
    def _load_popular_labs(self):
        """Load popular virtual labs"""
        labs = [
            VirtualLab('phet_forces', 'Forces and Motion', 'https://phet.colorado.edu/en/simulation/forces-and-motion-basics', 'PhET', 'Physics', (6, 12)),
            VirtualLab('phet_circuits', 'Circuit Construction', 'https://phet.colorado.edu/en/simulation/circuit-construction-kit-dc', 'PhET', 'Physics', (6, 12)),
            VirtualLab('phet_ph_scale', 'pH Scale', 'https://phet.colorado.edu/en/simulation/ph-scale', 'PhET', 'Chemistry', (7, 12)),
            VirtualLab('nasa_solar_system', 'Solar System Explorer', 'https://solarsystem.nasa.gov/eyes/', 'NASA', 'Astronomy', (5, 12)),
            VirtualLab('phet_genetics', 'Natural Selection', 'https://phet.colorado.edu/en/simulation/natural-selection', 'PhET', 'Biology', (7, 12))
        ]
        self.labs.extend(labs)
    
    def get_by_subject(self, subject: str) -> List[VirtualLab]:
        """Get labs by subject"""
        return [lab for lab in self.labs if subject.lower() in lab.subject.lower()]
    
    def get_by_grade(self, grade: int) -> List[VirtualLab]:
        """Get labs appropriate for grade level"""
        return [lab for lab in self.labs if lab.grade_range[0] <= grade <= lab.grade_range[1]]
