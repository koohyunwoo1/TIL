from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('<str:username>/profile/', views.profile, name='profile'),
    path('update/', views.update_user, name='update'),
    path('resign/', views.resign, name='resign'),
    path('<str:username>/add_seller/', views.add_seller, name='add_seller'),
]
