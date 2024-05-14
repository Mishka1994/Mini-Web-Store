from rest_framework import generics

from store.models import Subcategory
from store.serializers.subcategory import SubcategorySerializer


class SubcategoryCreateView(generics.CreateAPIView):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer
