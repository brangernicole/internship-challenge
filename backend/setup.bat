@echo off
REM Setup and run backend (Windows)

echo.
echo ========================================
echo Backend Setup ^& Run
echo ========================================
echo.

if not exist venv (
    echo Creating virtual environment...
    python -m venv venv
)

call venv\Scripts\activate.bat

echo Installing dependencies...
pip install -q -r requirements.txt >nul 2>&1

echo Setting up database...
python manage.py migrate --run-syncdb >nul 2>&1

echo.
echo ========================================
echo Starting server...
echo API: http://localhost:8000/api/lcm/
echo ========================================
echo.

python manage.py runserver 0.0.0.0:8000
