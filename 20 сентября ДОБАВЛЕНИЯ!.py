import sqlite3
conn = sqlite3.connect("test.db")
cursor = conn.cursor()

users = [
(1, 'Мирген', 'qtwre15243'),
(2, 'Иван', 'ivan1996'),
(3, 'Игорь', 'igor1994'),
    ]
cursor.executemany("INSERT INTO users (id, username, password) VALUES (?,?,?)", users)
conn.commit()
conn.close()
