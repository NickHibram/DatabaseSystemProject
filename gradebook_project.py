#!/usr/bin/env python3
"""
Grade Book Database Project
SQLite + Python implementation for Tasks 2–12
with human-readable codes for students, courses, categories, and assignments.
"""

import sqlite3
import os

DB_NAME = "gradebook.db"


def connect():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn


def reset_database():
    if os.path.exists(DB_NAME):
        os.remove(DB_NAME)


def create_tables():
    conn = connect()
    cur = conn.cursor()

    cur.executescript("""
    CREATE TABLE Student (
        student_id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_code TEXT UNIQUE NOT NULL,
        first_name TEXT NOT NULL,
        last_name  TEXT NOT NULL,
        email      TEXT UNIQUE NOT NULL
    );

    CREATE TABLE Course (
        course_id     INTEGER PRIMARY KEY AUTOINCREMENT,
        course_code   TEXT UNIQUE NOT NULL,
        department    TEXT NOT NULL,
        course_number TEXT NOT NULL,
        course_name   TEXT NOT NULL,
        semester      TEXT NOT NULL CHECK(semester IN ('Spring','Summer','Fall','Winter')),
        year          INTEGER NOT NULL
    );

    CREATE TABLE Enrollment (
        enrollment_id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id    INTEGER NOT NULL,
        course_id     INTEGER NOT NULL,
        FOREIGN KEY (student_id) REFERENCES Student(student_id) ON DELETE CASCADE,
        FOREIGN KEY (course_id)  REFERENCES Course(course_id) ON DELETE CASCADE,
        UNIQUE(student_id, course_id)
    );

    CREATE TABLE GradeCategory (
        category_id   INTEGER PRIMARY KEY AUTOINCREMENT,
        category_code TEXT UNIQUE NOT NULL,
        course_id     INTEGER NOT NULL,
        category_name TEXT NOT NULL,
        weight        REAL NOT NULL CHECK(weight > 0 AND weight <= 100),
        FOREIGN KEY (course_id) REFERENCES Course(course_id) ON DELETE CASCADE,
        UNIQUE(course_id, category_name)
    );

    CREATE TABLE Assignment (
        assignment_id   INTEGER PRIMARY KEY AUTOINCREMENT,
        assignment_code TEXT UNIQUE NOT NULL,
        category_id     INTEGER NOT NULL,
        assignment_name TEXT NOT NULL,
        max_points      REAL NOT NULL DEFAULT 100,
        FOREIGN KEY (category_id) REFERENCES GradeCategory(category_id) ON DELETE CASCADE
    );

    CREATE TABLE Score (
        score_id      INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id    INTEGER NOT NULL,
        assignment_id INTEGER NOT NULL,
        points_earned REAL NOT NULL CHECK(points_earned >= 0),
        FOREIGN KEY (student_id) REFERENCES Student(student_id) ON DELETE CASCADE,
        FOREIGN KEY (assignment_id) REFERENCES Assignment(assignment_id) ON DELETE CASCADE,
        UNIQUE(student_id, assignment_id)
    );
    """)
    conn.commit()
    conn.close()


