from django.urls import path
from . import views


urlpatterns = [
    path('todos/', views.todo_list),
    path('todos/<int:pk>/', views.fetch_todo),
]
