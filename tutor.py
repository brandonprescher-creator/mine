"""
Ultimate Tutoring Program - Main Application
Run with: streamlit run tutor.py
"""

import streamlit as st
import os
from database import (
    init_database, get_all_subjects, get_topics_by_subject, 
    get_lessons_by_topic, get_lesson_by_id, get_practice_problems_by_lesson,
    record_practice_attempt, get_lesson_progress, get_overall_progress,
    add_uploaded_file, mark_file_processed, get_uploaded_files,
    search_lessons, add_topic, add_lesson, add_practice_problem
)
from curriculum_data import seed_curriculum
from file_processor import process_uploaded_file
from lesson_generator import generate_lesson_from_text, generate_practice_problems, smart_split_content
from api_integrations import enrich_lesson_with_api_data, search_all_sources

# Page configuration
st.set_page_config(
    page_title="Ultimate Tutor",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# SUPER KID-FRIENDLY CSS - FUN COLORS & BIG BUTTONS!
st.markdown("""
<style>
    /* SUPER FUN KID STYLING! */
    .main {
        background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 50%, #fecfef 100%);
        font-family: 'Comic Sans MS', cursive, sans-serif;
    }
    
    .stButton>button {
        background: linear-gradient(45deg, #ff6b6b, #4ecdc4, #45b7d1, #96ceb4, #feca57);
        background-size: 300% 300%;
        animation: rainbow 3s ease infinite;
        color: white;
        font-size: 24px !important;
        font-weight: bold;
        border-radius: 25px;
        padding: 20px 40px;
        border: 4px solid #fff;
        box-shadow: 0 8px 15px rgba(0,0,0,0.2);
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        transform: scale(1.1);
        box-shadow: 0 12px 20px rgba(0,0,0,0.3);
    }
    
    @keyframes rainbow {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    h1 {
        color: #ff6b6b !important;
        font-size: 48px !important;
        font-weight: bold !important;
        text-shadow: 3px 3px 6px rgba(0,0,0,0.3);
        text-align: center;
        margin: 20px 0;
    }
    
    h2 {
        color: #4ecdc4 !important;
        font-size: 36px !important;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
    }
    
    h3 {
        color: #45b7d1 !important;
        font-size: 28px !important;
    }
    
    .step-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 25px;
        border-radius: 20px;
        margin: 15px 0;
        border: 3px solid #fff;
        box-shadow: 0 10px 20px rgba(0,0,0,0.2);
        font-size: 20px;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.3);
    }
    
    .example-box {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        color: white;
        padding: 20px;
        border-radius: 20px;
        margin: 15px 0;
        border: 3px solid #fff;
        box-shadow: 0 8px 15px rgba(0,0,0,0.2);
        font-size: 18px;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.3);
    }
    
    .practice-box {
        background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
        color: white;
        padding: 25px;
        border-radius: 20px;
        margin: 15px 0;
        border: 4px solid #fff;
        box-shadow: 0 10px 20px rgba(0,0,0,0.2);
        font-size: 20px;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.3);
    }
    
    .sidebar .sidebar-content {
        background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%);
    }
    
    .correct-answer {
        background: linear-gradient(135deg, #84fab0 0%, #8fd3f4 100%);
        color: #2d5016;
        padding: 20px;
        border-radius: 15px;
        border: 3px solid #4CAF50;
        font-size: 24px;
        font-weight: bold;
        text-align: center;
        box-shadow: 0 8px 15px rgba(0,0,0,0.2);
    }
    
    .incorrect-answer {
        background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 100%);
        color: #8b0000;
        padding: 20px;
        border-radius: 15px;
        border: 3px solid #ff6b6b;
        font-size: 20px;
        font-weight: bold;
        text-align: center;
        box-shadow: 0 8px 15px rgba(0,0,0,0.2);
    }
    
    .progress-badge {
        display: inline-block;
        background: linear-gradient(45deg, #ffd700, #ffed4e);
        color: #000;
        padding: 12px 20px;
        border-radius: 25px;
        font-weight: bold;
        margin: 8px;
        font-size: 18px;
        border: 3px solid #fff;
        box-shadow: 0 5px 10px rgba(0,0,0,0.2);
        animation: bounce 2s infinite;
    }
    
    @keyframes bounce {
        0%, 20%, 50%, 80%, 100% { transform: translateY(0); }
        40% { transform: translateY(-10px); }
        60% { transform: translateY(-5px); }
    }
    
    .fun-title {
        background: linear-gradient(45deg, #ff6b6b, #4ecdc4, #45b7d1, #96ceb4, #feca57);
        background-size: 300% 300%;
        animation: rainbow 3s ease infinite;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-size: 60px !important;
        font-weight: bold;
        text-align: center;
        text-shadow: none;
    }
    
    .big-emoji {
        font-size: 80px;
        text-align: center;
        display: block;
        margin: 20px 0;
        animation: spin 4s linear infinite;
    }
    
    @keyframes spin {
        from { transform: rotate(0deg); }
        to { transform: rotate(360deg); }
    }
    
    .subject-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 30px;
        border-radius: 25px;
        margin: 20px 0;
        border: 4px solid #fff;
        box-shadow: 0 15px 30px rgba(0,0,0,0.2);
        text-align: center;
        transition: all 0.3s ease;
    }
    
    .subject-card:hover {
        transform: scale(1.05);
        box-shadow: 0 20px 40px rgba(0,0,0,0.3);
    }
    
    .stTextInput>div>div>input {
        font-size: 24px !important;
        padding: 15px !important;
        border-radius: 15px !important;
        border: 3px solid #4ecdc4 !important;
    }
    
    .stSelectbox>div>div>select {
        font-size: 20px !important;
        padding: 10px !important;
        border-radius: 15px !important;
    }
</style>
""", unsafe_allow_html=True)

# Initialize database and seed curriculum
@st.cache_resource
def initialize_app():
    """Initialize database and seed curriculum (runs once)."""
    init_database()
    seed_curriculum()
    return True

initialize_app()

# Initialize session state
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'home'
if 'selected_subject' not in st.session_state:
    st.session_state.selected_subject = None
if 'selected_topic' not in st.session_state:
    st.session_state.selected_topic = None
if 'selected_lesson' not in st.session_state:
    st.session_state.selected_lesson = None
if 'view_mode' not in st.session_state:
    st.session_state.view_mode = 'lesson'  # 'lesson' or 'practice'
if 'practice_answers' not in st.session_state:
    st.session_state.practice_answers = {}
if 'show_feedback' not in st.session_state:
    st.session_state.show_feedback = {}

# SUPER FUN SIDEBAR!
with st.sidebar:
    st.markdown('<div class="fun-title">🎓 ULTIMATE TUTOR</div>', unsafe_allow_html=True)
    
    # Main navigation with BIG buttons
    page = st.radio(
        "Where do you want to go?",
        ["🏠 Home", "📚 Subjects", "📤 Upload Files", "🔍 Search", "❓ Ask Tutor", "📊 Progress"],
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    
    # FUN progress display
    progress = get_overall_progress()
    st.markdown("### 🏆 Your Awesome Progress!")
    st.markdown(f"**📚 Lessons:** {progress['lessons_started']}/{progress['total_lessons']}")
    st.markdown(f"**⭐ Mastered:** {progress['problems_mastered']}")
    
    st.markdown("---")
    st.markdown("### 🎮 Ready to Learn?")
    st.markdown("Pick a subject and start having fun!")

# Main content area
if "🏠 Home" in page:
    # SUPER FUN HOME PAGE!
    st.markdown('<div class="big-emoji">🎉</div>', unsafe_allow_html=True)
    st.markdown('<div class="fun-title">WELCOME TO ULTIMATE TUTOR!</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div style="text-align: center; font-size: 28px; color: #4ecdc4; margin: 30px 0;">
    🎮 Ready to have FUN while learning? 🎮
    </div>
    """, unsafe_allow_html=True)
    
    # BIG FUN BUTTONS
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("### 🎯")
        st.markdown("### LEARN")
        st.markdown("**Fun lessons with cool examples!**")
        if st.button("🚀 START LEARNING NOW!", key="learn_btn"):
            st.session_state.current_page = 'subjects'
            st.rerun()
    
    with col2:
        st.markdown("### 🎮")
        st.markdown("### PRACTICE")
        st.markdown("**Play games and get instant feedback!**")
        if st.button("🎯 PLAY & PRACTICE!", key="practice_btn"):
            st.session_state.current_page = 'subjects'
            st.rerun()
    
    with col3:
        st.markdown("### 📤")
        st.markdown("### UPLOAD")
        st.markdown("**Add your own cool stuff!**")
        if st.button("📁 UPLOAD FILES!", key="upload_btn"):
            st.session_state.current_page = 'upload'
            st.rerun()
    
    st.markdown("---")
    
    # FEATURED FUN STUFF
    st.markdown("### 🌟 SUPER COOL FEATURE: DIVISION MASTERY! 🌟")
    st.markdown("""
    <div style="text-align: center; font-size: 24px; color: #ff6b6b; margin: 20px 0;">
    🎯 Master division with 10 AWESOME methods! 🎯<br>
    Perfect for grades 3-5! 🚀
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown("""
        <div style="font-size: 20px; color: #45b7d1;">
        ✨ Learn long division, partial quotients, area models, and MORE! ✨<br>
        🎮 Each method has fun practice games! 🎮
        </div>
        """, unsafe_allow_html=True)
    with col2:
        if st.button("🎮 TRY IT NOW!", key="division_btn"):
            # Navigate to division mastery
            subjects = get_all_subjects()
            math_subject = next((s for s in subjects if s['name'] == 'Mathematics'), None)
            if math_subject:
                topics = get_topics_by_subject(math_subject['id'])
                division_topic = next((t for t in topics if 'Division' in t['name']), None)
                if division_topic:
                    st.session_state.selected_subject = math_subject
                    st.session_state.selected_topic = division_topic
                    st.session_state.current_page = 'lessons'
                    st.rerun()
    
    # FUN SUBJECT PREVIEW
    st.markdown("---")
    st.markdown("### 🎨 PICK YOUR FAVORITE SUBJECT! 🎨")
    
    subjects = get_all_subjects()
    cols = st.columns(3)
    for idx, subject in enumerate(subjects[:6]):  # Show first 6 subjects
        with cols[idx % 3]:
            st.markdown(f"""
            <div class="subject-card">
                <div style="font-size: 40px; margin-bottom: 10px;">{subject['icon']}</div>
                <div style="font-size: 24px; font-weight: bold;">{subject['name']}</div>
            </div>
            """, unsafe_allow_html=True)
            if st.button(f"EXPLORE {subject['name'].upper()}!", key=f"home_subject_{subject['id']}"):
                st.session_state.selected_subject = subject
                st.session_state.current_page = 'topics'
                st.rerun()

elif "📚 Subjects" in page:
    st.markdown('<div class="fun-title">🎨 PICK YOUR FAVORITE SUBJECT! 🎨</div>', unsafe_allow_html=True)
    
    subjects = get_all_subjects()
    
    # Display subjects in a SUPER FUN grid
    cols = st.columns(3)
    for idx, subject in enumerate(subjects):
        with cols[idx % 3]:
            st.markdown(f"""
            <div class="subject-card">
                <div style="font-size: 60px; margin-bottom: 15px;">{subject['icon']}</div>
                <div style="font-size: 28px; font-weight: bold; margin-bottom: 10px;">{subject['name']}</div>
                <div style="font-size: 18px; opacity: 0.9;">{subject['description']}</div>
            </div>
            """, unsafe_allow_html=True)
            if st.button(f"🚀 EXPLORE {subject['name'].upper()}!", key=f"subject_{subject['id']}"):
                st.session_state.selected_subject = subject
                st.session_state.current_page = 'topics'
                st.rerun()
    
    # If a subject is selected, show topics
    if st.session_state.selected_subject:
        st.markdown("---")
        subject = st.session_state.selected_subject
        st.markdown(f"""
        <div style="text-align: center; font-size: 36px; color: #ff6b6b; margin: 20px 0;">
        {subject['icon']} {subject['name'].upper()} {subject['icon']}
        </div>
        """, unsafe_allow_html=True)
        
        topics = get_topics_by_subject(subject['id'])
        
        st.markdown("### 🎯 PICK A TOPIC TO LEARN! 🎯")
        for topic in topics:
            st.markdown(f"""
            <div class="subject-card">
                <div style="font-size: 32px; font-weight: bold; margin-bottom: 10px;">{topic['name']}</div>
                <div style="font-size: 18px; opacity: 0.9;">{topic['description']}</div>
            </div>
            """, unsafe_allow_html=True)
            if st.button(f"🎮 START {topic['name'].upper()}!", key=f"topic_{topic['id']}"):
                st.session_state.selected_topic = topic
                st.session_state.current_page = 'lessons'
                st.rerun()
            st.markdown("---")

elif "📤 Upload Files" in page:
    st.markdown('<div class="fun-title">📤 UPLOAD YOUR COOL STUFF! 📤</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div style="text-align: center; font-size: 24px; color: #4ecdc4; margin: 20px 0;">
    🎯 Upload your files and I'll make AWESOME lessons! 🎯
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="font-size: 20px; color: #45b7d1; text-align: center; margin: 20px 0;">
    📄 PDF files • 📝 Word docs • 📋 Text files • 🖼️ Images<br>
    <strong>I'll turn them into fun lessons with practice games!</strong>
    </div>
    """, unsafe_allow_html=True)
    
    uploaded_file = st.file_uploader(
        "Choose a file",
        type=['pdf', 'docx', 'doc', 'txt', 'png', 'jpg', 'jpeg', 'bmp'],
        help="Upload educational content to generate lessons"
    )
    
    if uploaded_file is not None:
        st.success(f"✅ File uploaded: {uploaded_file.name}")
        
        if st.button("📖 Process & Create Lesson", type="primary"):
            with st.spinner("🔄 Reading and analyzing your file..."):
                # Process the file
                file_bytes = uploaded_file.read()
                file_type, extracted_text = process_uploaded_file(uploaded_file.name, file_bytes)
                
                if extracted_text:
                    # Save to database
                    file_id = add_uploaded_file(uploaded_file.name, file_type, extracted_text)
                    
                    st.success(f"✅ Extracted {len(extracted_text)} characters of text!")
                    
                    # Generate lesson
                    with st.spinner("🤖 Generating lesson..."):
                        lesson_data = generate_lesson_from_text(extracted_text)
                        
                        st.markdown("### 📝 Generated Lesson Preview")
                        
                        # Allow editing
                        lesson_title = st.text_input("Lesson Title", value=lesson_data['title'])
                        lesson_desc = st.text_area("Description", value=lesson_data['description'], height=100)
                        
                        st.markdown("**Teaching Steps:**")
                        steps = []
                        for i, step in enumerate(lesson_data['steps'], 1):
                            step_text = st.text_area(f"Step {i}", value=step, height=80, key=f"step_{i}")
                            steps.append(step_text)
                        
                        # Select subject and create topic
                        subjects = get_all_subjects()
                        subject_names = [s['name'] for s in subjects]
                        suggested_subject = lesson_data.get('subject', 'General')
                        default_idx = subject_names.index(suggested_subject) if suggested_subject in subject_names else 0
                        
                        selected_subject_name = st.selectbox("Subject", subject_names, index=default_idx)
                        selected_subject = next(s for s in subjects if s['name'] == selected_subject_name)
                        
                        new_topic_name = st.text_input("Topic Name", value="Uploaded Content")
                        
                        if st.button("💾 Save Lesson", type="primary"):
                            # Create topic
                            topic_id = add_topic(selected_subject['id'], new_topic_name, "Created from uploaded content")
                            
                            # Create lesson
                            lesson_id = add_lesson(
                                topic_id,
                                lesson_title,
                                lesson_desc,
                                steps,
                                lesson_data['examples'],
                                source_type='uploaded',
                                source_file=uploaded_file.name
                            )
                            
                            # Generate and add practice problems
                            practice_problems = generate_practice_problems(extracted_text, lesson_title, 5)
                            for i, problem in enumerate(practice_problems, 1):
                                add_practice_problem(
                                    lesson_id,
                                    problem['question'],
                                    problem['answer'],
                                    problem['steps'],
                                    problem['hints'],
                                    'medium',
                                    i
                                )
                            
                            mark_file_processed(file_id)
                            st.success("🎉 Lesson created successfully!")
                            st.balloons()
                else:
                    st.error("❌ Could not extract text from the file. Please try a different file.")
    
    # Show previously uploaded files
    st.markdown("---")
    st.markdown("### 📁 Previously Uploaded Files")
    uploaded_files = get_uploaded_files()
    
    if uploaded_files:
        for file in uploaded_files[:10]:  # Show last 10
            col1, col2, col3 = st.columns([3, 1, 1])
            with col1:
                st.write(f"📄 {file['filename']}")
            with col2:
                st.caption(file['file_type'].upper())
            with col3:
                if file['processed']:
                    st.success("✅ Processed")
                else:
                    st.warning("⏳ Pending")
    else:
        st.info("No files uploaded yet. Upload your first file above!")

elif "🔍 Search" in page:
    st.markdown('<div class="fun-title">🔍 SEARCH FOR COOL STUFF! 🔍</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div style="text-align: center; font-size: 24px; color: #4ecdc4; margin: 20px 0;">
    🎯 What do you want to learn about? 🎯
    </div>
    """, unsafe_allow_html=True)
    
    search_query = st.text_input("Type what you want to learn!", placeholder="e.g., division, fractions, dinosaurs, space...")
    
    if search_query:
        with st.spinner("Searching..."):
            results = search_lessons(search_query)
            
            if results:
                st.success(f"Found {len(results)} lessons!")
                
                for lesson in results:
                    with st.expander(f"📖 {lesson['title']} ({lesson['subject_name']} > {lesson['topic_name']})"):
                        st.write(lesson['description'])
                        if st.button("View Lesson", key=f"view_{lesson['id']}"):
                            st.session_state.selected_lesson = lesson['id']
                            st.session_state.view_mode = 'lesson'
                            st.session_state.current_page = 'lesson_view'
                            st.rerun()
            else:
                st.warning("No lessons found. Try different keywords or upload your own content!")

elif "❓ Ask Tutor" in page:
    st.markdown('<div class="fun-title">❓ ASK ME ANYTHING! ❓</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div style="text-align: center; font-size: 24px; color: #4ecdc4; margin: 20px 0;">
    🎯 I'm your smart tutor! Ask me anything! 🎯
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="font-size: 20px; color: #45b7d1; text-align: center; margin: 20px 0;">
    📚 I'll find answers from my lessons<br>
    📤 Your uploaded stuff<br>
    🌐 Cool websites like Wikipedia and Khan Academy!
    </div>
    """, unsafe_allow_html=True)
    
    question = st.text_area("What do you want to know?", placeholder="e.g., How does photosynthesis work? What is long division? Why is the sky blue?", height=100)
    
    if st.button("🔍 Get Answer", type="primary"):
        if question:
            with st.spinner("🤔 Searching for answers..."):
                # Search local lessons first
                local_results = search_lessons(question)
                
                # Search external APIs
                api_results = search_all_sources(question)
                
                st.markdown("### 📚 From Your Lessons")
                if local_results:
                    for lesson in local_results[:3]:
                        with st.expander(f"📖 {lesson['title']}"):
                            st.write(lesson['description'])
                            if st.button("View Full Lesson", key=f"ask_view_{lesson['id']}"):
                                st.session_state.selected_lesson = lesson['id']
                                st.session_state.current_page = 'lesson_view'
                                st.rerun()
                else:
                    st.info("No matching lessons found in your library.")
                
                st.markdown("---")
                st.markdown("### 🌐 From Educational Resources")
                
                if api_results['sources']:
                    for source in api_results['sources']:
                        if source.get('source') == 'Wikipedia':
                            st.markdown(f"**📖 Wikipedia: {source['title']}**")
                            st.write(source['summary'][:500] + "...")
                            st.markdown(f"[Read more on Wikipedia]({source['url']})")
                        
                        elif source.get('source') == 'Wikibooks':
                            st.markdown("**📚 Wikibooks**")
                            for result in source['results']:
                                st.markdown(f"- [{result['title']}]({result['url']})")
                        
                        elif source.get('source') == 'Open Educational Resources':
                            st.markdown("**🎓 Free Learning Resources**")
                            for resource in source['resources']:
                                st.markdown(f"- [{resource['title']}]({resource['url']}) - {resource['description']}")
                        
                        elif source.get('source') == 'Educational Videos':
                            st.markdown("**📺 Recommended Video Channels**")
                            for video in source['videos']:
                                st.markdown(f"- [{video['title']}]({video['url']}) - {video['channel']}")
                else:
                    st.info("Try different keywords or check your internet connection for online resources.")
        else:
            st.warning("Please enter a question!")

elif "📊 Progress" in page:
    st.markdown('<div class="fun-title">🏆 YOUR AWESOME PROGRESS! 🏆</div>', unsafe_allow_html=True)
    
    progress = get_overall_progress()
    
    st.markdown("""
    <div style="text-align: center; font-size: 24px; color: #4ecdc4; margin: 20px 0;">
    🎯 Look how much you've learned! 🎯
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f"""
        <div class="subject-card">
            <div style="font-size: 40px; margin-bottom: 10px;">📚</div>
            <div style="font-size: 24px; font-weight: bold;">Lessons Started</div>
            <div style="font-size: 32px; color: #ffd700;">{progress['lessons_started']}/{progress['total_lessons']}</div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
        <div class="subject-card">
            <div style="font-size: 40px; margin-bottom: 10px;">⭐</div>
            <div style="font-size: 24px; font-weight: bold;">Problems Mastered</div>
            <div style="font-size: 32px; color: #ffd700;">{progress['problems_mastered']}</div>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown(f"""
        <div class="subject-card">
            <div style="font-size: 40px; margin-bottom: 10px;">🎯</div>
            <div style="font-size: 24px; font-weight: bold;">Total Attempts</div>
            <div style="font-size: 32px; color: #ffd700;">{progress['total_problems_attempted']}</div>
        </div>
        """, unsafe_allow_html=True)
    
    # Progress percentage
    if progress['total_lessons'] > 0:
        progress_pct = (progress['lessons_started'] / progress['total_lessons']) * 100
        st.progress(progress_pct / 100)
        st.markdown(f"""
        <div style="text-align: center; font-size: 20px; color: #ff6b6b; margin: 10px 0;">
        🎉 You've explored {progress_pct:.1f}% of all lessons! 🎉
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 🏆 YOUR AMAZING BADGES! 🏆")
    
    # Award badges
    badges = []
    if progress['lessons_started'] >= 1:
        badges.append("🎯 First Steps")
    if progress['lessons_started'] >= 10:
        badges.append("📚 Bookworm")
    if progress['problems_mastered'] >= 10:
        badges.append("⭐ Rising Star")
    if progress['problems_mastered'] >= 50:
        badges.append("🏆 Master Learner")
    if progress['total_problems_attempted'] >= 100:
        badges.append("💪 Persistent")
    
    if badges:
        cols = st.columns(len(badges))
        for i, badge in enumerate(badges):
            with cols[i]:
                st.markdown(f'<div class="progress-badge">{badge}</div>', unsafe_allow_html=True)
    else:
        st.markdown("""
        <div style="text-align: center; font-size: 20px; color: #45b7d1; margin: 20px 0;">
        🎮 Start learning to earn cool badges! 🎮
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 🚀 KEEP GOING, SUPERSTAR! 🚀")
    st.markdown("""
    <div style="text-align: center; font-size: 20px; color: #4ecdc4; margin: 20px 0;">
    The more you practice, the more you learn!<br>
    Try a new lesson today and become even more awesome! 🌟
    </div>
    """, unsafe_allow_html=True)

# Lesson view (when a topic is selected)
if st.session_state.get('selected_topic') and 'current_page' not in st.session_state or st.session_state.get('current_page') == 'lessons':
    topic = st.session_state.selected_topic
    subject = st.session_state.selected_subject
    
    st.markdown(f"""
    <div style="text-align: center; font-size: 36px; color: #ff6b6b; margin: 20px 0;">
    {subject['icon']} {subject['name'].upper()} / {topic['name'].upper()} {subject['icon']}
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div style="text-align: center; font-size: 20px; color: #45b7d1; margin: 20px 0;">
    {topic['description']}
    </div>
    """, unsafe_allow_html=True)
    
    lessons = get_lessons_by_topic(topic['id'])
    
    if lessons:
        st.markdown("### 🎯 PICK A LESSON TO START! 🎯")
        for lesson in lessons:
            st.markdown(f"""
            <div class="subject-card">
                <div style="font-size: 28px; font-weight: bold; margin-bottom: 10px;">{lesson['title']}</div>
                <div style="font-size: 18px; opacity: 0.9;">{lesson['description'][:150] + "..." if len(lesson['description']) > 150 else lesson['description']}</div>
            </div>
            """, unsafe_allow_html=True)
            if st.button(f"🎮 START {lesson['title'].upper()}!", key=f"lesson_{lesson['id']}"):
                st.session_state.selected_lesson = lesson['id']
                st.session_state.view_mode = 'lesson'
                st.session_state.current_page = 'lesson_view'
                st.rerun()
            st.markdown("---")
    else:
        st.markdown("""
        <div style="text-align: center; font-size: 20px; color: #45b7d1; margin: 20px 0;">
        🎮 No lessons yet, but you can upload your own! 🎮
        </div>
        """, unsafe_allow_html=True)

# Individual lesson view
if st.session_state.get('current_page') == 'lesson_view' or st.session_state.get('selected_lesson'):
    lesson_id = st.session_state.selected_lesson
    lesson = get_lesson_by_id(lesson_id)
    
    if lesson:
        # FUN View toggle
        col1, col2, col3 = st.columns([1, 1, 2])
        with col1:
            if st.button("📖 LEARN", type="primary" if st.session_state.view_mode == 'lesson' else "secondary"):
                st.session_state.view_mode = 'lesson'
                st.rerun()
        with col2:
            if st.button("🎮 PRACTICE", type="primary" if st.session_state.view_mode == 'practice' else "secondary"):
                st.session_state.view_mode = 'practice'
                st.rerun()
        with col3:
            if st.button("🏠 BACK HOME"):
                st.session_state.selected_lesson = None
                st.session_state.current_page = 'topics'
                st.rerun()
        
        st.markdown("---")
        
        # LESSON VIEW
        if st.session_state.view_mode == 'lesson':
            st.markdown(f"""
            <div style="text-align: center; font-size: 36px; color: #ff6b6b; margin: 20px 0;">
            📖 {lesson['title'].upper()} 📖
            </div>
            """, unsafe_allow_html=True)
            st.markdown(f"""
            <div style="text-align: center; font-size: 20px; color: #45b7d1; margin: 20px 0; padding: 20px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 20px; color: white;">
            {lesson['description']}
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("### 🎯 HOW TO DO IT - STEP BY STEP! 🎯")
            for i, step in enumerate(lesson['steps'], 1):
                st.markdown(f'<div class="step-box"><strong>🎯 Step {i}:</strong> {step}</div>', unsafe_allow_html=True)
            
            # Examples
            if lesson['examples']:
                st.markdown("### 💡 COOL EXAMPLES! 💡")
                for example in lesson['examples']:
                    st.markdown(f'<div class="example-box"><strong>🌟 {example["title"]}:</strong><br>{example["content"]}</div>', unsafe_allow_html=True)
            
            # API enrichment (if online)
            with st.expander("🌐 More Resources (Online)"):
                st.caption("These resources require internet connection")
                try:
                    enriched = enrich_lesson_with_api_data(lesson['title'], lesson['title'])
                    
                    if enriched.get('wikipedia'):
                        wiki = enriched['wikipedia']
                        st.markdown(f"**📖 Wikipedia: [{wiki['title']}]({wiki['url']})**")
                        st.write(wiki['summary'][:300] + "...")
                    
                    if enriched.get('oer_resources'):
                        st.markdown("**🎓 Free Learning Resources:**")
                        for resource in enriched['oer_resources'][:3]:
                            st.markdown(f"- [{resource['title']}]({resource['url']})")
                    
                    if enriched.get('videos'):
                        st.markdown("**📺 Video Channels:**")
                        for video in enriched['videos'][:3]:
                            st.markdown(f"- [{video['title']}]({video['url']})")
                except Exception as e:
                    st.warning("Unable to load online resources. Check your internet connection.")
        
        # PRACTICE VIEW
        elif st.session_state.view_mode == 'practice':
            st.markdown(f"""
            <div style="text-align: center; font-size: 36px; color: #ff6b6b; margin: 20px 0;">
            🎮 PRACTICE TIME: {lesson['title'].upper()} 🎮
            </div>
            """, unsafe_allow_html=True)
            
            problems = get_practice_problems_by_lesson(lesson_id)
            
            if problems:
                for i, problem in enumerate(problems, 1):
                    st.markdown(f'<div class="practice-box">', unsafe_allow_html=True)
                    st.markdown(f"**🎯 Problem {i}:** {problem['question']}")
                    
                    # Answer input
                    user_answer = st.text_input(
                        f"Your awesome answer:",
                        key=f"answer_{problem['id']}",
                        placeholder="Type your answer here..."
                    )
                    
                    # Check button
                    if st.button(f"🎮 CHECK MY WORK!", key=f"check_{problem['id']}"):
                        st.session_state.practice_answers[problem['id']] = user_answer
                        st.session_state.show_feedback[problem['id']] = True
                        
                        # Record attempt
                        is_correct = user_answer.strip().lower() == problem['answer'].strip().lower()
                        record_practice_attempt(lesson_id, problem['id'], is_correct)
                        st.rerun()
                    
                    # Show feedback if checked
                    if st.session_state.show_feedback.get(problem['id']):
                        user_ans = st.session_state.practice_answers.get(problem['id'], '').strip().lower()
                        correct_ans = problem['answer'].strip().lower()
                        
                        if user_ans == correct_ans:
                            st.markdown('<div class="correct-answer">🎉 AWESOME! YOU GOT IT RIGHT! 🎉<br>You\'re doing GREAT! Keep it up! 🌟</div>', unsafe_allow_html=True)
                        else:
                            st.markdown(f'<div class="incorrect-answer">🤔 Not quite right, but that\'s OK! 🤔<br>The correct answer is: <strong>{problem["answer"]}</strong><br>Try again - you\'ve got this! 💪</div>', unsafe_allow_html=True)
                        
                        # Show solution steps
                        with st.expander("📋 SEE THE SOLUTION STEPS"):
                            for j, step in enumerate(problem['steps'], 1):
                                st.write(f"🎯 {j}. {step}")
                        
                        # Hints
                        if problem['hints']:
                            with st.expander("💡 HELPFUL HINTS"):
                                for hint in problem['hints']:
                                    st.write(f"💡 {hint}")
                    
                    st.markdown('</div>', unsafe_allow_html=True)
                    st.markdown("---")
                
                # Progress for this lesson
                lesson_prog = get_lesson_progress(lesson_id)
                if lesson_prog['total_problems'] > 0:
                    st.markdown("### 📊 Your Progress on This Lesson")
                    mastery_pct = (lesson_prog['mastered'] / lesson_prog['total_problems']) * 100
                    st.progress(mastery_pct / 100)
                    st.caption(f"{lesson_prog['mastered']} of {lesson_prog['total_problems']} problems mastered ({lesson_prog['avg_score']*100:.0f}% average)")
            else:
                st.info("No practice problems available yet for this lesson.")

# Footer
st.markdown("---")
st.caption("🎓 Ultimate Tutoring Program | Comprehensive K-8 Education | Offline Capable")

