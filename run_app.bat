@echo off
echo ============================================================
echo   Plant Disease Detection System — Starting Web App
echo   Madda Walabu University | Morketa Negash
echo ============================================================
echo.

REM Always use Python 3.11 — required for TensorFlow support
where py >nul 2>&1
if %errorlevel%==0 (
    py -3.11 --version >nul 2>&1
    if %errorlevel%==0 (
        echo [OK] Using Python 3.11 (TensorFlow compatible)
        echo Opening browser at http://localhost:8501
        echo Press Ctrl+C to stop the server.
        echo.
        py -3.11 -m streamlit run app.py --server.port 8501 --server.headless false
        pause
        exit /b
    )
)

REM Fallback: activate virtual environment if it exists
if exist venv\Scripts\activate.bat (
    call venv\Scripts\activate.bat
    echo [OK] Virtual environment activated.
) else (
    echo [WARN] Python 3.11 not found via py launcher. Trying default python...
    echo        TensorFlow may not be available if default Python is not 3.11.
)

echo Opening browser at http://localhost:8501
echo Press Ctrl+C to stop the server.
echo.
python -m streamlit run app.py --server.port 8501 --server.headless false
pause
