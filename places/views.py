from django.shortcuts import render
from . import models


def all_places(request):
    places = models.Place.objects.all()
    return render(
        request,
        "home.html",
        context={"places": places, "wow": '12039'})
