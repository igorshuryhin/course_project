from django.contrib import admin

from courses.models import Course, Tag, Category

# Register your models here.
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Course)