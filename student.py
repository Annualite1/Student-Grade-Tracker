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

