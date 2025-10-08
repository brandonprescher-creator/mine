"""
SQLAlchemy Database Models
Complete data model for K-12 homeschool platform
"""
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import json

db = SQLAlchemy()


class User(UserMixin, db.Model):
    """Parent or Admin user"""
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(20), nullable=False, default='parent')  # 'parent', 'admin'
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    last_login = db.Column(db.DateTime)
    
    # Relationships
    children = db.relationship('ChildProfile', backref='parent', lazy='dynamic', cascade='all, delete-orphan')
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def __repr__(self):
        return f'<User {self.email}>'


class ChildProfile(db.Model):
    """Student profile managed by parent"""
    __tablename__ = 'child_profiles'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, index=True)
    name = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(255), nullable=False)
    grade = db.Column(db.Integer, nullable=False)
    accommodations_json = db.Column(db.Text)  # JSON: larger_fonts, dyslexic_font, extra_time, etc.
    prefs_json = db.Column(db.Text)  # JSON: theme, interests, reading_level, etc.
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    lesson_plans = db.relationship('LessonPlan', backref='child', lazy='dynamic', cascade='all, delete-orphan')
    assignments = db.relationship('Assignment', backref='child', lazy='dynamic', cascade='all, delete-orphan')
    submissions = db.relationship('Submission', backref='child', lazy='dynamic', cascade='all, delete-orphan')
    skill_states = db.relationship('SkillState', backref='child', lazy='dynamic', cascade='all, delete-orphan')
    notebook_entries = db.relationship('NotebookEntry', backref='child', lazy='dynamic', cascade='all, delete-orphan')
    portfolio_items = db.relationship('PortfolioItem', backref='child', lazy='dynamic', cascade='all, delete-orphan')
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    @property
    def accommodations(self):
        return json.loads(self.accommodations_json) if self.accommodations_json else {}
    
    @accommodations.setter
    def accommodations(self, value):
        self.accommodations_json = json.dumps(value)
    
    @property
    def prefs(self):
        return json.loads(self.prefs_json) if self.prefs_json else {}
    
    @prefs.setter
    def prefs(self, value):
        self.prefs_json = json.dumps(value)
    
    def __repr__(self):
        return f'<ChildProfile {self.name}>'


class Standard(db.Model):
    """Educational standard (CCSS, NGSS, etc.)"""
    __tablename__ = 'standards'
    
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(50), nullable=False, index=True)
    grade = db.Column(db.Integer, nullable=False, index=True)
    code = db.Column(db.String(100), unique=True, nullable=False)
    name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    
    # Relationships
    skills = db.relationship('Skill', backref='standard', lazy='dynamic', cascade='all, delete-orphan')
    
    def __repr__(self):
        return f'<Standard {self.code}>'


class Skill(db.Model):
    """A specific skill within a standard"""
    __tablename__ = 'skills'
    
    id = db.Column(db.Integer, primary_key=True)
    standard_id = db.Column(db.Integer, db.ForeignKey('standards.id'), nullable=False, index=True)
    name = db.Column(db.String(200), nullable=False)
    tags_json = db.Column(db.Text)  # JSON array
    difficulty = db.Column(db.String(20))  # 'easy', 'medium', 'hard'
    
    # Relationships
    skill_states = db.relationship('SkillState', backref='skill', lazy='dynamic', cascade='all, delete-orphan')
    
    @property
    def tags(self):
        return json.loads(self.tags_json) if self.tags_json else []
    
    @tags.setter
    def tags(self, value):
        self.tags_json = json.dumps(value)
    
    def __repr__(self):
        return f'<Skill {self.name}>'


class LessonPlan(db.Model):
    """Weekly lesson plan for a child"""
    __tablename__ = 'lesson_plans'
    
    id = db.Column(db.Integer, primary_key=True)
    child_id = db.Column(db.Integer, db.ForeignKey('child_profiles.id'), nullable=False, index=True)
    week_start_date = db.Column(db.Date, nullable=False, index=True)
    settings_json = db.Column(db.Text)  # JSON: subjects, minutes_per_subject, etc.
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    lesson_items = db.relationship('LessonItem', backref='lesson_plan', lazy='dynamic', cascade='all, delete-orphan')
    
    @property
    def settings(self):
        return json.loads(self.settings_json) if self.settings_json else {}
    
    @settings.setter
    def settings(self, value):
        self.settings_json = json.dumps(value)
    
    def __repr__(self):
        return f'<LessonPlan child={self.child_id} week={self.week_start_date}>'


