from django import forms
from .models import Diary

class Diaryform(forms.ModelForm):

    class Meta:
        model = Diary
        fields = '__all__'