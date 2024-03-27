from django.urls import path
from . import views


# 무슨 앱을 위한 urls 인지 명확히 namespace 확정지어놓자.
app_name = 'articles'

urlpatterns = [
    # url -> view -> template(없을 수 도 있지만..) 
    # '경로/', 실행될 view함수, pattern name
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
]
