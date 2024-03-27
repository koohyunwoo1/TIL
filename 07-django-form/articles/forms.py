from django import forms
from .models import Article

# class ArticleForm(forms.Form):
#     title = forms.CharField(max_length=10)
#     content = forms.CharField(widget=forms.Textarea)


class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        widget = forms.TextInput(
            attrs={
                'class': 'my-title',
                'placeholder' : 'Enter the title',
            }
        )
    )
    class Meta:
        model = Article
        # 어떤 모델과 연동 ?
        fields = '__all__'
        # exclude = ('title',)
        # title을 뺴고 출력
        #  그 모델에서 어떤 필드를 쓸지 ?
        # ('title', 'content')