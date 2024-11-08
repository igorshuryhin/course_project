from django.contrib import admin

from orders.models import Order, OrderCourse


# Register your models here

class OrderCourseInline(admin.TabularInline):
    model = OrderCourse
    extra = 1
    readonly_fields = ('price',)


@admin.register(OrderCourse)
class OrderCourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'course')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderCourseInline]

    list_display = ('uuid', 'user')

    fields = ('user', 'total_price')
    readonly_fields = ('total_price',)
