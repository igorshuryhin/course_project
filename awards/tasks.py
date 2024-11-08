from course_project.celery import app
from telegram.models import TelegramUserAccount
from telegram.service import send_message
from awards.models import Award  # Import Award to retrieve the instance


@app.task(bind=True)
def send_new_award_notification(self, award_id):
    try:
        award = Award.objects.get(id=award_id)  # Retrieve the Award instance using ID
        print(f'You just got "{award.name}" award!')

        telegram_id = TelegramUserAccount.objects.get(user_id=award.user.id).telegram_id
        send_message(telegram_id, f'You just got "{award.name}" award!')

        return f'You just got "{award.name}" award!'
    except Award.DoesNotExist:
        print("Award not found.")