# Создать таблицу аудиторий в БД
import sqlite3 as sq


try:
    con = sq.connect('university.db')
    cur = con.cursor()

    cur.execute("DROP TABLE IF EXISTS classroom")

    cur.execute("""CREATE TABLE IF NOT EXISTS classroom(
        id_room INTEGER PRIMARY KEY AUTOINCREMENT,
        number_room INT NOT NULL,
        name_room TEXT NOT NULL,
        number_of_seats INT VARCHAR(3),
        responsible_person TEXT)
    """)

    cur.execute("""INSERT INTO classroom (number_room, name_room, number_of_seats, responsible_person)  
        VALUES(101, 'economic', 30, 'Mr.Adison')
    """)

    cur.execute("""INSERT INTO classroom (number_room, name_room, number_of_seats, responsible_person)  
        VALUES(201, 'mathematics', 60, 'Mr.Van')
    """)

    cur.execute("""INSERT INTO classroom (number_room, name_room, number_of_seats, responsible_person)  
        VALUES(301, 'informatics', 60, 'Mr.Adams')
    """)

    cur.execute("""SELECT DISTINCT name_room FROM classroom
        ORDER BY number_room
        LIMIT 2
    """)
    for result in cur:
        print(result)

    con.commit()
except sq.Error as Err:
    print("Ошибка выполнения запроса")
finally:
    con.close()

