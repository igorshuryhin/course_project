import os

import requests

from dotenv import load_dotenv
load_dotenv()


def send_message(user_id, message):
    requests.post(
        f"https://api.telegram.org/bot{os.getenv("TELEGRAM_BOT_TOKEN")}/sendMessage",
        json={
            "chat_id": user_id,
            "text": message
        }
    )


def set_webhook():
    resp = requests.post(
        f"https://api.telegram.org/bot{os.getenv("TELEGRAM_BOT_TOKEN")}/setWebhook",
        json={
            "url": "https://456d-195-248-162-253.ngrok-free.app/telegram"
        }
    )

    print(resp.json())


if __name__ == '__main__':
    set_webhook()
