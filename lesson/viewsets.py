from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter

from lesson.models import Attendance, Lesson
from lesson.serializers import AttendanceSerializer, LessonSerializer


class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

    def get_queryset(self):
        user = self.request.user

        if user.is_superuser:
            return self.queryset
        else:
            return self.queryset.filter(user=self.request.user)


class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

    permission_classes = []
    authentication_classes = []

    filter_backends = [SearchFilter, OrderingFilter]

    search_fields = ['name', 'homework__name']
    ordering_fields = ['name', 'date']