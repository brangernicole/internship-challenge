#!/usr/bin/env bash
# Setup and run backend (Linux/Mac)

echo "========================================"
echo "Backend Setup & Run"
echo "========================================"

if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python -m venv venv
fi

echo "Activating virtual environment..."
source venv/bin/activate

echo "Installing dependencies..."
pip install -q -r requirements.txt 2>/dev/null

echo "Setting up database..."
python manage.py migrate --run-syncdb

echo ""
echo "========================================"
echo "Starting server..."
echo "API: http://localhost:8000/api/lcm/"
echo "========================================"
echo ""

python manage.py runserver 0.0.0.0:8000
