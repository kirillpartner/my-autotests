import sqlite3

conn = sqlite3.connect("test.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS orders(
id INTEGER PRIMARY KEY,
user_id INTEGER,
product TEXT
)""")

cursor.execute("INSERT OR REPLACE INTO ORDERS VALUES (1,1, 'iPhone')")
conn.commit()

cursor.execute("""
SELECT users.username, orders.product
FROM users 
JOIN orders ON users.id = orders.user_id
""")

rows = cursor.fetchall()
for row in rows:
    print(row)

