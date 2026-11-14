@echo off

netstat -ano | findstr :8501 >nul
if %errorlevel%==0 (
    echo Project is already running.
    start http://localhost:8501
    exit
)

cd /d "%~dp0"
call .venv\Scripts\activate

netstat -ano | findstr :8000 >nul
if %errorlevel% neq 0 (
    start "API" cmd /c "cd api && python -m uvicorn main:app --reload"
)

timeout /t 4 >nul

start "UI" cmd /c "python -m streamlit run ui\app.py"

timeout /t 6 >nul
start http://localhost:8501