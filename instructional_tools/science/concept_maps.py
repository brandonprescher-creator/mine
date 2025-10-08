"""
Concept Map Builder
Visual organization of scientific concepts and relationships
"""
from typing import Dict, List, Any, Optional


class ConceptNode:
    """A single concept in the map"""
    def __init__(self, id: int, label: str, x: float, y: float):
        self.id = id
        self.label = label
        self.x = x
        self.y = y
    
    def to_dict(self) -> Dict[str, Any]:
        return {'id': self.id, 'label': self.label, 'x': self.x, 'y': self.y}


class ConceptConnection:
    """A connection between concepts"""
    def __init__(self, id: int, from_node: int, to_node: int, relationship: str):
        self.id = id
        self.from_node = from_node
        self.to_node = to_node
        self.relationship = relationship
    
    def to_dict(self) -> Dict[str, Any]:
        return {'id': self.id, 'from': self.from_node, 'to': self.to_node, 'relationship': self.relationship}


class ConceptMapBuilder:
    """Build and validate concept maps"""
    
    def __init__(self, topic: str):
        self.topic = topic
        self.nodes: List[ConceptNode] = []
        self.connections: List[ConceptConnection] = []
        self.node_id_counter = 0
        self.connection_id_counter = 0
    
    def add_node(self, label: str, x: float, y: float) -> ConceptNode:
        """Add a concept node"""
        node = ConceptNode(self.node_id_counter, label, x, y)
        self.nodes.append(node)
        self.node_id_counter += 1
        return node
    
    def add_connection(self, from_node_id: int, to_node_id: int, relationship: str) -> ConceptConnection:
        """Add a connection between nodes"""
        conn = ConceptConnection(self.connection_id_counter, from_node_id, to_node_id, relationship)
        self.connections.append(conn)
        self.connection_id_counter += 1
        return conn
    
    def validate_map(self) -> tuple[bool, List[str]]:
        """Validate the concept map"""
        errors = []
        
        if len(self.nodes) < 3:
            errors.append('Map should have at least 3 concepts')
        
        if len(self.connections) < 2:
            errors.append('Map should have at least 2 connections')
        
        # Check for orphaned nodes
        connected_nodes = set()
        for conn in self.connections:
            connected_nodes.add(conn.from_node)
            connected_nodes.add(conn.to_node)
        
        orphaned = [node for node in self.nodes if node.id not in connected_nodes]
        if orphaned:
            errors.append(f'{len(orphaned)} concept(s) are not connected')
        
        return len(errors) == 0, errors
    
    def to_dict(self) -> Dict[str, Any]:
        """Export map data"""
        return {
            'topic': self.topic,
            'nodes': [n.to_dict() for n in self.nodes],
            'connections': [c.to_dict() for c in self.connections],
            'is_valid': self.validate_map()[0]
        }
