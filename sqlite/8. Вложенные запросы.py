# вложенные SQL-запросы
import sqlite3 as sq

with sq.connect("education.db") as con:
    cur = con.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        sex INTEGER NOT NULL DEFAULT 1,
        old INTEGER
    )""")


    cur.execute("""CREATE TABLE IF NOT EXISTS marks (
        id INTEGER,
        subject TEXT,
        mark INTEGER 
    )""")

    cur.execute("""CREATE TABLE IF NOT EXISTS female (
        id INTEGER,
        name TEXT,
        sex INTEGER NOT NULL DEFAULT 2,
        old INTEGER
    )""")


con.close()


"""
SELECT mark FROM marks
WHERE id = 2 AND subject LIKE 'Си'

SELECT name, subject, mark FROM marks
JOIN students ON students.rowid = marks.id
WHERE mark > 3 AND subject LIKE 'Си'

==

SELECT name, subject, mark FROM marks
JOIN students ON students.rowid = marks.id
WHERE mark > (SELECT mark FROM marks
WHERE id = 2 AND subject LIKE 'Си')
AND subject LIKE 'Си'

# Вставить поля в другую таблицу
INSERT INTO female
SELECT * FROM students WHERE sex = 2

INSERT INTO female
SELECT NULL, name, sex, old FROM students WHERE sex = 2
"""