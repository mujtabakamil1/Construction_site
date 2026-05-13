# Development Guide

## Project Architecture

PCS Puri Construction Services follows a Flask application structure with clear separation of concerns:

```
Construction_site/
├── app.py              # Application factory and route handlers
├── config.py           # Configuration management
├── requirements.txt    # Python dependencies
├── templates/          # Jinja2 HTML templates
│   ├── base.html      # Base template with layouts
│   └── index.html     # Home page
├── static/            # Static assets
│   ├── css/           # Stylesheets
│   ├── js/            # JavaScript files
│   └── images/        # Image assets
├── run.bat            # Windows startup script
├── run.sh             # Linux/macOS startup script
└── README.md          # Project documentation
```

## Design Patterns

### MVC (Model-View-Controller)
- **Model**: Data layer (can be extended with database models)
- **View**: Jinja2 templates in `templates/` directory
- **Controller**: Route handlers in `app.py`

### Application Factory Pattern
The `create_app()` function in `app.py` implements the Flask application factory pattern, allowing for easier testing and configuration management.

## Frontend Architecture

### Technologies
- **HTML5**: Semantic markup
- **CSS3**: Tailwind CSS framework (CDN)
- **JavaScript**: Vanilla JS for interactivity
- **Icons**: Font Awesome 6.4

### Components
1. **Navigation Bar**: Fixed header with mobile menu
2. **Hero Section**: Eye-catching landing area
3. **About Us**: Company mission and vision
4. **Services**: Service cards with icons
5. **Legacy/Projects**: Timeline and project showcase
6. **Contact Form**: With client-side and server-side validation
7. **Footer**: Social links and quick navigation

### Responsive Design
- Mobile-first approach
- Tailwind breakpoints: `sm:`, `md:`, `lg:`, `xl:`, `2xl:`
- Touch-friendly navigation
- Optimized images and assets

## Backend Architecture

### Flask Configuration
- `config.py`: Manages development, production, and testing configurations
- Environment-based settings
- Secret key management

### Route Handlers

#### GET /
- Returns the home page template

#### GET /api/services
- Returns JSON list of services
- Can be extended to fetch from database

#### GET /api/projects
- Returns JSON list of completed projects
- Can be extended to fetch from database

#### POST /api/contact
- Accepts JSON contact form data
- Validates email and required fields
- Returns success/error response

### Error Handling
- 404: Resource not found
- 500: Internal server error
- Validation errors with descriptive messages

## JavaScript Features

### Client-Side
- Form validation before submission
- Mobile menu toggle
- Dynamic service and project loading
- Smooth animations and transitions
- Scroll event handling

### API Integration
- Fetch API for async requests
- JSON data handling
- Error handling and user feedback

## CSS Architecture

### Tailwind CSS
- Utility-first approach
- Custom colors: Purple gradient (`#667eea` to `#764ba2`)
- Responsive spacing and sizing
- Dark mode support (can be enabled)

### Custom Animations
- Fade-in effects
- Slide-up animations
- Hover transformations
- Smooth transitions

### Custom Classes
- `.gradient-text`: Text gradient effect
- `.gradient-bg`: Background gradient
- `.service-card`: Service component styling
- `.project-card`: Project component styling
- `.section-title`: Section heading with underline

## Extension Points

### Adding New Features

#### New Page
1. Create template in `templates/new_page.html`
2. Add route in `app.py`:
   ```python
   @app.route('/new-page')
   def new_page():
       return render_template('new_page.html')
   ```
3. Update navigation in `base.html`

#### New API Endpoint
```python
@app.route('/api/new-endpoint', methods=['GET', 'POST'])
def new_endpoint():
    # Implementation here
    return jsonify({...}), 200
```

#### Database Integration
1. Install ORM (SQLAlchemy recommended):
   ```bash
   pip install Flask-SQLAlchemy
   ```
2. Configure database in `config.py`
3. Create models
4. Use models in route handlers

#### Email Support
1. Install Flask-Mail:
   ```bash
   pip install Flask-Mail
   ```
2. Configure email settings in `config.py`
3. Send emails from contact form endpoint

## Development Workflow

### Local Development
1. Activate virtual environment
2. Install dependencies: `pip install -r requirements.txt`
3. Run development server: `python app.py`
4. Make code changes (auto-reload enabled)
5. Test in browser at `http://localhost:5000`

### Testing
1. Create test files in `tests/` directory
2. Install pytest: `pip install pytest`
3. Run tests: `pytest`

### Code Style
- Follow PEP 8 for Python
- Use meaningful variable and function names
- Add docstrings to functions
- Comment complex logic

### Version Control
Use `.gitignore` provided to exclude:
- Python cache files
- Virtual environment
- IDE settings
- Environment variables

## Deployment

### Development Server
```bash
python app.py
```

### Production Server (Gunicorn)
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:create_app()
```

### Cloud Deployment

Choose a hosting provider and deploy using:

1. **Heroku** (Recommended for beginners):
   - Connect your GitHub repo
   - Set buildpack to Python
   - Deploy with git push

2. **PythonAnywhere**:
   - Upload files
   - Configure WSGI
   - Set up virtual environment

3. **AWS/Azure/Google Cloud**:
   - Create VM instance
   - Install Python and dependencies
   - Use Gunicorn with Nginx reverse proxy

## Performance Optimization

### Frontend
- Minify CSS and JavaScript
- Optimize images
- Enable caching headers
- Use CDN for static assets

### Backend
- Enable gzip compression
- Cache API responses
- Implement database indexing
- Use connection pooling

### General
- Monitor application metrics
- Use logging for debugging
- Implement rate limiting
- Regular security audits

## Security Best Practices

1. **Environment Variables**: Never commit sensitive data
2. **CSRF Protection**: Add CSRF tokens if forms are used
3. **SQL Injection**: Use parameterized queries
4. **XSS Protection**: Sanitize user input
5. **HTTPS**: Use SSL/TLS in production
6. **Headers**: Set security headers
7. **Secrets**: Use secure secret key in production

## Troubleshooting

### Port Already in Use
```bash
# Windows
netstat -ano | findstr :5000
taskkill /PID <PID> /F

# Linux/macOS
lsof -i :5000
kill -9 <PID>
```

### Virtual Environment Issues
```bash
# Deactivate and remove
deactivate
rm -rf venv

# Recreate
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

### Dependency Issues
```bash
# Upgrade pip
python -m pip install --upgrade pip

# Reinstall dependencies
pip install -r requirements.txt
```

## Resources

- Flask Documentation: https://flask.palletsprojects.com/
- Tailwind CSS: https://tailwindcss.com/
- Python PEP 8: https://www.python.org/dev/peps/pep-0008/
- RESTful API Design: https://restfulapi.net/

---

**Last Updated**: 2024
