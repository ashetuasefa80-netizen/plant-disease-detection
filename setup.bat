@echo off
echo ============================================================
echo   Plant Disease Detection System — Setup
echo   Madda Walabu University | Morketa Negash
echo ============================================================
echo.

REM Check Python 3.11 is available (required for TensorFlow)
py -3.11 --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python 3.11 not found!
    echo.
    echo TensorFlow requires Python 3.11 or lower.
    echo Download Python 3.11 from: https://www.python.org/downloads/release/python-3119/
    echo Make sure to check "Add Python to PATH" during install.
    pause
    exit /b 1
)

echo [OK] Python 3.11 found.
echo.

echo [1/3] Creating virtual environment with Python 3.11...
py -3.11 -m venv venv
call venv\Scripts\activate.bat

echo.
echo [2/3] Installing required packages...
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

echo.
echo [3/3] Setup complete!
echo.
echo ============================================================
echo   NEXT STEPS:
echo.
echo   STEP 1 — Run the web application (Demo Mode, no training needed):
echo     run_app.bat
echo.
echo   STEP 2 — (Optional) Download the PlantVillage dataset:
echo     python utils/download_dataset.py
echo.
echo   STEP 3 — (Optional) Train the CNN model for real predictions:
echo     python model/train_model.py
echo ============================================================
pause
