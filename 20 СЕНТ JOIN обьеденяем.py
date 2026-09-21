import sqlite3
conn = sqlite3.connect("test.db")
cursor = conn.cursor()
cursor.execute("""
SELECT users.username, orders.product
FROM users
JOIN orders ON users.id = orders.user_id
""")
rows = cursor.fetchall()
for row in rows:
    print(row)
conn.commit()
conn.close()
