from flask import Flask, render_template, request, redirect
import sqlite3
import csv
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

def get_courses_by_week():
    conn = sqlite3.connect('course.db')
    c = conn.cursor()
    c.execute("SELECT id, day, time, subject, location, teacher, note FROM courses")
    rows = c.fetchall()
    conn.close()

    time_slots = sorted(list(set(row[2] for row in rows)))
    weekdays = ['一', '二', '三', '四', '五']

    schedule = {time: {day: None for day in weekdays} for time in time_slots}
    for row in rows:
        course_id, day, time, subject, location, teacher, note = row
        if day in weekdays:
            schedule[time][day] = {
                'id': course_id,
                'subject': subject,
                'location': location,
                'teacher': teacher,
                'note': note,
                'time': time
            }
    return schedule, time_slots, weekdays

def add_course(day, time, subject, location, teacher):
    conn = sqlite3.connect('course.db')
    c = conn.cursor()
    c.execute("INSERT INTO courses (day, time, subject, location, teacher) VALUES (?, ?, ?, ?, ?)",
              (day, time, subject, location, teacher))
    conn.commit()
    conn.close()

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        day = request.form['day']
        time = request.form['time']
        subject = request.form['subject']
        location = request.form['location']
        teacher = request.form['teacher']
        add_course(day, time, subject, location, teacher)
        return redirect('/')
    
    schedule, time_slots, weekdays = get_courses_by_week()
    return render_template("index.html", schedule=schedule, times=time_slots, days=weekdays)

@app.route('/delete/<int:course_id>', methods=['POST'])
def delete_course(course_id):
    conn = sqlite3.connect('course.db')
    c = conn.cursor()
    c.execute("DELETE FROM courses WHERE id = ?", (course_id,))
    conn.commit()
    conn.close()
    return redirect('/')

@app.route('/upload', methods=['POST'])
def upload_csv():
    file = request.files['csv_file']
    if not file:
        return redirect('/')
    filename = secure_filename(file.filename)
    filepath = os.path.join('uploads', filename)
    os.makedirs('uploads', exist_ok=True)
    file.save(filepath)

    with open(filepath, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            day = row.get('day')
            time = row.get('time')
            subject = row.get('subject')
            location = row.get('location', '')
            teacher = row.get('teacher', '')
            add_course(day, time, subject, location, teacher)

    os.remove(filepath)
    return redirect('/')

@app.route('/note/<int:course_id>', methods=['POST'])
def update_note(course_id):
    note = request.form['note']
    conn = sqlite3.connect('course.db')
    c = conn.cursor()
    c.execute("UPDATE courses SET note = ? WHERE id = ?", (note, course_id))
    conn.commit()
    conn.close()
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
