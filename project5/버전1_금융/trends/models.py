from django.db import models

# Create your models here.

class Keyword(models.Model):
    name = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    

class Trend(models.Model):
    keyword = models.ForeignKey(Keyword, on_delete = models.CASCADE)
    name = models.TextField()
    result = models.IntegerField()
    search_period = models.TextField()
    created_at = models.DateField(auto_now_add = True)

    # def __init__(self, name, result, search_period):
    #     self.name = name
    #     self.result = result
    #     self.search_period = search_period