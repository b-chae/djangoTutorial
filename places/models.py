from django.db import models
from core.models import TimeStampedModel
from users.models import User


class Place(TimeStampedModel):
    name = models.CharField(max_length=50, blank=False)
    address = models.CharField(max_length=255, blank=False)
    phone_number = models.CharField(max_length=50, blank=False)
    second_phone_number = models.CharField(max_length=50, blank=True)
    type = models.CharField(max_length=50, blank=False)
    description = models.CharField(max_length=512, blank=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + "-" + self.owner.username
