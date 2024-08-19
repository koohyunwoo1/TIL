from django.shortcuts import render , redirect
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

    # return render(request, 'articles/create.html')

    return redirect('articles:detail', article.pk)


def delete(request, pk):
    # 몇번 글 삭제할건데 ?
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')


def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article' : article,
    }
    return render(request, 'articles/edit.html', context)


def update(request, pk):

    article = Article.objects.get(pk=pk)

    title = request.POST.get('title')
    content = request.POST.get('content')

    article.title = title
    article.content = content
    article.save()

    return redirect('articles:detail', article.pk)
