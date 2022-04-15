# команды UPDATE и DELETE при работе с таблицами
# UPDATE
# UPDATE имя_таблицы SET имя_столбца = новое_значение WHERE условие

"""
UPDATE users SET score = 0
# с фильтром:
UPDATE users SET score = 1000 WHERE rowid = 1
#можно всем игрокам женского пола увеличить число очков на 500:
UPDATE users SET score = score+500 WHERE sex = 2
можем обратиться к игрокам по имени и указать им определенное число очков:
UPDATE users SET score = 1500 WHERE name LIKE 'Федор'
менять значения сразу несколько столбцов записи, перечисляя их через запятую:
UPDATE users SET score = 700, old = 45 WHERE old > 40
"""

# % - любое продолжение строки;
# _ - любой символ;
"""
UPDATE users SET score = score+100 WHERE name LIKE 'М%'
UPDATE users SET score = score+100 WHERE name LIKE 'С_рг%'
"""

# DELETE
# DELETE FROM имя_таблицы WHERE условие

"""
DELETE FROM users WHERE rowid IN(2, 5)
"""