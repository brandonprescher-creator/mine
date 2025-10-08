"""
Map Annotation Tools
Draw routes, mark locations, analyze geography
"""
from typing import Dict, List, Any, Optional


class MapAnnotation:
    """A single annotation on a map"""
    def __init__(self, id: int, annotation_type: str, data: Dict[str, Any], label: str):
        self.id = id
        self.annotation_type = annotation_type  # 'marker', 'route', 'region', 'label'
        self.data = data
        self.label = label
    
    def to_dict(self) -> Dict[str, Any]:
        return {'id': self.id, 'type': self.annotation_type, 'data': self.data, 'label': self.label}


class MapAnnotationTool:
    """Interactive map annotation tool"""
    
    def __init__(self, map_title: str, base_map: str):
        self.map_title = map_title
        self.base_map = base_map  # URL or identifier for base map
        self.annotations: List[MapAnnotation] = []
        self.annotation_id_counter = 0
    
    def add_marker(self, lat: float, lon: float, label: str, description: Optional[str] = None) -> MapAnnotation:
        """Add a location marker"""
        annotation = MapAnnotation(self.annotation_id_counter, 'marker', {'lat': lat, 'lon': lon, 'description': description}, label)
        self.annotations.append(annotation)
        self.annotation_id_counter += 1
        return annotation
    
    def add_route(self, points: List[Tuple[float, float]], label: str, description: Optional[str] = None) -> MapAnnotation:
        """Add a route/path"""
        annotation = MapAnnotation(self.annotation_id_counter, 'route', {'points': points, 'description': description}, label)
        self.annotations.append(annotation)
        self.annotation_id_counter += 1
        return annotation
    
    def to_dict(self) -> Dict[str, Any]:
        return {'title': self.map_title, 'base_map': self.base_map, 'annotations': [a.to_dict() for a in self.annotations], 'annotation_count': len(self.annotations)}
