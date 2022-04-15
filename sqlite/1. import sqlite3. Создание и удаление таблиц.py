# подключение к БД, создание и удаление таблиц
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
# Удаление таблицы:
    #cur.execute("DROP TABLE IF EXISTS users")
# Создание таблицы:
    cur.execute("""CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        sex INTEGER NOT NULL DEFAULT 1,
        old INTEGER,
        score INTEGER
    )""")


# команда SELECT для выбора записей из таблицы users:
# SELECT * FROM users
# SELECT rowid, * FROM users

# удалить таблицу
# cur.execute("DROP TABLE users")

# PRIMARY KEY, AUTOINCREMENT, NOT NULL и DEFAULT
# user_id INTEGER PRIMARY KEY AUTOINCREMENT
# INSERT INTO users (name, old, score) VALUES('Алексей', 18, 1000)


    cur.execute("""CREATE TABLE IF NOT EXISTS games (
        user_id INTEGER,
        score INTEGER,
        time INTEGER
    )""")


    cur.execute("""CREATE TABLE IF NOT EXISTS tab1 (
            score INTEGER,
            'from' TEXT
        )""")


    cur.execute("""CREATE TABLE IF NOT EXISTS tab2 (
                val INTEGER,
                type TEXT
            )""")


con.close()