def insert_data():
    conn = connect()
    cur = conn.cursor()

    cur.executescript("""
    INSERT INTO Student (student_code, first_name, last_name, email)
    VALUES
    ('NIABRAM', 'Nicholas', 'Abram', 'nicholas.abram@bison.howard.edu'),
    ('ZOHALL', 'Zoey', 'Hall', 'zoey.hall@bison.howard.edu'),
    ('JOQUINN', 'Jordan', 'Quinn', 'jordan.quinn@bison.howard.edu'),
    ('AVCARTER', 'Ava', 'Carter', 'ava.carter@bison.howard.edu'),
    ('MAEVANS', 'Malik', 'Evans', 'malik.evans@bison.howard.edu'),
    ('TABROOKS', 'Taylor', 'Brooks', 'taylor.brooks@bison.howard.edu'),
    ('JAREED', 'Jasmine', 'Reed', 'jasmine.reed@bison.howard.edu'),
    ('ETCOLEMAN', 'Ethan', 'Coleman', 'ethan.coleman@bison.howard.edu'),
    ('MATURNER', 'Maya', 'Turner', 'maya.turner@bison.howard.edu');

    INSERT INTO Course (course_code, department, course_number, course_name, semester, year)
    VALUES
    ('CSCI432', 'CSCI', '432', 'Database Systems', 'Spring', 2026),
    ('CSCI363', 'CSCI', '363', 'Large Scale Programming', 'Spring', 2026),
    ('CSCI350', 'CSCI', '350', 'Structure of Programming Languages', 'Spring', 2026);

    INSERT INTO Enrollment (student_id, course_id)
    VALUES
    (1,1),(1,2),(1,3),
    (2,1),(2,2),(2,3),
    (3,1),(3,2),
    (4,1),(4,3),
    (5,2),(5,3),
    (6,1),
    (7,2),
    (8,3),
    (9,1),(9,2);

    INSERT INTO GradeCategory (category_code, course_id, category_name, weight)
    VALUES
    ('CSCI432_PART',1,'Participation',20),
    ('CSCI432_HW',1,'Homework',20),
    ('CSCI432_TEST',1,'Tests',30),
    ('CSCI432_PROJ',1,'Projects',30),

    ('CSCI363_PART',2,'Participation',20),
    ('CSCI363_HW',2,'Homework',20),
    ('CSCI363_TEST',2,'Tests',30),
    ('CSCI363_PROJ',2,'Projects',30),

    ('CSCI350_PART',3,'Participation',20),
    ('CSCI350_HW',3,'Homework',20),
    ('CSCI350_TEST',3,'Tests',30),
    ('CSCI350_PROJ',3,'Projects',30);

    INSERT INTO Assignment (assignment_code, category_id, assignment_name, max_points)
    VALUES
    ('CSCI432_PART',1, 'CSCI 432 Participation', 100),
    ('CSCI432_HW1',2, 'CSCI 432 HW1', 100),
    ('CSCI432_HW2',2, 'CSCI 432 HW2', 100),
    ('CSCI432_HW3',2, 'CSCI 432 HW3', 100),
    ('CSCI432_HW4',2, 'CSCI 432 HW4', 100),
    ('CSCI432_TEST1',3, 'CSCI 432 Test 1', 100),
    ('CSCI432_TEST2',3, 'CSCI 432 Test 2', 100),
    ('CSCI432_PROJ1',4, 'CSCI 432 Project 1', 100),

    ('CSCI363_PART',5, 'CSCI 363 Participation', 100),
    ('CSCI363_HW1',6, 'CSCI 363 HW1', 100),
    ('CSCI363_HW2',6, 'CSCI 363 HW2', 100),
    ('CSCI363_TEST1',7, 'CSCI 363 Test 1', 100),
    ('CSCI363_TEST2',7, 'CSCI 363 Test 2', 100),
    ('CSCI363_PROJ1',8, 'CSCI 363 Project 1', 100),
    ('CSCI363_PROJ2',8, 'CSCI 363 Project 2', 100),

    ('CSCI350_PART',9, 'CSCI 350 Participation', 100),
    ('CSCI350_HW1',10, 'CSCI 350 HW1', 100),
    ('CSCI350_HW2',10, 'CSCI 350 HW2', 100),
    ('CSCI350_HW3',10, 'CSCI 350 HW3', 100),
    ('CSCI350_TEST1',11, 'CSCI 350 Test 1', 100),
    ('CSCI350_TEST2',11, 'CSCI 350 Test 2', 100),
    ('CSCI350_PROJ1',12, 'CSCI 350 Project 1', 100);
    """)

    scores = [
        (1,1,95),(1,2,96),(1,3,94),(1,4,95),(1,5,96),(1,6,94),(1,7,95),(1,8,96),
        (2,1,94),(2,2,95),(2,3,96),(2,4,95),(2,5,94),(2,6,96),(2,7,95),(2,8,95),
        (3,1,84),(3,2,86),(3,3,80),(3,4,82),(3,5,85),(3,6,83),(3,7,81),(3,8,87),
        (4,1,88),(4,2,90),(4,3,87),(4,4,85),(4,5,89),(4,6,86),(4,7,88),(4,8,91),
        (6,1,76),(6,2,79),(6,3,81),(6,4,74),(6,5,78),(6,6,80),(6,7,77),(6,8,82),
        (9,1,91),(9,2,89),(9,3,90),(9,4,92),(9,5,88),(9,6,90),(9,7,91),(9,8,93),

        (1,9,95),(1,10,96),(1,11,94),(1,12,95),(1,13,96),(1,14,94),(1,15,95),
        (2,9,94),(2,10,95),(2,11,96),(2,12,95),(2,13,94),(2,14,96),(2,15,95),
        (3,9,82),(3,10,84),(3,11,86),(3,12,80),(3,13,83),(3,14,85),(3,15,81),
        (5,9,88),(5,10,87),(5,11,90),(5,12,86),(5,13,89),(5,14,88),(5,15,91),
        (7,9,79),(7,10,81),(7,11,78),(7,12,80),(7,13,82),(7,14,77),(7,15,83),
        (9,9,90),(9,10,91),(9,11,89),(9,12,92),(9,13,90),(9,14,88),(9,15,91),

        (1,16,95),(1,17,96),(1,18,94),(1,19,95),(1,20,96),(1,21,94),(1,22,95),
        (2,16,94),(2,17,95),(2,18,96),(2,19,95),(2,20,94),(2,21,96),(2,22,95),
        (4,16,89),(4,17,90),(4,18,88),(4,19,87),(4,20,91),(4,21,89),(4,22,90),
        (5,16,84),(5,17,82),(5,18,86),(5,19,85),(5,20,83),(5,21,87),(5,22,84),
        (8,16,78),(8,17,80),(8,18,77),(8,19,79),(8,20,81),(8,21,76),(8,22,80),
    ]
    cur.executemany(
        "INSERT INTO Score (student_id, assignment_id, points_earned) VALUES (?, ?, ?)",
        scores
    )

    conn.commit()
    conn.close()


