from django.contrib.auth.models import User
from django.test import TestCase

from homework.models import Homework, Grade
from homework.serializers import HomeworkSerializer


class HomeworksApiTest(TestCase):
    def setUp(self):
        self.homework = Homework.objects.create(name='test1')
        self.user = User.objects.create_user(username='test', password='<PASSWORD>')

    def test_all_ok(self):
        self.client.force_login(self.user)
        response = self.client.get('/api/homeworks/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
            "next": None,
            "previous": None,
            "results": [],
            'page_size': 10
        })

    def test_all_ok_superuser(self):
        self.client.force_login(User.objects.create_superuser(username='test1'))
        response = self.client.get('/api/homeworks/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
            "next": None,
            "previous": None,
            "results": [
                HomeworkSerializer(self.homework).data,
            ],
            'page_size': 10
        })

    def test_no_auth(self):
        response = self.client.get('/api/homeworks/')
        self.assertEqual(response.status_code, 401)
