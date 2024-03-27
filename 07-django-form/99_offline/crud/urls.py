"""
URL configuration for crud project.

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

urlpatterns = [
    path('admin/', admin.site.urls),
    # app 별로, 본인들의 기능과 연관된 요청을 따로 관리
    # 처음 app 생성시에는, django가 별도로 app.urls 를 제공하지는 않는다.
        # -> 헉! 어떡하지? 만들면된다.
    path('articles/', include('articles.urls')),
]
