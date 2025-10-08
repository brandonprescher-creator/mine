# Deployment Guide - Ultimate Tutor Platform

Complete guide for deploying the Ultimate Tutor Platform to production.

## Prerequisites

- Python 3.11+
- Git
- Domain name (optional)
- Render.com account (free tier available)

## Local Development

### 1. Environment Setup

```bash
# Clone repository
git clone <your-repo-url>
cd Tutor

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Configure Environment

```bash
# Copy example environment file
cp .env.example .env

# Edit .env file with your settings
# Minimum required:
SECRET_KEY=your-random-secret-key-here
DATABASE_URL=tutor_app.db
```

### 3. Initialize Database

```bash
python -c "from app_updated import initialize_database; initialize_database()"
```

### 4. Run Development Server

```bash
python app_updated.py
```

Visit `http://localhost:5001` in your browser.

## Production Deployment (Render.com)

### Method 1: Using render.yaml (Recommended)

1. **Push code to GitHub**
   ```bash
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

2. **Create Render Account**
   - Go to https://render.com
   - Sign up with GitHub

3. **Create New Web Service**
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Render will automatically detect `render.yaml`

4. **Configure Environment Variables**
   - In Render dashboard, go to Environment
   - Add:
     ```
     SECRET_KEY=<generate-random-key>
     FLASK_ENV=production
     DATABASE_URL=./tutor_app.db
     ```

5. **Deploy**
   - Click "Create Web Service"
   - Render will automatically deploy

### Method 2: Manual Configuration

1. **Create Web Service**
   - New + → Web Service
   - Connect repository

2. **Configure Build**
   - Name: `ultimate-tutor`
   - Environment: `Python 3`
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app_updated:app --bind 0.0.0.0:$PORT --workers 4 --worker-class eventlet`

3. **Set Environment Variables**
   ```
   SECRET_KEY=<generate-strong-key>
   FLASK_ENV=production
   DATABASE_URL=./tutor_app.db
   PYTHON_VERSION=3.11.0
   ```

4. **Deploy**
   - Click "Create Web Service"

## Database Options

### SQLite (Default - Good for Small/Medium Scale)

```
DATABASE_URL=./tutor_app.db
```

**Pros:**
- No setup required
- Simple
- Free

**Cons:**
- Single file
- Limited concurrent writes
- Not ideal for high traffic

### PostgreSQL (Recommended for Production)

1. **Create PostgreSQL Database on Render**
   - Dashboard → New + → PostgreSQL
   - Choose free plan
   - Copy connection string

2. **Update Environment**
   ```
   DATABASE_URL=postgresql://user:pass@host:5432/dbname
   ```

3. **Update app_updated.py**
   - Change SQLite code to use SQLAlchemy
   - Or use `psycopg2` for PostgreSQL

## Custom Domain

1. **In Render Dashboard**
   - Go to your service
   - Settings → Custom Domain
   - Add your domain

2. **DNS Configuration**
   - Add CNAME record:
     ```
     Type: CNAME
     Name: www (or @)
     Value: <your-app>.onrender.com
     ```

## Environment Variables Reference

### Required

```bash
SECRET_KEY=<strong-random-key>
DATABASE_URL=<database-connection-string>
FLASK_ENV=production
```

### Optional

```bash
# Email
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-app-password

# Redis (for caching/sessions)
REDIS_URL=redis://localhost:6379/0

# API Keys
OPENAI_API_KEY=sk-...
NASA_API_KEY=...

# File Uploads
MAX_CONTENT_LENGTH=16777216

# Session
PERMANENT_SESSION_LIFETIME=3600
```

## Monitoring & Logs

### View Logs in Render

1. Go to your service dashboard
2. Click "Logs" tab
3. View real-time logs

### Health Checks

Render automatically checks:
- URL: `/` (home page)
- Expected: HTTP 200

## Scaling

### Vertical Scaling (Render)

1. Dashboard → Service
2. Settings → Instance Type
3. Upgrade plan:
   - Free: 512MB RAM
   - Starter: 1GB RAM, $7/mo
   - Standard: 2GB RAM, $15/mo

### Horizontal Scaling

Update Procfile:
```
web: gunicorn app_updated:app --workers 8 --worker-class eventlet
```

## Backup & Recovery

### Database Backup (SQLite)

```bash
# Local backup
sqlite3 tutor_app.db .dump > backup.sql

# Restore
sqlite3 tutor_app.db < backup.sql
```

### Automated Backups (PostgreSQL)

Render automatically backs up PostgreSQL databases.

## Security Checklist

- [ ] Strong SECRET_KEY (32+ random characters)
- [ ] HTTPS enabled (automatic on Render)
- [ ] Environment variables secured
- [ ] Database credentials not in code
- [ ] CORS properly configured
- [ ] File upload limits set
- [ ] Input validation enabled
- [ ] SQL injection protection (parameterized queries)
- [ ] XSS protection enabled

## Troubleshooting

### App Won't Start

1. **Check logs**: Render Dashboard → Logs
2. **Verify dependencies**: `pip install -r requirements.txt`
3. **Check Python version**: `python --version`
4. **Database connection**: Verify DATABASE_URL

### Database Errors

```bash
# Re-initialize database
python -c "from app_updated import initialize_database; initialize_database()"
```

### Performance Issues

1. **Enable caching**: Add Redis
2. **Optimize queries**: Index frequently accessed fields
3. **Upgrade plan**: More RAM/CPU
4. **Use CDN**: For static files

## Cost Estimates

### Free Tier (Render)

- Web Service: Free (sleeps after 15min inactivity)
- PostgreSQL: Free (90 days, then $7/mo)
- Total: $0-7/month

### Production (Low Traffic)

- Web Service: $7/month (Starter)
- PostgreSQL: $7/month
- Domain: $12/year
- Total: ~$15/month

### Production (Medium Traffic)

- Web Service: $15/month (Standard)
- PostgreSQL: $15/month
- Redis: $10/month
- Domain: $12/year
- Total: ~$41/month

## Performance Optimization

### 1. Enable Caching

Add Redis and cache frequent queries.

### 2. Optimize Images

Use image optimization service or CDN.

### 3. Database Indexing

```sql
CREATE INDEX idx_lessons_topic ON lessons(topic_id);
CREATE INDEX idx_problems_lesson ON practice_problems(lesson_id);
```

### 4. Static Files CDN

Configure CDN (Cloudflare, AWS CloudFront) for static assets.

## Support

- Documentation: See README.md
- Issues: GitHub Issues
- Email: support@ultimatetutor.com

---

**Good luck with your deployment! 🚀**
