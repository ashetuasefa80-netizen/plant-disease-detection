@echo off
echo ============================================================
echo   Plant Disease Detection System — Starting Web App
echo   Madda Walabu University | Morketa Negash
echo ============================================================
echo.

REM Activate virtual environment if it exists
if exist venv\Scripts\activate.bat (
    call venv\Scripts\activate.bat
    echo [OK] Virtual environment activated.
    goto :run
)

REM Try Python 3.11 first (required for TensorFlow)
where py >nul 2>&1
if %errorlevel%==0 (
    py -3.11 --version >nul 2>&1
    if %errorlevel%==0 (
        echo [OK] Using Python 3.11
        echo Opening browser at http://localhost:8501
        echo Press Ctrl+C to stop the server.
        echo.
        py -3.11 -m streamlit run app.py --server.port 8501 --server.headless false
        pause
        exit /b
    )
)

:run
echo Opening browser at http://localhost:8501
echo Press Ctrl+C to stop the server.
echo.
python -m streamlit run app.py --server.port 8501 --server.headless false
pause
