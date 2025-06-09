# Installation Instructions

## Prerequisites
- Raspberry Pi Zero 2 W
- Python 3 installed
- Git (for code download)

## Steps
```bash
git clone https://github.com/yourname/offline-timetable.git
cd offline-timetable
python3 generate_schedule.py
```
### To view the schedule:
Start a local HTTP server:
python3 -m http.server 8000

Then open this URL in your browser:
http://<your-pi-ip>:8000 (You can get your IP using hostname -I)
