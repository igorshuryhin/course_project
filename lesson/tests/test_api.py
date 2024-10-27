from django.contrib.auth.models import User
from django.test import TestCase

from lesson.models import Lesson, Attendance
from lesson.serializers import LessonSerializer, AttendanceSerializer


class LessonsApiTest(TestCase):
    def setUp(self):
        self.lesson = Lesson.objects.create(name='test1')
        self.user = User.objects.create_user(username='tester')

    def test_all_ok(self):
        self.client.force_login(self.user)
        response = self.client.get('/api/lessons/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
            "next": None,
            "previous": None,
            "results": [
                LessonSerializer(self.lesson).data,
            ],
            'page_size': 10
        })


class AttendanceApiTest(TestCase):
    def setUp(self):
        lesson = Lesson.objects.create(name='test1')
        self.user = User.objects.create_user(username='tester')
        self.attendance = Attendance.objects.create(lesson=lesson, user=self.user)

    def test_all_ok(self):
        self.client.force_login(self.user)
        response = self.client.get('/api/attendance/')
        self.assertEqual(response.status_code, 200)
        print(AttendanceSerializer(self.attendance).data)
        self.assertEqual(response.json(), {
            "next": None,
            'page_size': 10,
            "previous": None,
            "results": [
                AttendanceSerializer(self.attendance).data
            ],

        })
