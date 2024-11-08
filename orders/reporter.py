from google_sheets.services import write_to_sheet
from orders.models import Order


def report_orders():
    orders = Order.objects.all().prefetch_related('courses')

    sheets_data = []
    for order in orders:
        django_admin_link = "http://localhost:8000/admin/orders/order/{}/change/".format(order.uuid)

        sheets_data.append([
            str(order.uuid),
            order.user.email,
            float(order.total_price),
            django_admin_link,
            order.created_at.strftime("%Y-%m-%d, %H:%M:%S"),
        ])

    write_to_sheet('A2:E', sheets_data)


def report_order_stats():
    orders = Order.objects.all().prefetch_related('courses').order_by('created_at')

    total_orders = orders.count()
    total_price = sum([order.total_price for order in orders])
    total_courses = sum([len(order.courses.all()) for order in orders])

    sheets_data = [
        ["Total Orders", total_orders],
        ["Total Courses", total_courses],
        ["Total Price", total_price]
    ]

    write_to_sheet('G2:H', sheets_data)
