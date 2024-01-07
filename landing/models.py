from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    user_type = models.CharField(max_length=50,default='Student')

    def __str__(self):
        return f"{self.username} ({self.user_type})"