@echo off
echo ============================================================
echo   Plant Disease Detection System — Model Training
echo ============================================================
echo.

REM Activate virtual environment if it exists
if exist venv\Scripts\activate.bat (
    call venv\Scripts\activate.bat
)

echo Starting CNN model training...
echo This may take 30-60 minutes depending on your hardware.
echo.

python model/train_model.py

echo.
echo Training complete! Run run_app.bat to start the web app.
pause
