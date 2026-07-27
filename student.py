from database import (
    add_student,
    get_students,
    search_student,
    update_student,
    delete_student,
)

def validate_student(student_id, full_name, gender, age, class_name):
    """
    Validate student information before saving.
    """

    if not str(student_id).isdigit():
        print("Student ID must be a number.")
        return False

    if full_name.strip() == "":
        print("Student name cannot be empty.")
        return False

    if gender.lower() not in ["male", "female"]:
        print("Gender must be Male or Female.")
        return False

    if not str(age).isdigit() or int(age) <= 0:
        print("Age must be a positive number.")
        return False

    if class_name.strip() == "":
        print("Class name cannot be empty.")
        return False

    return True





def add_student_menu():
    """
    Get student information from the user and save it to the database.
    """

    student_id = input("Enter Student ID: ")
    full_name = input("Enter Full Name: ")
    gender = input("Enter Gender (Male/Female): ")
    age = input("Enter Age: ")
    class_name = input("Enter Class Name: ")

    if validate_student(student_id, full_name, gender, age, class_name):
        try:
            add_student(
                int(student_id),
                full_name,
                gender,
                int(age),
                class_name
            )
            print("Student added successfully!")

        except Exception as e:
            print("Error:", e)

def view_students():
    """
    Display all students in the database.
    """
    students = get_students()

    if not students:
        print("No students found.")
        return

    print("\n------ Student List ------")

    for student in students:
        print(f"ID: {student[0]}")
        print(f"Name: {student[1]}")
        print(f"Gender: {student[2]}")
        print(f"Age: {student[3]}")
        print(f"Class: {student[4]}")
        print("-" * 30)

def search_student_menu():
    """
    Search for a student by ID.
    """

    student_id = input("Enter Student ID: ")

    if not student_id.isdigit():
        print("Student ID must be a number.")
        return

    student = search_student(int(student_id))

    if student:
        print("\n------ Student Found ------")
        print(f"ID: {student[0]}")
        print(f"Name: {student[1]}")
        print(f"Gender: {student[2]}")
        print(f"Age: {student[3]}")
        print(f"Class: {student[4]}")
    else:
        print("Student not found.")

def update_student_menu():
    """
    Update student information.
    """

    student_id = input("Enter Student ID to update: ")

    if not student_id.isdigit():
        print("Student ID must be a number.")
        return

    student = search_student(int(student_id))

    if not student:
        print("Student not found.")
        return

    print("\nLeave blank to keep the current value.")

    full_name = input(f"Full Name ({student[1]}): ")
    gender = input(f"Gender ({student[2]}): ")
    age = input(f"Age ({student[3]}): ")
    class_name = input(f"Class ({student[4]}): ")

    if full_name == "":
        full_name = student[1]

    if gender == "":
        gender = student[2]

    if age == "":
        age = student[3]
    else:
        age = int(age)

    if class_name == "":
        class_name = student[4]

    if update_student(
        int(student_id),
        full_name,
        gender,
        age,
        class_name,
    ):
        print("Student updated successfully!")
    else:
        print("Update failed.")

def delete_student_menu():
    """
    Delete a student.
    """

    student_id = input("Enter Student ID to delete: ")

    if not student_id.isdigit():
        print("Student ID must be a number.")
        return

    confirm = input("Are you sure? (yes/no): ").lower()

    if confirm != "yes":
        print("Deletion cancelled.")
        return

    if delete_student(int(student_id)):
        print("Student deleted successfully!")
    else:
        print("Student not found.")

if __name__ == "__main__":
    while True:
        print("\n===== Student Menu =====")
        print("1. Add Student")
        print("2. View Students")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student_menu()

        elif choice == "2":
            view_students()

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

   
