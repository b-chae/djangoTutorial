from django.contrib import admin
from . import models


@admin.register(models.Place, models.Photo)
class CustomPlaceAdmin(admin.ModelAdmin):
    pass
