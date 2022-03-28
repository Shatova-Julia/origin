# *Сделать связь таблиц
import sqlite3 as sq

with sq.connect('university.db') as con:
    cur = con.cursor()

    cur.execute("DROP TABLE IF EXISTS student_room")

    cur.execute("""CREATE TABLE IF NOT EXISTS student_room(
        student_id INTEGER NOT NULL,
        id_room INTEGER NOT NULL,
        FOREIGN KEY (student_id) REFERENCES students (student_id) 
        FOREIGN KEY (id_room) REFERENCES classroom (id_room))  
    """)
    cur.execute("""INSERT INTO student_room VALUES
        (1, 1),
        (1, 2),        
        (2, 1), 
        (2, 3), 
        (4, 2), 
        (5, 1), 
        (5, 2),
        (6, 2),
        (8, 3), 
        (9, 1), 
        (10, 2)
    """)

    cur.execute("""
            SELECT
                s.*,
                cl.responsible_person
            FROM student_room AS sr
            JOIN students AS s
                ON s.student_id = sr.student_id
            JOIN classroom AS cl
                ON cl.id_room = sr.id_room    
            WHERE sr.id_room = 1
            ORDER BY
                sr.student_id
        """)
    for result in cur:
        print(result)

