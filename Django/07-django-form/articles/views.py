from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)


# def new(request):
#     form = ArticleForm()
#     context = {
#         'form' : form,
#     }
#     return render(request, 'articles/new.html', context)


# def create(request):
#     # title = request.POST.get('title')
#     # content = request.POST.get('content')
#     # article = Article(title=title, content=content)
#     # article.save()
#     form = ArticleForm(request.POST)
#     if form.is_valid():
#         article = form.save()
#         return redirect('articles:detail', article.pk)
#     context = {
#         'form': form,
#     }
#     return render(request, 'articles/new.html', context)

def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else: # GET일때 ? X -> 'POST가 아닌 다른 모든 경우'
        form = ArticleForm()
    context = {
        'form' : form,
    }
    
    return render(request, 'articles/create.html', context)




def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')


# def edit(request, pk):
#     article = Article.objects.get(pk=pk)
#     form = ArticleForm(instance=article)
#     context = {
#         'article': article,
#         'form' : form,
#     }
#     return render(request, 'articles/edit.html', context)


# def update(request, pk):
#     # title = request.POST.get('title')
#     # content = request.POST.get('content')

#     # article.title = title
#     # article.content = content
#     # article.save()
#     article = Article.objects.get(pk=pk)
#     form = ArticleForm(request.POST, instance=article)
    
#     if form.is_valid():
#         form.save()
#         return redirect('articles:detail', article.pk)
#     context = {
#         'article' : article,
#         'form': form,
#     }
#     return render(request, 'articles/edit.html', context)

def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST , instance=article)
        if form.is_valid():
            form.save()
        return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'article' : article,
        'form' : form,

    }
    return render(request, 'articles/update.html', context)


# def create(request):
#     if request.method == 'POST':
#         pass
#     else:
#         pass
# else 부분부터 작성해야한다.