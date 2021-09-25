from rest_framework import generics, permissions
from items.models import Item
from api.permissions import IsOwnerOrReadOnly
from .serializers import ItemSerializer


class ItemList(generics.ListCreateAPIView):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]


class ItemOwnerList(generics.ListAPIView):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        items = super().get_queryset()
        return items.filter(owner=self.request.user)
