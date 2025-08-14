import os
import requests

def send_sms(phone_number, message):
    api_key = os.getenv("FAST2SMS_API_KEY")
    if not api_key:
        print("FAST2SMS API Key missing.")
        return False

    url = "https://www.fast2sms.com/dev/bulkV2"
    headers = {
        "authorization": api_key,
        "Content-Type": "application/json"
    }
    payload = {
        "route": "v3",
        "sender_id": "TXTIND",
        "message": message,
        "language": "english",
        "flash": 0,
        "numbers": phone_number
    }

    response = requests.post(url, json=payload, headers=headers)
    return response.status_code == 200