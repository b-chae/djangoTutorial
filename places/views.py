from django.shortcuts import render
from . import models


def all_places(request):
    page = int(request.GET.get('page', 1))
    places = models.Place.objects.all()
    start = (page - 1) * 10
    return render(
        request,
        "home.html",
        context={"places": places[start:start+10]})


def place_detail(request, pk):
    place = models.Place.objects.get(pk=pk)
    return render(request, "places/detail.html", context={"place": place})
