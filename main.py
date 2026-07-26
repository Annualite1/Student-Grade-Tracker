students = []

def add_student():
    print("\n--- Add Student ---")

    student_id = input("Enter Student ID: ")
    student_name = input("Enter Student Name: ")
    subject = input("Enter Subject: ")

    student{
        "Student ID": student_id,
        "Student Name": student_name,
        "Subject": subject,
        "Grade": grade
    }
    students.append(student)
    print("Student added successfully!!.")

def view_students():
    if not students:
        print("No students found.")
        return

    print("\n------ STUDENT LIST ------")

    for student in students:
        print(f"""
  Student ID : {student['id']}
  Name       : {student['name']}
  Subject    : {student['subject']}
  Grade      : {student['grade']}
  -----------------------------
  """)
      
def search_student():
    student_id = input("Enter Student ID: ")

    for student in students:
        if student["id"] == student_id:
            print("\nStudent Found")
            print("------------------")
            print(f"ID      : {student['id']}")
            print(f"Name    : {student['name']}")
            print(f"Subject : {student['subject']}")
            print(f"Grade   : {student['grade']}")
            return

    print("Student not found.")

def update_student():
    student_id = input("Enter Student ID: ")

    for student in students:
        if student["id"] == student_id:

            print("\nLeave blank to keep current value.")

            name = input(f"New Name ({student['name']}): ")
            subject = input(f"New Subject ({student['subject']}): ")
            grade = input(f"New Grade ({student['grade']}): ")

            if name:
                student["name"] = name

            if subject:
                student["subject"] = subject

            if grade:
                student["grade"] = float(grade)

            print("Student updated successfully!")
            return

    print("Student not found.")

def delete_student():
    student_id = input("Enter Student ID: ")

    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            print("Student deleted successfully!")
            return

    print("Student not found.")

def main():
    while True:
        print("\n=======================================")
        print("      STUDENT GRADE TRACKER")
        print("=======================================")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")
        print("=======================================")

         choice = input("Enter your choice (1-8): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("Thank you for using Student Grade Tracker!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
