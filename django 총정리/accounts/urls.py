from django.urls import path
from . import views


app_name = 'accounts'

urlpatterns = [
    # path('url 경로/', 실행될 views함수 , pattern 이름)
    path('signup/', views.signup, name = 'signup')
]
