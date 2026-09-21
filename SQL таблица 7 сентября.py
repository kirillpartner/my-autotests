import sqlite3

conn = sqlite3.connect("test.db")
cursor = conn.cursor()

cursor.execute("UPDATE users SET password = 'qwerty123' WHERE username = 'emilys'")
conn.commit()
print("✔ Пароль обновлен")

conn.close()