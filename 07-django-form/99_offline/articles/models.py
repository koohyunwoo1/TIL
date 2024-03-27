from django.db import models

# Create your models here.

'''
    DB 동작과 python Object 동작 구분짓기.
    django 안에서 작성하는 모든 코드는 파이썬 코드다.
    파이썬 객체 다루는 방법을 따른다.
'''
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    is_hidden = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.pk}번째 게시글 {self.title}'
    