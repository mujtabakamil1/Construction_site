from flask import Flask, render_template, request, jsonify, send_from_directory
from flask_cors import CORS
import os
from config import config
from datetime import datetime
import re

def create_app(config_name='development'):
    """Application factory function."""
    app = Flask(__name__, 
                template_folder='templates',
                static_folder='static')
    
    # Load configuration
    app.config.from_object(config[config_name])
    
    # Enable CORS
    CORS(app)
    
    # Register blueprints and routes
    register_routes(app)
    
    return app

def register_routes(app):
    """Register all application routes."""
    
    @app.route('/')
    def home():
        """Home page route."""
        return render_template('index.html')
    
    @app.route('/api/contact', methods=['POST'])
    def submit_contact():
        """Handle contact form submission."""
        try:
            data = request.get_json()
            
            # Validate required fields
            if not all(k in data for k in ['name', 'email', 'subject', 'message']):
                return jsonify({
                    'success': False,
                    'message': 'Missing required fields'
                }), 400
            
            # Basic email validation
            if not validate_email(data['email']):
                return jsonify({
                    'success': False,
                    'message': 'Invalid email address'
                }), 400
            
            # Process the contact form
            contact_data = {
                'name': data['name'].strip(),
                'email': data['email'].strip(),
                'phone': data.get('phone', '').strip(),
                'subject': data['subject'].strip(),
                'message': data['message'].strip(),
                'timestamp': datetime.now().isoformat()
            }
            
            # TODO: In production, save to database or send email
            print(f"Contact form received: {contact_data}")
            
            return jsonify({
                'success': True,
                'message': 'Thank you for your message. We will get back to you soon!'
            }), 200
            
        except Exception as e:
            print(f"Error processing contact form: {str(e)}")
            return jsonify({
                'success': False,
                'message': 'An error occurred. Please try again later.'
            }), 500
    
    @app.route('/api/services', methods=['GET'])
    def get_services():
        """Get list of services."""
        services = [
            {
                'id': 1,
                'name': 'Residential Construction',
                'description': 'Building quality homes with modern designs',
                'icon': '🏠'
            },
            {
                'id': 2,
                'name': 'Commercial Projects',
                'description': 'Professional commercial building solutions',
                'icon': '🏢'
            },
            {
                'id': 3,
                'name': 'Renovation & Remodeling',
                'description': 'Transform your existing spaces',
                'icon': '🔨'
            },
            {
                'id': 4,
                'name': 'Infrastructure',
                'description': 'Durable infrastructure development',
                'icon': '🌉'
            }
        ]
        return jsonify(services), 200
    
    @app.route('/api/projects', methods=['GET'])
    def get_projects():
        """Get list of completed projects."""
        projects = [
            {
                'id': 1,
                'title': 'Puri Heights Residential',
                'category': 'Residential',
                'year': 2023,
                'description': 'Luxury residential complex with 50 units'
            },
            {
                'id': 2,
                'title': 'Business Park Development',
                'category': 'Commercial',
                'year': 2023,
                'description': 'Modern office space for 200+ employees'
            },
            {
                'id': 3,
                'title': 'Urban Shopping Center',
                'category': 'Commercial',
                'year': 2022,
                'description': 'Multi-story shopping and entertainment center'
            },
            {
                'id': 4,
                'title': 'Residential Township',
                'category': 'Residential',
                'year': 2022,
                'description': 'Community living project with 100+ apartments'
            }
        ]
        return jsonify(projects), 200
    
    @app.errorhandler(404)
    def not_found_error(error):
        """Handle 404 errors."""
        return jsonify({
            'success': False,
            'message': 'Resource not found'
        }), 404
    
    @app.errorhandler(500)
    def internal_error(error):
        """Handle 500 errors."""
        return jsonify({
            'success': False,
            'message': 'Internal server error'
        }), 500

def validate_email(email):
    """Validate email format."""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

app = create_app()
if __name__ == '__main__':
    app = create_app('development')
    app.run(debug=True, host='127.0.0.1', port=5000)

