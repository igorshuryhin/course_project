from django_filters import FilterSet, CharFilter

from courses.models import Course


class CoursesFilterSet(FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains')
    price__gte = CharFilter(field_name='price', lookup_expr='gte')
    price__lte = CharFilter(field_name='price', lookup_expr='lte')

    lessons_amount__gte = CharFilter(field_name='lessons_amount', lookup_expr='gte')
    lessons_amount__lte = CharFilter(field_name='lessons_amount', lookup_expr='lte')

    category = CharFilter(field_name='category__name', lookup_expr='icontains')
    tags = CharFilter(method='filter_tags', field_name='tags', label='Tags')

    def filter_tags(self, queryset, name, value):
        tags = value.split(',')

        for tag in tags:
            queryset = queryset.filter(tags__name__icontains=tag)
        return queryset

    q = CharFilter(method='filter_query', field_name='q',label="Query")

    def filter_query(self, queryset, name, value):
        return (queryset.filter(name__icontains=value) |
                queryset.filter(category__name__icontains=value) |
                queryset.filter(tags__name__icontains=value) |
                queryset.filter(duration=value))

    class Meta:
        model = Course
        fields = ['name', 'course_price', 'category', 'tags', 'duration', 'lessons_amount']