# Student Database Application

A PostgreSQL + Python CLI app demonstrating CRUD operations on a `students` table.

## Project Structure
- `database/setup.sql` - schema + seed data
- `app/db.py` - PostgreSQL connection helper
- `app/main.py` - CRUD functions + interactive menu
- `app/requirements.txt` - Python dependencies

## Prerequisites
- PostgreSQL 16+ (tested on 18)
- Python 3.9+

## Setup

1. Install PostgreSQL and pgAdmin from https://www.postgresql.org/download/macosx/

2. Create the database:

       psql -U postgres -c "CREATE DATABASE student_db;"

3. Load the schema and seed data:

       psql -U postgres -d student_db -f database/setup.sql

4. Install Python dependencies inside a virtualenv:

       cd app
       python3 -m venv .venv
       source .venv/bin/activate
       pip install -r requirements.txt

5. Edit app/db.py and set your PostgreSQL password.

6. Run:

       python3 main.py

## Functions
- getAllStudents() - displays all records
- addStudent(first, last, email, date) - inserts a new student
- updateStudentEmail(id, email) - updates a student's email
- deleteStudent(id) - deletes a student

## Demo Video
[PASTE YOUTUBE LINK HERE]
