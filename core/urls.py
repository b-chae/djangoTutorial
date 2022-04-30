from django.urls import path
from places import views as place_views

app_name = "core"

urlpatterns = [
    path("", place_views.all_places, name="home")
]
