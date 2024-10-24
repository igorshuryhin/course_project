from rest_framework import viewsets
from rest_framework.filters import SearchFilter

from awards.models import Award
from awards.serializers import AwardSerializer


class AwardViewSet(viewsets.ModelViewSet):
    queryset = Award.objects.all()
    serializer_class = AwardSerializer

    permission_classes = []
    authentication_classes = []

    filter_backends = [SearchFilter]

    search_fields = ['name', 'id']