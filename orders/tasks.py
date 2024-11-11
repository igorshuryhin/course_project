from course_project.celery import app
from orders.emails import send_html_email
from orders.reporter import report_orders, report_order_stats
from telegram.models import TelegramUserAccount
from telegram.service import send_message


@app.task(bind=True)
def send_order_creation_notification(self, order_id, user_id):
    print(f"Order {order_id} was created!")
    telegram_id = TelegramUserAccount.objects.get(user_id=user_id).telegram_id

    send_message(telegram_id, f"Order {order_id} was created!")

    return f"Order {order_id} was created!"


@app.task(bind=True)
def update_orders_report(self):
    report_orders()


@app.task(bind=True)
def update_order_totals_report(self):
    report_order_stats()


@app.task(bind=True)
def send_order_creation_email(self, customer_name, customer_email, order_id, order_courses, total_price):
    print(f"Sending email for Order ID {order_id}")
    print(f"Customer: {customer_name}")
    print(f"Courses: {order_courses}")  # List of course IDs or names
    print(f"Total Price: {total_price}")

    send_html_email(customer_name, customer_email, order_id, order_courses, total_price)
