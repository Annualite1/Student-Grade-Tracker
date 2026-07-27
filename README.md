# Student Grade Tracker

A simple command-line app we built in Python (with SQLite for storage) that lets a teacher or admin log in and manage students, subjects, and grades — and pull up reports on how everyone's doing.

## What it does

Once you log in, you land on a main menu with four areas:

- **Students** – add new students, view the list, update or delete a record. Basic validation is in place too, so you can't save an empty name or a negative age.
- **Subjects** – add, view, update, and delete subjects.
- **Grades** – record a mark for a student in a subject, view/update/delete grades, and calculate a student's average. Marks have to fall between 0 and 100, otherwise it'll ask you to re-enter.
- **Reports** – individual student reports, a full class report, the top and lowest performing student, and stats per subject (average/highest/lowest).

Averages get turned into a letter grade using this scale:

| Average | Grade |
|---|---|
| 80–100 | A |
| 70–79 | B |
| 60–69 | C |
| 50–59 | D |
| below 50 | F |

## How the files fit together

```
Student-Grade-Tracker/
├── main.py               # starts the app, handles login, main menu
├── student_menu.py       # student sub-menu, hooks into the other modules
├── student.py             # everything student-related (add, view, validate)
├── subjects_module.py     # subject CRUD
├── grade.py                # grade CRUD + calculating averages
├── grades_validation.py    # checks marks are 0–100, converts avg to letter grade
├── report.py                # student/class reports, top & lowest student, subject stats
├── database.py               # sets up SQLite, creates tables, handles login
└── README.md
```

## Running it

You just need Python 3 installed — no extra packages, it's all standard library.

```bash
git clone https://github.com/<org-or-user>/Student-Grade-Tracker.git
cd Student-Grade-Tracker
python main.py
```

The first time you run it, it sets up the database tables and some default users automatically, then asks you to log in.

Once you're in, just follow the numbered menus — enter a number, hit enter, and it'll walk you through whatever you're trying to do (add a student, record a grade, pull a report, etc). If you type something invalid, it'll just tell you and let you try again rather than crashing.

## Behind the scenes (database)

Four tables: `users` (login info + role), `students`, `subjects`, and `grades` (which links a student and a subject to a mark).

## Who worked on what

| Member | Focus | Files |
|---|---|---|
| Member 1 | Database & login | `database.py` |
| Member 2 | Student management | `student.py` |
| Member 3 | Subjects & grades | `subjects_module.py`, `grade.py`, `grades_validation.py` |
| Member 4 | Reports | `report.py` |
| Member 5 | Menus & tying it all together | `main.py`, `student_menu.py` |
| Member 6 | Testing, README, screenshots & presentation | — |

## Screenshots

*(swap these placeholders for real screenshots before submitting — GitHub repo view, commit history, and the app actually running: login, each menu, and a sample report)*

- [ ] GitHub repo / file structure
- [ ] Commit history
- [ ] App: login screen
- [ ] App: main menu
- [ ] App: student / subject / grade / report sub-menus
- [ ] App: a sample report output

## Testing

We went through the CRUD operations in every module by hand — adding, viewing, updating, deleting students/subjects/grades — and checked the validation catches the obvious bad input (letters where a number's expected, empty names, marks outside 0–100, that kind of thing). Reports were also tested on students who don't have any grades yet, to make sure it doesn't break.

## Ideas for later

- Hash the passwords instead of storing them as-is
- Let reports be exported to CSV or PDF
- Add proper automated tests instead of just manual testing
