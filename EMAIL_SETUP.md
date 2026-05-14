# Email Contact Form Setup Guide

## Overview
Your contact form is now fully functional! Users can fill out the form and you'll receive their messages via email at **pcpl2626@gmail.com**.

## How It Works

### 1. **Frontend (HTML Form)**
Located in [templates/index.html](templates/index.html) - Contact Section
- Users fill out: Name, Email, Phone (optional), Subject, Message
- Form is styled with Tailwind CSS

### 2. **Frontend (JavaScript)**
Located in [static/js/script.js](static/js/script.js)
- Handles form submission when user clicks "Send Message"
- Validates all required fields
- Shows loading state during submission
- Displays success/error messages
- Auto-clears form on successful submission

### 3. **Backend (Flask API)**
Located in [app.py](app.py) - `/api/contact` route
- Receives form data as JSON
- Validates email format
- Creates HTML-formatted email
- Sends email via SMTP
- Returns success/error response

### 4. **Email Configuration**
Located in [config.py](config.py) and [.env](.env)
- Email Provider: Gmail
- SMTP Server: smtp.gmail.com
- Port: 587 (TLS)
- Email: pcpl2626@gmail.com

## Current Status ✅

✅ Contact form HTML - Ready
✅ Form submission JavaScript - Ready
✅ Backend API route - Ready
✅ Email configuration - Ready
✅ Email sending with Flask-Mail - Ready

## Running the Application

```bash
# Install dependencies
pip install -r requirements.txt

# Run the Flask app
python app.py
```

Visit: http://localhost:5000

## Testing the Form

1. Fill out the contact form with:
   - Name: Your name
   - Email: Your email address
   - Subject: Test message
   - Message: Test content

2. Click "Send Message"

3. Check **pcpl2626@gmail.com** for the email

4. You should see a success message: "Thank you for your message. We will get back to you soon!"

## Email Notifications

When a user submits the form, you'll receive an email containing:
- User's Name
- User's Email
- User's Phone (if provided)
- Subject
- Full Message
- Timestamp of submission

The email will be formatted as HTML for better readability.

## Troubleshooting

### If emails aren't sending:

1. **Check Gmail App Password**: 
   - The password in `.env` should be a Gmail App Password, not your regular Gmail password
   - Go to: https://myaccount.google.com/apppasswords
   - Generate one for "Mail" and "Windows"

2. **Enable Less Secure Apps** (if using regular password):
   - Go to: https://myaccount.google.com/lesssecureapps
   - Turn ON "Allow less secure app access"

3. **Check Firewall**: Ensure port 587 is not blocked

4. **Debug Email Sending**:
   ```bash
   python test_email.py
   ```

## Customization

### Change recipient email:
Edit [app.py](app.py) line with:
```python
recipients=['your-email@gmail.com']
```

### Add more fields to form:
1. Add input field to HTML form in [templates/index.html](templates/index.html)
2. Add field name to JavaScript validation in [static/js/script.js](static/js/script.js)
3. Add field to form data dict in [app.py](app.py)
4. Update email template HTML in [app.py](app.py)

## Dependencies

All dependencies are already in [requirements.txt](requirements.txt):
- Flask: Web framework
- Flask-CORS: Cross-origin support
- Flask-Mail: Email sending
- python-dotenv: Environment variables

## Files Modified

- `static/js/script.js` - Added form submission handler
- `.env` - Already configured with email settings
