# Grade Book Database Project (Python Version)

## Overview
This project implements a grade book database system using Python and SQLite.

The program:
- creates the database
- creates all tables
- inserts sample data
- prints all table contents
- runs Tasks 4–12

## Readable Codes Added
To make the database easier to read and debug, the design includes human-readable codes in addition to numeric primary keys:

- `student_code` (example: `NIABRAM`)
- `course_code` (example: `CSCI432`)
- `category_code` (example: `CSCI432_HW`)
- `assignment_code` (example: `CSCI432_HW1`)

Numeric IDs are still used as primary keys and foreign keys to preserve referential integrity.

## Requirements
- Python 3.x
- SQLite (included with Python's `sqlite3` module)

## How to Run
Open a terminal in the project folder and run:

```bash
python3 gradebook_project.py
```

## Output
The script will:
1. create a fresh `gradebook.db` database
2. create all required tables
3. insert sample data
4. print the contents of each table
5. execute the SQL for Tasks 4–12

## Files
- `gradebook_project.py` — main Python script
- `gradebook.db` — SQLite database generated when script runs
- `report_template_python.md` — report template for submission
- `README_python.md` — this file

## Notes
- Category weights for each course total 100%.
- Assignment names and codes include the course number to avoid ambiguity.
- Nicholas Abram and Zoey Hall were intentionally given strong grades to test final grade calculations.
