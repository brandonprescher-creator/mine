"""
PDF Generation Services
Weekly reports, transcripts, worksheets
"""
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
from io import BytesIO
from datetime import datetime


def generate_weekly_report(child, assignments, week_start, week_end):
    """Generate weekly progress report PDF"""
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    story = []
    styles = getSampleStyleSheet()
    
    # Title
    title = Paragraph(f"Weekly Report: {child.name}", styles['Title'])
    story.append(title)
    story.append(Spacer(1, 0.3*inch))
    
    # Header info
    info = Paragraph(f"Week: {week_start.strftime('%m/%d/%Y')} - {week_end.strftime('%m/%d/%Y')}", styles['Normal'])
    story.append(info)
    story.append(Paragraph(f"Grade: {child.grade}", styles['Normal']))
    story.append(Spacer(1, 0.3*inch))
    
    # Summary
    completed = len([a for a in assignments if a.status == 'completed'])
    total = len(assignments)
    
    summary = Paragraph(f"<b>Completed:</b> {completed}/{total} assignments", styles['Normal'])
    story.append(summary)
    story.append(Spacer(1, 0.3*inch))
    
    # Assignments table
    data = [['Subject', 'Date', 'Status', 'Score']]
    
    for assignment in assignments:
        submission = assignment.submissions.first()
        score = submission.score if submission else 'N/A'
        
        data.append([
            assignment.lesson_item.subject if hasattr(assignment, 'lesson_item') and assignment.lesson_item else 'N/A',
            assignment.date.strftime('%m/%d'),
            assignment.status.title(),
            f"{score:.0f}%" if isinstance(score, (int, float)) else str(score)
        ])
    
    table = Table(data)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))
    
    story.append(table)
    
    doc.build(story)
    buffer.seek(0)
    return buffer


def generate_transcript(child, submissions):
    """Generate academic transcript PDF"""
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    story = []
    styles = getSampleStyleSheet()
    
    # Title
    title = Paragraph(f"Academic Transcript: {child.name}", styles['Title'])
    story.append(title)
    story.append(Spacer(1, 0.3*inch))
    
    # Student info
    info = [
        Paragraph(f"<b>Grade:</b> {child.grade}", styles['Normal']),
        Paragraph(f"<b>Generated:</b> {datetime.utcnow().strftime('%m/%d/%Y')}", styles['Normal'])
    ]
    for p in info:
        story.append(p)
    
    story.append(Spacer(1, 0.5*inch))
    
    # Group by subject
    by_subject = {}
    for sub in submissions:
        if hasattr(sub.assignment, 'lesson_item') and sub.assignment.lesson_item:
            subject = sub.assignment.lesson_item.subject
            if subject not in by_subject:
                by_subject[subject] = []
            by_subject[subject].append(sub)
    
    # Add subject sections
    for subject, subs in by_subject.items():
        story.append(Paragraph(f"<b>{subject}</b>", styles['Heading2']))
        
        avg_score = sum(s.score for s in subs if s.score) / len([s for s in subs if s.score]) if any(s.score for s in subs) else 0
        story.append(Paragraph(f"Assignments: {len(subs)} | Average Score: {avg_score:.1f}%", styles['Normal']))
        story.append(Spacer(1, 0.2*inch))
    
    doc.build(story)
    buffer.seek(0)
    return buffer
