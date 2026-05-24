@echo off
title Plant Disease Detection System
echo ============================================================
echo   Plant Disease Detection System
echo   Madda Walabu University ^| Morketa Negash
echo ============================================================
echo.

REM ── Use Python 3.11 explicitly (required for TensorFlow) ──
py -3.11 --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python 3.11 is not installed.
    echo         Download it from https://www.python.org/downloads/release/python-3119/
    pause
    exit /b 1
)

echo [OK] Python 3.11 found — TensorFlow will be available.
echo [OK] Starting app at http://localhost:8501
echo      Press Ctrl+C in this window to stop the server.
echo.

py -3.11 -m streamlit run app.py --server.port 8501 --server.headless false
pause
