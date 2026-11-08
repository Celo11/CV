# CV & Cover Letter Generation Environment

This repository uses Python with **ReportLab** and **Pillow** to programmatically generate professional CVs and cover letters as PDFs.

## Setup Overview (Windows)

- **Python Version**: Python 3.12+ (Installed in user profile and added to PATH)
- **Virtual Environment**: Located at `cv/.venv`
- **Dependencies**: Listed in `cv/requirements.txt` (`reportlab`, `pillow`)

---

## How to Build

### Option 1: Build All CVs and Cover Letters
From PowerShell or Command Prompt:
```powershell
cd cv
.\.venv\Scripts\python build_all.py
```
Or simply double-click [build_all.bat](file:///c:/Users/muham/Downloads/cv-20261106T125812Z-1-001/cv/build_all.bat).

### Option 2: Build a Specific CV / Cover Letter
Activate the virtual environment or run directly:
```powershell
cd cv
.\.venv\Scripts\python make_cv.py
# or specific company CVs:
.\.venv\Scripts\python make_cv_wayve.py
.\.venv\Scripts\python make_cover_archangel.py
```

### Option 3: Reinstall / Update Dependencies
If you need to update dependencies in the virtual environment:
```powershell
cd cv
.\.venv\Scripts\pip install -r requirements.txt
```
