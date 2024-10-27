from django.contrib.auth.models import User
from django.test import TestCase

from vacancies.models import Vacancy
from vacancies.serializers import VacancySerializer


class VacanciesApiTest(TestCase):
    def setUp(self):
        self.vacancy = Vacancy.objects.create(name='test1')
        self.user = User.objects.create_user(username='tester')

    def test_all_ok(self):
        self.client.force_login(self.user)
        response = self.client.get('/api/vacancies/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
            "next": None,
            "previous": None,
            "results": [
                VacancySerializer(self.vacancy).data,
            ],
            'page_size': 10
        })
