from django.contrib.auth.models import User
from django.test import TestCase

from courses.models import Course
from courses.serializers import CourseSerializer


class CourseTestApi(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test')
        self.course = Course.objects.create(name='test1', course_price=12345)

    def test_all_ok(self):
        self.client.force_login(self.user)
        response = self.client.get('/api/courses/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {
            'next': None,
            'previous': None,
            'results': [CourseSerializer(self.course).data],
            'page_size': 10
        })
