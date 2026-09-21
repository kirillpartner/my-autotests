from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://yandex.ru")

time.sleep(3)  # даём странице загрузиться

print("Заголовок:", driver.title)

driver.quit()
