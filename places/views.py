from django.shortcuts import render
from . import models


def all_places(request):
    # print(dir(request))
    print(request.GET)
    places = models.Place.objects.all()
    return render(
        request,
        "home.html",
        context={"places": places, "wow": '12039'})


def place_detail(request, pk):
    place = models.Place.objects.get(pk=pk)
    return render(request, "places/detail.html", context={"place": place})
