from django.shortcuts import render
from .forms import LoginForm
# Create your views here.
def login(request):
    form = LoginForm()
    print(form)
    return render(request, 'accounts/login.html')