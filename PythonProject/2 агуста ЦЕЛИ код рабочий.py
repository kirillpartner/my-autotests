from datetime import datetime
import os

print("Твои жизненные цели - создаем документ")

# Создаём папку, если её нет
folder = "цели"
if not os.path.exists(folder):
    os.makedirs(folder)

goals = []

while True:
    goal = input("Введи цель (или 'стоп' для завершения): ")
    if goal.lower() == "стоп":
        break
    goals.append(goal)

now = datetime.now()
filename = os.path.join(folder, f'цели_{now.strftime("%Y.%m.%d.%H.%M.%S")}.txt')

with open(filename, "w", encoding="utf-8") as file:
    file.write("=== МОИ ЖИЗНЕННЫЕ ЦЕЛИ ===\n")
    file.write(f'Запись от: {now.strftime("%d.%m.%Y %H:%M")}\n\n')
    for i, g in enumerate(goals, 1):
        file.write(f"{i}. {g}\n")
    file.write(f"\nВсего целей: {len(goals)}")

print(f"\n✅ Сохранено {len(goals)} целей в файл: {filename}")