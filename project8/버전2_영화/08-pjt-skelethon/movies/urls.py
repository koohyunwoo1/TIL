from django.urls import path
from . import views

app_name = "movies"
urlpatterns = [
    path("", views.index, name="index"),
    path("filter-genre/", views.filter_genre, name="filter_genre"),
    path("recommended/", views.recommended, name="recommended"),
]
