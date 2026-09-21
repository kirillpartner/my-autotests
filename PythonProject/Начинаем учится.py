print("Я меняю свою жизнь, начинаю учиться")
name = input('Как тебя зовут?')
age = input( "Сколько тебе лет?" )
city = input("В каком городе живешь?")
job = input("Где работаешь?")
# Спрашиваем про деньги
salary =int(input("Сколько ты зарабатываешь в месяц?"))
spending=int(input("Сколько тратишь в месяц?"))

# Cчитаем
profit=salary-spending
year_savings=profit*12

# Выводим на экран
print(f"Привет,{name}! тебе {age} лет, ты живешь в {city}, работаешь на {job}.")
print(f"Ты зарабатываешь {salary} рублей в месяц.")
print(f" Тратишь {spending} рублей в месяц.")
print(f'Остается {profit}рублей в месяц')
print(f" За год ты сможешь накопить {year_savings} рублей.")
print(" Учись автоматизации и сможешь зарабатывать куда больше, у тебя получиться!")

with open("../user_data.txt", "w", encoding="utf") as file:
    file.write(f"Имя:{name}\n")
    file.write(f"Возраст:{age}\n")
    file.write(f"Город:{city}\n")
    file.write(f'Работа:{job}\n')
    file.write(f"Зарплата:{salary}\n руб.\n")
    file.write(f"Расходы:{profit}\n руб.\n")
    file.write(f"Остаток в месяц: {year_savings}\n руб \n")

    print("Данные сохранены в файл user_data.txt")
