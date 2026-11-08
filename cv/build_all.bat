@echo off
cd /d "%~dp0"
if exist ".venv\Scripts\python.exe" (
    ".venv\Scripts\python.exe" build_all.py %*
) else (
    python build_all.py %*
)
pause
