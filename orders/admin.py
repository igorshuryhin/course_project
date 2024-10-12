from django.contrib import admin

from orders.models import Order, OrderCourses

# Register your models here.
admin.site.register(Order)
admin.site.register(OrderCourses)
