#!/bin/bash

# PCS Puri Construction Services - Linux/macOS Startup Script

echo ""
echo "========================================"
echo "PCS Puri Construction Services"
echo "========================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed"
    echo "Please install Python from https://www.python.org/downloads/"
    exit 1
fi

# Check if venv exists, if not create it
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
    echo "Virtual environment created."
fi

# Activate virtual environment
source venv/bin/activate

# Install/upgrade dependencies
echo ""
echo "Installing dependencies..."
pip install -r requirements.txt

# Run Flask app
echo ""
echo "Starting Flask application..."
echo ""
echo "========================================"
echo "Server running at: http://localhost:5000"
echo "Press Ctrl+C to stop the server"
echo "========================================"
echo ""

python app.py
