
from django.contrib.auth.models import AbstractUser
from django.db import models
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)  # Уникальная почта для авторизации
    phone = models.CharField(max_length=15, blank=True, null=True)  # Дополнительное поле
    def __str__(self):
        return self.username
   