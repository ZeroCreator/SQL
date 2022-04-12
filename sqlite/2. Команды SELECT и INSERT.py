# Команды SELECT и INSERT
# INSERT – добавление записи в таблицу;
# SELECT – выборка данных из таблиц (в том числе и при создании сводной выборки из нескольких таблиц).

# INSERT INTO <table_name> (<column_name1>, <column_name2>, ...) VALUES (<value1>, <value2>, …)
# INSERT INTO <table_name> VALUES (<value1>, <value2>, …)
INSERT INTO users VALUES('Михаил', 1, 19, 1000)
INSERT INTO users (name, old, score) VALUES('Федор', 32, 200)

# SELECT col1, col2, … FROM <table_name>
# SELECT name, old, score FROM users
SELECT name, old, score FROM users
SELECT * FROM users


# Оператор WHERE - добавить фильтр для выбираемых записей
# SELECT col1, col2, … FROM <table_name> WHERE <условие>
SELECT * FROM users WHERE score < 1000

# операторы:
# = или ==, >, <, >=, <=, !=, BETWEEN
SELECT * FROM users WHERE score BETWEEN 500 AND 1000
SELECT * FROM users WHERE old = 32

# Составные условия
# AND – условное И: exp1 AND exp2. Истинно, если одновременно истинны exp1 и exp2.
# OR – условное ИЛИ: exp1 OR exp2. Истинно, если истинно exp1 или exp2 или оба выражения.
# NOT – условное НЕ: NOT exp. Преобразует ложное условие в истинное и, наоборот, истинное – в ложное.
# IN – вхождение во множество значений: col IN (val1, val2, …)
# NOT IN – не вхождение во множество значений: col NOT IN (val1, val2, …)
SELECT * FROM users WHERE old > 20 AND score < 1000
SELECT * FROM users WHERE old IN(19, 32) AND score < 1000
SELECT * FROM users WHERE old IN(19, 32) AND score > 300 OR sex = 1
SELECT * FROM users WHERE (old IN(19, 32) OR sex = 1) AND score > 300
SELECT * FROM users WHERE old IN(19, 32) AND NOT score > 300

# Сортировка ORDER BY
# после оператора ORDER BY указывается поле, по которому производится сортировка записей в выборке
SELECT * FROM users WHERE score < 1000 ORDER BY old
SELECT * FROM users WHERE score < 1000 ORDER BY old ASC

# Если нужно отсортировать данные по убыванию, то после имени поля следует указать флаг DESC:
SELECT * FROM users WHERE score < 1000 ORDER BY old DESC





