from django.contrib import admin

from courses.models import Course, Tag, Category

# Register your models here.
admin.site.register(Tag)
admin.site.register(Category)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'course_price', 'category')
    list_display_links = ('name',)
    list_filter = ('category', 'created_at')
    search_fields = ('name', 'category__name', 'tags__name')
    list_per_page = 10
    list_editable = ('course_price',)
    filter_horizontal = ('tags',)
