from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter

from courses.filtersets import CoursesFilterSet
from courses.models import Course
from courses.serializers import CourseSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    authentication_classes = []
    permission_classes = []
    filterset_class = CoursesFilterSet
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)

    search_fields = ['name']
    ordering_fields = ['id', 'course_price', 'name', 'lessons_amount']