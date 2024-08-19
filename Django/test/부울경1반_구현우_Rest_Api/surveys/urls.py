from django.urls import path
from . import views

urlpatterns = [
    path('', views.topic_create_list),
    path('<int:topic_pk>/', views.topic_detail_update_delete),
    path('<int:topic_pk>/question/', views.question_create_list),
    path('<int:topic_pk>/question/<int:question_pk>/', views.question_detail_update_delete),
    path('<int:topic_pk>/question/<int:question_pk>/good/', views.question_good),
    path('<int:question_pk>/choice/', views.choice_create_list),
    path('<int:question_pk>/choice/<int:choice_pk>/', views.choice_detail_update_delete),
    path('<int:choice_pk>/answer/', views.answer_create_list),
    path('<int:choice_pk>/answer/<int:answer_pk>/', views.answer_detail_update_delete),
]
