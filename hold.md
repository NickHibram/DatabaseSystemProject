this is it?: # Grade Book Database System (Python + SQLite)

## 1. Overview
This project implements a **grade book database system** using Python and SQLite. The system models students, courses, enrollments, grading categories, assignments, and scores.

The project fulfills all required tasks:
- database design using an ER diagram
- table creation and data insertion
- querying and updating data (Tasks 4–12)
- computing final grades (with and without dropping lowest scores)

The system demonstrates **relational database design, SQL querying, and Python integration**.

---

## 2. Project Components

This submission includes the following files:

- `gradebook_project.py` — main Python implementation
- `gradebook.db` — SQLite database (generated when script runs)
- ERD diagram — visual representation of database design
- Commands file — SQL for creating tables and queries
- Output + Test Cases — results of all tasks
- Task 3 Tables — table contents
- `README.md` — this file

---

## 3. Database Design (ERD)

The database consists of six main entities:

### Student
- student_id (PK)
- student_code (UNIQUE)
- first_name
- last_name
- email

### Course
- course_id (PK)
- course_code (UNIQUE)
- department
- course_number
- course_name
- semester
- year

### Enrollment
- enrollment_id (PK)
- student_id (FK)
- course_id (FK)

Constraint:
- UNIQUE(student_id, course_id)

### GradeCategory
- category_id (PK)
- category_code (UNIQUE)
- course_id (FK)
- category_name
- weight

Constraint:
- UNIQUE(course_id, category_name)

### Assignment
- assignment_id (PK)
- assignment_code (UNIQUE)
- category_id (FK)
- assignment_name
- max_points

### Score
- score_id (PK)
- student_id (FK)
- assignment_id (FK)
- points_earned

Constraint:
- UNIQUE(student_id, assignment_id)

---

## 4. Design Notes

- Each course contains multiple grading categories.
- Each category contains multiple assignments.
- Each assignment has one score per student.
- Category weights sum to 100% for each course.
- Assignment weights are evenly distributed within categories.

Example:
If Homework = 20% and there are 5 assignments:
Each assignment = 4%

---

## 5. Readable Code System

To improve clarity, the database includes readable identifiers:

- student_code → NIABRAM
- course_code → CSCI432
- category_code → CSCI432_HW
- assignment_code → CSCI432_HW1

These are used in queries and outputs while numeric IDs maintain relational integrity.

---

## 6. Requirements

- Python 3.x
- SQLite (included with Python)

---

## 7. How to Run

Run the program:

```
python3 gradebook_project.py
```bash
## 8. Program Execution Flow

The script performs the following steps:

Deletes any existing database
Creates a new SQLite database
Creates all tables
Inserts sample data
Displays all tables (Task 3)
Executes Tasks 4–12:
queries
updates
grade calculations
## 9. Implemented Tasks
Task 2
SQL commands for creating tables
SQL commands for inserting values
Task 3
Displays contents of all tables
Task 4
Computes average, highest, and lowest score for an assignment
Task 5
Lists all students in a course
Task 6
Lists all students and their assignment scores
Task 7
Adds a new assignment
Task 8
Updates category weights
Task 9
Adds 2 points to all students on an assignment
Task 10
Adds 2 points only to students with "Q" in last name
Task 11
Computes final grade using weighted averages
Task 12
Computes final grade with lowest score dropped
## 10. Important Behavior

The script executes tasks sequentially.

This means:

Task 7 modifies assignments
Task 8 changes weights
Task 9–10 modify scores

👉 Later results reflect earlier updates

## 11. Output Verification

The program prints results for all tasks.

Example outputs include:

Assignment statistics:
Average: 89.17
Highest: 96
Lowest: 79
Final grade:
95.375
Final grade (drop lowest):
95.7

These outputs confirm correct functionality.

## 12. Testing

The system was tested using structured test cases.

Each test case includes:

purpose
input
expected result
actual result

Example:

Test Case: Compute final grade
Expected: ~95
Actual: 95.375
Test Case: Drop lowest score
Expected: slightly higher
Actual: 95.7

All test cases produced expected results.

## 13. Assumptions
All assignments have equal maximum points (100)
Category weights always sum to 100%
Each student receives one score per assignment
## 14. Limitations
No graphical user interface
Static dataset (no user input)
Equal assignment weighting within categories
## 15. Conclusion

This project successfully demonstrates:

relational database design
SQL querying and updates
integration with Python

The system accurately manages grading data and performs all required computations, including advanced features such as dropping the lowest score.