def print_query(title, query, params=()):
    conn = connect()
    cur = conn.cursor()
    cur.execute(query, params)
    rows = cur.fetchall()
    print(f"\n{'='*90}\n{title}\n{'='*90}")
    if not rows:
        print("(no rows)")
        conn.close()
        return
    headers = rows[0].keys()
    print(" | ".join(headers))
    print("-" * 90)
    for row in rows:
        print(" | ".join(str(row[h]) for h in headers))
    conn.close()


def show_all_tables():
    for table in ["Student", "Course", "Enrollment", "GradeCategory", "Assignment", "Score"]:
        print_query(f"Table: {table}", f"SELECT * FROM {table};")


def task4():
    print_query(
        "Task 4: Average / Highest / Lowest score for CSCI 432 HW1",
        """
        SELECT 
            c.course_code,
            a.assignment_code,
            a.assignment_name,
            AVG(s.points_earned) AS average_score,
            MAX(s.points_earned) AS highest_score,
            MIN(s.points_earned) AS lowest_score
        FROM Course c
        JOIN GradeCategory gc ON c.course_id = gc.course_id
        JOIN Assignment a ON gc.category_id = a.category_id
        JOIN Score s ON a.assignment_id = s.assignment_id
        WHERE c.course_code = 'CSCI432'
          AND a.assignment_code = 'CSCI432_HW1'
        GROUP BY c.course_code, a.assignment_code, a.assignment_name;
        """
    )


def task5():
    print_query(
        "Task 5: Students in CSCI432",
        """
        SELECT 
            s.student_id,
            s.student_code,
            s.first_name,
            s.last_name,
            s.email
        FROM Student s
        JOIN Enrollment e ON s.student_id = e.student_id
        JOIN Course c ON e.course_id = c.course_id
        WHERE c.course_code = 'CSCI432'
        ORDER BY s.last_name, s.first_name;
        """
    )


def task6():
    print_query(
        "Task 6: Students in CSCI432 and all assignment scores",
        """
        SELECT 
            s.student_code,
            s.first_name,
            s.last_name,
            a.assignment_code,
            a.assignment_name,
            sc.points_earned
        FROM Student s
        JOIN Enrollment e ON s.student_id = e.student_id
        JOIN Course c ON e.course_id = c.course_id
        JOIN GradeCategory gc ON c.course_id = gc.course_id
        JOIN Assignment a ON gc.category_id = a.category_id
        LEFT JOIN Score sc 
            ON s.student_id = sc.student_id 
           AND a.assignment_id = sc.assignment_id
        WHERE c.course_code = 'CSCI432'
        ORDER BY s.last_name, s.first_name, a.assignment_code;
        """
    )


def task7():
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO Assignment (assignment_code, category_id, assignment_name, max_points)
        VALUES (
            'CSCI432_HW5',
            (
                SELECT gc.category_id
                FROM GradeCategory gc
                JOIN Course c ON gc.course_id = c.course_id
                WHERE c.course_code = 'CSCI432'
                  AND gc.category_name = 'Homework'
            ),
            'CSCI 432 HW5',
            100
        );
    """)
    conn.commit()
    conn.close()
    print_query("Task 7: New assignment added", "SELECT * FROM Assignment WHERE assignment_code = 'CSCI432_HW5';")


def task8():
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
        UPDATE GradeCategory
        SET weight = CASE category_name
            WHEN 'Participation' THEN 10
            WHEN 'Homework' THEN 30
            WHEN 'Tests' THEN 30
            WHEN 'Projects' THEN 30
        END
        WHERE course_id = (
            SELECT course_id
            FROM Course
            WHERE course_code = 'CSCI432'
        );
    """)
    conn.commit()
    conn.close()
    print_query(
        "Task 8: Updated weights for CSCI432",
        """
        SELECT gc.category_code, gc.category_name, gc.weight
        FROM GradeCategory gc
        JOIN Course c ON gc.course_id = c.course_id
        WHERE c.course_code = 'CSCI432'
        ORDER BY gc.category_id;
        """
    )


