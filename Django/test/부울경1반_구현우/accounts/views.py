from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash, get_user_model

from .forms import CustomUserCreationForm, CustomUserChangeForm


def login(request):
    if request.user.is_authenticated:
        return redirect('shops:index')

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('shops:index')
    else:
        form = AuthenticationForm(request)

    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)


def logout(request):
    if request.user.is_authenticated and request.method == 'POST':
        auth_logout(request)
        return redirect('accounts:login')
    
    return redirect('shops:index')


def signup(request):
    if request.user.is_authenticated:
        return redirect('shops:index')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('shops:index')
    else:
        form = CustomUserCreationForm()
    
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)


def profile(request, username):
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    
    person = get_user_model().objects.get(username=username)
    context = {
        'person': person,
    }
    return render(request, 'accounts/profile.html', context)


# 문제 7. 유저 정보가 수정되지 않음
def update_user(request):
    if not request.user.is_authenticated:
        return redirect('shops:index')
    
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('accounts:profile', request.user.username)
        
    else:
        form = CustomUserChangeForm(instance=request.user)

    context = {
        'form': form,
    }
    return render(request, 'accounts/update.html', context)


# 문제 6. 다른 사람의 password 변경 화면으로 이동 후 수정할 수 있음
# 본인만 비밀번호를 수정할 수 있도록 수정
def change_password(request, user_pk):

    person = get_user_model().objects.get(pk=user_pk)
    if not request.user.is_authenticated:
        return redirect('shops:index')
    else:
        if request.method == 'POST':
            form = PasswordChangeForm(person, request.POST)
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, person)
                return redirect('accounts:update')
        
        else:
            form = PasswordChangeForm(person)
        
        context = {
            'form': form,
            'person': person,
        }
        return render(request, 'accounts/password.html', context)


def resign(request):
    if request.method == 'POST' and request.user.is_authenticated:
        request.user.delete()
        auth_logout(request)
    
    return redirect('shops:index')


def add_seller(request, username):
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    
    seller = get_user_model().objects.get(username=username)
    if request.method == 'POST':
        if seller in request.user.good_seller.all():
            request.user.good_seller.remove(seller)
        else:
            request.user.good_seller.add(seller)

    return redirect('accounts:profile', seller.username)