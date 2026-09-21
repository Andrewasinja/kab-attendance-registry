import json
import os
from datetime import datetime

DATA_FILE = "attendance_log.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return {"students": {}, "logs": []}
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def create_student(student_id, name):
    data = load_data()
    if student_id in data["students"]:
        print(f"Student ID {student_id} already exists.")
        return
    data["students"][student_id] = name
    save_data(data)
    print(f"Student '{name}' registered successfully.")

def log_check_in(student_id, status):
    if status not in ["Present", "Late"]:
        print("Invalid status! Use 'Present' or 'Late'.")
        return
    data = load_data()
    if student_id not in data["students"]:
        print("Student not found.")
        return

    entry = {
        "student_id": student_id,
        "status": status,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "date": datetime.now().strftime("%Y-%m-%d")
    }
    data["logs"].append(entry)
    save_data(data)
    print(f"Check-in recorded: {data['students'][student_id]} marked as {status}.")

def today_summary():
    data = load_data()
    today = datetime.now().strftime("%Y-%m-%d")
    print(f"\n--- Check-Ins Today ({today}) ---")
    found = False
    for log in data["logs"]:
        if log["date"] == today:
            name = data["students"].get(log["student_id"], "Unknown")
            print(f"- {name} ({log['student_id']}): {log['status']} at {log['timestamp']}")
            found = True
    if not found:
        print("No check-ins recorded for today.")