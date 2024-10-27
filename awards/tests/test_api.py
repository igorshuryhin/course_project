from django.contrib.auth.models import User
from django.test import TestCase

from awards.models import Award
from awards.serializers import AwardSerializer


class AwardTestApi(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test')
        self.award = Award.objects.create(user=self.user, name='test1')

    def test_all_ok(self):
        self.client.force_login(self.user)
        response = self.client.get('/api/awards/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {
            'next': None,
            'previous': None,
            'results': [AwardSerializer(self.award).data],
            'page_size': 10
        })
