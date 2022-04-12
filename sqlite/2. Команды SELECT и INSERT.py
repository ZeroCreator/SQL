# Команды SELECT и INSERT
import sqlite3 as sq


with sq.connect("saper.db") as con:
    cur = con.cursor()

    cur.execute("SELECT * FROM users WHERE score > 100 ORDER BY score DESC LIMIT 5")
    # result = cur.fetchall()
    # print(result)
    # for result in cur:
    #     print(result)


# con.close()
    result1 = cur.fetchone()
    result2 = cur.fetchmany(2)
    print(result1)
    print(result2)






