from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    bio = models.TextField(max_length=1000, default="There is no bio yet!")
    first_name = models.CharField(max_length=25, default="")
    last_name = models.CharField(max_length=25, default="")

    def __str__(self):
        return self.username