class LessonItem(db.Model):
    """A single lesson/activity item in a plan"""
    __tablename__ = 'lesson_items'
    
    id = db.Column(db.Integer, primary_key=True)
    lesson_plan_id = db.Column(db.Integer, db.ForeignKey('lesson_plans.id'), nullable=False, index=True)
    subject = db.Column(db.String(50), nullable=False, index=True)
    type = db.Column(db.String(50), nullable=False)  # 'lesson', 'practice', 'assessment', 'reading', etc.
    skill_ids_json = db.Column(db.Text)  # JSON array of skill IDs
    resource_ids_json = db.Column(db.Text)  # JSON array of resource IDs
    est_minutes = db.Column(db.Integer, default=30)
    order_index = db.Column(db.Integer, default=0)
    
    # Relationships
    assignments = db.relationship('Assignment', backref='lesson_item', lazy='dynamic', cascade='all, delete-orphan')
    
    @property
    def skill_ids(self):
        return json.loads(self.skill_ids_json) if self.skill_ids_json else []
    
    @skill_ids.setter
    def skill_ids(self, value):
        self.skill_ids_json = json.dumps(value)
    
    @property
    def resource_ids(self):
        return json.loads(self.resource_ids_json) if self.resource_ids_json else []
    
    @resource_ids.setter
    def resource_ids(self, value):
        self.resource_ids_json = json.dumps(value)
    
    def __repr__(self):
        return f'<LessonItem {self.subject} {self.type}>'


class Assignment(db.Model):
    """Assignment given to a child for a specific date"""
    __tablename__ = 'assignments'
    
    id = db.Column(db.Integer, primary_key=True)
    child_id = db.Column(db.Integer, db.ForeignKey('child_profiles.id'), nullable=False, index=True)
    lesson_item_id = db.Column(db.Integer, db.ForeignKey('lesson_items.id'), nullable=False, index=True)
    date = db.Column(db.Date, nullable=False, index=True)
    status = db.Column(db.String(20), default='pending')  # 'pending', 'in_progress', 'completed', 'excused'
    started_at = db.Column(db.DateTime)
    completed_at = db.Column(db.DateTime)
    
    # Relationships
    submissions = db.relationship('Submission', backref='assignment', lazy='dynamic', cascade='all, delete-orphan')
    time_entries = db.relationship('TimeOnTask', backref='assignment', lazy='dynamic', cascade='all, delete-orphan')
    
    def __repr__(self):
        return f'<Assignment {self.id} child={self.child_id} date={self.date}>'


class Submission(db.Model):
    """Student work submission"""
    __tablename__ = 'submissions'
    
    id = db.Column(db.Integer, primary_key=True)
    assignment_id = db.Column(db.Integer, db.ForeignKey('assignments.id'), nullable=False, index=True)
    child_id = db.Column(db.Integer, db.ForeignKey('child_profiles.id'), nullable=False, index=True)
    artifacts_json = db.Column(db.Text)  # JSON: photos, text, canvas, audio URLs
    score = db.Column(db.Float)
    rubric_json = db.Column(db.Text)  # JSON: criterion scores
    feedback = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    
    @property
    def artifacts(self):
        return json.loads(self.artifacts_json) if self.artifacts_json else {}
    
    @artifacts.setter
    def artifacts(self, value):
        self.artifacts_json = json.dumps(value)
    
    @property
    def rubric(self):
        return json.loads(self.rubric_json) if self.rubric_json else {}
    
    @rubric.setter
    def rubric(self, value):
        self.rubric_json = json.dumps(value)
    
    def __repr__(self):
        return f'<Submission {self.id}>'


class Assessment(db.Model):
    """Quiz or exam"""
    __tablename__ = 'assessments'
    
    id = db.Column(db.Integer, primary_key=True)
    child_id = db.Column(db.Integer, db.ForeignKey('child_profiles.id'), nullable=False, index=True)
    subject = db.Column(db.String(50), nullable=False)
    items_json = db.Column(db.Text, nullable=False)  # JSON array of questions
    scheduled_for = db.Column(db.DateTime, index=True)
    duration_minutes = db.Column(db.Integer, default=30)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    attempts = db.relationship('AssessmentAttempt', backref='assessment', lazy='dynamic', cascade='all, delete-orphan')
    
    @property
    def items(self):
        return json.loads(self.items_json) if self.items_json else []
    
    @items.setter
    def items(self, value):
        self.items_json = json.dumps(value)
    
    def __repr__(self):
        return f'<Assessment {self.id} {self.subject}>'


class AssessmentAttempt(db.Model):
    """Attempt at an assessment"""
    __tablename__ = 'assessment_attempts'
    
    id = db.Column(db.Integer, primary_key=True)
    assessment_id = db.Column(db.Integer, db.ForeignKey('assessments.id'), nullable=False, index=True)
    child_id = db.Column(db.Integer, db.ForeignKey('child_profiles.id'), nullable=False, index=True)
    responses_json = db.Column(db.Text)  # JSON: {item_id: response}
    score = db.Column(db.Float)
    started_at = db.Column(db.DateTime, default=datetime.utcnow)
    finished_at = db.Column(db.DateTime)
    
    @property
    def responses(self):
        return json.loads(self.responses_json) if self.responses_json else {}
    
    @responses.setter
    def responses(self, value):
        self.responses_json = json.dumps(value)
    
    def __repr__(self):
        return f'<AssessmentAttempt {self.id}>'


