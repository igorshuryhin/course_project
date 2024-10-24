from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter

from orders.models import Order
from orders.serializers import OrderSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    filter_backends = (SearchFilter, OrderingFilter)

    search_fields = ('course__id',)
    ordering_fields = ('created_at',)

    def get_queryset(self):
        user = self.request.user

        if user.is_superuser:
            return self.queryset
        else:
            return self.queryset.filter(user=self.request.user)
