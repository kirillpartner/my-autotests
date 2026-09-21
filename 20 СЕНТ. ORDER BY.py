import sqlite3

conn = sqlite3.connect("test.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM users ORDER BY username DESC")
rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.execute("SELECT COUNT(*) FROM users")
count = cursor.fetchone()
print(f"Всего пользователей: {count[0]}")
conn.close()
