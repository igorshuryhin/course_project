from rest_framework import viewsets

from orders.models import Order
from orders.serializers import OrderSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_queryset(self):
        user = self.request.user

        if user.is_superuser:
            return self.queryset
        else:
            return self.queryset.filter(user=self.request.user)