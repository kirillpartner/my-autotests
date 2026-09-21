import sqlite3

# Подключаемся к базе (файл появится сам)
conn = sqlite3.connect("test.db")
cursor = conn.cursor()

# Создаём таблицу
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    username TEXT,
    password TEXT
)
""")

# Добавляем пользователей
cursor.execute("DELETE FROM users")  # чистим, чтобы не было дублей

users = [
    (1, 'emilys', 'emilyspass'),
    (2, 'michaelw', 'michaelwpass'),
    (3, 'sophiab', 'sophiabpass'),
]
cursor.executemany("INSERT INTO users VALUES (?, ?, ?)", users)

conn.commit()
print("✅ База готова")
conn.close()