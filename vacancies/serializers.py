from rest_framework import serializers

from vacancies.models import Vacancy


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = ('name',)


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = ('id', 'name')


class VacancySerializer(serializers.ModelSerializer):
    type = TypeSerializer()
    tags = TagSerializer(many=True)

    class Meta:
        model = Vacancy
        fields = ('name', 'description', 'type', 'tags', 'created_at')