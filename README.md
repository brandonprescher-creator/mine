# 🎓 Ultimate Tutoring Program

A comprehensive, self-contained K-8 educational tutoring application that runs with a single command. Features offline capability, file upload support, automatic lesson generation, and integration with free educational APIs.

## ✨ Features

### 📚 Comprehensive K-8 Curriculum
- **Mathematics**: Addition, subtraction, multiplication, division (with 10 mastery methods!), fractions, decimals, geometry, algebra, statistics
- **English Language Arts**: Phonics, reading comprehension, writing, grammar, vocabulary
- **Science**: Life science, physical science, Earth science, space science, scientific method
- **Social Studies**: US history, world history, geography, civics, economics
- **Arts**: Visual arts, music
- **World Languages**: Spanish, French, ESL support
- **Technology & STEAM**: Coding basics, media literacy, STEAM projects
- **PE & Health**: Fitness, nutrition, wellness
- **Life Skills**: Study skills, test preparation

### 🌟 Special Feature: Division Mastery
Complete module with **10 different division methods**:
1. Long Division
2. Partial Quotients
3. Distributive Property
4. Repeated Subtraction
5. Equal Groups
6. Array / Area Model
7. Number Line Jumps
8. Ratio Table
9. Place Value Division
10. Bar Model

Each method includes:
- Step-by-step teaching instructions
- Worked examples
- 4-6 practice problems with instant feedback
- Hints and solution steps

### 📤 File Upload & AI Lesson Generation
- Upload PDF, Word documents, text files, or images
- Automatic text extraction (including OCR for images)
- AI-powered lesson generation from your content
- Automatic practice problem creation
- Edit lessons before saving

### 🌐 Educational API Integration
Enriches lessons with free resources from:
- Wikipedia
- Wikibooks
- Khan Academy (links)
- CK-12 Foundation
- CommonLit
- NASA Kids Club
- National Geographic Education
- And more!

### ✍️ Interactive Learning
- Step-by-step lessons with clear explanations
- Interactive practice problems
- Instant feedback on answers
- Progress tracking and mastery levels
- Achievement badges

### 💾 Offline Capable
- Local SQLite database
- Works without internet connection
- API-fetched content is cached for offline use
- All lessons available anytime

### 👶 Kid-Friendly Interface
- Large, readable fonts
- Clear icons and colors
- Simple navigation
- Encouraging feedback
- Visual progress tracking

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- (Optional) Tesseract OCR for image text extraction

### Installation

1. **Clone or download this repository**

2. **Install Python dependencies:**

```bash
pip install -r requirements.txt
```

3. **Install Tesseract OCR (Optional, for image text extraction):**

   - **Windows**: Download installer from https://github.com/UB-Mannheim/tesseract/wiki
   - **Mac**: `brew install tesseract`
   - **Linux**: `sudo apt-get install tesseract-ocr`

### Running the Application

**Single command to start:**

```bash
streamlit run tutor.py
```

The app will automatically:
- Initialize the database
- Seed the complete K-8 curriculum
- Open in your default web browser

**Default URL:** http://localhost:8501

## 📖 How to Use

### 1. **Home Dashboard**
- View featured lessons
- Quick access to subjects
- See your progress at a glance

### 2. **Browse Subjects**
- Click on any subject (Math, Science, ELA, etc.)
- Select a topic
- Choose a lesson

### 3. **Learn**
- Read step-by-step instructions
- Review worked examples
- Access additional online resources

### 4. **Practice**
- Toggle to Practice mode
- Answer questions
- Get instant feedback
- See solution steps
- Track your mastery

### 5. **Upload Files**
- Drag and drop PDF, Word, text, or image files
- App extracts the text automatically
- Review generated lesson
- Edit and save to your curriculum

### 6. **Search**
- Search across all lessons
- Find topics quickly
- Jump directly to lessons

### 7. **Ask Tutor**
- Type any academic question
- Get answers from built-in lessons
- Access online educational resources
- See relevant video channels

### 8. **Track Progress**
- View lessons started
- See problems mastered
- Earn achievement badges
- Monitor your learning journey

## 🗂️ Project Structure

```
tutor/
├── tutor.py                  # Main Streamlit application
├── database.py               # SQLite database functions
├── curriculum_data.py        # K-8 curriculum content
├── file_processor.py         # File upload & text extraction
├── lesson_generator.py       # AI lesson generation
├── api_integrations.py       # Educational API connections
├── requirements.txt          # Python dependencies
├── README.md                 # This file
└── tutor_app.db             # SQLite database (created on first run)
```

## 🔧 Configuration

### Database Location
The SQLite database `tutor_app.db` is created in the same directory as the application. All curriculum, progress, and uploaded content is stored here.

### Adding Custom Content
1. Use the **Upload Files** feature in the app
2. Or manually add to the database using the functions in `database.py`

### Extending the Curriculum
Edit `curriculum_data.py` to add more subjects, topics, or lessons. The structure is:
```python
subject_id = add_subject(name, description, icon, order)
topic_id = add_topic(subject_id, name, description, order)
lesson_id = add_lesson(topic_id, title, description, steps, examples)
add_practice_problem(lesson_id, question, answer, steps, hints)
```

## 🌐 API Integration

The app integrates with free educational APIs:

- **Wikipedia API**: Article summaries and content
- **Wikibooks API**: Free textbook content
- **Curated OER Links**: Khan Academy, CK-12, CommonLit, etc.

All API responses are cached locally for offline access. Internet connection is optional.

## 🎯 Perfect For

- **Homeschooling families**
- **Students** needing extra practice
- **Teachers** wanting supplemental materials
- **Parents** helping with homework
- **Self-directed learners**

## 📊 Database Schema

### Tables
- `subjects` - Subject categories
- `topics` - Topics within subjects
- `lessons` - Lesson content
- `practice_problems` - Practice questions
- `student_progress` - Progress tracking
- `uploaded_files` - Uploaded documents
- `api_cache` - Cached API responses
- `standards` - Educational standards alignment

## 🔒 Privacy & Data

- **100% local** - No data sent to external servers
- **No accounts required** - No sign-up or login
- **No tracking** - Your learning data stays on your computer
- **No API keys needed** - Uses free, public APIs only

## 🐛 Troubleshooting

### "Module not found" errors
```bash
pip install -r requirements.txt --upgrade
```

### OCR not working
Make sure Tesseract is installed and in your system PATH.

### Database errors
Delete `tutor_app.db` and restart the app to reset everything.

### Port already in use
```bash
streamlit run tutor.py --server.port 8502
```

## 🤝 Contributing

This is a self-contained educational tool. Feel free to:
- Add more curriculum content
- Improve lesson generation algorithms
- Add more API integrations
- Enhance the UI/UX

## 📝 License

This project is provided as-is for educational purposes.

## 🙏 Acknowledgments

Educational content inspired by:
- Common Core State Standards
- Next Generation Science Standards
- Free educational resources from Khan Academy, CK-12, and others

---

## 🎓 Get Started Learning!

```bash
streamlit run tutor.py
```

**Happy Learning! 📚✨**

