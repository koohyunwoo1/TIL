from django.urls import path
from . import views


app_name = 'todos'

urlpatterns = [
    path('', views.index, name='index'),
    path('create_todo/', views.create_todo, name='create_todo'),
    path('<int:todo_pk>/', views.detail, name='detail'),
    path('new_todo/', views.new_todo, name='new_todo'),
    path('<int:todo_pk>/delete/', views.delete_todo, name='delete_todo'),
    path('<int:todo_pk>/update_todo/', views.update_todo, name='update_todo'),
    path('<int:todo_pk>/edit_todo/', views.edit_todo, name='edit_todo'),
]