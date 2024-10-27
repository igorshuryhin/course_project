from django.contrib import admin

from awards.models import Award


# Register your models here.

@admin.register(Award)
class AwardAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'user')
    list_display_links = ('id', 'name')
