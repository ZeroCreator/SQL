import sqlite3 as sq

con = sq.connect("saper.db")
cur = con.cursor()

cur.execute("""
""")

con.close()

# *.db, *.db3, *.sqlite и *.sqlite3

# через менеджер контекста:
with sq.connect("saper.db") as con:
    cur = con.cursor()

# Создание и удаление таблиц
cur.execute("""CREATE TABLE users (
    name TEXT,
    sex INTEGER,
    old INTEGER,
    score INTEGER
)""")

# SELECT * FROM users
# SELECT rowid, * FROM users

# удалить таблицу
# cur.execute("DROP TABLE users")

# PRIMARY KEY, AUTOINCREMENT, NOT NULL и DEFAULT
# user_id INTEGER PRIMARY KEY AUTOINCREMENT