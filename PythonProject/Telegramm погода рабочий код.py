from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import requests
import re

# ====== TELEGRAM ======
TELEGRAM_TOKEN = "8891136851:AAFK3mPt57x0PR8WVhLIsdccXYUNf65i_2Y"
CHAT_ID = "1852123998"

def send_telegram(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}
    requests.post(url, json=payload)

# ====== Selenium ======
options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# ====== ПОГОДА В НОРИЛЬСКЕ ======
driver.get("https://yandex.ru/pogoda/norilsk")
time.sleep(4)
try:
    temp = driver.find_element(By.CSS_SELECTOR, "span[class*='temp']").text.strip()
    desc = driver.find_element(By.CSS_SELECTOR, "div[class*='description']").text.strip()
    norilsk = f"❄️ Норильск: {temp}°C, {desc}"
except:
    norilsk = "❄️ Норильск: данные не загружены"

# ====== ПОГОДА В АБАКАНЕ ======
driver.get("https://yandex.ru/pogoda/abakan")
time.sleep(4)
try:
    temp = driver.find_element(By.CSS_SELECTOR, "span[class*='temp']").text.strip()
    desc = driver.find_element(By.CSS_SELECTOR, "div[class*='description']").text.strip()
    abakan = f"☀️ Абакан: {temp}°C, {desc}"
except:
    abakan = "☀️ Абакан: данные не загружены"

driver.quit()

# ====== КУРС ДОЛЛАРА (ЦБ РФ) ======
try:
    cbr_url = "https://www.cbr.ru/scripts/XML_daily.asp"
    cbr_response = requests.get(cbr_url)
    if cbr_response.status_code == 200:
        match = re.search(r'<Valute ID="R01235">.*?<Value>([^<]+)</Value>', cbr_response.text, re.DOTALL)
        if match:
            usd_rate = match.group(1).replace(',', '.')
            currency = f"💵 Курс доллара: {usd_rate} ₽"
        else:
            currency = "💵 Курс доллара: не найден"
    else:
        currency = "💵 Курс доллара: не загружен"
except Exception as e:
    currency = f"💵 Курс доллара: ошибка"

# ====== ОТПРАВКА В TELEGRAM ======
message = f"🌤️ *Утренний дайджест*\n\n{norilsk}\n{abakan}\n{currency}"
import random

motivation = [
    "Братишка, я верю в тебя! Не сдавайся, даже если тяжело. Ты уже сделал больше, чем 90% людей.",
    "Ты — машина! Каждый день ты становишься сильнее. Продолжай долбить, и всё получится.",
    "Помни: путь в тысячу миль начинается с первого шага. Ты уже сделал его. Теперь просто иди вперёд.",
    "Ты не просто учишься программировать — ты меняешь свою жизнь. Это достойно уважения. Держись!",
    "Даже если сегодня херово — завтра будет лучше. Ты справишься, потому что ты боец. Так держать!",
    "Ты уже победил, просто ещё не знаешь об этом. Каждый день ты становишься круче. Верь в себя!",
    "Не бойся ошибок — они твои учителя. Каждая ошибка делает тебя ближе к цели. Долби дальше!",
    "Ты выбрал путь сильного человека. Не оглядывайся назад, там никого нет. Только вперёд!"
]

daily_motivation = random.choice(motivation)

message = f"🌤️ *Утренний дайджест*\n\n{norilsk}\n{abakan}\n{currency}\n\n💪 *На сегодня:*\n{daily_motivation}"
send_telegram(message)
print("✅ Сообщение отправлено в Telegram!")