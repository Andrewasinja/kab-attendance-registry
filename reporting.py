import json
import os

DATA_FILE = "attendance_log.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return {"students": {}, "logs": []}
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def log_absence(student_id, date_str):
    data = load_data()
    if student_id not in data["students"]:
        print("Student not found.")
        return
    entry = {
        "student_id": student_id,
        "status": "Absent",
        "timestamp": f"{date_str} 00:00:00",
        "date": date_str
    }
    data["logs"].append(entry)
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)
    print(f"Recorded absence for {data['students'][student_id]} on {date_str}.")

def calculate_attendance_health():
    data = load_data()
    students = data["students"]
    logs = data["logs"]

    if not students or not logs:
        print("Insufficient data for health score calculation.")
        return {}

    total_days = len(set(log["date"] for log in logs))
    if total_days == 0:
        return {}

    health_scores = {}
    for sid, name in students.items():
        attended_days = len([
            log for log in logs 
            if log["student_id"] == sid and log["status"] in ["Present", "Late"]
        ])
        rate = (attended_days / total_days) * 100
        health_scores[sid] = {"name": name, "rate": rate}
    return health_scores

def report_chronic_absentees(threshold=85.0):
    scores = calculate_attendance_health()
    print(f"\n--- Chronically Absent Students (< {threshold}%) ---")
    found = False
    for sid, info in scores.items():
        if info["rate"] < threshold:
            print(f"- {info['name']} ({sid}): {info['rate']:.1f}% attendance")
            found = True
    if not found:
        print("No students are currently flagged for chronic absence.")
