from django.contrib import admin

from courses.models import Course, Tag, Category

# Register your models here.
admin.site.register(Tag)
admin.site.register(Category)

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category')
    list_display_links = ('id', 'name')