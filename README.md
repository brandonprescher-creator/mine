# Ultimate Tutor Platform

Professional K-12 education platform with comprehensive curriculum, real-time progress tracking, and 50+ educational API integrations.

## Features

- 🎓 **Comprehensive K-12 Curriculum** - Complete coverage of Math, Science, ELA, Social Studies, Arts, and more
- 🔌 **50+ API Integrations** - Wikipedia, NASA, Khan Academy, OpenStax, and dozens of free educational resources
- 📊 **Progress Tracking** - Real-time mastery tracking with spaced repetition and personalized learning paths
- 🎮 **Interactive Games** - Gamified learning with achievements, multiplayer challenges, and instant feedback
- 📄 **Worksheet Generator** - AI-powered worksheet and quiz generation with PDF export
- 👨‍👩‍👧‍👦 **Parent Dashboard** - Comprehensive monitoring and reporting tools
- 🎨 **Modern UI** - Professional dark theme with responsive design
- 🔐 **Authentication** - Multi-role system (Student, Teacher, Parent, Admin)

## Quick Start

### Prerequisites

- Python 3.11+
- pip

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Tutor
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

5. **Initialize database**
   ```bash
   python -c "from app_updated import initialize_database; initialize_database()"
   ```

6. **Run the application**
   ```bash
   python app_updated.py
   ```

7. **Open your browser**
   ```
   http://localhost:5001
   ```

## Project Structure

```
Tutor/
├── app_updated.py          # Main application file
├── models/                 # Database models
├── auth/                   # Authentication blueprint
├── blueprints/             # Feature blueprints
├── templates/              # HTML templates
│   ├── base.html          # Base template
│   ├── partials/          # Reusable components
│   ├── auth/              # Auth pages
│   └── errors/            # Error pages
├── static/                 # Static assets
│   ├── css/               # Stylesheets
│   └── js/                # JavaScript files
├── services/              # Business logic
├── open_learning/         # API integrations
└── requirements.txt       # Python dependencies
```

## API Integrations

The platform integrates with 50+ free educational APIs including:

- **General Knowledge**: Wikipedia, Wikidata, Wikiquote
- **Science**: NASA, USGS, GBIF, PubChem
- **Math**: Wolfram Alpha API, Numbers API
- **Literature**: Open Library, Google Books, Project Gutenberg
- **Museums**: Met Museum, Smithsonian, Rijksmuseum
- **Educational**: Khan Academy, OpenStax, CK-12
- **Geography**: REST Countries, UN Data, World Bank
- **And many more!**

## User Roles

- **Student**: Access lessons, practice problems, games, and track progress
- **Teacher**: Create content, monitor student progress, generate materials
- **Parent**: View child progress, set goals, receive reports
- **Admin**: Manage users, content, and system configuration

## Deployment

### Render

1. Create account on [Render](https://render.com)
2. Connect your repository
3. Use the included `render.yaml` configuration
4. Set environment variables in Render dashboard
5. Deploy!

### Manual Deployment

```bash
# Using gunicorn
gunicorn app_updated:app --bind 0.0.0.0:$PORT --workers 4 --worker-class eventlet

# Using environment variables
export SECRET_KEY="your-production-secret-key"
export FLASK_ENV=production
gunicorn app_updated:app
```

## Development

### Running Tests

```bash
pytest
```

### Code Formatting

```bash
black .
```

### Linting

```bash
ruff check .
```

## Technologies

- **Backend**: Flask, Flask-Login, Flask-SocketIO
- **Frontend**: TailwindCSS, Alpine.js, Vanilla JavaScript
- **Database**: SQLite (development), PostgreSQL (production ready)
- **Real-time**: Socket.IO
- **PDF Generation**: ReportLab, WeasyPrint
- **APIs**: requests, aiohttp

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

MIT License - see LICENSE file for details

## Support

For questions or issues:
- Open a GitHub issue
- Email: support@ultimatetutor.com

## Roadmap

- [ ] Mobile apps (iOS/Android)
- [ ] Advanced AI tutoring with GPT integration
- [ ] Video lessons integration
- [ ] Offline mode with PWA
- [ ] Advanced analytics dashboard
- [ ] Multi-language support
- [ ] Accessibility enhancements (WCAG 2.1 AA)
- [ ] Integration with LMS platforms

---

**Ultimate Tutor Platform** - Empowering K-12 Education 🎓