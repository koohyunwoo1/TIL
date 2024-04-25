from django.urls import path
from . import views

app_name = 'shops'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:product_pk>/', views.detail, name='detail'),
    path('<int:product_pk>/update/', views.update, name='update'),
    path('<int:product_pk>/delete/', views.delete, name='delete'),
    path('<int:product_pk>/review/', views.create_review, name='create_review'), 
    path('<int:product_pk>/review/<int:review_pk>/delete/', views.delete_review, name='delete_review'),
    path('<int:product_pk>/order/', views.order, name='order'),
    path('my_order/', views.order_detail, name='my_order'),
]
