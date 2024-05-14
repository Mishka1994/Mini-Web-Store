from rest_framework import generics

from users.models import User
from users.serializers import UserCreateSerializer


class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
