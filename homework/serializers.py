from rest_framework import serializers

from homework.models import Homework, Grade


class HomeworkSerializer(serializers.ModelSerializer):

    class Meta:
        model = Homework
        fields = ('name', 'deadline', 'retakes_amount', 'complexity', 'passed_amount', 'avg_grade', 'description')


class GradeSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    homework = HomeworkSerializer()

    class Meta:
        model = Grade
        fields = ('user', 'homework', 'grade')