from django.shortcuts import render
from .models import Author
# Create your views here.

def index(request):
    author = Author.objects.all()
    context = {
        'authors': author
    }
    return render(request, 'libraries/index.html',context)


def detail(request, pk):
    author = Author.objects.get(pk=pk)
    context = {
        'author' : author,
    }
    return render(request, 'libraries/detail.html', context)