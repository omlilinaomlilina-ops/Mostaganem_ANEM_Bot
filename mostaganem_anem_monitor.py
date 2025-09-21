import os
import time
import requests
from telegram import Bot
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

bot = Bot(token=TELEGRAM_TOKEN)

URL = "https://www.anem.dz/"
last_status = ""

def check_updates():
    global last_status
    try:
        response = requests.get(URL, timeout=10)
        response.raise_for_status()
        page_content = response.text

        if "منحة البطالة" in page_content:
            if last_status != "available":
                bot.send_message(chat_id=CHAT_ID, text="📢 تم تحديث مواعيد منحة البطالة في موقع ANEM.")
                last_status = "available"
        else:
            last_status = "not_available"

    except Exception as e:
        bot.send_message(chat_id=CHAT_ID, text=f"⚠️ خطأ في التحقق: {e}")

if __name__ == "__main__":
    bot.send_message(chat_id=CHAT_ID, text="✅ البوت متصل وجاهز لمراقبة موقع ANEM Mostaganem.")
    while True:
        check_updates()
        time.sleep(300)
