import sqlite3
conn = sqlite3.connect("test.db")
cursor = conn.cursor()
orders = [
(2, 2, 'Samsung')
    ]
cursor.executemany("INSERT INTO orders (id, user_id, product) VALUES (?,?,?)", orders)


conn.commit()
conn.close()
