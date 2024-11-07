from course_project.celery import app
from telegram.models import TelegramUserAccount
from telegram.service import send_message


@app.task(bind=True)
def send_order_creation_notification(self, order_id):
    print(f"Order {order_id} was created!")
    telegram_id = TelegramUserAccount.objects.first().telegram_id

    send_message(telegram_id, f"Order {order_id} was created!")

    return f"Order {order_id} was created!"
