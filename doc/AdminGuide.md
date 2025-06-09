
## 📄 `AdminGuide.md`

# Admin Guide

This document describes how to configure and maintain the offline timetable system on Raspberry Pi Zero 2 W.

## Configuration

### File Structure

All files should be placed in: /root/schedule_project/


Essential files:

- `course.csv` — the schedule data
- `generate_schedule.py` — generates `index.html`
- `index.html` — the final page for display
- `edit_schedule.sh` — helper script for editing
- `upload_form.html`, `upload_server.py` — (optional) local tools not used in final version

### Initial Setup

1. Clone the repository:

git clone https://github.com/TWsimplecat/113poss-IDK.git
cd 113poss-IDK/schedule_project

2.Generate HTML page:
python3 generate_schedule.py

3.Start HTTP server (if needed):
python3 -m http.server 8000
