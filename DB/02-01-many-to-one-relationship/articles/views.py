from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Article, Comment
from .forms import ArticleForm, CommentForm


# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    # 특정 게시글에 작성된 모든 댓글 조회 (Article -> Comment, 역참조)
    comments = article.comment_set.all()
    # DB의 모든 댓글을 조회(특정 게시글에 작성된 모든 댓글 조회가 아님)
    # Comment.objects.all()


    # 사용자로부터 댓글 데이터 입력을 받기 위한 form
    comment_form = CommentForm()
    context = {
        'article': article,
        'comments' : comments,
        'comment_form' : comment_form,
    }
    return render(request, 'articles/detail.html', context)


@login_required
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)


@login_required
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')


@login_required
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'form': form,
        'article': article,
    }
    return render(request, 'articles/update.html', context)

def comments_create(request, pk):
    # 게시글 조회 (어떤 게시글에 작성이 되어야 하는지 ?)
    article = Article.objects.get(pk=pk)
    comments = article.comment_set.all()
    # 사용자 입력 데이터를 받아서 Comment 저장 (+ 유효성 검사)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.save()
        return redirect('articles:detail', article.pk)
    
    context = {
        'comment_form' : comment_form,
        'article' : article,
        'comments': comments ,
    }
    return render(request, 'articles/detail.html', context)
    # else:


def comments_delete(request, article_pk, comment_pk):
    # 어떤 댓글을 삭제하는지 조회
    comment = Comment.objects.get(pk=comment_pk)
    # 아래 코드처럼 작성가능
    # 단, 이렇게 작성할 경우 url에서 article_pk가 제거되고 url 구성을 변경하여야 함
    # 지금까지의 url 전체 구성 및 동일성을 유지하기 위해 아래코드 방식을 선택하지 않음
    # article.pk = comment.article.pk
    article_pk = comment.article.pk
    comment.delete()
    return redirect('articles:detail', article_pk)