from django.urls import path
from . import views


app_name = 'libraries'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:book_pk>/', views.detail, name='detail'),
    path('<int:book_pk>/reviews_create/', views.reviews_create, name='reviews_create'),
    path('<int:book_pk>/reviews_delete/<int:review_pk>/', views.reviews_delete, name='reviews_delete'),
]
