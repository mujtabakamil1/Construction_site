# PCS Puri Construction Services

A professional construction website for PCS Puri Construction Services built with Flask, HTML5, Tailwind CSS, and JavaScript.

## Project Structure

```
Construction_site/
├── app.py                 # Flask application entry point
├── config.py             # Configuration settings
├── requirements.txt      # Python dependencies
├── templates/
│   ├── base.html        # Base template with styling
│   └── index.html       # Home page with all sections
├── static/
│   ├── css/
│   │   └── style.css    # Additional CSS (if needed)
│   ├── js/
│   │   └── script.js    # Additional JavaScript
│   └── images/          # Image assets
└── README.md            # This file
```

## Features

### Frontend
- **Responsive Design**: Mobile-first approach using Tailwind CSS
- **Modern UI**: Beautiful gradient colors and smooth animations
- **Sections**:
  - Hero Section with call-to-action
  - About Us with company mission and vision
  - Services showcase
  - Legacy/Projects section with timeline
  - Contact form with validation
  - Footer with social links

### Backend (Flask)
- **RESTful API**: Endpoints for services, projects, and contact submissions
- **Form Validation**: Email and required field validation
- **CORS Support**: Cross-origin resource sharing enabled
- **Error Handling**: Comprehensive error handling with appropriate HTTP status codes
- **Configuration Management**: Environment-based configuration

## Setup Instructions

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Installation

1. **Clone/Navigate to the project**
   ```bash
   cd d:\Construction_site
   ```

2. **Create a virtual environment** (recommended)
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

4. **Run the Flask application**
   ```bash
   python app.py
   ```

5. **Open in browser**
   ```
   http://localhost:5000
   ```

## API Endpoints

### GET /api/services
Returns a list of construction services.

**Response:**
```json
[
  {
    "id": 1,
    "name": "Service Name",
    "description": "Service Description",
    "icon": "🏠"
  }
]
```

### GET /api/projects
Returns a list of completed projects.

**Response:**
```json
[
  {
    "id": 1,
    "title": "Project Title",
    "category": "Residential",
    "year": 2023,
    "description": "Project Description"
  }
]
```

### POST /api/contact
Submits a contact form.

**Request Body:**
```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "phone": "+91 XXXXXXXXXX",
  "subject": "Project Inquiry",
  "message": "Your message here"
}
```

**Response:**
```json
{
  "success": true,
  "message": "Thank you for your message. We will get back to you soon!"
}
```

## Customization

### Update Company Information
Edit [templates/index.html](templates/index.html) to update:
- Company name and contact details
- Services offered
- Project information
- Social media links

### Add More Pages
1. Create new template in `templates/` folder
2. Add route in `app.py`
3. Update navigation in base template

### Add Images
1. Place images in `static/images/`
2. Reference in HTML: `<img src="{{ url_for('static', filename='images/yourimage.jpg') }}">`

## Technologies Used

- **Frontend**: HTML5, CSS3, Tailwind CSS, JavaScript
- **Backend**: Python Flask
- **Styling**: Tailwind CSS CDN, Font Awesome Icons
- **Architecture**: MVC (Model-View-Controller) pattern

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers

## Production Deployment

Before deploying to production:

1. Set `DEBUG = False` in config.py
2. Update `SECRET_KEY` with a secure random key
3. Configure proper email sending for contact forms
4. Set up database for storing contacts (optional)
5. Use a production WSGI server like Gunicorn on your hosting provider:
   ```bash
   pip install gunicorn
   gunicorn -w 4 -b 0.0.0.0:5000 app:create_app()
   ```
6. Popular hosting options:
   - Heroku (easy deployment)
   - PythonAnywhere (Python-focused)
   - AWS/Azure/Google Cloud (scalable)
   - DigitalOcean (affordable VPS)

## Environment Variables

Create a `.env` file (optional):
```
FLASK_ENV=development
SECRET_KEY=your-secret-key-here
```

## License

PCS Puri Construction Services © 2024

## Support

For support or inquiries:
- Email: info@pcspuri.com
- Phone: +91 XXXXXXXXXX
- Location: Puri, Odisha, India

---

**Built with ❤️ for excellence in construction**
