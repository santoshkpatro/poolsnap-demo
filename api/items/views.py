import os
from django.http import Http404
from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from items.models import Item
from api.permissions import IsOwnerOrReadOnly
from items.utils import handle_local_upload
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


class ItemUploadView(APIView):
    parser_classes = [MultiPartParser]
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def get_object(self, pk):
        try:
            item = Item.objects.get(id=pk)
            return item
        except Item.DoesNotExist:
            raise Http404

    def post(self, request, pk, format=None):
        item = self.get_object(pk)
        file_obj = request.data['file']
        if os.environ['DJANGO_SETTINGS_MODULE'] == 'poolsnap.settings.local':
            file_url = handle_local_upload(file_obj)
            host = request.get_host()
            path = 'http://' + host + file_url
            item.resource_url = path
            item.save()
            serializer = ItemSerializer(item)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=201)

    def delete(self, request, pk, format=None):
        item = self.get_object(pk)
        item.resource_url = None
        item.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ItemOwnerList(generics.ListAPIView):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        items = super().get_queryset()
        return items.filter(owner=self.request.user)
