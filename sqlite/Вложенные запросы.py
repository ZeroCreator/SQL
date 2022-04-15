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


con.close()