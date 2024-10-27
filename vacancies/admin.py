from django.contrib import admin

from vacancies.models import Vacancy, Type, Tag

# Register your models here.
admin.site.register(Type)
admin.site.register(Tag)


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'type')
    list_display_links = ('id', 'name')
