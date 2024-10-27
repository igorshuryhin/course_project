from django_filters import FilterSet, CharFilter

from vacancies.models import Vacancy


class VacancyFilterSet(FilterSet):
    tags = CharFilter(method='filter_tags', field_name='tags', label='Tags')

    def filter_tags(self, queryset, name, value):
        tags = value.split(',')

        for tag in tags:
            queryset = queryset.filter(tags__name__icontains=tag)
        return queryset

    class Meta:
        model = Vacancy
        fields = []
