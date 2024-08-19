from django.shortcuts import render, redirect
from .models import Diary
from .forms import Diaryform

# Create your views here.
def index(request):
    diaries = Diary.objects.all()
    context = {
        'diaries': diaries,
    }
    return render(request, 'diaries/index.html', context)

def create(request):
    if request.method == 'POST':
        form = Diaryform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('diaries:index')
    else:
        form = Diaryform()
    context = {
        'form': form
    }
    return render(request, 'diaries/create.html', context)
