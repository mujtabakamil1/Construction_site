#!/usr/bin/env python
"""Test script to verify email configuration."""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

print("=" * 60)
print("EMAIL CONFIGURATION TEST")
print("=" * 60)

# Check environment variables
print("\n1. CHECKING ENVIRONMENT VARIABLES:")
print(f"   MAIL_SERVER: {os.environ.get('MAIL_SERVER', 'NOT SET')}")
print(f"   MAIL_PORT: {os.environ.get('MAIL_PORT', 'NOT SET')}")
print(f"   MAIL_USE_TLS: {os.environ.get('MAIL_USE_TLS', 'NOT SET')}")
print(f"   MAIL_USERNAME: {os.environ.get('MAIL_USERNAME', 'NOT SET')}")
print(f"   MAIL_PASSWORD: {'*' * len(os.environ.get('MAIL_PASSWORD', '')) if os.environ.get('MAIL_PASSWORD') else 'NOT SET'}")
print(f"   MAIL_DEFAULT_SENDER: {os.environ.get('MAIL_DEFAULT_SENDER', 'NOT SET')}")

# Try to import and test Flask-Mail
print("\n2. CHECKING FLASK-MAIL INSTALLATION:")
try:
    from flask_mail import Mail, Message
    print("   ✅ Flask-Mail is installed")
except ImportError as e:
    print(f"   ❌ Flask-Mail import failed: {e}")
    exit(1)

# Try to create app and mail
print("\n3. INITIALIZING FLASK APP:")
try:
    from flask import Flask
    from config import config
    
    app = Flask(__name__)
    app.config.from_object(config['development'])
    
    print("   ✅ Flask app created successfully")
    print(f"   MAIL_SERVER: {app.config.get('MAIL_SERVER')}")
    print(f"   MAIL_PORT: {app.config.get('MAIL_PORT')}")
    print(f"   MAIL_USE_TLS: {app.config.get('MAIL_USE_TLS')}")
    print(f"   MAIL_USERNAME: {app.config.get('MAIL_USERNAME')}")
    print(f"   MAIL_PASSWORD: {'*' * len(app.config.get('MAIL_PASSWORD', '')) if app.config.get('MAIL_PASSWORD') else 'NOT SET'}")
    
except Exception as e:
    print(f"   ❌ Flask app creation failed: {e}")
    exit(1)

# Try to initialize Mail
print("\n4. INITIALIZING FLASK-MAIL:")
try:
    mail = Mail(app)
    print("   ✅ Flask-Mail initialized successfully")
except Exception as e:
    print(f"   ❌ Flask-Mail initialization failed: {e}")
    exit(1)

# Try to send test email
print("\n5. SENDING TEST EMAIL:")
try:
    with app.app_context():
        msg = Message(
            subject="Test Email from PCS Puri Construction",
            recipients=['pcpl2626@gmail.com'],
            html="<h2>This is a test email</h2><p>If you receive this, email configuration is working!</p>"
        )
        mail.send(msg)
        print("   ✅ Test email sent successfully!")
        print("   Check your email inbox at pcpl2626@gmail.com")
except Exception as e:
    print(f"   ❌ Email sending failed: {e}")
    print(f"   Error type: {type(e).__name__}")
    print(f"   Error details: {str(e)}")
    exit(1)

print("\n" + "=" * 60)
print("ALL TESTS PASSED! ✅")
print("=" * 60)
