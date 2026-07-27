from student import add_student_menu, view_students, search_student_menu, update_student_menu, delete_student_menu
from subjects_module import subject_modules
from grade import grades_module
from report import report_module

def student_menu():
    while True:
      print("\n===== Student Menu =====")
      print("1. Add Student")
      print("2. View Students")
      print("3. Search Student")
      print("4. Update Student")
      print("5. Delete Student")
      print("0. Back")

      choice = input("Enter your choice: ")

      if choice == "1":
        add_student_menu()

      elif choice == "2":
        view_students()

      elif choice == "3":
        search_student_menu()

      elif choice == "4":
        update_student_menu()

      elif choice == "5":
        delete_student_menu()

      elif choice == "0":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")