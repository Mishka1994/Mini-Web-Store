from rest_framework import generics

from store.models import Category
from store.serializers.category import CategorySerializer


class CategoryCreateView(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
