from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.utils import timezone


def send_html_email(customer_name, customer_email, order_id, order_courses, total_price):
    subject = 'Order Confirmation'
    order_date = timezone.now().strftime("%Y-%m-%d %H:%M:%S")

    # Log to check values before rendering
    print(f"Rendering email for Order ID {order_id} with Total Price: {total_price}")

    # Render the HTML template with context data
    html_content = render_to_string('order_email.html', {
        'customer_name': customer_name,
        'order_uuid': order_id,  # Correctly pass the UUID
        'order_date': order_date,
        'order_items': order_courses,
        'total_price': total_price,  # Ensure this is being passed correctly
    })

    # Use strip_tags to create a plain text version as a fallback
    plain_message = strip_tags(html_content)

    try:
        send_mail(
            subject,
            message=plain_message,
            from_email='shurigin.igor12@gmail.com',
            recipient_list=[customer_email],
            html_message=html_content,
        )
        print(customer_name, order_id, order_courses, total_price)
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")
