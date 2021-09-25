from rest_framework import generics, permissions
from orders.models import Order
from .serializers import OrderSerializer
from .permissions import IsOwner


class OrderList(generics.ListAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        orders = super().get_queryset()
        return orders.filter(user=self.request.user)


class OrderDetail(generics.RetrieveAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    permission_classes = [permissions.IsAuthenticated, IsOwner]
