import os
import requests

def send_telegram_message(user_id, message):
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    if not token:
        print("Telegram bot token not found.")
        return False

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": user_id,
        "text": message
    }

    response = requests.post(url, data=payload)
    return response.status_code == 200