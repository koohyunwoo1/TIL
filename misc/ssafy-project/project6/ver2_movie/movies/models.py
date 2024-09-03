from django.db import models
from django.conf import settings
# Create your models here.


class Movie(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    like_user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')
    title = models.CharField(max_length = 10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    content = models.CharField(max_length=200)
    movie = models.ForeignKey(Movie, on_delete = models.CASCADE)
