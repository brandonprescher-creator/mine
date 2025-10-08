# Quick Start Guide - Ultimate Tutor Platform

Get up and running in 5 minutes!

## 🚀 Quick Installation

### 1. Clone and Setup (30 seconds)

```bash
git clone <your-repo-url>
cd Tutor
python -m venv venv
```

### 2. Activate Environment (Platform-Specific)

**Windows:**
```bash
venv\Scripts\activate
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

### 3. Install Dependencies (2 minutes)

```bash
pip install -r requirements.txt
```

### 4. Initialize Database (30 seconds)

```bash
python -c "from app_updated import initialize_database; initialize_database()"
```

### 5. Run the App (10 seconds)

```bash
python app_updated.py
```

### 6. Open Your Browser

Navigate to: **http://localhost:5001**

## 🎉 You're Ready!

### First Steps

1. **Explore Subjects** - Click "Explore Subjects" on the home page
2. **Try a Lesson** - Select a subject → topic → lesson
3. **Create Account** - Register as Student/Teacher/Parent (top right)
4. **Practice Problems** - Test your knowledge with interactive problems
5. **Explore APIs** - Check out 50+ educational API integrations

### Demo Accounts

Try these pre-configured accounts:

- **Student**: `student` / `demo123`
- **Teacher**: `teacher` / `demo123`
- **Parent**: `parent` / `demo123`

## 📚 Key Features to Try

### 1. Subject Learning Path

Home → Subjects → Pick a subject → Browse topics → Start a lesson

### 2. Practice Mode

Any lesson → "Practice" tab → Solve problems → Get instant feedback

### 3. Dashboard (Requires Login)

Login → Dashboard → View your progress, achievements, and recommendations

### 4. API Explorer

Home → "Explore 50+ APIs" → Pick an API → Search for resources

### 5. Worksheet Generator

Home → "Generate Worksheets" → Select options → Download PDF

### 6. Parent Dashboard (Parent Role)

Login as parent → Parent Dashboard → Add students → Monitor progress

## 🎨 Customization

### Change Theme Colors

Edit `static/css/modern.css`:

```css
:root {
    --color-primary: #0ea5e9;  /* Change this! */
    --color-secondary: #8b5cf6;
}
```

### Add Your Own Subjects

Edit `curriculum_data.py` and add to the subjects list.

### Configure APIs

Many APIs work without keys! For advanced features:

1. Get API keys from providers
2. Add to `.env` file
3. Update `open_learning/adapters/` files

## 🐛 Troubleshooting

### Port Already in Use

Change port in `app_updated.py`:

```python
socketio.run(app, port=5002)  # Changed from 5001
```

### Database Error

Delete and recreate:

```bash
rm tutor_app.db
python -c "from app_updated import initialize_database; initialize_database()"
```

### Missing Dependencies

```bash
pip install --upgrade -r requirements.txt
```

### Python Version Error

Ensure Python 3.11+:

```bash
python --version
```

## 📖 Next Steps

- **Read Full Documentation**: `README.md`
- **Deploy to Production**: `DEPLOYMENT_GUIDE.md`
- **Explore API Integrations**: `open_learning/` directory
- **Customize Curriculum**: `curriculum_data.py`

## 💡 Pro Tips

1. **Use Search**: Every page has search functionality
2. **Track Progress**: Login to save your progress
3. **Multiple Users**: Create different accounts for students/teachers
4. **API Explorer**: Discover new learning resources daily
5. **Worksheets**: Generate unlimited practice materials

## 🆘 Need Help?

- **Documentation**: Check `README.md`
- **Issues**: Open a GitHub issue
- **Email**: support@ultimatetutor.com

---

**Enjoy your learning journey! 🎓**
