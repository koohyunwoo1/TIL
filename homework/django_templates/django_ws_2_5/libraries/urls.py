from django.urls import path
from . import views


app_name = 'libraries'

urlpatterns = [
    path('recommend/', views.recommend, name='recommend'),
    path('bestseller/', views.bestseller, name='bestseller'),
]
