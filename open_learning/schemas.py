"""
Data schemas for API responses
"""

from typing import Optional, List, Dict, Any
from dataclasses import dataclass, asdict


@dataclass
class ContentCard:
    """Unified content card from any API"""

    source: str  # 'wikipedia', 'openlibrary', etc.
    title: str
    url: Optional[str] = None
    text: Optional[str] = None  # summary/description
    image: Optional[str] = None
    meta: Dict[str, Any] = None  # raw fields

    def __post_init__(self):
        if self.meta is None:
            self.meta = {}

    def to_dict(self) -> Dict:
        return asdict(self)


@dataclass
class QAItem:
    """Quiz/trivia question"""

    question: str
    source: str
    choices: Optional[List[str]] = None
    answer: Optional[str] = None
    difficulty: Optional[str] = None
    category: Optional[str] = None
    explanation: Optional[str] = None

    def to_dict(self) -> Dict:
        return asdict(self)


@dataclass
class SchoolData:
    """School/education data"""

    name: str
    source: str
    location: Optional[str] = None
    grade_levels: Optional[str] = None
    type: Optional[str] = None
    metadata: Optional[Dict] = None

    def __post_init__(self):
        if self.metadata is None:
            self.metadata = {}

    def to_dict(self) -> Dict:
        return asdict(self)


@dataclass
class ArtworkData:
    """Museum artwork data"""

    title: str
    artist: Optional[str]
    source: str
    image_url: Optional[str] = None
    date: Optional[str] = None
    description: Optional[str] = None
    url: Optional[str] = None

    def to_dict(self) -> Dict:
        return asdict(self)


@dataclass
class ScientificData:
    """Scientific/STEM data"""

    title: str
    source: str
    description: Optional[str] = None
    data_points: Optional[Dict] = None
    url: Optional[str] = None

    def __post_init__(self):
        if self.data_points is None:
            self.data_points = {}

    def to_dict(self) -> Dict:
        return asdict(self)
