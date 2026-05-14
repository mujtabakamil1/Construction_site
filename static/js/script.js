/**
 * PCS Puri Construction Services - Main JavaScript
 * Additional interactive features and utilities
 */

// Utility function to check if element is in viewport
function isInViewport(element) {
    const rect = element.getBoundingClientRect();
    return (
        rect.top <= (window.innerHeight || document.documentElement.clientHeight) &&
        rect.bottom >= 0
    );
}

// Scroll animation trigger
function handleScrollAnimations() {
    const elements = document.querySelectorAll('.slide-up');
    elements.forEach(el => {
        if (isInViewport(el)) {
            el.classList.add('animate-fade-in');
        }
    });
}

// Debounce function for performance
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// Smooth scroll to element
function smoothScrollTo(elementId) {
    const element = document.getElementById(elementId);
    if (element) {
        element.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
}

// Add scroll event listener with debounce
window.addEventListener('scroll', debounce(handleScrollAnimations, 100));

// Contact Form Handler
function handleContactFormSubmit(event) {
    event.preventDefault();
    
    const form = event.target;
    const formMessage = document.getElementById('form-message');
    const submitBtn = form.querySelector('button[type="submit"]');
    
    // Get form data
    const formData = {
        name: document.getElementById('name').value.trim(),
        email: document.getElementById('email').value.trim(),
        phone: document.getElementById('phone').value.trim(),
        subject: document.getElementById('subject').value.trim(),
        message: document.getElementById('message').value.trim()
    };
    
    // Basic client-side validation
    if (!formData.name || !formData.email || !formData.subject || !formData.message) {
        showFormMessage('Please fill in all required fields', 'error', formMessage);
        return;
    }
    
    // Email regex validation
    const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    if (!emailRegex.test(formData.email)) {
        showFormMessage('Please enter a valid email address', 'error', formMessage);
        return;
    }
    
    // Disable submit button and show loading state
    submitBtn.disabled = true;
    const originalText = submitBtn.textContent;
    submitBtn.textContent = 'Sending...';
    
    // Send form data to backend
    fetch('/api/contact', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData)
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            showFormMessage(data.message, 'success', formMessage);
            form.reset(); // Clear the form
            console.log('Contact form submitted successfully');
        } else {
            showFormMessage(data.message || 'An error occurred', 'error', formMessage);
            console.error('Form submission error:', data);
        }
    })
    .catch(error => {
        showFormMessage('Failed to send message. Please try again later.', 'error', formMessage);
        console.error('Fetch error:', error);
    })
    .finally(() => {
        // Re-enable submit button
        submitBtn.disabled = false;
        submitBtn.textContent = originalText;
    });
}

// Display form messages
function showFormMessage(message, type, messageElement) {
    messageElement.textContent = message;
    messageElement.className = `p-4 rounded-lg text-center ${
        type === 'success' 
            ? 'bg-green-100 text-green-700 border border-green-400' 
            : 'bg-red-100 text-red-700 border border-red-400'
    }`;
    messageElement.classList.remove('hidden');
    
    // Auto-hide success message after 5 seconds
    if (type === 'success') {
        setTimeout(() => {
            messageElement.classList.add('hidden');
        }, 5000);
    }
}

// Initialize animations on page load
document.addEventListener('DOMContentLoaded', () => {
    handleScrollAnimations();
    
    // Attach contact form handler
    const contactForm = document.getElementById('contact-form');
    if (contactForm) {
        contactForm.addEventListener('submit', handleContactFormSubmit);
    }
    
    console.log('PCS Puri Construction Services - Website loaded successfully');
});

// Log version info
console.log('Version: 1.0.0 | Building Excellence');
