import random

from django.contrib.auth.models import User
from django.test import TestCase

from homework.models import Homework, Grade
from homework.serializers import HomeworkSerializer


class TestSignal(TestCase):

    def test_signal(self):
        homework = Homework(name="test")
        homework.save()

        user = User.objects.create(username="test1")
        grade = Grade.objects.create(user=user, grade=1)

        homework.grades.add(grade)

        homework.refresh_from_db()

        serializer = HomeworkSerializer(homework)

        self.assertEqual(serializer.data['avg_grade'], 1)