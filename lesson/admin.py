from django.contrib import admin

from lesson.models import Lesson, Attendance

# Register your models here.
admin.site.register(Lesson)
admin.site.register(Attendance)
