"""
VISUAL CONTENT GENERATOR
Automatically creates pictures, diagrams, and images for EVERY lesson!
Uses matplotlib, PIL, and SVG to generate educational visuals.
"""

import matplotlib
matplotlib.use('Agg')  # Non-interactive backend
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import Circle, Rectangle, Polygon, FancyBboxPatch, Wedge
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import io
import base64
import os
from typing import Dict, List, Tuple

class VisualContentGenerator:
    def __init__(self):
        """Initialize visual content generator"""
        self.output_dir = 'static/images/lessons'
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
        
        # Color schemes for kid-friendly visuals
        self.colors = {
            'primary': ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8'],
            'pastel': ['#FFB6C1', '#FFE4E1', '#E0BBE4', '#D4A5A5', '#A8E6CF'],
            'bright': ['#FF1744', '#00E676', '#2196F3', '#FFEA00', '#FF6E40']
        }
        
    def generate_visual_for_lesson(self, lesson_data: Dict) -> Dict:
        """Generate all visuals for a lesson"""
        subject = lesson_data.get('subject', 'general')
        topic = lesson_data.get('topic', '')
        lesson_id = lesson_data.get('lesson_id', 0)
        
        visuals = {
            'header_image': self.create_header_image(topic, subject),
            'concept_diagrams': [],
            'step_illustrations': [],
            'practice_images': []
        }
        
        # Generate subject-specific visuals
        if 'math' in subject.lower():
            visuals['concept_diagrams'] = self.create_math_diagrams(topic, lesson_id)
        elif 'science' in subject.lower():
            visuals['concept_diagrams'] = self.create_science_diagrams(topic, lesson_id)
        
        # Generate step-by-step illustrations
        steps = lesson_data.get('steps', [])
        for i, step in enumerate(steps[:5]):  # First 5 steps
            visual = self.create_step_illustration(step, i, subject)
            if visual:
                visuals['step_illustrations'].append(visual)
        
        return visuals
    
    def create_header_image(self, topic: str, subject: str) -> str:
        """Create colorful header image for lesson"""
        fig, ax = plt.subplots(figsize=(12, 3))
        
        # Gradient background
        gradient = np.linspace(0, 1, 256).reshape(1, -1)
        gradient = np.vstack((gradient, gradient))
        
        ax.imshow(gradient, aspect='auto', cmap='rainbow', extent=[0, 12, 0, 3])
        
        # Add text
        ax.text(6, 1.5, topic.upper(), fontsize=32, weight='bold',
                ha='center', va='center', color='white',
                bbox=dict(boxstyle='round,pad=0.5', facecolor='black', alpha=0.5))
        
        # Subject emoji
        emojis = {
            'math': '📐',
            'science': '🔬',
            'english': '📖',
            'social': '🌍'
        }
        emoji = next((v for k, v in emojis.items() if k in subject.lower()), '📚')
        ax.text(1, 1.5, emoji, fontsize=48, ha='center', va='center')
        
        ax.axis('off')
        
        # Save to base64
        return self.fig_to_base64(fig)
    
    def create_math_diagrams(self, topic: str, lesson_id: int) -> List[Dict]:
        """Create math-specific diagrams"""
        diagrams = []
        
        topic_lower = topic.lower()
        
        # Division visuals
        if 'division' in topic_lower:
            diagrams.append(self.create_division_visual(24, 6))
            diagrams.append(self.create_division_visual(48, 8))
        
        # Fraction visuals
        elif 'fraction' in topic_lower:
            diagrams.append(self.create_fraction_visual(1, 2))
            diagrams.append(self.create_fraction_visual(3, 4))
            diagrams.append(self.create_fraction_visual(2, 3))
        
        # Geometry visuals
        elif 'geometry' in topic_lower or 'shape' in topic_lower:
            diagrams.append(self.create_shapes_visual())
            diagrams.append(self.create_angles_visual())
        
        # Number line
        elif 'number' in topic_lower or 'counting' in topic_lower:
            diagrams.append(self.create_number_line(0, 20))
        
        # Multiplication array
        elif 'multiplication' in topic_lower:
            diagrams.append(self.create_multiplication_array(4, 5))
            diagrams.append(self.create_multiplication_array(3, 6))
        
        # Graph/coordinate plane
        elif 'graph' in topic_lower or 'coordinate' in topic_lower:
            diagrams.append(self.create_coordinate_plane())
        
        return diagrams
    
    def create_division_visual(self, dividend: int, divisor: int) -> Dict:
        """Create visual representation of division"""
        fig, ax = plt.subplots(figsize=(10, 6))
        
        quotient = dividend // divisor
        remainder = dividend % divisor
        
        # Draw groups
        colors = self.colors['primary']
        for i in range(divisor):
            color = colors[i % len(colors)]
            
            # Calculate position
            x = (i % 4) * 2.5
            y = (i // 4) * 2
            
            # Draw group box
            rect = FancyBboxPatch((x, y), 2, 1.5, 
                                 boxstyle="round,pad=0.1",
                                 facecolor=color, alpha=0.3,
                                 edgecolor=color, linewidth=3)
            ax.add_patch(rect)
            
            # Add items in group
            for j in range(quotient):
                circle = Circle((x + 0.3 + j*0.4, y + 0.75), 0.15,
                              facecolor=color, edgecolor='black', linewidth=2)
                ax.add_patch(circle)
            
            # Group label
            ax.text(x + 1, y - 0.3, f'Group {i+1}', ha='center', fontsize=10, weight='bold')
        
        # Title
        ax.text(5, 8.5, f'{dividend} ÷ {divisor} = {quotient}' + 
               (f' remainder {remainder}' if remainder else ''),
               fontsize=20, weight='bold', ha='center')
        
        ax.set_xlim(-0.5, 10)
        ax.set_ylim(-1, 9)
        ax.axis('off')
        
        return {
            'type': 'division',
            'image': self.fig_to_base64(fig),
            'caption': f'Visual representation: {dividend} items divided into {divisor} groups of {quotient}'
        }
    
    def create_fraction_visual(self, numerator: int, denominator: int) -> Dict:
        """Create visual representation of fractions"""
        fig, ax = plt.subplots(figsize=(8, 8))
        
        # Draw circle divided into parts
        radius = 3
        center = (0, 0)
        
        # Calculate angles
        angle_per_part = 360 / denominator
        
        for i in range(denominator):
            start_angle = i * angle_per_part
            end_angle = (i + 1) * angle_per_part
            
            # Color filled parts
            color = self.colors['primary'][0] if i < numerator else '#E0E0E0'
            alpha = 0.8 if i < numerator else 0.3
            
            wedge = Wedge(center, radius, start_angle, end_angle,
                         facecolor=color, edgecolor='black', linewidth=3, alpha=alpha)
            ax.add_patch(wedge)
        
        # Add fraction text
        ax.text(0, -4.5, f'{numerator}/{denominator}', fontsize=40, weight='bold',
               ha='center', va='center')
        
        ax.set_xlim(-4, 4)
        ax.set_ylim(-5, 4)
        ax.set_aspect('equal')
        ax.axis('off')
        
        return {
            'type': 'fraction',
            'image': self.fig_to_base64(fig),
            'caption': f'{numerator} out of {denominator} parts shaded'
        }
    
    def create_shapes_visual(self) -> Dict:
        """Create visual of basic shapes"""
        fig, ax = plt.subplots(figsize=(12, 8))
        
        shapes = [
            ('Circle', Circle((2, 6), 1.5, facecolor=self.colors['primary'][0], alpha=0.6)),
            ('Square', Rectangle((5, 4.5), 3, 3, facecolor=self.colors['primary'][1], alpha=0.6)),
            ('Triangle', Polygon([(10, 4.5), (11.5, 7.5), (13, 4.5)], 
                                facecolor=self.colors['primary'][2], alpha=0.6)),
            ('Rectangle', Rectangle((1, 1), 4, 2, facecolor=self.colors['primary'][3], alpha=0.6)),
            ('Pentagon', Polygon([(7, 2), (8.5, 3), (8, 4.5), (6, 4.5), (5.5, 3)],
                                facecolor=self.colors['primary'][4], alpha=0.6))
        ]
        
        for name, shape in shapes:
            ax.add_patch(shape)
            # Add label
            if hasattr(shape, 'center'):
                x, y = shape.center
            else:
                x, y = shape.get_xy()
                x += shape.get_width() / 2 if hasattr(shape, 'get_width') else 0
                y -= 0.5
            
            ax.text(x, y - 0.3, name, ha='center', fontsize=14, weight='bold')
        
        ax.set_xlim(0, 14)
        ax.set_ylim(0, 8)
        ax.set_aspect('equal')
        ax.axis('off')
        ax.set_title('Basic Shapes', fontsize=24, weight='bold', pad=20)
        
        return {
            'type': 'shapes',
            'image': self.fig_to_base64(fig),
            'caption': 'Common geometric shapes'
        }
    
    def create_angles_visual(self) -> Dict:
        """Create visual of different angles"""
        fig, ax = plt.subplots(figsize=(12, 8))
        
        angles = [
            ('Acute (45°)', 45, (2, 5)),
            ('Right (90°)', 90, (6, 5)),
            ('Obtuse (120°)', 120, (10, 5)),
            ('Straight (180°)', 180, (4, 2))
        ]
        
        for name, angle, pos in angles:
            x, y = pos
            
            # Draw angle
            line1 = np.array([[x, x+2], [y, y]])
            line2_x = x + 2*np.cos(np.radians(angle))
            line2_y = y + 2*np.sin(np.radians(angle))
            line2 = np.array([[x, line2_x], [y, line2_y]])
            
            ax.plot(line1[0], line1[1], 'b-', linewidth=3)
            ax.plot(line2[0], line2[1], 'r-', linewidth=3)
            
            # Arc
            arc = patches.Arc((x, y), 1, 1, angle=0, theta1=0, theta2=angle,
                            color=self.colors['primary'][0], linewidth=2)
            ax.add_patch(arc)
            
            # Label
            ax.text(x, y-0.5, name, ha='center', fontsize=12, weight='bold')
        
        ax.set_xlim(0, 14)
        ax.set_ylim(0, 8)
        ax.set_aspect('equal')
        ax.axis('off')
        ax.set_title('Types of Angles', fontsize=24, weight='bold', pad=20)
        
        return {
            'type': 'angles',
            'image': self.fig_to_base64(fig),
            'caption': 'Different types of angles'
        }
    
    def create_number_line(self, start: int, end: int) -> Dict:
        """Create number line visual"""
        fig, ax = plt.subplots(figsize=(14, 3))
        
        # Draw line
        ax.plot([start, end], [0, 0], 'k-', linewidth=3)
        
        # Add ticks and numbers
        for i in range(start, end + 1):
            ax.plot([i, i], [-0.1, 0.1], 'k-', linewidth=2)
            ax.text(i, -0.4, str(i), ha='center', fontsize=12, weight='bold')
        
        # Highlight some numbers
        highlights = [start + (end-start)//4, start + (end-start)//2, start + 3*(end-start)//4]
        for h in highlights:
            if start <= h <= end:
                circle = Circle((h, 0), 0.3, facecolor=self.colors['primary'][0], 
                              edgecolor='black', linewidth=2, zorder=5)
                ax.add_patch(circle)
        
        ax.set_xlim(start-1, end+1)
        ax.set_ylim(-1, 1)
        ax.axis('off')
        ax.set_title(f'Number Line: {start} to {end}', fontsize=20, weight='bold', pad=20)
        
        return {
            'type': 'number_line',
            'image': self.fig_to_base64(fig),
            'caption': f'Number line from {start} to {end}'
        }
    
    def create_multiplication_array(self, rows: int, cols: int) -> Dict:
        """Create multiplication array visual"""
        fig, ax = plt.subplots(figsize=(10, 8))
        
        # Draw array of dots
        for i in range(rows):
            for j in range(cols):
                circle = Circle((j, rows-1-i), 0.3, 
                              facecolor=self.colors['primary'][i % len(self.colors['primary'])],
                              edgecolor='black', linewidth=2)
                ax.add_patch(circle)
        
        # Add labels
        ax.text(cols/2 - 0.5, -1, f'{rows} rows', ha='center', fontsize=16, weight='bold')
        ax.text(-1, rows/2 - 0.5, f'{cols} columns', ha='center', fontsize=16, weight='bold', rotation=90)
        ax.text(cols/2 - 0.5, rows + 0.5, f'{rows} × {cols} = {rows*cols}', 
               ha='center', fontsize=24, weight='bold')
        
        ax.set_xlim(-2, cols+1)
        ax.set_ylim(-2, rows+1)
        ax.set_aspect('equal')
        ax.axis('off')
        
        return {
            'type': 'multiplication_array',
            'image': self.fig_to_base64(fig),
            'caption': f'Array showing {rows} × {cols} = {rows*cols}'
        }
    
    def create_coordinate_plane(self) -> Dict:
        """Create coordinate plane"""
        fig, ax = plt.subplots(figsize=(10, 10))
        
        # Draw axes
        ax.axhline(y=0, color='k', linewidth=2)
        ax.axvline(x=0, color='k', linewidth=2)
        
        # Grid
        ax.grid(True, alpha=0.3)
        
        # Plot some points
        points = [(2, 3), (-3, 2), (4, -2), (-2, -3)]
        colors = self.colors['primary']
        
        for i, (x, y) in enumerate(points):
            ax.plot(x, y, 'o', color=colors[i % len(colors)], markersize=15)
            ax.text(x+0.3, y+0.3, f'({x}, {y})', fontsize=12, weight='bold')
        
        ax.set_xlim(-5, 5)
        ax.set_ylim(-5, 5)
        ax.set_xlabel('X-axis', fontsize=14, weight='bold')
        ax.set_ylabel('Y-axis', fontsize=14, weight='bold')
        ax.set_title('Coordinate Plane', fontsize=20, weight='bold', pad=20)
        ax.set_aspect('equal')
        
        return {
            'type': 'coordinate_plane',
            'image': self.fig_to_base64(fig),
            'caption': 'Coordinate plane with example points'
        }
    
    def create_science_diagrams(self, topic: str, lesson_id: int) -> List[Dict]:
        """Create science-specific diagrams"""
        diagrams = []
        
        topic_lower = topic.lower()
        
        if 'cell' in topic_lower:
            diagrams.append(self.create_cell_diagram())
        elif 'photosynthesis' in topic_lower or 'plant' in topic_lower:
            diagrams.append(self.create_photosynthesis_diagram())
        elif 'water cycle' in topic_lower:
            diagrams.append(self.create_water_cycle())
        elif 'solar system' in topic_lower or 'planet' in topic_lower:
            diagrams.append(self.create_solar_system())
        
        return diagrams
    
    def create_cell_diagram(self) -> Dict:
        """Create simple cell diagram"""
        fig, ax = plt.subplots(figsize=(10, 10))
        
        # Cell membrane
        cell = Circle((5, 5), 4, facecolor='#E8F4F8', edgecolor='black', linewidth=3)
        ax.add_patch(cell)
        
        # Nucleus
        nucleus = Circle((5, 5), 1.5, facecolor='#FFE4E1', edgecolor='black', linewidth=2)
        ax.add_patch(nucleus)
        ax.text(5, 5, 'Nucleus', ha='center', va='center', fontsize=10, weight='bold')
        
        # Mitochondria
        for i, pos in enumerate([(3, 3), (7, 7), (3, 7)]):
            mito = patches.Ellipse(pos, 0.8, 0.4, facecolor=self.colors['primary'][i], 
                                  edgecolor='black', linewidth=1)
            ax.add_patch(mito)
        
        ax.text(3, 2.5, 'Mitochondria', fontsize=9)
        
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        ax.set_aspect('equal')
        ax.axis('off')
        ax.set_title('Simple Cell Diagram', fontsize=20, weight='bold', pad=20)
        
        return {
            'type': 'cell',
            'image': self.fig_to_base64(fig),
            'caption': 'Basic parts of a cell'
        }
    
    def create_photosynthesis_diagram(self) -> Dict:
        """Create photosynthesis diagram"""
        fig, ax = plt.subplots(figsize=(12, 8))
        
        # Sun
        sun = Circle((2, 6), 0.8, facecolor='#FFD700', edgecolor='orange', linewidth=3)
        ax.add_patch(sun)
        ax.text(2, 7.2, '☀️ Sunlight', ha='center', fontsize=12, weight='bold')
        
        # Leaf
        leaf = patches.Ellipse((6, 4), 3, 2, facecolor='#90EE90', edgecolor='green', linewidth=3)
        ax.add_patch(leaf)
        ax.text(6, 4, 'LEAF', ha='center', va='center', fontsize=14, weight='bold')
        
        # Arrows
        ax.annotate('', xy=(5, 5), xytext=(3, 6),
                   arrowprops=dict(arrowstyle='->', lw=3, color='orange'))
        ax.text(4, 5.8, 'Energy', fontsize=10)
        
        # CO2 in
        ax.text(2, 3, 'CO₂', fontsize=16, weight='bold')
        ax.annotate('', xy=(4.5, 3.5), xytext=(2.5, 3),
                   arrowprops=dict(arrowstyle='->', lw=3, color='blue'))
        
        # O2 out
        ax.annotate('', xy=(9, 5), xytext=(7.5, 4.5),
                   arrowprops=dict(arrowstyle='->', lw=3, color='green'))
        ax.text(9.5, 5, 'O₂', fontsize=16, weight='bold')
        
        # Glucose
        ax.text(6, 2, '🍬 Glucose\n(Sugar/Food)', ha='center', fontsize=12, weight='bold')
        
        ax.set_xlim(0, 12)
        ax.set_ylim(0, 8)
        ax.axis('off')
        ax.set_title('Photosynthesis Process', fontsize=20, weight='bold', pad=20)
        
        return {
            'type': 'photosynthesis',
            'image': self.fig_to_base64(fig),
            'caption': 'How plants make food from sunlight'
        }
    
    def create_water_cycle(self) -> Dict:
        """Create water cycle diagram"""
        fig, ax = plt.subplots(figsize=(14, 10))
        
        # Ocean
        ocean = Rectangle((0, 0), 6, 2, facecolor='#4682B4', alpha=0.6)
        ax.add_patch(ocean)
        ax.text(3, 1, 'OCEAN', ha='center', va='center', fontsize=16, weight='bold', color='white')
        
        # Mountain/Cloud
        ax.plot([8, 10, 12], [2, 5, 2], 'k-', linewidth=3)
        ax.fill([8, 10, 12], [2, 5, 2], color='#8B4513', alpha=0.4)
        
        # Clouds
        for x in [4, 8, 11]:
            cloud = Circle((x, 7), 0.7, facecolor='lightgray', alpha=0.8)
            ax.add_patch(cloud)
        
        # Arrows
        ax.annotate('Evaporation', xy=(3.5, 6.5), xytext=(2, 3),
                   arrowprops=dict(arrowstyle='->', lw=3, color='red'),
                   fontsize=12, weight='bold')
        
        ax.annotate('Precipitation', xy=(10, 2.5), xytext=(10, 6),
                   arrowprops=dict(arrowstyle='->', lw=3, color='blue'),
                   fontsize=12, weight='bold')
        
        ax.set_xlim(0, 14)
        ax.set_ylim(0, 9)
        ax.axis('off')
        ax.set_title('The Water Cycle', fontsize=24, weight='bold', pad=20)
        
        return {
            'type': 'water_cycle',
            'image': self.fig_to_base64(fig),
            'caption': 'How water moves through our environment'
        }
    
    def create_solar_system(self) -> Dict:
        """Create solar system diagram"""
        fig, ax = plt.subplots(figsize=(16, 10))
        
        # Sun
        sun = Circle((2, 5), 1, facecolor='#FFD700', edgecolor='orange', linewidth=3)
        ax.add_patch(sun)
        ax.text(2, 3.5, 'Sun', ha='center', fontsize=12, weight='bold')
        
        # Planets
        planets = [
            ('Mercury', 4, 0.2, '#A9A9A9'),
            ('Venus', 5.5, 0.3, '#FFA500'),
            ('Earth', 7, 0.35, '#4169E1'),
            ('Mars', 8.5, 0.25, '#CD5C5C'),
            ('Jupiter', 10.5, 0.6, '#DAA520'),
            ('Saturn', 12.5, 0.5, '#F4A460'),
            ('Uranus', 14, 0.4, '#87CEEB'),
            ('Neptune', 15.5, 0.4, '#4682B4')
        ]
        
        for name, x, size, color in planets:
            planet = Circle((x, 5), size, facecolor=color, edgecolor='black', linewidth=2)
            ax.add_patch(planet)
            ax.text(x, 3, name, ha='center', fontsize=8, weight='bold')
        
        ax.set_xlim(0, 17)
        ax.set_ylim(2, 8)
        ax.axis('off')
        ax.set_title('Our Solar System', fontsize=24, weight='bold', pad=20)
        
        return {
            'type': 'solar_system',
            'image': self.fig_to_base64(fig),
            'caption': 'The planets in our solar system'
        }
    
    def create_step_illustration(self, step: Dict, step_num: int, subject: str) -> Dict:
        """Create illustration for a teaching step"""
        fig, ax = plt.subplots(figsize=(10, 6))
        
        # Step number badge
        circle = Circle((1, 5), 0.8, facecolor=self.colors['primary'][step_num % len(self.colors['primary'])],
                       edgecolor='black', linewidth=3)
        ax.add_patch(circle)
        ax.text(1, 5, str(step_num + 1), ha='center', va='center', 
               fontsize=32, weight='bold', color='white')
        
        # Step content box
        rect = FancyBboxPatch((2.5, 3.5), 6.5, 3,
                             boxstyle="round,pad=0.1",
                             facecolor='lightyellow', alpha=0.8,
                             edgecolor=self.colors['primary'][step_num % len(self.colors['primary'])],
                             linewidth=3)
        ax.add_patch(rect)
        
        # Step title
        title = step.get('title', f'Step {step_num + 1}')
        ax.text(5.75, 5.5, title, ha='center', fontsize=14, weight='bold', wrap=True)
        
        # Add icon based on subject
        icons = {'math': '📐', 'science': '🔬', 'english': '📖', 'social': '🌍'}
        icon = next((v for k, v in icons.items() if k in subject.lower()), '💡')
        ax.text(8.5, 5, icon, fontsize=48, ha='center', va='center')
        
        ax.set_xlim(0, 10)
        ax.set_ylim(2, 7)
        ax.axis('off')
        
        return {
            'step': step_num + 1,
            'image': self.fig_to_base64(fig),
            'caption': title
        }
    
    def fig_to_base64(self, fig) -> str:
        """Convert matplotlib figure to base64 string"""
        buf = io.BytesIO()
        fig.savefig(buf, format='png', dpi=100, bbox_inches='tight', 
                   facecolor='white', edgecolor='none')
        buf.seek(0)
        img_base64 = base64.b64encode(buf.read()).decode('utf-8')
        plt.close(fig)
        return f'data:image/png;base64,{img_base64}'


# Global instance
visual_generator = VisualContentGenerator()


def generate_lesson_visuals(lesson_data: Dict) -> Dict:
    """Quick function to generate all visuals for a lesson"""
    return visual_generator.generate_visual_for_lesson(lesson_data)

