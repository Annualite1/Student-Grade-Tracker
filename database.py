import sqlite3

DB_NAME = "school.db"


def connect_db():
    return sqlite3.connect(DB_NAME)


def create_tables():
    conn = connect_db()
    cursor = conn.cursor()

    # Users table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        role TEXT NOT NULL
    )
    """)

    # Students table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        student_id INTEGER PRIMARY KEY,
        full_name TEXT NOT NULL,
        gender TEXT NOT NULL,
        age INTEGER NOT NULL,
        class_name TEXT NOT NULL
    )
    """)

    # Subjects table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS subjects (
        subject_id INTEGER PRIMARY KEY AUTOINCREMENT,
        subject_name TEXT UNIQUE NOT NULL
    )
    """)

    # Grades table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS grades (
        grade_id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER,
        subject_id INTEGER,
        marks REAL,
        FOREIGN KEY(student_id) REFERENCES students(student_id),
        FOREIGN KEY(subject_id) REFERENCES subjects(subject_id)
    )
    """)

    conn.commit()
    conn.close()


def create_default_users():
    conn = connect_db()
    cursor = conn.cursor()

    users = [
        ("admin", "admin123", "Admin"),
        ("teacher", "teacher123", "Teacher"),
    ]

    for user in users:
        try:
            cursor.execute(
                "INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
                user,
            )
        except sqlite3.IntegrityError:
            # user already exists; ignore
            pass

    conn.commit()
    conn.close()


def login(username, password):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT role FROM users WHERE username = ? AND password = ?",
        (username, password),
    )

    result = cursor.fetchone()
    conn.close()

    if result:
        return result[0]
    return None


def add_student(student_id, full_name, gender, age, class_name):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        """
    INSERT INTO students (student_id, full_name, gender, age, class_name)
    VALUES (?, ?, ?, ?, ?)
    """,
        (student_id, full_name, gender, age, class_name),
    )

    conn.commit()
    conn.close()


def get_students():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    conn.close()
    return students


def search_student(student_id):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students WHERE student_id = ?", (student_id,))
    student = cursor.fetchone()

    conn.close()
    return student


if __name__ == "__main__":
    create_tables()
    create_default_users()
    print("Database and tables created successfully!")