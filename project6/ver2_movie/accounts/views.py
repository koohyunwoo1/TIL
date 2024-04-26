from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import get_user_model
from .forms import CustomUserCreationForm, CustomUserChangeForm
from movies.models import Movie


# Create your views here.
@require_http_methods(['GET', 'POST'])
def login(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(request, request.POST)
        if login_form.is_valid():
            auth_login(request, login_form.get_user())
            return redirect('movies:index')
    else:
        login_form = AuthenticationForm()
    context = {
        'login_form': login_form,
    }
    return render(request, 'accounts/login.html', context)

# @require_http_methods(['POST'])
@login_required
def logout(request):
    auth_logout(request)
    return redirect('movies:index')

@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.method == 'POST':
        signup_form = CustomUserCreationForm(request.POST)
        if signup_form.is_valid():
            user = signup_form.save()
            auth_login(request, user)
            return redirect('movies:index')
    else:
        signup_form = CustomUserCreationForm()
    context = {
        'signup_form': signup_form,
    }
    return render(request, 'accounts/signup.html', context)

@require_http_methods(['GET', 'POST'])
@login_required
def update(request, user_pk):
    if request.method == 'POST':
        user_form = CustomUserChangeForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            return redirect('movies:index')
    else:
        user_form = CustomUserChangeForm(instance=request.user)
    context = {
        'user_form': user_form,
    }
    return render(request, 'accounts/update.html', context)

@require_http_methods(['GET', 'POST'])
@login_required
def change_password(request, user_pk):
    if request.method == 'POST':
        change_pw_form = PasswordChangeForm(request.user, request.POST)
        if change_pw_form.is_valid():
            user = change_pw_form.save()
            update_session_auth_hash(request, user)
            return redirect('movies:index')
    change_pw_form = PasswordChangeForm(request.user)
    context = {
        'change_pw_form': change_pw_form,
    }
    return render(request, 'accounts/change_password.html', context)

@require_http_methods(['POST'])
@login_required
def delete(request, user_pk):
    user = get_user_model()
    person = user.objects.get(pk=user_pk)
    if request.user == person:
        person.delete()
    return redirect('movies:index')

# @require_http_methods(['POST'])
def profile(request, username):
    user = get_user_model()
    person = user.objects.get(username=username)
    movies = Movie.objects.filter(user_id=person.pk)
    like_movies = person.like_movies.all()
    context = {
        'person': person,
        'movies': movies,
        'like_movies': like_movies,
    }
    return render(request, 'accounts/profile.html', context)

@require_http_methods(['POST'])
def follow(request, user_pk):
    user = get_user_model()
    person = user.objects.get(pk=user_pk)
    if person != request.user:
        if request.user in person.followers.all():
            person.followers.remove(request.user)
        else:
            person.followers.add(request.user)
    return redirect('accounts:profile', person.username)