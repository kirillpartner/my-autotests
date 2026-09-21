import sqlite3

conn = sqlite3.connect("test.db")
cursor = conn.cursor()


cursor.execute("UPDATE users SET password = 'mirgen1993' WHERE username = 'Мирген'")
rows = cursor.fetchall()

for row in rows:
    print(row)
conn.commit()
conn.close()