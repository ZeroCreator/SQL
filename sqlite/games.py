import sqlite3 as sq

with sq.connect("games.db") as con:
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS games (
        user_id INTEGER,
        score INTEGER,
        time INTEGER
    )""")