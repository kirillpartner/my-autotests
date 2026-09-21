from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service(r"D:\Программы\Драйвера\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://ya.ru")  # короткая ссылка на Яндекс
time.sleep(7)  # даём больше времени на загрузку

# Ищем поле поиска через NAME (он стабильнее)
search_box = driver.find_element(By.NAME, "text")
search_box.send_keys("Абакан")
search_box.submit()

time.sleep(5)

page_text = driver.find_element(By.TAG_NAME, "body").text

if "Абакан" in page_text:
    print("✅ Тест пройден: Абакан найден")
else:
    print("❌ Тест упал: Абакан не найден")

driver.quit()