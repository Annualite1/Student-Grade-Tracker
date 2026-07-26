from student import add_student_menu, view_students
from subjects_module import subject_modules
from grade import grades_module
from report import report_module

def student_menu():
    while True:
        print("\n===== STUDENT MENU =====")
        print("1. Add Student")
        print("2. View Students")
        print("0. Back")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student_menu()

        elif choice == "2":
            view_students()

        elif choice == "0":
            break

        else:
            print("Invalid choice.")

def subject_menu():
    subject_modules()


def grade_menu():
    grades_module()


def report_menu():
    report_module()