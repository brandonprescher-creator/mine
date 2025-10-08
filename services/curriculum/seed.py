"""
Database Seeding
Create initial data for demo and testing
"""
from models.database import db, User, ChildProfile, Standard, Skill, Resource
from datetime import date


def seed_database():
    """Seed database with initial data"""
    
    # Check if already seeded
    if User.query.first():
        print("Database already seeded")
        return
    
    print("Seeding database...")
    
    # Create demo parent
    parent = User(email='parent@demo.com', role='parent')
    parent.set_password('demo123')
    db.session.add(parent)
    db.session.flush()
    
    # Create demo student
    child = ChildProfile(
        user_id=parent.id,
        name='Alex Demo',
        username='alex',
        grade=3
    )
    child.set_password('demo123')
    child.accommodations = {}
    child.prefs = {'interests': ['space', 'animals', 'art']}
    db.session.add(child)
    
    # Seed standards - Grade 3 Math
    math_standards = [
        ('CCSS.MATH.3.OA.A.1', 'Multiplication basics', 'Understand multiplication as repeated addition'),
        ('CCSS.MATH.3.OA.A.2', 'Division basics', 'Understand division as partitioning'),
        ('CCSS.MATH.3.NBT.A.1', 'Place value', 'Understand place value to 1000'),
        ('CCSS.MATH.3.NF.A.1', 'Fractions intro', 'Understand fractions as parts of a whole'),
        ('CCSS.MATH.3.MD.A.1', 'Time', 'Tell and write time to the nearest minute')
    ]
    
    for code, name, desc in math_standards:
        standard = Standard(
            subject='Math',
            grade=3,
            code=code,
            name=name,
            description=desc
        )
        db.session.add(standard)
        db.session.flush()
        
        # Add skills for this standard
        skill = Skill(
            standard_id=standard.id,
            name=name,
            difficulty='medium'
        )
        skill.tags = [subject.lower() for subject in ['math', 'grade3']]
        db.session.add(skill)
    
    # Seed standards - Grade 3 ELA
    ela_standards = [
        ('CCSS.ELA.3.RL.1', 'Ask and answer questions', 'Refer explicitly to text'),
        ('CCSS.ELA.3.RL.2', 'Main idea', 'Determine central message or lesson'),
        ('CCSS.ELA.3.W.1', 'Opinion writing', 'Write opinion pieces'),
        ('CCSS.ELA.3.W.2', 'Informative writing', 'Write informative/explanatory texts'),
        ('CCSS.ELA.3.L.1', 'Grammar', 'Demonstrate command of conventions')
    ]
    
    for code, name, desc in ela_standards:
        standard = Standard(
            subject='English Language Arts',
            grade=3,
            code=code,
            name=name,
            description=desc
        )
        db.session.add(standard)
        db.session.flush()
        
        skill = Skill(
            standard_id=standard.id,
            name=name,
            difficulty='medium'
        )
        skill.tags = ['ela', 'grade3', 'reading' if 'RL' in code else 'writing']
        db.session.add(skill)
    
    # Seed some resources
    resources = [
        ('Introduction to Multiplication', 'https://www.khanacademy.org/math/multiplication', 'Math', 'Khan Academy', 'video', 15),
        ('Fractions for Kids', 'https://www.mathsisfun.com/fractions.html', 'Math', 'Math is Fun', 'article', 10),
        ('Solar System Overview', 'https://solarsystem.nasa.gov/', 'Science', 'NASA', 'interactive', 20),
        ('Grammar Basics', 'https://www.grammarly.com/blog/grammar/', 'English Language Arts', 'Grammarly', 'article', 12),
        ('US Geography', 'https://www.nationalgeographic.org/encyclopedia/united-states/', 'Social Studies', 'Nat Geo', 'article', 15)
    ]
    
    for title, url, subject, provider, media_type, minutes in resources:
        resource = Resource(
            title=title,
            url=url,
            subject=subject,
            grade_band='3-5',
            media_type=media_type,
            length_minutes=minutes,
            provider=provider,
            attribution=f'{provider} educational resource'
        )
        resource.topics = [subject.lower(), 'grade3']
        db.session.add(resource)
    
    db.session.commit()
    print("Database seeded successfully!")
    print("Demo parent: parent@demo.com / demo123")
    print("Demo student: alex / demo123")
