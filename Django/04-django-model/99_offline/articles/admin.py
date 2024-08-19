from django.contrib import admin
from .models import Article
# 관리자 페이지에서
# 내가만든 (models.py) 있는 class
# 관리 할 수 있도록 등록

# Register your models here.
# 관리자 사이트에 등록 (Article)
# 아싸리 
# a. si. re
admin.site.register(Article)