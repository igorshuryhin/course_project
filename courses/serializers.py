from rest_framework import serializers

from courses.models import Course, Tag, Category


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ("id", "name")


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name")


class CourseSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Course
        fields = ('id', 'name', 'lessons_amount', 'duration', 'description',
                  'course_price', 'start_date', 'category', 'tags')
