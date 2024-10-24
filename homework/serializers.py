from rest_framework import serializers

from homework.models import Homework, Grade


class GradeSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Grade
        fields = ("user", "grade")


class HomeworkSerializer(serializers.ModelSerializer):
    grade = GradeSerializer()

    class Meta:
        model = Homework
        fields = ('name', 'deadline', 'retakes_amount', 'complexity', 'passed_amount', 'avg_grade', 'description', 'grade')
