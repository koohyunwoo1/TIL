from django import forms


'''
    한가지 확실한건, 둘다 class에 상속 시켜줄 class라는점
    class -> PascalCase
    Form vs ModelForm

    Form -> Model에 대한 정보가 없는 Form을 위한 클래스

    ModelForm -> Model에 대한 정보가 있는 Form을 위한 클래스
'''

# class ArticleForm(forms.Form):
#     # 모델에 대한 정보 없이 Form을 구성하려면?
#     # 적절한 Field들을 내가 직접 작성해 줘야한다.
#     '''
#         HTML에서 쓸 form 태그를 구성해주는 class인데...
#         field에 대한 정보가 없으면...? input tag 뭘 써야 할지 알 수가 없다.
#         그래서... 그 field들 내가 정의한다.
#         정의하는 방법은? django Model 정의하는거랑 똑같다.
#     '''
#     title = forms.CharField(max_length=100)
#     content = forms.CharField()
#     is_hidden = forms.BooleanField()
from .models import Article
class ArticleForm(forms.ModelForm):
    # 필드명을 변수로 
    title = forms.CharField(
        max_length=100, 
        # form내부에서 보여줄 input을 어떻게 정의할 것인가.
        # 어떤 input으로 만들어주는지는 누가 만들어줬는데?
        # html tag는 여러개의 속성을 가지고 있는데...
            # 이 속성을 쓰는 방법은
            # 속성명="값" -> 키: 벨류
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '제목을 입력해 주세요.'
            }
        )
    )
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': '내용을 입력해 주세요.'

            }
        )
    )
    # HTML에서 사용할 form 태그를 구성할 필드 정보를
    # model로 부터 받아온다.
    class Meta:
        model = Article
        fields = '__all__'
        # fields = ('title', )
        # fields = ('title', 'content', 'is_hidden',)
        '''
            내가 가진 field들 중에, 어떤 이름을 가진 필드들의
            속성만 간단하게 수정하고 싶어.
            field 각 이름은? 고유값 -> 가진 어떤 속성 (value)
        '''
        widgets = {
            'is_hidden': forms.RadioSelect(
                attrs={
                    'class': 'form-check'
                },
                choices=(
                    (True, '비공개'), (False, '공개')
                )
            )
        }