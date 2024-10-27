from django_filters import FilterSet, CharFilter

from homework.models import Homework


class HomeworkFilterSet(FilterSet):
    grade__grade__gte = CharFilter(field_name='grades__grade', lookup_expr='gte')
    grade__grade__lte = CharFilter(field_name='grades__grade', lookup_expr='lte')

    class Meta:
        model = Homework
        fields = []