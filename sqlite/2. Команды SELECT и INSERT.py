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


"""
INSERT INTO users VALUES('Михаил', 1, 19, 1000)
INSERT INTO users (name, old, score) VALUES('Федор', 32, 200)
"""

# SELECT
# выборку данных из таблицы. В самом простом случае она записывается по такому синтаксису:
# SELECT col1, col2, … FROM <table_name>
"""
SELECT name, old, score FROM users
"""

# Оператор WHERE
# Если нам нужно добавить фильтр для выбираемых записей, то это делается с помощью ключевого слова WHERE,
# которое записывается после имени таблицы:
# SELECT col1, col2, … FROM <table_name> WHERE <условие>
# = или ==, >, <, >=, <=, !=, BETWEEN

"""
#все записи со значением очков меньше 1000:
SELECT * FROM users WHERE score < 1000
#Будут выбраны все записи с числом очков в диапазоне от 500 до 1000:
SELECT * FROM users WHERE score BETWEEN 500 AND 1000
#Выбираются записи с игроками возрастом 32 года:
SELECT * FROM users WHERE old = 32
"""

# Составные условия
"""
#Выбирает игроков возрастом более 20 лет и с числом очков менее 1000:
SELECT * FROM users WHERE old > 20 AND score < 1000
#Создается выборка из игроков возрастом 19 или 32 года и числом очков менее 1000:
SELECT * FROM users WHERE old IN(19, 32) AND score < 1000
#Выберет все записи из таблицы users:
SELECT * FROM users WHERE old IN(19, 32) AND score > 300 OR sex = 1
#выбор игроков возрастом 19 или 32 года или мужского пола и, вместе с тем, чтобы число очков у них было более 300:
SELECT * FROM users WHERE (old IN(19, 32) OR sex = 1) AND score > 300
"""

# Сортировка ORDER BY
"""
#выбрать всех игроков с числом очков менее 1000 и отсортировать их по возрастанию возраста:
SELECT * FROM users WHERE score < 1000 ORDER BY old
#отсортировать данные по убыванию, то после имени поля следует указать флаг DESC:
SELECT * FROM users WHERE score < 1000 ORDER BY old DESC
#если нужно явно показать, что сортировка производится по возрастанию, то можно записать флаг ASC:
SELECT * FROM users WHERE score < 1000 ORDER BY old ASC
"""

# Ограничение выборки LIMIT
# чтобы сформировать ТОП-10 лучших. Для этого в команде SELECT используется еще один оператор – LIMIT,
# который записывает в самом конце и имеет следующие синтаксисы:
# LIMIT <max> [OFFSET offset]
# LIMIT <offset, max>
"""
#сформируем запрос на выбор лучших пяти игроков:
SELECT * FROM users WHERE score > 100 ORDER BY score DESC LIMIT 5
#Дополнительный параметр OFFSET позволяет пропускать несколько первых записей:
SELECT * FROM users WHERE score > 100 ORDER BY score DESC LIMIT 5 OFFSET 2
SELECT * FROM users WHERE score > 100 ORDER BY score DESC LIMIT 2, 5
"""

# Работа с выборкой в программе на Python