from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None

    email = models.EmailField(verbose_name='Почта', unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
