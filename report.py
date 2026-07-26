from database import connect_db, get_students, search_student
from grades_validation import calculate_category


def generate_student_report(student_id):
    db = connect_db()
    cursor = db.cursor()

    student = search_student(student_id)
    if not student:
        print("No student found with that ID.")
        return

    cursor.execute("""
        SELECT subjects.subject_name, grades.marks
        FROM grades
        JOIN subjects ON grades.subject_id = subjects.subject_id
        WHERE grades.student_id = ?
    """, (student_id,))
    rows = cursor.fetchall()
    db.close()

    if not rows:
        print("No grades recorded yet for this student.")
        return

    marks = [m for name, m in rows]
    average = sum(marks) / len(marks)

    print("\n--- Student Report ---")
    print("Name:", student[1])
    print("Class:", student[4])
    for subject_name, mark in rows:
        print(subject_name, ":", mark)
    print("Average:", average)
    print("Category:", calculate_category(average))


def generate_class_report(class_name):
    db = connect_db()
    cursor = db.cursor()

    cursor.execute("SELECT student_id, full_name FROM students WHERE class_name = ?", (class_name,))
    students = cursor.fetchall()

    print("\n--- Class Report:", class_name, "---")
    for student_id, full_name in students:
        cursor.execute("SELECT AVG(marks) FROM grades WHERE student_id = ?", (student_id,))
        avg = cursor.fetchone()[0]
        if avg is None:
            print(full_name, ": no grades yet")
        else:
            print(full_name, ": average =", avg, "category =", calculate_category(avg))

    db.close()


def display_top_student():
    db = connect_db()
    cursor = db.cursor()

    cursor.execute("""
        SELECT students.full_name, AVG(grades.marks) as avg_marks
        FROM students
        JOIN grades ON students.student_id = grades.student_id
        GROUP BY students.student_id
        ORDER BY avg_marks DESC
        LIMIT 1
    """)
    result = cursor.fetchone()
    db.close()

    if result:
        print("\nTop Student:", result[0], "- Average:", result[1])
    else:
        print("No grades recorded yet.")


def display_lowest_student():
    db = connect_db()
    cursor = db.cursor()

    cursor.execute("""
        SELECT students.full_name, AVG(grades.marks) as avg_marks
        FROM students
        JOIN grades ON students.student_id = grades.student_id
        GROUP BY students.student_id
        ORDER BY avg_marks ASC
        LIMIT 1
    """)
    result = cursor.fetchone()
    db.close()

    if result:
        print("\nLowest Student:", result[0], "- Average:", result[1])
    else:
        print("No grades recorded yet.")


def display_subject_statistics(subject_name):
    db = connect_db()
    cursor = db.cursor()

    cursor.execute("""
        SELECT AVG(grades.marks), MAX(grades.marks), MIN(grades.marks)
        FROM grades
        JOIN subjects ON grades.subject_id = subjects.subject_id
        WHERE subjects.subject_name = ?
    """, (subject_name,))
    result = cursor.fetchone()
    db.close()

    if result and result[0] is not None:
        print("\n--- Subject Stats:", subject_name, "---")
        print("Average:", result[0])
        print("Highest:", result[1])
        print("Lowest:", result[2])
    else:
        print("No grades recorded yet for this subject.")


def report_module():
    while True:
        print("\n===== reports part =====")
        print("1. Student Report")
        print("2. Class Report")
        print("3. Top Student")
        print("4. Lowest Student")
        print("5. Subject Statistics")
        print("0. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            print(get_students())
            student_id = int(input("Enter student ID: "))
            generate_student_report(student_id)
        elif choice == "2":
            class_name = input("Enter class name: ")
            generate_class_report(class_name)
        elif choice == "3":
            display_top_student()
        elif choice == "4":
            display_lowest_student()
        elif choice == "5":
            subject_name = input("Enter subject name: ")
            display_subject_statistics(subject_name)
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    report_module()