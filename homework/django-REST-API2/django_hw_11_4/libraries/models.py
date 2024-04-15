from django.db import models

# Create your models here.
class Book(models.Model):
    isbn = models.TextField(max_length=10)
    author = models.TextField()
    title = models.TextField()

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    content = models.TextField()
    score = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)