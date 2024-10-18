from rest_framework import serializers

from homework.serializers import HomeworkSerializer
from lesson.models import Lesson, Attendance


class LessonSerializer(serializers.ModelSerializer):
    homework = HomeworkSerializer()

    class Meta:
        model = Lesson
        fields = ('name', 'date', 'notes', 'video', 'homework')


class AttendanceSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    lesson = LessonSerializer()

    class Meta:
        model = Attendance
        fields = ('user', 'lesson', 'present')