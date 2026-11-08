@echo off
cd /d "%~dp0"
"C:\Program Files\Git\cmd\git.exe" add .
"C:\Program Files\Git\cmd\git.exe" commit -m "Update CVs and cover letters" 2>nul
"C:\Program Files\Git\cmd\git.exe" push -u origin main
pause
