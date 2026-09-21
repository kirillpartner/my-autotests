import requests
import sqlite3

response = requests.get("https://dummyjson.com/users/1")
data = response.json()

conn = sqlite3.connect("test.db")
cursor = conn.cursor()

cursor.execute("""
INSERT OR REPLACE INTO users (id, username, password)
VALUES (?, ?, ?)
""", (data["id"], data["username"], data["password"]))

conn.commit()
print("✅ Пользователь добавлен в базу")
conn.close()