def task9():
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
        UPDATE Score
        SET points_earned = MIN(points_earned + 2, 100)
        WHERE assignment_id = (
            SELECT a.assignment_id
            FROM Assignment a
            WHERE a.assignment_code = 'CSCI432_HW1'
        );
    """)
    conn.commit()
    conn.close()
    print_query(
        "Task 9: Scores after adding 2 points to everyone on CSCI432_HW1",
        """
        SELECT s.student_code, s.first_name, s.last_name, a.assignment_code, sc.points_earned
        FROM Score sc
        JOIN Student s ON sc.student_id = s.student_id
        JOIN Assignment a ON sc.assignment_id = a.assignment_id
        WHERE a.assignment_code = 'CSCI432_HW1'
        ORDER BY s.last_name, s.first_name;
        """
    )


def task10():
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
        UPDATE Score
        SET points_earned = MIN(points_earned + 2, 100)
        WHERE assignment_id = (
            SELECT a.assignment_id
            FROM Assignment a
            WHERE a.assignment_code = 'CSCI432_HW1'
        )
        AND student_id IN (
            SELECT student_id
            FROM Student
            WHERE last_name LIKE '%Q%'
        );
    """)
    conn.commit()
    conn.close()
    print_query(
        "Task 10: Scores after adding 2 points to students with Q in last name",
        """
        SELECT s.student_code, s.first_name, s.last_name, a.assignment_code, sc.points_earned
        FROM Score sc
        JOIN Student s ON sc.student_id = s.student_id
        JOIN Assignment a ON sc.assignment_id = a.assignment_id
        WHERE a.assignment_code = 'CSCI432_HW1'
        ORDER BY s.last_name, s.first_name;
        """
    )


def task11():
    print_query(
        "Task 11: Final grade for Nicholas Abram in CSCI432",
        """
        WITH category_results AS (
            SELECT 
                gc.category_code,
                gc.category_name,
                gc.weight,
                SUM(sc.points_earned) AS earned_points,
                SUM(a.max_points) AS total_points,
                ((SUM(sc.points_earned) * 1.0) / SUM(a.max_points)) * gc.weight AS category_contribution
            FROM Student s
            JOIN Enrollment e ON s.student_id = e.student_id
            JOIN Course c ON e.course_id = c.course_id
            JOIN GradeCategory gc ON c.course_id = gc.course_id
            JOIN Assignment a ON gc.category_id = a.category_id
            JOIN Score sc 
                ON sc.student_id = s.student_id
               AND sc.assignment_id = a.assignment_id
            WHERE s.student_code = 'NIABRAM'
              AND c.course_code = 'CSCI432'
            GROUP BY gc.category_code, gc.category_name, gc.weight
        )
        SELECT SUM(category_contribution) AS final_grade
        FROM category_results;
        """
    )


def task12():
    print_query(
        "Task 12: Final grade for Nicholas Abram in CSCI432 with lowest score dropped",
        """
        WITH category_results AS (
            SELECT 
                gc.category_code,
                gc.category_name,
                gc.weight,
                COUNT(a.assignment_id) AS num_assignments,
                SUM(sc.points_earned) AS total_earned,
                SUM(a.max_points) AS total_max,
                MIN(sc.points_earned) AS dropped_score,
                CASE 
                    WHEN COUNT(a.assignment_id) > 1 THEN
                        (((SUM(sc.points_earned) - MIN(sc.points_earned)) * 1.0) /
                         (SUM(a.max_points) - MIN(a.max_points))) * gc.weight
                    ELSE
                        ((SUM(sc.points_earned) * 1.0) / SUM(a.max_points)) * gc.weight
                END AS category_contribution
            FROM Student s
            JOIN Enrollment e ON s.student_id = e.student_id
            JOIN Course c ON e.course_id = c.course_id
            JOIN GradeCategory gc ON c.course_id = gc.course_id
            JOIN Assignment a ON gc.category_id = a.category_id
            JOIN Score sc 
                ON sc.student_id = s.student_id
               AND sc.assignment_id = a.assignment_id
            WHERE s.student_code = 'NIABRAM'
              AND c.course_code = 'CSCI432'
            GROUP BY gc.category_code, gc.category_name, gc.weight
        )
        SELECT SUM(category_contribution) AS final_grade_drop_lowest
        FROM category_results;
        """
    )


def main():
    reset_database()
    create_tables()
    insert_data()
    show_all_tables()
    task4()
    task5()
    task6()
    task7()
    task8()
    task9()
    task10()
    task11()
    task12()


if __name__ == "__main__":
    main()
