from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    colorFav = models.CharField(max_length=100, blank=True)
    pass