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

    def thumbnail(self):
        if len(self.photos.all()) > 0:
            return list(self.photos.all())[0].file.url
        else:
            return None


class Photo(TimeStampedModel):
    file = models.ImageField(blank=True, upload_to="static/img/place_photos")
    caption = models.CharField(blank=True, max_length=100)
    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        related_name="photos"
    )
