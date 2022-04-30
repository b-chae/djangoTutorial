from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    GENDER_CHOICES = (("male", "Male"), ("female", "Female"))
    gender = models.CharField(max_length=10, blank=True, choices=GENDER_CHOICES)
    phone_number = models.CharField(max_length=20)
    is_owner = models.BooleanField(default=False)
