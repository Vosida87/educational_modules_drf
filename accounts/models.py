from django.db import models
from django.contrib.auth.models import User

NULLABLE = {'blank': True, 'null': True}


class UserProfile(models.Model):
    """Расширенная модель пользователя"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    description = models.TextField(**NULLABLE)
    date_joined = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
