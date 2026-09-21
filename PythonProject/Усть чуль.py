from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import requests

# ====== TELEGRAM ======
TELEGRAM_TOKEN = "8891136851:AAFK3mPt57x0PR8WVhLIsdccXYUNf65i_2Y"
CHAT_ID = "1852123998"

def send_telegram(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}
    requests.post(url, json=payload)

# ====== SELENIUM ======
options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Открываем страницу погоды для Усть-Чулы
driver.get("https://yandex.ru/pogoda/ust-chul")
time.sleep(4)

try:
    # Получаем весь текст со страницы
    page_text = driver.find_element(By.TAG_NAME, "body").text
    print("📄 Текст страницы получен")

    # Проверяем наличие дождя
    if "дождь" in page_text.lower() or "ливень" in page_text.lower():
        print("🌧️ Найдено упоминание дождя!")
        send_telegram("🌧️ В Усть-Чуле ожидается дождь! Не забудь зонт.")
    else:
        print("☀️ Дождя не обнаружено")
        send_telegram("☀️ В Усть-Чуле дождя нет. Можно гулять!")

except Exception as e:
    print(f"Ошибка: {e}")
    send_telegram(f"Ошибка при проверке погоды: {e}")

time.sleep(3)
driver.quit()