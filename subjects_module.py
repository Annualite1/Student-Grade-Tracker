from database import connect_db

def insert_subjects():    
    db = connect_db()
    cursor = db.cursor()
    while True:
        subject_name = input("Enter subject name: ")
        query = "INSERT INTO subjects(subject_name) VALUES(?)"
        cursor.execute(query, (subject_name,))
        db.commit()
        option = input("Do you want to record another subject: (yes/ no): ").lower()
        if option != "yes":
            break
    db.close()
    print("Inserted New subject successfully!")

def retrieve_subjects():
    try:
       db = connect_db()
       cursor = db.cursor()
       cursor.execute("SELECT * FROM subjects")
       subjects = cursor.fetchall()
       for subject in subjects:
            print(subject)
       return subjects
    except Exception as e:
        return ("Oooops Error", e)
    finally:
        if db:
            cursor.close()
            db.close()


def update_subject():

    try:
        db = connect_db()
        cursor = db.cursor()
        update = input("Do you want to update any subject? (yes/ no): ").lower() 
        if update == "yes":
            subject_name = input("Enter the subject you want to update: ")
            new_subject_name = input("Enter new subject name: ")
            query = "UPDATE subjects SET subject_name=? WHERE subject_name=?"
            cursor.execute(query, (new_subject_name, subject_name))
            db.commit()
        
        
    except Exception as e:
        return ("Oooops Error", e)
    finally:
        if db:
            cursor.close()
            db.close()

def delete_subject():
    try:
       db = connect_db()
       cursor = db.cursor() 
       opt = input("Do you want to delete any subject? (yes/ no) :").lower()
       if opt == "yes":
           subject_name = input("Enter the subject you want to delete: ").lower()
           query = "DELETE FROM subjects WHERE subject_name=?"
           cursor.execute(query, (subject_name, ))
           db.commit()
           if cursor.rowcount > 0:
            print( f"{subject_name} deleted successfully.")
           else:
            print (f"{subject_name} was not found.")
       
       elif opt == "no":
           return("You chose No!")
       else:
           return ("Invalid Choice!!!")

    except Exception as e:
        return ("Oooops Error", e)
    finally:
        if db:
            cursor.close()
            db.close()
