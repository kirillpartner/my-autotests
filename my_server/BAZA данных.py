import sqlite3

conn = sqlite3.connect("test.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM users WHERE username = 'emilys'")
row = cursor.fetchone()
print(row)
conn.close()

