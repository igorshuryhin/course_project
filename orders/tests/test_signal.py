from django.contrib.auth.models import User
from django.test import TestCase

from courses.models import Course
from orders.models import Order, OrderCourse


class TestSignal(TestCase):
    def test_signal(self):
        course = Course.objects.create(name='test', course_price=12345)
        order = Order.objects.create(user=User.objects.create_user(username='test'))

        ordercourse = OrderCourse.objects.create(order=order, course=course)

        self.assertEqual(ordercourse.price, course.course_price)