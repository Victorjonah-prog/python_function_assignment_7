"""
Attendance Register

Task:
- Track attendance of students.
- Use a dictionary { "student_id": {"name": str, "present_days": list, "absent_days": list} }
- Functions to mark attendance, check history, and get reports.
- Use your head/logic to mark multiple students at once.
- Use **kwargs for flexible reporting (e.g., only_present=True).

// NOT FOR THIS ASSIGNMENT
Future OOP Extension:
- Student class with mark_present() and mark_absent().
- AttendanceRegister class that manages records.
"""

import datetime

attendance = {
    1: {
        "student_id": 1,
        "name": "k9ine",
        "present_days": ["monday", "thursday", "wednesday"],
        "absent_days": ["tuesday", "friday"]
    }
}


def register_student(student_id, name):
    """Register a new student in the attendance dictionary."""
    if student_id in attendance:
        return f"Student ID {student_id} already exists" 
    else:

        attendance[student_id] = {
        "student_id": student_id,
        "name": name,
        "present_days": [],
        "absent_days": []
    }
    return f"Student {name} with ID {student_id} registered successfully"  
print(register_student(2,"mp"))  
print(attendance)        

"""Register a student in the system."""
    

def mark_present(student_ids):
    """Mark multiple students as present for today."""
    today = str(datetime.date.today())
    results = []
    for student_id in student_ids:
        if student_id in attendance:
            if today not in attendance[student_id]["present_days"]:
                attendance[student_id]["present_days"].append(today)
                if today in attendance[student_id]["absent_days"]:
                    attendance[student_id]["absent_days"].remove(today)
                results.append(f"Student ID {student_id} marked present for {today}")
            else:
                results.append(f"Student ID {student_id} already marked present for {today}")
        else:
            results.append(f"Student ID {student_id} not found")
    return results
print(mark_present([]))
print(attendance)    
    
    # implement logic


def mark_absent(student_ids):
    """Mark multiple students as absent for today."""
    today = str(datetime.date.today())
    results = []
    for student_id in student_ids:
        if student_id in attendance:
            if today not in attendance[student_id]["absent_days"]:
                attendance[student_id]["absent_days"].append(today)
                if today in attendance[student_id]["present_days"]:
                    attendance[student_id]["present_days"].remove(today)
                results.append(f"Student ID {student_id} marked absent for {today}")
            else:
                results.append(f"Student ID {student_id} already marked absent for {today}")
        else:
            results.append(f"Student ID {student_id} not found")
    return results
print(mark_absent([1,2]))  
print(attendance)  


def get_report(**kwargs):
    """Generate attendance report with optional filters."""
    report = {}
    for student_id in attendance:
        report[student_id] = {
            "name": attendance[student_id]["name"],
            "present_count": len(attendance[student_id]["present_days"]),
            "absent_count": len(attendance[student_id]["absent_days"])
        }
    return report
    # implement logic

print(get_report())
