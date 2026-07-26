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


def retrieve_grades():
    try:
       db = connect_db()
       cursor = db.cursor()
       cursor.execute(
           """SELECT grades.grade_id, students.full_name, subjects.subject_name, grades.marks 
           FROM grades JOIN subjects on grades.subject_id=subjects.subject_id 
           JOIN students on grades.student_id=students.student_id""")
       grades = cursor.fetchall()
       return grades      
    except Exception as e:
        return ("Oooops Error", e)
    finally:
        if db:
            cursor.close()
            db.close()


def update_grade():

    try:
        db = connect_db()
        cursor = db.cursor()
        print(retrieve_grades())
        grade_id = input("Enter Student's id whom you want to upgrade his marks ")
        mark = int(input("Enter new grade :"))
        query = "UPDATE grades SET marks=? WHERE grade_id=?"
        cursor.execute(query, (mark, grade_id))
        db.commit()
        print("Updated Marks Successfully!!")
        
    except Exception as e:
        return ("Oooops Error", e)
    finally:
        if db:
            cursor.close()
            db.close()

