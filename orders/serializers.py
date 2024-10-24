from orders.models import Order, OrderCourse
from rest_framework import serializers


class OrderCourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderCourse
        fields = ('course', 'price')

class OrderSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    order_courses = OrderCourseSerializer(many=True)

    class Meta:
        model = Order
        fields = ('uuid', 'user', 'order_courses', 'created_at')
        read_only_fields = ('created_at',)