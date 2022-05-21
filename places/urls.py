from django.urls import path
from . import views

app_name = "places"

urlpatterns = [
    path("<int:pk>", views.place_detail, name="detail")
]
