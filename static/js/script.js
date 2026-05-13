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

// Initialize animations on page load
document.addEventListener('DOMContentLoaded', () => {
    handleScrollAnimations();
    console.log('PCS Puri Construction Services - Website loaded successfully');
});

// Log version info
console.log('Version: 1.0.0 | Building Excellence');
