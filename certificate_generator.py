"""
Certificate Generator using ReportLab
Creates beautiful printable achievement certificates
"""

import os
from datetime import datetime
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont


class CertificateGenerator:
    """Generate beautiful PDF certificates for achievements"""

    def __init__(self):
        self.output_dir = "certificates"
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def generate_certificate(
        self, student_name: str, achievement_name: str, date: str = None
    ) -> str:
        """Generate a certificate PDF"""
        if date is None:
            date = datetime.now().strftime("%B %d, %Y")

        # Create filename
        filename = f"{student_name.replace(' ', '_')}_{achievement_name.replace(' ', '_')}_{datetime.now().strftime('%Y%m%d')}.pdf"
        filepath = os.path.join(self.output_dir, filename)

        # Create PDF
        c = canvas.Canvas(filepath, pagesize=landscape(letter))
        width, height = landscape(letter)

        # Background
        c.setFillColor(colors.HexColor("#f0f3ff"))
        c.rect(0, 0, width, height, fill=True, stroke=False)

        # Border
        c.setStrokeColor(colors.HexColor("#667eea"))
        c.setLineWidth(10)
        c.rect(20, 20, width - 40, height - 40, fill=False, stroke=True)

        # Inner border
        c.setStrokeColor(colors.HexColor("#764ba2"))
        c.setLineWidth(2)
        c.rect(30, 30, width - 60, height - 60, fill=False, stroke=True)

        # Title
        c.setFillColor(colors.HexColor("#667eea"))
        c.setFont("Helvetica-Bold", 48)
        c.drawCentredString(width / 2, height - 100, "CERTIFICATE OF ACHIEVEMENT")

        # Star decorations
        c.setFillColor(colors.HexColor("#ffd700"))
        c.setFont("Helvetica", 60)
        c.drawString(100, height - 110, "⭐")
        c.drawString(width - 150, height - 110, "⭐")

        # "This certifies that"
        c.setFillColor(colors.HexColor("#333333"))
        c.setFont("Helvetica", 24)
        c.drawCentredString(width / 2, height - 180, "This certifies that")

        # Student Name
        c.setFillColor(colors.HexColor("#667eea"))
        c.setFont("Helvetica-Bold", 42)
        c.drawCentredString(width / 2, height - 240, student_name)

        # Line under name
        c.setStrokeColor(colors.HexColor("#667eea"))
        c.setLineWidth(2)
        c.line(width / 2 - 200, height - 250, width / 2 + 200, height - 250)

        # "has successfully completed"
        c.setFillColor(colors.HexColor("#333333"))
        c.setFont("Helvetica", 24)
        c.drawCentredString(width / 2, height - 300, "has successfully completed")

        # Achievement Name
        c.setFillColor(colors.HexColor("#764ba2"))
        c.setFont("Helvetica-Bold", 36)
        # Handle long achievement names
        if len(achievement_name) > 40:
            # Split into two lines
            words = achievement_name.split()
            mid = len(words) // 2
            line1 = " ".join(words[:mid])
            line2 = " ".join(words[mid:])
            c.drawCentredString(width / 2, height - 360, line1)
            c.drawCentredString(width / 2, height - 400, line2)
            current_y = height - 440
        else:
            c.drawCentredString(width / 2, height - 370, achievement_name)
            current_y = height - 410

        # Congratulatory message
        c.setFillColor(colors.HexColor("#666666"))
        c.setFont("Helvetica-Oblique", 18)
        c.drawCentredString(
            width / 2,
            current_y - 30,
            "Demonstrating dedication, perseverance, and excellence in learning!",
        )

        # Date
        c.setFillColor(colors.HexColor("#333333"))
        c.setFont("Helvetica", 20)
        c.drawCentredString(width / 2, 120, f"Date: {date}")

        # Signature lines
        c.setStrokeColor(colors.HexColor("#333333"))
        c.setLineWidth(1)
        # Left signature line
        c.line(100, 90, 300, 90)
        c.setFont("Helvetica", 14)
        c.drawCentredString(200, 70, "Parent/Guardian")

        # Right signature line
        c.line(width - 300, 90, width - 100, 90)
        c.drawCentredString(width - 200, 70, "Ultimate Tutor")

        # Bottom decoration
        c.setFillColor(colors.HexColor("#667eea"))
        c.setFont("Helvetica", 48)
        c.drawString(width / 2 - 100, 20, "🎓")
        c.drawString(width / 2 + 70, 20, "🏆")

        # Save PDF
        c.save()

        return filepath

    def generate_mastery_certificate(
        self, student_name: str, subject: str, topics_mastered: int, date: str = None
    ) -> str:
        """Generate a subject mastery certificate"""
        if date is None:
            date = datetime.now().strftime("%B %d, %Y")

        filename = f"{student_name.replace(' ', '_')}_{subject}_Mastery_{datetime.now().strftime('%Y%m%d')}.pdf"
        filepath = os.path.join(self.output_dir, filename)

        c = canvas.Canvas(filepath, pagesize=landscape(letter))
        width, height = landscape(letter)

        # Gold gradient background
        c.setFillColor(colors.HexColor("#fff9e6"))
        c.rect(0, 0, width, height, fill=True, stroke=False)

        # Border
        c.setStrokeColor(colors.HexColor("#ffd700"))
        c.setLineWidth(15)
        c.rect(15, 15, width - 30, height - 30, fill=False, stroke=True)

        # Title
        c.setFillColor(colors.HexColor("#d4af37"))
        c.setFont("Helvetica-Bold", 52)
        c.drawCentredString(width / 2, height - 100, "🏆 MASTERY ACHIEVED 🏆")

        # Student name
        c.setFillColor(colors.HexColor("#333333"))
        c.setFont("Helvetica", 24)
        c.drawCentredString(width / 2, height - 180, "Presented to")

        c.setFillColor(colors.HexColor("#d4af37"))
        c.setFont("Helvetica-Bold", 44)
        c.drawCentredString(width / 2, height - 240, student_name)

        # Achievement
        c.setFillColor(colors.HexColor("#333333"))
        c.setFont("Helvetica", 28)
        c.drawCentredString(
            width / 2, height - 310, f"for mastering {topics_mastered} topics in"
        )

        c.setFillColor(colors.HexColor("#d4af37"))
        c.setFont("Helvetica-Bold", 40)
        c.drawCentredString(width / 2, height - 370, subject.upper())

        # Congratulations
        c.setFillColor(colors.HexColor("#666666"))
        c.setFont("Helvetica-Oblique", 20)
        c.drawCentredString(
            width / 2,
            height - 430,
            "Outstanding dedication and excellence in learning!",
        )

        # Date
        c.setFillColor(colors.HexColor("#333333"))
        c.setFont("Helvetica-Bold", 22)
        c.drawCentredString(width / 2, 100, date)

        # Signature line
        c.setStrokeColor(colors.HexColor("#333333"))
        c.line(width / 2 - 150, 60, width / 2 + 150, 60)
        c.setFont("Helvetica", 14)
        c.drawCentredString(width / 2, 40, "Parent/Guardian Signature")

        c.save()
        return filepath

    def generate_sister_quest_certificate(
        self,
        student1_name: str,
        student2_name: str,
        quest_name: str,
        date: str = None,
    ) -> str:
        """Generate a certificate for completing a sister quest together"""
        if date is None:
            date = datetime.now().strftime("%B %d, %Y")

        filename = f"Sister_Quest_{quest_name.replace(' ', '_')}_{datetime.now().strftime('%Y%m%d')}.pdf"
        filepath = os.path.join(self.output_dir, filename)

        c = canvas.Canvas(filepath, pagesize=landscape(letter))
        width, height = landscape(letter)

        # Background
        c.setFillColor(colors.HexColor("#ffe6f0"))
        c.rect(0, 0, width, height, fill=True, stroke=False)

        # Border
        c.setStrokeColor(colors.HexColor("#ff69b4"))
        c.setLineWidth(12)
        c.rect(20, 20, width - 40, height - 40, fill=False, stroke=True)

        # Title
        c.setFillColor(colors.HexColor("#ff1493"))
        c.setFont("Helvetica-Bold", 48)
        c.drawCentredString(width / 2, height - 100, "👭 SISTER QUEST COMPLETED! 👭")

        # Quest name
        c.setFillColor(colors.HexColor("#333333"))
        c.setFont("Helvetica-Bold", 36)
        c.drawCentredString(width / 2, height - 170, quest_name)

        # Completed by
        c.setFont("Helvetica", 24)
        c.drawCentredString(width / 2, height - 240, "Successfully completed by")

        # Both names
        c.setFillColor(colors.HexColor("#ff1493"))
        c.setFont("Helvetica-Bold", 38)
        c.drawCentredString(width / 2, height - 300, f"{student1_name} & {student2_name}")

        # Teamwork message
        c.setFillColor(colors.HexColor("#666666"))
        c.setFont("Helvetica-Oblique", 22)
        c.drawCentredString(
            width / 2,
            height - 370,
            "Working together, learning together, growing together!",
        )

        # Special message
        c.setFillColor(colors.HexColor("#ff69b4"))
        c.setFont("Helvetica-Bold", 28)
        c.drawCentredString(width / 2, height - 430, "⭐ TEAMWORK MAKES THE DREAM WORK! ⭐")

        # Date
        c.setFillColor(colors.HexColor("#333333"))
        c.setFont("Helvetica", 20)
        c.drawCentredString(width / 2, 100, f"Completed on: {date}")

        c.save()
        return filepath


# Global instance
certificate_generator = CertificateGenerator()


def generate_certificate(student_name: str, achievement_id: str) -> str:
    """Helper function to generate a certificate"""
    return certificate_generator.generate_certificate(student_name, achievement_id)


if __name__ == "__main__":
    # Test certificate generation
    gen = CertificateGenerator()

    print("Testing certificate generation...")

    # Test achievement certificate
    cert1 = gen.generate_certificate("Emily Johnson", "Complete 10 Math Lessons")
    print(f"✅ Generated: {cert1}")

    # Test mastery certificate
    cert2 = gen.generate_mastery_certificate("Sarah Johnson", "Mathematics", 15)
    print(f"✅ Generated: {cert2}")

    # Test sister quest certificate
    cert3 = gen.generate_sister_quest_certificate(
        "Emily Johnson", "Sarah Johnson", "The Great Salt Lake Ecosystem Project"
    )
    print(f"✅ Generated: {cert3}")

    print("\n✨ All certificates generated successfully!")
    print(f"📁 Check the '{gen.output_dir}' folder")

