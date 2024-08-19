from django.shortcuts import render
from .models import Article

# Create your views here.
def index(request):
    # 전체 게시글 조회해서 저장
    articles = Article.objects.all()
    context = {
        'articles' : articles,

    }
    return render(request, 'articles/index.html', context)