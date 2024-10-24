from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter

from homework.filtersets import HomeworkFilterSet
from homework.models import Homework
from homework.serializers import HomeworkSerializer


class HomeworkViewSet(viewsets.ModelViewSet):
    queryset = Homework.objects.all()
    serializer_class = HomeworkSerializer

    filterset_class = HomeworkFilterSet
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)

    search_fields = ('name', 'description')
    ordering_fields = ('name', 'retakes_amount', 'complexity', 'avg_grade', 'deadline')

    def get_queryset(self):
        user = self.request.user

        if user.is_superuser:
            return self.queryset
        else:
            return self.queryset.filter(user=self.request.user)

