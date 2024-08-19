from django.urls import path
# 명시적 상대경로
from . import views

app_name = 'articles'
urlpatterns = [
    path('index/', views.index, name = 'index'),
    path('dinner/', views.dinner, name = 'dinner'),
    path('search/', views.search, name = 'search'),
    path('throw/', views.throw, name = 'throw'),
    path('catch/', views.catch, name = 'catch'),
    path('greeting/<str:name>/', views.greeting, name = 'greeting'),
    path('articles/<int:num>/', views.detail, name = 'detail'),
]
