from django.urls import path

from users.apps import UsersConfig
from users.views import UserCreateView

app_name = UsersConfig.name

urlpatterns = [
    path('create/', UserCreateView.as_view(), name='user-create'),

]