class SkillState(db.Model):
    """Mastery tracking for a child's skill"""
    __tablename__ = 'skill_states'
    
    id = db.Column(db.Integer, primary_key=True)
    child_id = db.Column(db.Integer, db.ForeignKey('child_profiles.id'), nullable=False, index=True)
    skill_id = db.Column(db.Integer, db.ForeignKey('skills.id'), nullable=False, index=True)
    level = db.Column(db.Integer, default=0)  # 0-5 mastery levels
    last_practice = db.Column(db.DateTime)
    next_due = db.Column(db.DateTime, index=True)
    evidence_count = db.Column(db.Integer, default=0)
    history_json = db.Column(db.Text)  # JSON: [{date, success, score}, ...]
    
    __table_args__ = (db.UniqueConstraint('child_id', 'skill_id', name='_child_skill_uc'),)
    
    @property
    def history(self):
        return json.loads(self.history_json) if self.history_json else []
    
    @history.setter
    def history(self, value):
        self.history_json = json.dumps(value)
    
    def __repr__(self):
        return f'<SkillState child={self.child_id} skill={self.skill_id} level={self.level}>'


class NotebookEntry(db.Model):
    """Daily notebook entry"""
    __tablename__ = 'notebook_entries'
    
    id = db.Column(db.Integer, primary_key=True)
    child_id = db.Column(db.Integer, db.ForeignKey('child_profiles.id'), nullable=False, index=True)
    date = db.Column(db.Date, nullable=False, index=True)
    content_text = db.Column(db.Text)
    canvas_svg = db.Column(db.Text)
    attachments_json = db.Column(db.Text)  # JSON: [{type, url, caption}, ...]
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    @property
    def attachments(self):
        return json.loads(self.attachments_json) if self.attachments_json else []
    
    @attachments.setter
    def attachments(self, value):
        self.attachments_json = json.dumps(value)
    
    def __repr__(self):
        return f'<NotebookEntry child={self.child_id} date={self.date}>'


class PortfolioItem(db.Model):
    """Best work showcased in portfolio"""
    __tablename__ = 'portfolio_items'
    
    id = db.Column(db.Integer, primary_key=True)
    child_id = db.Column(db.Integer, db.ForeignKey('child_profiles.id'), nullable=False, index=True)
    submission_id = db.Column(db.Integer, db.ForeignKey('submissions.id'), nullable=False, index=True)
    reflection = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    submission = db.relationship('Submission', backref='portfolio_items')
    
    def __repr__(self):
        return f'<PortfolioItem {self.id}>'


class AttendanceLog(db.Model):
    """Daily attendance tracking"""
    __tablename__ = 'attendance_logs'
    
    id = db.Column(db.Integer, primary_key=True)
    child_id = db.Column(db.Integer, db.ForeignKey('child_profiles.id'), nullable=False, index=True)
    date = db.Column(db.Date, nullable=False, index=True)
    minutes = db.Column(db.Integer, default=0)
    status = db.Column(db.String(20), default='present')  # 'present', 'absent', 'half_day', 'holiday'
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    __table_args__ = (db.UniqueConstraint('child_id', 'date', name='_child_date_uc'),)
    
    def __repr__(self):
        return f'<AttendanceLog child={self.child_id} date={self.date}>'


class TimeOnTask(db.Model):
    """Time tracking for assignments"""
    __tablename__ = 'time_on_task'
    
    id = db.Column(db.Integer, primary_key=True)
    child_id = db.Column(db.Integer, db.ForeignKey('child_profiles.id'), nullable=False, index=True)
    assignment_id = db.Column(db.Integer, db.ForeignKey('assignments.id'), nullable=False, index=True)
    seconds_active = db.Column(db.Integer, default=0)
    session_start = db.Column(db.DateTime, default=datetime.utcnow)
    session_end = db.Column(db.DateTime)
    
    def __repr__(self):
        return f'<TimeOnTask assignment={self.assignment_id} seconds={self.seconds_active}>'


class Resource(db.Model):
    """Educational resource from APIs or uploads"""
    __tablename__ = 'resources'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300), nullable=False)
    url = db.Column(db.String(500))
    subject = db.Column(db.String(50), index=True)
    grade_band = db.Column(db.String(20))  # 'K-2', '3-5', '6-8', '9-12'
    topics_json = db.Column(db.Text)  # JSON array
    media_type = db.Column(db.String(50))  # 'video', 'article', 'interactive', 'worksheet', etc.
    length_minutes = db.Column(db.Integer)
    provider = db.Column(db.String(100), index=True)
    attribution = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    @property
    def topics(self):
        return json.loads(self.topics_json) if self.topics_json else []
    
    @topics.setter
    def topics(self, value):
        self.topics_json = json.dumps(value)
    
    def __repr__(self):
        return f'<Resource {self.title}>'


class SyncState(db.Model):
    """PWA offline sync tracking"""
    __tablename__ = 'sync_states'
    
    id = db.Column(db.Integer, primary_key=True)
    entity = db.Column(db.String(50), nullable=False)  # 'submission', 'notebook', 'time', etc.
    entity_id = db.Column(db.Integer, nullable=False)
    version = db.Column(db.Integer, default=1)
    last_synced_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    __table_args__ = (db.UniqueConstraint('entity', 'entity_id', name='_entity_id_uc'),)
    
    def __repr__(self):
        return f'<SyncState {self.entity}:{self.entity_id}>'
