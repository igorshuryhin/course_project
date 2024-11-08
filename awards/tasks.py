from course_project.celery import app
from telegram.models import TelegramUserAccount
from telegram.service import send_message


@app.task(bind=True)
def send_new_award_notification(self, award_name):
    print(f'You just got "{award_name}" award!')
    telegram_id = TelegramUserAccount.objects.first().telegram_id

    send_message(telegram_id, f'You just got "{award_name}" award!')

    return f'You just got "{award_name}" award!'
