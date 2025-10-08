"""
Portfolio Builder
Collect and showcase best work
"""
from typing import Dict, List, Any, Optional
from datetime import datetime

class PortfolioBuilder:
    """
    Student Portfolio System
    
    Students can:
    - Select their best work
    - Add reflections
    - Organize by subject/skill
    - Share with teachers/parents
    """
    
    def __init__(self, student_id: int):
        self.student_id = student_id
        self.items = []
    
    def add_item(
        self,
        submission_id: int,
        title: str,
        work_type: str,
        reflection: str,
        featured: bool = False,
        tags: Optional[List[str]] = None
    ) -> Dict[str, Any]:
        """Add an item to the portfolio"""
        item = {
            'id': len(self.items) + 1,
            'submission_id': submission_id,
            'title': title,
            'work_type': work_type,
            'reflection': reflection,
            'featured': featured,
            'tags': tags or [],
            'added_at': datetime.utcnow().isoformat()
        }
        self.items.append(item)
        return item
    
    def get_featured_items(self) -> List[Dict[str, Any]]:
        """Get featured portfolio items"""
        return [item for item in self.items if item['featured']]
    
    def get_items_by_tag(self, tag: str) -> List[Dict[str, Any]]:
        """Get items with a specific tag"""
        return [item for item in self.items if tag in item['tags']]
    
    def get_items_by_subject(self, subject: str) -> List[Dict[str, Any]]:
        """Get items for a specific subject"""
        return self.get_items_by_tag(subject.lower())
    
    def generate_showcase(self) -> Dict[str, Any]:
        """Generate a portfolio showcase view"""
        return {
            'student_id': self.student_id,
            'total_items': len(self.items),
            'featured_items': self.get_featured_items(),
            'subjects': self._get_subject_distribution(),
            'work_types': self._get_work_type_distribution(),
            'recent_additions': sorted(self.items, key=lambda x: x['added_at'], reverse=True)[:5]
        }
    
    def _get_subject_distribution(self) -> Dict[str, int]:
        """Get count of items per subject"""
        distribution = {}
        for item in self.items:
            for tag in item['tags']:
                if tag in ['math', 'science', 'ela', 'social studies', 'arts']:
                    distribution[tag] = distribution.get(tag, 0) + 1
        return distribution
    
    def _get_work_type_distribution(self) -> Dict[str, int]:
        """Get count of items per work type"""
        distribution = {}
        for item in self.items:
            work_type = item['work_type']
            distribution[work_type] = distribution.get(work_type, 0) + 1
        return distribution
