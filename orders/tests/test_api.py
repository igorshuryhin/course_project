from django.contrib.auth.models import User
from django.test import TestCase

from courses.models import Course
from orders.models import Order, OrderCourse
from orders.serializers import OrderSerializer


class OrderApiTestCase(TestCase):

    def setUp(self):
        course = Course.objects.create(name="Test Course", course_price=12345)
        self.user = User.objects.create(username='test')
        self.order = Order.objects.create(user=self.user)
        OrderCourse.objects.create(order=self.order, course=course)

    def test_no_auth(self):
        response = self.client.get('/api/orders/')
        self.assertEqual(response.status_code, 401)

    def test_all_ok(self):
        self.client.force_login(self.user)
        response = self.client.get('/api/orders/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
            "next": None,
            "previous": None,
            "results": [
                OrderSerializer(self.order).data,
            ],
            'page_size': 10
        })

    def test_different_user(self):
        self.client.force_login(User.objects.create(username='test2'))
        response = self.client.get('/api/orders/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
            "next": None,
            "previous": None,
            "results": [],
            'page_size': 10
        })

    def test_different_superuser(self):
        self.client.force_login(User.objects.create(username='test3', is_superuser=True))
        response = self.client.get('/api/orders/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
            "next": None,
            "previous": None,
            "results": [
                OrderSerializer(self.order).data
            ],
            'page_size': 10
        })
