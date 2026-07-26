from database import (
    add_student,
    get_students,
    search_student,
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


if __name__ == "__main__":
    add_student_menu()