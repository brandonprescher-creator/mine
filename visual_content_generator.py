"""
VISUAL CONTENT GENERATOR
Automatically creates pictures, diagrams, and images for EVERY lesson!
Uses matplotlib, PIL, and SVG to generate educational visuals.
"""

import matplotlib

matplotlib.use("Agg")  # Non-interactive backend
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
        self.output_dir = "static/images/lessons"
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

        # Color schemes for kid-friendly visuals
        self.colors = {
            "primary": ["#FF6B6B", "#4ECDC4", "#45B7D1", "#FFA07A", "#98D8C8"],
            "pastel": ["#FFB6C1", "#FFE4E1", "#E0BBE4", "#D4A5A5", "#A8E6CF"],
            "bright": ["#FF1744", "#00E676", "#2196F3", "#FFEA00", "#FF6E40"],
        }

    def generate_visual_for_lesson(self, lesson_data: Dict) -> Dict:
        """Generate all visuals for a lesson"""
        subject = lesson_data.get("subject", "general")
        topic = lesson_data.get("topic", "")
        lesson_id = lesson_data.get("lesson_id", 0)

        visuals = {
            "header_image": self.create_header_image(topic, subject),
            "concept_diagrams": [],
            "step_illustrations": [],
            "practice_images": [],
        }

        # Generate subject-specific visuals
        if "math" in subject.lower():
            visuals["concept_diagrams"] = self.create_math_diagrams(topic, lesson_id)
        elif "science" in subject.lower():
            visuals["concept_diagrams"] = self.create_science_diagrams(topic, lesson_id)

        # Generate step-by-step illustrations
        steps = lesson_data.get("steps", [])
        for i, step in enumerate(steps[:5]):  # First 5 steps
            visual = self.create_step_illustration(step, i, subject)
            if visual:
                visuals["step_illustrations"].append(visual)

        return visuals

    def create_header_image(self, topic: str, subject: str) -> str:
        """Create colorful header image for lesson"""
        fig, ax = plt.subplots(figsize=(12, 3))

        # Gradient background
        gradient = np.linspace(0, 1, 256).reshape(1, -1)
        gradient = np.vstack((gradient, gradient))

        ax.imshow(gradient, aspect="auto", cmap="rainbow", extent=[0, 12, 0, 3])

        # Add text
        ax.text(
            6,
            1.5,
            topic.upper(),
            fontsize=32,
            weight="bold",
            ha="center",
            va="center",
            color="white",
            bbox=dict(boxstyle="round,pad=0.5", facecolor="black", alpha=0.5),
        )

        # Subject emoji
        emojis = {"math": "📐", "science": "🔬", "english": "📖", "social": "🌍"}
        emoji = next((v for k, v in emojis.items() if k in subject.lower()), "📚")
        ax.text(1, 1.5, emoji, fontsize=48, ha="center", va="center")

        ax.axis("off")

        # Save to base64
        return self.fig_to_base64(fig)

    def create_math_diagrams(self, topic: str, lesson_id: int) -> List[Dict]:
        """Create math-specific diagrams"""
        diagrams = []

        topic_lower = topic.lower()

        # Division visuals
        if "division" in topic_lower:
            diagrams.append(self.create_division_visual(24, 6))
            diagrams.append(self.create_division_visual(48, 8))

        # Fraction visuals
        elif "fraction" in topic_lower:
            diagrams.append(self.create_fraction_visual(1, 2))
            diagrams.append(self.create_fraction_visual(3, 4))
            diagrams.append(self.create_fraction_visual(2, 3))

        # Geometry visuals
        elif "geometry" in topic_lower or "shape" in topic_lower:
            diagrams.append(self.create_shapes_visual())
            diagrams.append(self.create_angles_visual())

        # Number line
        elif "number" in topic_lower or "counting" in topic_lower:
            diagrams.append(self.create_number_line(0, 20))

        # Multiplication array
        elif "multiplication" in topic_lower:
            diagrams.append(self.create_multiplication_array(4, 5))
            diagrams.append(self.create_multiplication_array(3, 6))

        # Graph/coordinate plane
        elif "graph" in topic_lower or "coordinate" in topic_lower:
            diagrams.append(self.create_coordinate_plane())

        return diagrams

    def create_division_visual(self, dividend: int, divisor: int) -> Dict:
        """Create visual representation of division"""
        fig, ax = plt.subplots(figsize=(10, 6))

        quotient = dividend // divisor
        remainder = dividend % divisor

        # Draw groups
        colors = self.colors["primary"]
        for i in range(divisor):
            color = colors[i % len(colors)]

            # Calculate position
            x = (i % 4) * 2.5
            y = (i // 4) * 2

            # Draw group box
            rect = FancyBboxPatch(
                (x, y),
                2,
                1.5,
                boxstyle="round,pad=0.1",
                facecolor=color,
                alpha=0.3,
                edgecolor=color,
                linewidth=3,
            )
            ax.add_patch(rect)

            # Add items in group
            for j in range(quotient):
                circle = Circle(
                    (x + 0.3 + j * 0.4, y + 0.75),
                    0.15,
                    facecolor=color,
                    edgecolor="black",
                    linewidth=2,
                )
                ax.add_patch(circle)

            # Group label
            ax.text(
                x + 1, y - 0.3, f"Group {i+1}", ha="center", fontsize=10, weight="bold"
            )

        # Title
        ax.text(
            5,
            8.5,
            f"{dividend} ÷ {divisor} = {quotient}"
            + (f" remainder {remainder}" if remainder else ""),
            fontsize=20,
            weight="bold",
            ha="center",
        )

        ax.set_xlim(-0.5, 10)
        ax.set_ylim(-1, 9)
        ax.axis("off")

        return {
            "type": "division",
            "image": self.fig_to_base64(fig),
            "caption": f"Visual representation: {dividend} items divided into {divisor} groups of {quotient}",
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
            color = self.colors["primary"][0] if i < numerator else "#E0E0E0"
            alpha = 0.8 if i < numerator else 0.3

            wedge = Wedge(
                center,
                radius,
                start_angle,
                end_angle,
                facecolor=color,
                edgecolor="black",
                linewidth=3,
                alpha=alpha,
            )
            ax.add_patch(wedge)

        # Add fraction text
        ax.text(
            0,
            -4.5,
            f"{numerator}/{denominator}",
            fontsize=40,
            weight="bold",
            ha="center",
            va="center",
        )

        ax.set_xlim(-4, 4)
        ax.set_ylim(-5, 4)
        ax.set_aspect("equal")
        ax.axis("off")

        return {
            "type": "fraction",
            "image": self.fig_to_base64(fig),
            "caption": f"{numerator} out of {denominator} parts shaded",
        }

    def create_shapes_visual(self) -> Dict:
        """Create visual of basic shapes"""
        fig, ax = plt.subplots(figsize=(12, 8))

        shapes = [
            (
                "Circle",
                Circle((2, 6), 1.5, facecolor=self.colors["primary"][0], alpha=0.6),
            ),
            (
                "Square",
                Rectangle(
                    (5, 4.5), 3, 3, facecolor=self.colors["primary"][1], alpha=0.6
                ),
            ),
            (
                "Triangle",
                Polygon(
                    [(10, 4.5), (11.5, 7.5), (13, 4.5)],
                    facecolor=self.colors["primary"][2],
                    alpha=0.6,
                ),
            ),
            (
                "Rectangle",
                Rectangle((1, 1), 4, 2, facecolor=self.colors["primary"][3], alpha=0.6),
            ),
            (
                "Pentagon",
                Polygon(
                    [(7, 2), (8.5, 3), (8, 4.5), (6, 4.5), (5.5, 3)],
                    facecolor=self.colors["primary"][4],
                    alpha=0.6,
                ),
            ),
        ]

        for name, shape in shapes:
            ax.add_patch(shape)
            # Add label
            if hasattr(shape, "center"):
                x, y = shape.center
            else:
                x, y = shape.get_xy()
                x += shape.get_width() / 2 if hasattr(shape, "get_width") else 0
                y -= 0.5

            ax.text(x, y - 0.3, name, ha="center", fontsize=14, weight="bold")

        ax.set_xlim(0, 14)
        ax.set_ylim(0, 8)
        ax.set_aspect("equal")
        ax.axis("off")
        ax.set_title("Basic Shapes", fontsize=24, weight="bold", pad=20)

        return {
            "type": "shapes",
            "image": self.fig_to_base64(fig),
            "caption": "Common geometric shapes",
        }

    def create_angles_visual(self) -> Dict:
        """Create visual of different angles"""
        fig, ax = plt.subplots(figsize=(12, 8))

        angles = [
            ("Acute (45°)", 45, (2, 5)),
            ("Right (90°)", 90, (6, 5)),
            ("Obtuse (120°)", 120, (10, 5)),
            ("Straight (180°)", 180, (4, 2)),
        ]

        for name, angle, pos in angles:
            x, y = pos

            # Draw angle
            line1 = np.array([[x, x + 2], [y, y]])
            line2_x = x + 2 * np.cos(np.radians(angle))
            line2_y = y + 2 * np.sin(np.radians(angle))
            line2 = np.array([[x, line2_x], [y, line2_y]])

            ax.plot(line1[0], line1[1], "b-", linewidth=3)
            ax.plot(line2[0], line2[1], "r-", linewidth=3)

            # Arc
            arc = patches.Arc(
                (x, y),
                1,
                1,
                angle=0,
                theta1=0,
                theta2=angle,
                color=self.colors["primary"][0],
                linewidth=2,
            )
            ax.add_patch(arc)

            # Label
            ax.text(x, y - 0.5, name, ha="center", fontsize=12, weight="bold")

        ax.set_xlim(0, 14)
        ax.set_ylim(0, 8)
        ax.set_aspect("equal")
        ax.axis("off")
        ax.set_title("Types of Angles", fontsize=24, weight="bold", pad=20)

        return {
            "type": "angles",
            "image": self.fig_to_base64(fig),
            "caption": "Different types of angles",
        }

    def create_number_line(self, start: int, end: int) -> Dict:
        """Create number line visual"""
        fig, ax = plt.subplots(figsize=(14, 3))

        # Draw line
        ax.plot([start, end], [0, 0], "k-", linewidth=3)

        # Add ticks and numbers
        for i in range(start, end + 1):
            ax.plot([i, i], [-0.1, 0.1], "k-", linewidth=2)
            ax.text(i, -0.4, str(i), ha="center", fontsize=12, weight="bold")

        # Highlight some numbers
        highlights = [
            start + (end - start) // 4,
            start + (end - start) // 2,
            start + 3 * (end - start) // 4,
        ]
        for h in highlights:
            if start <= h <= end:
                circle = Circle(
                    (h, 0),
                    0.3,
                    facecolor=self.colors["primary"][0],
                    edgecolor="black",
                    linewidth=2,
                    zorder=5,
                )
                ax.add_patch(circle)

        ax.set_xlim(start - 1, end + 1)
        ax.set_ylim(-1, 1)
        ax.axis("off")
        ax.set_title(
            f"Number Line: {start} to {end}", fontsize=20, weight="bold", pad=20
        )

        return {
            "type": "number_line",
            "image": self.fig_to_base64(fig),
            "caption": f"Number line from {start} to {end}",
        }

    def create_multiplication_array(self, rows: int, cols: int) -> Dict:
        """Create multiplication array visual"""
        fig, ax = plt.subplots(figsize=(10, 8))

        # Draw array of dots
        for i in range(rows):
            for j in range(cols):
                circle = Circle(
                    (j, rows - 1 - i),
                    0.3,
                    facecolor=self.colors["primary"][i % len(self.colors["primary"])],
                    edgecolor="black",
                    linewidth=2,
                )
                ax.add_patch(circle)

        # Add labels
        ax.text(
            cols / 2 - 0.5, -1, f"{rows} rows", ha="center", fontsize=16, weight="bold"
        )
        ax.text(
            -1,
            rows / 2 - 0.5,
            f"{cols} columns",
            ha="center",
            fontsize=16,
            weight="bold",
            rotation=90,
        )
        ax.text(
            cols / 2 - 0.5,
            rows + 0.5,
            f"{rows} × {cols} = {rows*cols}",
            ha="center",
            fontsize=24,
            weight="bold",
        )

        ax.set_xlim(-2, cols + 1)
        ax.set_ylim(-2, rows + 1)
        ax.set_aspect("equal")
        ax.axis("off")

        return {
            "type": "multiplication_array",
            "image": self.fig_to_base64(fig),
            "caption": f"Array showing {rows} × {cols} = {rows*cols}",
        }

    def create_coordinate_plane(self) -> Dict:
        """Create coordinate plane"""
        fig, ax = plt.subplots(figsize=(10, 10))

        # Draw axes
        ax.axhline(y=0, color="k", linewidth=2)
        ax.axvline(x=0, color="k", linewidth=2)

        # Grid
        ax.grid(True, alpha=0.3)

        # Plot some points
        points = [(2, 3), (-3, 2), (4, -2), (-2, -3)]
        colors = self.colors["primary"]

        for i, (x, y) in enumerate(points):
            ax.plot(x, y, "o", color=colors[i % len(colors)], markersize=15)
            ax.text(x + 0.3, y + 0.3, f"({x}, {y})", fontsize=12, weight="bold")

        ax.set_xlim(-5, 5)
        ax.set_ylim(-5, 5)
        ax.set_xlabel("X-axis", fontsize=14, weight="bold")
        ax.set_ylabel("Y-axis", fontsize=14, weight="bold")
        ax.set_title("Coordinate Plane", fontsize=20, weight="bold", pad=20)
        ax.set_aspect("equal")

        return {
            "type": "coordinate_plane",
            "image": self.fig_to_base64(fig),
            "caption": "Coordinate plane with example points",
        }

    def create_science_diagrams(self, topic: str, lesson_id: int) -> List[Dict]:
        """Create science-specific diagrams"""
        diagrams = []

        topic_lower = topic.lower()

        if "cell" in topic_lower:
            diagrams.append(self.create_cell_diagram())
        elif "photosynthesis" in topic_lower or "plant" in topic_lower:
            diagrams.append(self.create_photosynthesis_diagram())
        elif "water cycle" in topic_lower:
            diagrams.append(self.create_water_cycle())
        elif "solar system" in topic_lower or "planet" in topic_lower:
            diagrams.append(self.create_solar_system())

        return diagrams

    def create_cell_diagram(self) -> Dict:
        """Create simple cell diagram"""
        fig, ax = plt.subplots(figsize=(10, 10))

        # Cell membrane
        cell = Circle((5, 5), 4, facecolor="#E8F4F8", edgecolor="black", linewidth=3)
        ax.add_patch(cell)

        # Nucleus
        nucleus = Circle(
            (5, 5), 1.5, facecolor="#FFE4E1", edgecolor="black", linewidth=2
        )
        ax.add_patch(nucleus)
        ax.text(5, 5, "Nucleus", ha="center", va="center", fontsize=10, weight="bold")

        # Mitochondria
        for i, pos in enumerate([(3, 3), (7, 7), (3, 7)]):
            mito = patches.Ellipse(
                pos,
                0.8,
                0.4,
                facecolor=self.colors["primary"][i],
                edgecolor="black",
                linewidth=1,
            )
            ax.add_patch(mito)

        ax.text(3, 2.5, "Mitochondria", fontsize=9)

        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        ax.set_aspect("equal")
        ax.axis("off")
        ax.set_title("Simple Cell Diagram", fontsize=20, weight="bold", pad=20)

        return {
            "type": "cell",
            "image": self.fig_to_base64(fig),
            "caption": "Basic parts of a cell",
        }

    def create_photosynthesis_diagram(self) -> Dict:
        """Create photosynthesis diagram"""
        fig, ax = plt.subplots(figsize=(12, 8))

        # Sun
        sun = Circle((2, 6), 0.8, facecolor="#FFD700", edgecolor="orange", linewidth=3)
        ax.add_patch(sun)
        ax.text(2, 7.2, "☀️ Sunlight", ha="center", fontsize=12, weight="bold")

        # Leaf
        leaf = patches.Ellipse(
            (6, 4), 3, 2, facecolor="#90EE90", edgecolor="green", linewidth=3
        )
        ax.add_patch(leaf)
        ax.text(6, 4, "LEAF", ha="center", va="center", fontsize=14, weight="bold")

        # Arrows
        ax.annotate(
            "",
            xy=(5, 5),
            xytext=(3, 6),
            arrowprops=dict(arrowstyle="->", lw=3, color="orange"),
        )
        ax.text(4, 5.8, "Energy", fontsize=10)

        # CO2 in
        ax.text(2, 3, "CO₂", fontsize=16, weight="bold")
        ax.annotate(
            "",
            xy=(4.5, 3.5),
            xytext=(2.5, 3),
            arrowprops=dict(arrowstyle="->", lw=3, color="blue"),
        )

        # O2 out
        ax.annotate(
            "",
            xy=(9, 5),
            xytext=(7.5, 4.5),
            arrowprops=dict(arrowstyle="->", lw=3, color="green"),
        )
        ax.text(9.5, 5, "O₂", fontsize=16, weight="bold")

        # Glucose
        ax.text(
            6, 2, "🍬 Glucose\n(Sugar/Food)", ha="center", fontsize=12, weight="bold"
        )

        ax.set_xlim(0, 12)
        ax.set_ylim(0, 8)
        ax.axis("off")
        ax.set_title("Photosynthesis Process", fontsize=20, weight="bold", pad=20)

        return {
            "type": "photosynthesis",
            "image": self.fig_to_base64(fig),
            "caption": "How plants make food from sunlight",
        }

    def create_water_cycle(self) -> Dict:
        """Create water cycle diagram"""
        fig, ax = plt.subplots(figsize=(14, 10))

        # Ocean
        ocean = Rectangle((0, 0), 6, 2, facecolor="#4682B4", alpha=0.6)
        ax.add_patch(ocean)
        ax.text(
            3,
            1,
            "OCEAN",
            ha="center",
            va="center",
            fontsize=16,
            weight="bold",
            color="white",
        )

        # Mountain/Cloud
        ax.plot([8, 10, 12], [2, 5, 2], "k-", linewidth=3)
        ax.fill([8, 10, 12], [2, 5, 2], color="#8B4513", alpha=0.4)

        # Clouds
        for x in [4, 8, 11]:
            cloud = Circle((x, 7), 0.7, facecolor="lightgray", alpha=0.8)
            ax.add_patch(cloud)

        # Arrows
        ax.annotate(
            "Evaporation",
            xy=(3.5, 6.5),
            xytext=(2, 3),
            arrowprops=dict(arrowstyle="->", lw=3, color="red"),
            fontsize=12,
            weight="bold",
        )

        ax.annotate(
            "Precipitation",
            xy=(10, 2.5),
            xytext=(10, 6),
            arrowprops=dict(arrowstyle="->", lw=3, color="blue"),
            fontsize=12,
            weight="bold",
        )

        ax.set_xlim(0, 14)
        ax.set_ylim(0, 9)
        ax.axis("off")
        ax.set_title("The Water Cycle", fontsize=24, weight="bold", pad=20)

        return {
            "type": "water_cycle",
            "image": self.fig_to_base64(fig),
            "caption": "How water moves through our environment",
        }

    def create_solar_system(self) -> Dict:
        """Create solar system diagram"""
        fig, ax = plt.subplots(figsize=(16, 10))

        # Sun
        sun = Circle((2, 5), 1, facecolor="#FFD700", edgecolor="orange", linewidth=3)
        ax.add_patch(sun)
        ax.text(2, 3.5, "Sun", ha="center", fontsize=12, weight="bold")

        # Planets
        planets = [
            ("Mercury", 4, 0.2, "#A9A9A9"),
            ("Venus", 5.5, 0.3, "#FFA500"),
            ("Earth", 7, 0.35, "#4169E1"),
            ("Mars", 8.5, 0.25, "#CD5C5C"),
            ("Jupiter", 10.5, 0.6, "#DAA520"),
            ("Saturn", 12.5, 0.5, "#F4A460"),
            ("Uranus", 14, 0.4, "#87CEEB"),
            ("Neptune", 15.5, 0.4, "#4682B4"),
        ]

        for name, x, size, color in planets:
            planet = Circle(
                (x, 5), size, facecolor=color, edgecolor="black", linewidth=2
            )
            ax.add_patch(planet)
            ax.text(x, 3, name, ha="center", fontsize=8, weight="bold")

        ax.set_xlim(0, 17)
        ax.set_ylim(2, 8)
        ax.axis("off")
        ax.set_title("Our Solar System", fontsize=24, weight="bold", pad=20)

        return {
            "type": "solar_system",
            "image": self.fig_to_base64(fig),
            "caption": "The planets in our solar system",
        }

    def create_step_illustration(self, step: Dict, step_num: int, subject: str) -> Dict:
        """Create illustration for a teaching step"""
        fig, ax = plt.subplots(figsize=(10, 6))

        # Step number badge
        circle = Circle(
            (1, 5),
            0.8,
            facecolor=self.colors["primary"][step_num % len(self.colors["primary"])],
            edgecolor="black",
            linewidth=3,
        )
        ax.add_patch(circle)
        ax.text(
            1,
            5,
            str(step_num + 1),
            ha="center",
            va="center",
            fontsize=32,
            weight="bold",
            color="white",
        )

        # Step content box
        rect = FancyBboxPatch(
            (2.5, 3.5),
            6.5,
            3,
            boxstyle="round,pad=0.1",
            facecolor="lightyellow",
            alpha=0.8,
            edgecolor=self.colors["primary"][step_num % len(self.colors["primary"])],
            linewidth=3,
        )
        ax.add_patch(rect)

        # Step title
        title = step.get("title", f"Step {step_num + 1}")
        ax.text(5.75, 5.5, title, ha="center", fontsize=14, weight="bold", wrap=True)

        # Add icon based on subject
        icons = {"math": "📐", "science": "🔬", "english": "📖", "social": "🌍"}
        icon = next((v for k, v in icons.items() if k in subject.lower()), "💡")
        ax.text(8.5, 5, icon, fontsize=48, ha="center", va="center")

        ax.set_xlim(0, 10)
        ax.set_ylim(2, 7)
        ax.axis("off")

        return {
            "step": step_num + 1,
            "image": self.fig_to_base64(fig),
            "caption": title,
        }

    def fig_to_base64(self, fig) -> str:
        """Convert matplotlib figure to base64 string"""
        buf = io.BytesIO()
        fig.savefig(
            buf,
            format="png",
            dpi=100,
            bbox_inches="tight",
            facecolor="white",
            edgecolor="none",
        )
        buf.seek(0)
        img_base64 = base64.b64encode(buf.read()).decode("utf-8")
        plt.close(fig)
        return f"data:image/png;base64,{img_base64}"


# Global instance
visual_generator = VisualContentGenerator()


def generate_visual_content(lesson_data: Dict) -> Dict:
    """Backward-compatible alias for visual generation helper."""
    return visual_generator.generate_visual_for_lesson(lesson_data)


def generate_lesson_visuals(lesson_data: Dict) -> Dict:
    """Quick function to generate all visuals for a lesson"""
    try:
        return visual_generator.generate_visual_for_lesson(lesson_data)
    except Exception as e:
        print(f"Visual generation error: {e}")
        # Return simple fallback visuals
        return create_simple_visuals(lesson_data)

def create_simple_visuals(lesson_data: Dict) -> Dict:
    """Create simple but effective visuals when full generation fails"""
    lesson_title = lesson_data.get('title', '').lower()
    subject = lesson_data.get('subject_name', '').lower()
    
    visuals = []
    
    # Math visuals
    if 'math' in subject or any(word in lesson_title for word in ['division', 'fraction', 'multiplication', 'addition', 'subtraction', 'geometry', 'shape']):
        if 'division' in lesson_title:
            visuals.append(create_division_visual())
        elif 'fraction' in lesson_title:
            visuals.append(create_fraction_visual())
        elif 'multiplication' in lesson_title or 'times' in lesson_title:
            visuals.append(create_multiplication_visual())
        elif 'addition' in lesson_title or 'add' in lesson_title:
            visuals.append(create_addition_visual())
        elif 'geometry' in lesson_title or 'shape' in lesson_title:
            visuals.append(create_geometry_visual())
        else:
            visuals.append(create_math_general_visual())
    
    # Science visuals
    elif 'science' in subject:
        visuals.append(create_science_visual(lesson_title))
    
    # ELA visuals
    elif 'english' in subject or 'language' in subject:
        visuals.append(create_ela_visual(lesson_title))
    
    # Default visual
    if not visuals:
        visuals.append(create_general_visual(lesson_data))
    
    return {
        "success": True,
        "visuals": visuals
    }

def create_division_visual() -> Dict:
    """Create a simple division visual"""
    return {
        "type": "division",
        "title": "Division Visual",
        "description": "See how division works with groups!",
        "svg": """
        <svg width="400" height="300" xmlns="http://www.w3.org/2000/svg">
            <rect width="400" height="300" fill="#f0f8ff"/>
            <text x="200" y="30" text-anchor="middle" font-size="24" font-weight="bold" fill="#333">12 ÷ 3 = ?</text>
            
            <!-- Original group -->
            <text x="50" y="80" font-size="16" fill="#666">12 items:</text>
            <g transform="translate(50, 100)">
                <circle cx="0" cy="0" r="8" fill="#ff6b6b"/>
                <circle cx="25" cy="0" r="8" fill="#4ecdc4"/>
                <circle cx="50" cy="0" r="8" fill="#45b7d1"/>
                <circle cx="75" cy="0" r="8" fill="#ffa07a"/>
                <circle cx="100" cy="0" r="8" fill="#98d8c8"/>
                <circle cx="125" cy="0" r="8" fill="#ff6b6b"/>
                <circle cx="150" cy="0" r="8" fill="#4ecdc4"/>
                <circle cx="175" cy="0" r="8" fill="#45b7d1"/>
                <circle cx="200" cy="0" r="8" fill="#ffa07a"/>
                <circle cx="225" cy="0" r="8" fill="#98d8c8"/>
                <circle cx="250" cy="0" r="8" fill="#ff6b6b"/>
                <circle cx="275" cy="0" r="8" fill="#4ecdc4"/>
            </g>
            
            <!-- Arrow -->
            <path d="M 200 130 L 200 150" stroke="#333" stroke-width="3" marker-end="url(#arrowhead)"/>
            <defs>
                <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
                    <polygon points="0 0, 10 3.5, 0 7" fill="#333"/>
                </marker>
            </defs>
            
            <!-- 3 groups -->
            <text x="200" y="180" text-anchor="middle" font-size="16" fill="#666">Split into 3 groups:</text>
            
            <!-- Group 1 -->
            <text x="80" y="220" text-anchor="middle" font-size="14" fill="#333">Group 1</text>
            <g transform="translate(50, 240)">
                <circle cx="0" cy="0" r="8" fill="#ff6b6b"/>
                <circle cx="20" cy="0" r="8" fill="#4ecdc4"/>
                <circle cx="40" cy="0" r="8" fill="#45b7d1"/>
                <circle cx="60" cy="0" r="8" fill="#ffa07a"/>
            </g>
            
            <!-- Group 2 -->
            <text x="200" y="220" text-anchor="middle" font-size="14" fill="#333">Group 2</text>
            <g transform="translate(170, 240)">
                <circle cx="0" cy="0" r="8" fill="#98d8c8"/>
                <circle cx="20" cy="0" r="8" fill="#ff6b6b"/>
                <circle cx="40" cy="0" r="8" fill="#4ecdc4"/>
                <circle cx="60" cy="0" r="8" fill="#45b7d1"/>
            </g>
            
            <!-- Group 3 -->
            <text x="320" y="220" text-anchor="middle" font-size="14" fill="#333">Group 3</text>
            <g transform="translate(290, 240)">
                <circle cx="0" cy="0" r="8" fill="#ffa07a"/>
                <circle cx="20" cy="0" r="8" fill="#98d8c8"/>
                <circle cx="40" cy="0" r="8" fill="#ff6b6b"/>
                <circle cx="60" cy="0" r="8" fill="#4ecdc4"/>
            </g>
            
            <text x="200" y="280" text-anchor="middle" font-size="18" font-weight="bold" fill="#28a745">Answer: 4 items per group!</text>
        </svg>
        """,
        "caption": "12 items divided into 3 equal groups = 4 items per group"
    }

def create_fraction_visual() -> Dict:
    """Create a simple fraction visual"""
    return {
        "type": "fraction",
        "title": "Fraction Visual",
        "description": "See fractions as parts of a whole!",
        "svg": """
        <svg width="400" height="300" xmlns="http://www.w3.org/2000/svg">
            <rect width="400" height="300" fill="#fff5f5"/>
            
            <!-- 1/2 -->
            <text x="100" y="30" text-anchor="middle" font-size="20" font-weight="bold" fill="#333">1/2</text>
            <circle cx="100" cy="80" r="40" fill="none" stroke="#333" stroke-width="3"/>
            <path d="M 60 80 L 140 80" stroke="#ff6b6b" stroke-width="4"/>
            <path d="M 100 40 L 100 80" stroke="#ff6b6b" stroke-width="4"/>
            <text x="100" y="140" text-anchor="middle" font-size="14" fill="#666">Half shaded</text>
            
            <!-- 1/4 -->
            <text x="300" y="30" text-anchor="middle" font-size="20" font-weight="bold" fill="#333">1/4</text>
            <circle cx="300" cy="80" r="40" fill="none" stroke="#333" stroke-width="3"/>
            <path d="M 300 40 L 300 80" stroke="#4ecdc4" stroke-width="4"/>
            <path d="M 300 80 L 340 80" stroke="#4ecdc4" stroke-width="4"/>
            <path d="M 300 40 L 340 40" stroke="#4ecdc4" stroke-width="4"/>
            <path d="M 340 40 L 340 80" stroke="#4ecdc4" stroke-width="4"/>
            <text x="300" y="140" text-anchor="middle" font-size="14" fill="#666">Quarter shaded</text>
            
            <!-- 3/4 -->
            <text x="200" y="180" text-anchor="middle" font-size="20" font-weight="bold" fill="#333">3/4</text>
            <circle cx="200" cy="230" r="40" fill="none" stroke="#333" stroke-width="3"/>
            <path d="M 200 190 L 200 230" stroke="#45b7d1" stroke-width="4"/>
            <path d="M 200 230 L 240 230" stroke="#45b7d1" stroke-width="4"/>
            <path d="M 200 190 L 240 190" stroke="#45b7d1" stroke-width="4"/>
            <path d="M 240 190 L 240 230" stroke="#45b7d1" stroke-width="4"/>
            <path d="M 200 190 L 240 230" stroke="#45b7d1" stroke-width="4"/>
            <text x="200" y="290" text-anchor="middle" font-size="14" fill="#666">Three quarters shaded</text>
        </svg>
        """,
        "caption": "Fractions show parts of a whole circle"
    }

def create_multiplication_visual() -> Dict:
    """Create a simple multiplication visual"""
    return {
        "type": "multiplication",
        "title": "Multiplication Visual",
        "description": "See multiplication as arrays!",
        "svg": """
        <svg width="400" height="300" xmlns="http://www.w3.org/2000/svg">
            <rect width="400" height="300" fill="#f0fff0"/>
            <text x="200" y="30" text-anchor="middle" font-size="24" font-weight="bold" fill="#333">3 × 4 = 12</text>
            
            <!-- Array grid -->
            <g transform="translate(150, 80)">
                <!-- Row 1 -->
                <circle cx="0" cy="0" r="12" fill="#ff6b6b"/>
                <circle cx="30" cy="0" r="12" fill="#4ecdc4"/>
                <circle cx="60" cy="0" r="12" fill="#45b7d1"/>
                <circle cx="90" cy="0" r="12" fill="#ffa07a"/>
                
                <!-- Row 2 -->
                <circle cx="0" cy="30" r="12" fill="#98d8c8"/>
                <circle cx="30" cy="30" r="12" fill="#ff6b6b"/>
                <circle cx="60" cy="30" r="12" fill="#4ecdc4"/>
                <circle cx="90" cy="30" r="12" fill="#45b7d1"/>
                
                <!-- Row 3 -->
                <circle cx="0" cy="60" r="12" fill="#ffa07a"/>
                <circle cx="30" cy="60" r="12" fill="#98d8c8"/>
                <circle cx="60" cy="60" r="12" fill="#ff6b6b"/>
                <circle cx="90" cy="60" r="12" fill="#4ecdc4"/>
            </g>
            
            <!-- Labels -->
            <text x="120" y="110" font-size="16" fill="#666">3 rows</text>
            <text x="280" y="110" font-size="16" fill="#666">4 columns</text>
            
            <text x="200" y="180" text-anchor="middle" font-size="18" font-weight="bold" fill="#28a745">3 rows × 4 columns = 12 total!</text>
            
            <!-- Count animation -->
            <text x="200" y="220" text-anchor="middle" font-size="14" fill="#666">Count all the circles: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12</text>
        </svg>
        """,
        "caption": "3 rows of 4 items = 12 total items"
    }

def create_addition_visual() -> Dict:
    """Create a simple addition visual"""
    return {
        "type": "addition",
        "title": "Addition Visual",
        "description": "See addition on a number line!",
        "svg": """
        <svg width="400" height="200" xmlns="http://www.w3.org/2000/svg">
            <rect width="400" height="200" fill="#f0f8ff"/>
            <text x="200" y="30" text-anchor="middle" font-size="24" font-weight="bold" fill="#333">5 + 3 = ?</text>
            
            <!-- Number line -->
            <line x1="50" y1="100" x2="350" y2="100" stroke="#333" stroke-width="3"/>
            
            <!-- Numbers -->
            <text x="50" y="120" text-anchor="middle" font-size="16" fill="#333">0</text>
            <text x="80" y="120" text-anchor="middle" font-size="16" fill="#333">1</text>
            <text x="110" y="120" text-anchor="middle" font-size="16" fill="#333">2</text>
            <text x="140" y="120" text-anchor="middle" font-size="16" fill="#333">3</text>
            <text x="170" y="120" text-anchor="middle" font-size="16" fill="#333">4</text>
            <text x="200" y="120" text-anchor="middle" font-size="16" fill="#333">5</text>
            <text x="230" y="120" text-anchor="middle" font-size="16" fill="#333">6</text>
            <text x="260" y="120" text-anchor="middle" font-size="16" fill="#333">7</text>
            <text x="290" y="120" text-anchor="middle" font-size="16" fill="#333">8</text>
            <text x="320" y="120" text-anchor="middle" font-size="16" fill="#333">9</text>
            <text x="350" y="120" text-anchor="middle" font-size="16" fill="#333">10</text>
            
            <!-- Start at 5 -->
            <circle cx="200" cy="100" r="8" fill="#4facfe"/>
            <text x="200" y="80" text-anchor="middle" font-size="14" font-weight="bold" fill="#4facfe">START</text>
            
            <!-- Jump +3 -->
            <path d="M 200 100 L 290 100" stroke="#ff6b6b" stroke-width="4" marker-end="url(#arrow)"/>
            <text x="245" y="85" text-anchor="middle" font-size="14" font-weight="bold" fill="#ff6b6b">+3</text>
            
            <!-- End at 8 -->
            <circle cx="290" cy="100" r="8" fill="#28a745"/>
            <text x="290" y="80" text-anchor="middle" font-size="14" font-weight="bold" fill="#28a745">END</text>
            
            <defs>
                <marker id="arrow" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
                    <polygon points="0 0, 10 3.5, 0 7" fill="#ff6b6b"/>
                </marker>
            </defs>
            
            <text x="200" y="160" text-anchor="middle" font-size="18" font-weight="bold" fill="#28a745">Answer: 5 + 3 = 8</text>
        </svg>
        """,
        "caption": "Start at 5, jump 3 spaces forward = 8"
    }

def create_geometry_visual() -> Dict:
    """Create a simple geometry visual"""
    return {
        "type": "geometry",
        "title": "Geometric Shapes",
        "description": "Learn about different shapes!",
        "svg": """
        <svg width="400" height="300" xmlns="http://www.w3.org/2000/svg">
            <rect width="400" height="300" fill="#fff8f0"/>
            
            <!-- Triangle -->
            <text x="100" y="30" text-anchor="middle" font-size="16" font-weight="bold" fill="#333">Triangle</text>
            <polygon points="100,60 80,100 120,100" fill="#ff6b6b" stroke="#333" stroke-width="2"/>
            <text x="100" y="120" text-anchor="middle" font-size="12" fill="#666">3 sides</text>
            
            <!-- Square -->
            <text x="200" y="30" text-anchor="middle" font-size="16" font-weight="bold" fill="#333">Square</text>
            <rect x="180" y="60" width="40" height="40" fill="#4ecdc4" stroke="#333" stroke-width="2"/>
            <text x="200" y="120" text-anchor="middle" font-size="12" fill="#666">4 equal sides</text>
            
            <!-- Circle -->
            <text x="300" y="30" text-anchor="middle" font-size="16" font-weight="bold" fill="#333">Circle</text>
            <circle cx="300" cy="80" r="20" fill="#45b7d1" stroke="#333" stroke-width="2"/>
            <text x="300" y="120" text-anchor="middle" font-size="12" fill="#666">No sides</text>
            
            <!-- Rectangle -->
            <text x="150" y="180" text-anchor="middle" font-size="16" font-weight="bold" fill="#333">Rectangle</text>
            <rect x="120" y="200" width="60" height="30" fill="#ffa07a" stroke="#333" stroke-width="2"/>
            <text x="150" y="250" text-anchor="middle" font-size="12" fill="#666">4 sides (2 long, 2 short)</text>
            
            <!-- Pentagon -->
            <text x="300" y="180" text-anchor="middle" font-size="16" font-weight="bold" fill="#333">Pentagon</text>
            <polygon points="300,200 315,210 310,225 290,225 285,210" fill="#98d8c8" stroke="#333" stroke-width="2"/>
            <text x="300" y="250" text-anchor="middle" font-size="12" fill="#666">5 sides</text>
        </svg>
        """,
        "caption": "Different shapes have different numbers of sides"
    }

def create_math_general_visual() -> Dict:
    """Create a general math visual"""
    return {
        "type": "math_general",
        "title": "Math Concepts",
        "description": "Explore math concepts visually!",
        "svg": """
        <svg width="400" height="200" xmlns="http://www.w3.org/2000/svg">
            <rect width="400" height="200" fill="#f0f8ff"/>
            <text x="200" y="30" text-anchor="middle" font-size="20" font-weight="bold" fill="#333">Math is Everywhere!</text>
            
            <!-- Math symbols -->
            <text x="100" y="80" font-size="40" fill="#ff6b6b">+</text>
            <text x="150" y="80" font-size="40" fill="#4ecdc4">-</text>
            <text x="200" y="80" font-size="40" fill="#45b7d1">×</text>
            <text x="250" y="80" font-size="40" fill="#ffa07a">÷</text>
            <text x="300" y="80" font-size="40" fill="#98d8c8">=</text>
            
            <text x="200" y="120" text-anchor="middle" font-size="16" fill="#666">Addition, Subtraction, Multiplication, Division</text>
            <text x="200" y="150" text-anchor="middle" font-size="14" fill="#666">All these operations help us solve problems!</text>
        </svg>
        """,
        "caption": "Math operations help us solve problems"
    }

def create_science_visual(lesson_title: str) -> Dict:
    """Create a science visual"""
    return {
        "type": "science",
        "title": "Science Visual",
        "description": "Explore science concepts!",
        "svg": """
        <svg width="400" height="200" xmlns="http://www.w3.org/2000/svg">
            <rect width="400" height="200" fill="#f0fff0"/>
            <text x="200" y="30" text-anchor="middle" font-size="20" font-weight="bold" fill="#333">Science is Amazing!</text>
            
            <!-- Science symbols -->
            <circle cx="100" cy="80" r="15" fill="#ff6b6b"/>
            <text x="100" y="110" text-anchor="middle" font-size="12" fill="#666">Atom</text>
            
            <rect x="150" y="65" width="30" height="30" fill="#4ecdc4"/>
            <text x="165" y="110" text-anchor="middle" font-size="12" fill="#666">Cell</text>
            
            <polygon points="250,65 265,80 250,95 235,80" fill="#45b7d1"/>
            <text x="250" y="110" text-anchor="middle" font-size="12" fill="#666">Crystal</text>
            
            <circle cx="320" cy="80" r="15" fill="#ffa07a"/>
            <text x="320" y="110" text-anchor="middle" font-size="12" fill="#666">Planet</text>
            
            <text x="200" y="140" text-anchor="middle" font-size="14" fill="#666">Science helps us understand the world!</text>
        </svg>
        """,
        "caption": "Science helps us understand the world around us"
    }

def create_ela_visual(lesson_title: str) -> Dict:
    """Create an ELA visual"""
    return {
        "type": "ela",
        "title": "Language Arts Visual",
        "description": "Explore language and reading!",
        "svg": """
        <svg width="400" height="200" xmlns="http://www.w3.org/2000/svg">
            <rect width="400" height="200" fill="#fff8f0"/>
            <text x="200" y="30" text-anchor="middle" font-size="20" font-weight="bold" fill="#333">Language Arts!</text>
            
            <!-- Books -->
            <rect x="80" y="60" width="20" height="30" fill="#ff6b6b"/>
            <rect x="105" y="60" width="20" height="30" fill="#4ecdc4"/>
            <rect x="130" y="60" width="20" height="30" fill="#45b7d1"/>
            
            <!-- Letters -->
            <text x="200" y="80" font-size="30" fill="#ffa07a">A</text>
            <text x="230" y="80" font-size="30" fill="#98d8c8">B</text>
            <text x="260" y="80" font-size="30" fill="#ff6b6b">C</text>
            
            <!-- Words -->
            <text x="200" y="120" text-anchor="middle" font-size="16" fill="#666">Reading • Writing • Speaking</text>
            <text x="200" y="150" text-anchor="middle" font-size="14" fill="#666">Language helps us communicate!</text>
        </svg>
        """,
        "caption": "Language arts help us communicate and express ideas"
    }

def create_general_visual(lesson_data: Dict) -> Dict:
    """Create a general visual for any lesson"""
    title = lesson_data.get('title', 'Learning')
    return {
        "type": "general",
        "title": f"{title} Visual",
        "description": "Visual learning helps you understand better!",
        "svg": """
        <svg width="400" height="200" xmlns="http://www.w3.org/2000/svg">
            <rect width="400" height="200" fill="#f8f9fa"/>
            <text x="200" y="40" text-anchor="middle" font-size="20" font-weight="bold" fill="#333">Learning is Fun!</text>
            
            <!-- Light bulb -->
            <circle cx="200" cy="100" r="25" fill="#ffea00" stroke="#333" stroke-width="2"/>
            <text x="200" y="105" text-anchor="middle" font-size="20" fill="#333">💡</text>
            
            <!-- Stars -->
            <text x="150" y="80" font-size="20" fill="#ff6b6b">⭐</text>
            <text x="250" y="80" font-size="20" fill="#4ecdc4">⭐</text>
            <text x="150" y="130" font-size="20" fill="#45b7d1">⭐</text>
            <text x="250" y="130" font-size="20" fill="#ffa07a">⭐</text>
            
            <text x="200" y="160" text-anchor="middle" font-size="14" fill="#666">Keep learning and exploring!</text>
        </svg>
        """,
        "caption": "Visual learning makes everything easier to understand"
    }
