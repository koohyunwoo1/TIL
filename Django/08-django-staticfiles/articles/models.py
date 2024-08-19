from django.db import models


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    image = models.ImageField(blank=True, upload_to='%Y/%M/%d')
    # blank = True : 빈 문자열도 저장을 할 수 있도록 설정
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # 모델에 변경 사항이 생겼으면 makemigrations