from rest_framework import generics
from .serializers import CategorySerializer
from category.models import Category


class CategoryList(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
