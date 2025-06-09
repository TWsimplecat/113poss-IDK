# User Guide

This system allows users to view and manage a class schedule entirely offline, using CSV files and static HTML pages.

## How to Use

### 1. View the Timetable

After generating the HTML file (`index.html`), you can open it in any browser:

- If using HTTP server:
  ```bash
  python3 -m http.server 8000

Then open http://<your-pi-ip>:8000 in your browser.
Or transfer the file to your computer via SCP or USB and open index.html directly.

### 2. Edit the Timetable
You can edit the schedule using: nano course.csv
### 3. Regenerate the HTML
After editing course.csv, regenerate the HTML file: python3 generate_schedule.py
### 4. One-Step Edit and Update
Use this helper script:./edit_schedule.sh

It will:
Open course.csv for editing
Automatically regenerate index.html after you save and close

## Features for Users
View class schedule with current time and auto-highlighting
Editable with any CSV editor or text editor
No server or internet required
