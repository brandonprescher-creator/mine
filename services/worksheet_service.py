"""
Worksheet Generation Service
Generates PDF worksheets and quizzes
"""

from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib import colors
from io import BytesIO
from datetime import datetime
import random


class WorksheetGenerator:
    """Generate professional worksheets and quizzes"""
    
    def __init__(self):
        self.styles = getSampleStyleSheet()
        self._setup_custom_styles()
    
    def _setup_custom_styles(self):
        """Setup custom paragraph styles"""
        self.styles.add(ParagraphStyle(
            name='CustomTitle',
            parent=self.styles['Heading1'],
            fontSize=24,
            textColor=colors.HexColor('#0ea5e9'),
            spaceAfter=30,
            alignment=TA_CENTER
        ))
        
        self.styles.add(ParagraphStyle(
            name='CustomHeading',
            parent=self.styles['Heading2'],
            fontSize=16,
            textColor=colors.HexColor('#38bdf8'),
            spaceAfter=12,
            spaceBefore=12
        ))
        
        self.styles.add(ParagraphStyle(
            name='Question',
            parent=self.styles['Normal'],
            fontSize=12,
            spaceAfter=20,
            spaceBefore=10
        ))
    
    def generate_math_worksheet(self, topic, grade_level, num_problems=20):
        """Generate a math worksheet"""
        buffer = BytesIO()
        doc = SimpleDocTemplate(buffer, pagesize=letter)
        story = []
        
        # Title
        title = Paragraph(f"{topic} Worksheet", self.styles['CustomTitle'])
        story.append(title)
        
        # Header info
        header_data = [
            ['Name: _______________', f'Date: {datetime.now().strftime("%m/%d/%Y")}'],
            ['Grade: ' + str(grade_level), 'Score: _____/' + str(num_problems)]
        ]
        header_table = Table(header_data, colWidths=[3*inch, 3*inch])
        header_table.setStyle(TableStyle([
            ('FONTSIZE', (0, 0), (-1, -1), 10),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 10),
        ]))
        story.append(header_table)
        story.append(Spacer(1, 20))
        
        # Instructions
        instructions = Paragraph(
            "<b>Instructions:</b> Solve each problem. Show your work in the space provided.",
            self.styles['Normal']
        )
        story.append(instructions)
        story.append(Spacer(1, 20))
        
        # Generate problems based on topic
        problems = self._generate_math_problems(topic, num_problems)
        
        for i, problem in enumerate(problems, 1):
            question = Paragraph(f"<b>{i}.</b> {problem['question']}", self.styles['Question'])
            story.append(question)
            story.append(Spacer(1, 40))  # Space for answer
        
        # Answer key on new page
        story.append(PageBreak())
        story.append(Paragraph("Answer Key", self.styles['CustomTitle']))
        story.append(Spacer(1, 20))
        
        for i, problem in enumerate(problems, 1):
            answer = Paragraph(
                f"<b>{i}.</b> {problem['answer']}",
                self.styles['Normal']
            )
            story.append(answer)
            story.append(Spacer(1, 10))
        
        # Build PDF
        doc.build(story)
        buffer.seek(0)
        return buffer
    
    def generate_quiz(self, topic, questions, num_questions=10):
        """Generate a multiple choice quiz"""
        buffer = BytesIO()
        doc = SimpleDocTemplate(buffer, pagesize=letter)
        story = []
        
        # Title
        title = Paragraph(f"{topic} Quiz", self.styles['CustomTitle'])
        story.append(title)
        
        # Header
        header_data = [
            ['Name: _______________', f'Date: {datetime.now().strftime("%m/%d/%Y")}'],
            ['Time Limit: 20 minutes', 'Score: _____/' + str(num_questions)]
        ]
        header_table = Table(header_data, colWidths=[3*inch, 3*inch])
        header_table.setStyle(TableStyle([
            ('FONTSIZE', (0, 0), (-1, -1), 10),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 10),
        ]))
        story.append(header_table)
        story.append(Spacer(1, 20))
        
        # Instructions
        instructions = Paragraph(
            "<b>Instructions:</b> Circle the letter of the correct answer for each question.",
            self.styles['Normal']
        )
        story.append(instructions)
        story.append(Spacer(1, 20))
        
        # Questions
        selected_questions = random.sample(questions, min(num_questions, len(questions)))
        
        for i, q in enumerate(selected_questions, 1):
            question = Paragraph(f"<b>{i}.</b> {q['question']}", self.styles['Question'])
            story.append(question)
            
            for letter, choice in zip(['A', 'B', 'C', 'D'], q.get('choices', [])):
                choice_text = Paragraph(f"&nbsp;&nbsp;&nbsp;&nbsp;{letter}. {choice}", self.styles['Normal'])
                story.append(choice_text)
                story.append(Spacer(1, 5))
            
            story.append(Spacer(1, 15))
        
        # Answer key on new page
        story.append(PageBreak())
        story.append(Paragraph("Answer Key", self.styles['CustomTitle']))
        story.append(Spacer(1, 20))
        
        for i, q in enumerate(selected_questions, 1):
            answer = Paragraph(
                f"<b>{i}.</b> {q['answer']} - {q.get('explanation', '')}",
                self.styles['Normal']
            )
            story.append(answer)
            story.append(Spacer(1, 10))
        
        # Build PDF
        doc.build(story)
        buffer.seek(0)
        return buffer
    
    def _generate_math_problems(self, topic, num_problems):
        """Generate math problems based on topic"""
        problems = []
        
        if 'addition' in topic.lower():
            for _ in range(num_problems):
                a, b = random.randint(1, 100), random.randint(1, 100)
                problems.append({
                    'question': f"{a} + {b} = _____",
                    'answer': str(a + b)
                })
        
        elif 'subtraction' in topic.lower():
            for _ in range(num_problems):
                a, b = random.randint(50, 100), random.randint(1, 49)
                problems.append({
                    'question': f"{a} - {b} = _____",
                    'answer': str(a - b)
                })
        
        elif 'multiplication' in topic.lower():
            for _ in range(num_problems):
                a, b = random.randint(1, 12), random.randint(1, 12)
                problems.append({
                    'question': f"{a} × {b} = _____",
                    'answer': str(a * b)
                })
        
        elif 'division' in topic.lower():
            for _ in range(num_problems):
                b = random.randint(2, 12)
                result = random.randint(1, 12)
                a = b * result
                problems.append({
                    'question': f"{a} ÷ {b} = _____",
                    'answer': str(result)
                })
        
        else:
            # Generic problems
            for i in range(num_problems):
                problems.append({
                    'question': f"Solve problem #{i+1}",
                    'answer': "Answer will vary"
                })
        
        return problems
    
    def generate_study_guide(self, topic, content):
        """Generate a study guide"""
        buffer = BytesIO()
        doc = SimpleDocTemplate(buffer, pagesize=letter)
        story = []
        
        # Title
        title = Paragraph(f"{topic} Study Guide", self.styles['CustomTitle'])
        story.append(title)
        story.append(Spacer(1, 30))
        
        # Content sections
        for section in content.get('sections', []):
            heading = Paragraph(section['title'], self.styles['CustomHeading'])
            story.append(heading)
            
            body = Paragraph(section['content'], self.styles['Normal'])
            story.append(body)
            story.append(Spacer(1, 20))
        
        # Key terms
        if content.get('key_terms'):
            story.append(Paragraph("Key Terms", self.styles['CustomHeading']))
            
            terms_data = [[term, definition] for term, definition in content['key_terms'].items()]
            terms_table = Table(terms_data, colWidths=[2*inch, 4*inch])
            terms_table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#0ea5e9')),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, 0), 12),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                ('GRID', (0, 0), (-1, -1), 1, colors.black)
            ]))
            story.append(terms_table)
        
        # Build PDF
        doc.build(story)
        buffer.seek(0)
        return buffer


# Global instance
worksheet_generator = WorksheetGenerator()
