from rest_framework import serializers

from awards.models import Award


class AwardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Award
        fields = ('id', 'name', 'description')