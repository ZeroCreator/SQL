import sqlite3 as sq

#con = sq.connect("saper.db")
#cur = con.cursor() # Возвращает экземпляр класса курсор

#cur.execute("""
#""")

#con.close()

# *.db, *.db3, *.sqlite и *.sqlite3

# через менеджер контекста:
with sq.connect("saper.db") as con:
    cur = con.cursor()
# Создание и удаление таблиц
    cur.execute("DROP TABLE IF EXISTS users")

    cur.execute("""CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        sex INTEGER NOT NULL DEFAULT 1,
        old INTEGER,
        score INTEGER
    )""")

con.close()
# SELECT * FROM users
# SELECT rowid, * FROM users

# удалить таблицу
# cur.execute("DROP TABLE users")

# PRIMARY KEY, AUTOINCREMENT, NOT NULL и DEFAULT
# user_id INTEGER PRIMARY KEY AUTOINCREMENT