# Создать таблицу со студентами в БД
import sqlite3 as sq

with sq.connect('university.db') as con:
    cur = con.cursor()

    cur.execute("DROP TABLE IF EXISTS students")

    cur.execute("""CREATE TABLE IF NOT EXISTS students(
        student_id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT,
        last_name TEXT,
        age INT,
        speciality TEXT,
        course INT VARCHAR(1),
        main_classroom INT)
    """)

    cur.execute("""INSERT INTO students
        VALUES(1, 'Bob', 'Adison', 18, 'economic', 1, 101)
    """)

    cur.execute("""INSERT INTO students
        VALUES(2, 'Jack', 'Moris', 17, 'economic', 1, 101)
    """)

    cur.execute("""INSERT INTO students
        VALUES(3, 'John', 'Crus', 18, 'economic', 1, 101)
    """)

    cur.execute("""INSERT INTO students (first_name, last_name, speciality, main_classroom)
        VALUES('Ann', 'Smith', 'economic', 101)
    """)

    cur.execute("""INSERT INTO students (first_name, last_name, age, speciality, course, main_classroom)
        VALUES('Lee', 'Van', 19, 'mathematics', 2, 201)
    """)

    cur.execute("""INSERT INTO students (first_name, last_name, age, speciality, course, main_classroom)
        VALUES('Andy', 'Simpson', 20, 'mathematics', 2, 201)
    """)

    cur.execute("""INSERT INTO students (first_name, last_name, age, speciality, course, main_classroom)
        VALUES('Wandy', 'Simpson', 19, 'mathematics', 2, 201)
    """)

    cur.execute("""INSERT INTO students (first_name, last_name, age, speciality, course, main_classroom)
        VALUES('Sheldon', 'Adams', 20, 'informatics', 3, 301)
    """)

    cur.execute("""INSERT INTO students (first_name, last_name, age, speciality, course, main_classroom)
        VALUES('Nikita', 'Moris', 21, 'informatics', 3, 301)
    """)

    cur.execute("""INSERT INTO students (first_name, last_name, age, speciality, course, main_classroom)
        VALUES('Rose', 'Cooper', 19, 'informatics', 3, 301)
    """)

    cur.execute("""UPDATE students SET last_name = 'Cooper' WHERE first_name LIKE 'Ann' AND last_name = 'Smith'
    """)

    cur.execute("""DELETE FROM students WHERE student_id = 3
    """)

    con.commit()

    cur.execute("""SELECT * FROM students WHERE age IN(17,19)
        ORDER BY main_classroom DESC
    """)
    result = cur.fetchmany(10)
    print(result)

    cur.execute("""SELECT DISTINCT main_classroom FROM students
        ORDER BY main_classroom
        LIMIT 2
    """)
    for result in cur:
        print(result)

