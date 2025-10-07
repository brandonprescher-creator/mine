import re
from typing import Dict, List, Tuple

def analyze_content(text: str) -> Dict:
    """Analyze extracted text to determine topic and structure."""
    # Simple keyword-based analysis
    text_lower = text.lower()
    
    # Detect subject
    subject = "General"
    if any(word in text_lower for word in ['math', 'equation', 'algebra', 'geometry', 'calculate', 'number', 'division', 'multiplication']):
        subject = "Mathematics"
    elif any(word in text_lower for word in ['science', 'experiment', 'hypothesis', 'cell', 'atom', 'energy', 'matter']):
        subject = "Science"
    elif any(word in text_lower for word in ['reading', 'writing', 'grammar', 'sentence', 'paragraph', 'essay', 'vocabulary']):
        subject = "English Language Arts"
    elif any(word in text_lower for word in ['history', 'geography', 'government', 'civics', 'culture', 'society']):
        subject = "Social Studies"
    
    # Extract potential title (first non-empty line or first sentence)
    lines = [line.strip() for line in text.split('\n') if line.strip()]
    title = lines[0] if lines else "Untitled Lesson"
    if len(title) > 100:
        # If first line is too long, take first sentence
        sentences = re.split(r'[.!?]', text)
        title = sentences[0][:100] if sentences else title[:100]
    
    return {
        'subject': subject,
        'title': title,
        'word_count': len(text.split())
    }

def generate_lesson_from_text(text: str, custom_title: str = None) -> Dict:
    """
    Generate a lesson structure from extracted text.
    Returns a dictionary with title, description, steps, and examples.
    """
    analysis = analyze_content(text)
    
    # Split text into paragraphs
    paragraphs = [p.strip() for p in text.split('\n\n') if p.strip()]
    
    # Generate title
    title = custom_title if custom_title else analysis['title']
    
    # Generate description (first paragraph or first 200 chars)
    description = paragraphs[0] if paragraphs else text[:200]
    if len(description) > 300:
        description = description[:297] + "..."
    
    # Generate teaching steps (split content into numbered steps)
    steps = []
    
    # Look for existing numbered steps in the text
    numbered_pattern = r'(?:^|\n)\s*(?:\d+[\.\):]|Step\s+\d+)'
    if re.search(numbered_pattern, text, re.IGNORECASE):
        # Text already has numbered steps
        parts = re.split(numbered_pattern, text, flags=re.IGNORECASE)
        for part in parts[1:]:  # Skip first empty part
            step_text = part.strip()
            if step_text and len(step_text) > 10:
                steps.append(step_text[:500])  # Limit step length
    else:
        # Create steps from paragraphs
        for i, para in enumerate(paragraphs[:8], 1):  # Max 8 steps
            if len(para) > 20:  # Skip very short paragraphs
                steps.append(para[:500])
    
    # If no steps found, split text into chunks
    if not steps:
        words = text.split()
        chunk_size = len(words) // 5  # Aim for 5 steps
        if chunk_size < 20:
            chunk_size = 20
        
        for i in range(0, min(len(words), 500), chunk_size):
            chunk = ' '.join(words[i:i+chunk_size])
            if chunk:
                steps.append(chunk)
    
    # Generate a worked example (look for example keywords or use a paragraph)
    examples = []
    example_pattern = r'(?:example|for instance|for example)[:\s]+([^\.]+(?:\.[^\.]+){0,3}\.)'
    example_matches = re.finditer(example_pattern, text, re.IGNORECASE)
    
    for match in list(example_matches)[:2]:  # Max 2 examples
        examples.append({
            'title': 'Example',
            'content': match.group(1).strip()
        })
    
    # If no examples found, create a generic one
    if not examples and len(paragraphs) > 2:
        examples.append({
            'title': 'Example',
            'content': paragraphs[1][:300] if len(paragraphs) > 1 else "Practice the concepts explained above."
        })
    
    return {
        'title': title,
        'description': description,
        'steps': steps[:10],  # Max 10 steps
        'examples': examples,
        'subject': analysis['subject'],
        'source_text': text[:1000]  # Keep first 1000 chars for reference
    }

def generate_practice_problems(text: str, lesson_title: str, count: int = 5) -> List[Dict]:
    """
    Generate practice problems based on lesson content.
    Returns a list of problem dictionaries.
    """
    problems = []
    
    # Check if text contains questions
    question_pattern = r'([^\n]*\?)'
    questions = re.findall(question_pattern, text)
    
    if questions:
        for q in questions[:count]:
            if len(q.strip()) > 10:
                problems.append({
                    'question': q.strip(),
                    'answer': "Check your work with your teacher or use the lesson content above.",
                    'steps': [
                        "Review the lesson content carefully.",
                        "Identify the key concepts needed.",
                        "Apply the method step by step.",
                        "Check your answer."
                    ],
                    'hints': ["Review the lesson examples", "Break the problem into smaller steps"]
                })
    
    # Generate generic practice problems if none found
    if len(problems) < count:
        for i in range(count - len(problems)):
            problems.append({
                'question': f"Practice Question {i+1}: Apply the concepts from '{lesson_title}' to solve a similar problem.",
                'answer': "Work through this problem using the steps taught in the lesson.",
                'steps': [
                    "Read the question carefully.",
                    "Identify what you're being asked to find.",
                    "Apply the lesson method.",
                    "Show your work clearly.",
                    "Check your answer makes sense."
                ],
                'hints': [
                    "Look at the worked examples in the lesson",
                    "Follow each step carefully",
                    "Don't skip steps - write everything out"
                ]
            })
    
    return problems[:count]

def smart_split_content(text: str, max_length: int = 2000) -> List[str]:
    """Split long content into manageable chunks for lesson creation."""
    if len(text) <= max_length:
        return [text]
    
    chunks = []
    paragraphs = text.split('\n\n')
    current_chunk = ""
    
    for para in paragraphs:
        if len(current_chunk) + len(para) <= max_length:
            current_chunk += para + "\n\n"
        else:
            if current_chunk:
                chunks.append(current_chunk.strip())
            current_chunk = para + "\n\n"
    
    if current_chunk:
        chunks.append(current_chunk.strip())
    
    return chunks

