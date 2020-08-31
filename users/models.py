from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    profileimg = models.ImageField(upload_to='media', default='img.jpg')
    bio = models.TextField(max_length=1000, default="There is no bio yet!")
    first_name = models.CharField(max_length=25, default="")
    last_name = models.CharField(max_length=25, default="")
    email = models.CharField(max_length=50, default="")


    def __str__(self):
        return self.username