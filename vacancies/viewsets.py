from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter

from vacancies.filtersets import VacancyFilterSet
from vacancies.models import Vacancy
from vacancies.serializers import VacancySerializer


class VacancyViewSet(viewsets.ModelViewSet):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer

    permission_classes = []
    authentication_classes = []

    filterset_class = VacancyFilterSet
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    search_fields = ['name', 'type__name', 'tags__name']
    ordering_fields = ('created_at', 'name')