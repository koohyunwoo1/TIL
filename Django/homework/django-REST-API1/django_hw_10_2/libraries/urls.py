from django.urls import path
from . import views


urlpatterns = [
    path('libraries/', views.book_list),
    path('libraries/<int:pk>', views.book_detail),
]
