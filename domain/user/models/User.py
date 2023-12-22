from django.db import models
from django.contrib.auth.models import AbstractUser


# Django: abstract-user
class User(AbstractUser):
    middle_name = models.CharField(max_length=255, null=True, blank=True)
