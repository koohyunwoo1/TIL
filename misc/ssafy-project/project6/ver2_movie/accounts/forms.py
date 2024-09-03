from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth import models, get_user_model

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        label='Email address'
    )
                             
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2',)

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = (
            'email',
            'first_name',
            'last_name',
        )