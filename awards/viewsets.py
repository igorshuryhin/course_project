from rest_framework import viewsets

from awards.models import Award
from awards.serializers import AwardSerializer


class AwardViewSet(viewsets.ModelViewSet):
    queryset = Award.objects.all()
    serializer_class = AwardSerializer
