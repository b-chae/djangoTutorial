from django.shortcuts import render


def all_places(request):
    return render(request, "home.html")
