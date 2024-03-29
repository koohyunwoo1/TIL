from django.shortcuts import render
from .forms import LoginForm

# Create your views here.
def login(request):
    form = LoginForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)