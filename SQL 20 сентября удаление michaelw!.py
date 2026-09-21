import sqlite3
conn = sqlite3.connect("test.db")
cursor = conn.cursor()

cursor.execute("DELETE FROM users WHERE id = 1")

conn.commit()
conn.close()
