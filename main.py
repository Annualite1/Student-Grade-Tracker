from student_menu import student_menu, subject_menu, grade_menu, report_menu
from database import create_tables, create_default_users, login

def main_menu():

    while True:
        print("\n========================================")
        print("     STUDENT GRADE TRACKER SYSTEM")
        print("========================================")
        print("1. Student Management")
        print("2. Subject Management")
        print("3. Grade Management")
        print("4. Reports")
        print("5. Exit")
        print("========================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            student_menu()

        elif choice == "2":
            subject_menu()

        elif choice == "3":
            grade_menu()

        elif choice == "4":
            report_menu()

        elif choice == "5":
            print("Thank you for using the system.")
            break

        else:
            print("Invalid choice.")


def login_menu():

    print("===================================")
    print(" STUDENT GRADE TRACKER SYSTEM")
    print("===================================")

    while True:

        username = input("Username: ")
        password = input("Password: ")

        role = login(username, password)

        if role:
            print(f"\nWelcome {role}!\n")
            main_menu()
            break

        else:
            print("Invalid username or password.\n")


if __name__ == "__main__":

    create_tables()
    create_default_users()
    login_menu()
