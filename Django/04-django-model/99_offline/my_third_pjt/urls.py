"""
URL configuration for my_third_pjt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


# 특정 app의 기능을 사용하기 위한 요청 경로는
# 그 app이 직접 관리 할 수 있도록 구분해준다.

urlpatterns = [
    path('admin/', admin.site.urls),
    # articles에서 사용할 경로는 /articles/ 뒤에 붙여서 요청 받겠다
    path('articles/', include('articles.urls'))
]
