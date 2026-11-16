"""main.py - CRUD app for the students table."""
import sys
from datetime import date
from db import get_connection

"""the collection of all students being returned"""
def getAllStudents():
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT student_id, first_name, last_name, email, enrollment_date "
                "FROM students ORDER BY student_id;"
            )
            rows = cur.fetchall()
        if not rows:
            print("(No students found)")
            return
        print(f"{'ID':<5}{'First Name':<15}{'Last Name':<15}{'Email':<30}{'Enrollment Date'}")
        print("-" * 80)
        for sid, first, last, email, enr in rows:
            print(f"{sid:<5}{first:<15}{last:<15}{email:<30}{enr}")
    except Exception as e:
        print(f"Error retrieving students: {e}")
    finally:
        conn.close()

"""adding a student to the postgre database and returning info"""
def addStudent(first_name, last_name, email, enrollment_date):
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO students (first_name, last_name, email, enrollment_date) "
                "VALUES (%s, %s, %s, %s) RETURNING student_id;",
                (first_name, last_name, email, enrollment_date),
            )
            new_id = cur.fetchone()[0]
        conn.commit()
        print(f"Added student '{first_name} {last_name}' with ID {new_id}.")
    except Exception as e:
        conn.rollback()
        print(f"Error adding student: {e}")
    finally:
        conn.close()

"""changing the email in both the database and returning"""
def updateStudentEmail(student_id, new_email):
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(
                "UPDATE students SET email = %s WHERE student_id = %s;",
                (new_email, student_id),
            )
            if cur.rowcount == 0:
                print(f"No student found with ID {student_id}.")
            else:
                print(f"Updated email for student {student_id} to {new_email}.")
        conn.commit()
    except Exception as e:
        conn.rollback()
        print(f"Error updating email: {e}")
    finally:
        conn.close()

"""delete that student brah"""
def deleteStudent(student_id):
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM students WHERE student_id = %s;", (student_id,))
            if cur.rowcount == 0:
                print(f"No student found with ID {student_id}.")
            else:
                print(f"Deleted student with ID {student_id}.")
        conn.commit()
    except Exception as e:
        conn.rollback()
        print(f"Error deleting student: {e}")
    finally:
        conn.close()

"""print the menu. Use the nice === so it looks pretty, as seen in COMP2404"""
def menu():
    while True:
        print("\n===== Student Database Menu =====")
        print("1. Get all students")
        print("2. Add a student")
        print("3. Update a student's email")
        print("4. Delete a student")
        print("5. Exit")
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            getAllStudents()
        elif choice == "2":
            first = input("First name: ").strip()
            last  = input("Last name: ").strip()
            email = input("Email: ").strip()
            enr   = input("Enrollment date (YYYY-MM-DD): ").strip()
            addStudent(first, last, email, enr or date.today().isoformat())
        elif choice == "3":
            sid = int(input("Student ID: ").strip())
            email = input("New email: ").strip()
            updateStudentEmail(sid, email)
        elif choice == "4":
            sid = int(input("Student ID: ").strip())
            deleteStudent(sid)
        elif choice == "5":
            print("Goodbye!")
            sys.exit(0)
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    menu()
