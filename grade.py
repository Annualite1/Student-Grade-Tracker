from database import connect_db, get_students
from subjects_module import retrieve_subjects
from grades_validation import  calculate_category, validate_marks

students = get_students()
subjects = retrieve_subjects()

def insert_grades():    
    db = connect_db()
    cursor = db.cursor()
    while True:
        print(students)
        student_id = int(input("Enter student's number that you want to give grades to :"))

        for subject in subjects:
            print(subject)
        subject_id =  int(input("Enter subject id corrsponding to subject that you want to grade: "))

        marks = float(input("Enter Grade: "))
        if not validate_marks(marks):
            print("Marks should be betwen 0 and 100")
            continue

        query = "INSERT INTO grades(student_id, subject_id, marks) VALUES(?, ?, ?)"
        cursor.execute(query, (student_id, subject_id, marks))
        db.commit()
        option = input("Do you want to record another grade? : (yes/ no): ").lower()
        if option != "yes":
            break
    db.close()
    print("Recorded Grades successfully!")
