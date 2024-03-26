from django.shortcuts import render
from . models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles' : articles,
    }
    return render(request, 'articles/index.html', context)



def detail(request, pk):
    article =  Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)


def new(request):
    return render(request, 'articles/new.html')

def create(request):

    title = request.POST.get('title')
    content = request.POST.get('content')

    # 1
    # article = Artic.POST
    # article.title = title
    # article.content = content
    # article.save()

    # 2
    article = Article(title=title , content=content)
    article.save()

    # 3
    # Article.objects.create(title=title, content=content)

    return render(request, 'articles/create.html')