from django.urls import path
from . import views


urlpatterns = [
    path('articles/', views.article_list),
    path('articles/<int:article_pk>/', views.article_detail),
    path('comments/', views.comment_list),
    path('comments/<int:comment_pk>/', views.comment_detail),
    # 위의 url을 사용해서 삭제 & 수정 기능 구현
    path('articles/<int:article_pk>/comments/', views.comment_create),
]
