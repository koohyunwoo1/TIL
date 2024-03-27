from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
    is_hidden = request.GET.get('is_hidden')
    # print(is_hidden) # 문자열옵니다...
    # is_hidden에 대한 요청이 없거나
    # is_hidden에 대한 요청이 True라면, 전부 보여주기
    if is_hidden == None or is_hidden == 'True':
        articles = Article.objects.order_by('-pk')  # pk기준 내림차준 정렬
    else:
        # is_hidden -> False -> 공개인 게시글들만 보여주기.
        articles = Article.objects.filter(is_hidden=False)
    # articles = Article.objects.all()
    context = {
        'articles': articles
    }
    # '..articles/templates/articles/index.html'
    return render(request, 'articles/index.html', context)

def create(request):
    # 생성을 위한 요청은 2가지 작업이 필요하다.
    '''
        1. 생성 하기 위한 데이터를 입력할 수 있는 페이지
        2. 입력한 데이터를 토대로 실제로 데이터를 생성하는 함수
    '''
    # 사용자 요청 방식에 따라서 조건 분기
    if request.method == 'POST':    # POST 요청이 올려면 GET 요청 처리가 먼저다.
        article_form = ArticleForm(request.POST)
        if article_form.is_valid(): # 상속받은 ModelForm에 정의되어 있던
            # 유효성 검사 메서드 통과 : DB에 저장할 수 있을 것 같음
            # -> Form에 field를 내가 지정하죠?
            # 항상 모든 필드에 대한 정보를 받는건 아니죠?
            # 사용자가 보내온 데이터가 정의된 field에 삽입하기 적절하다.
            article_form.save()
            # 너는 save 메서드 어디서났니?
            # model = Article 넘겨줬으니 거기서 났지요
            # 저장이 내가 할 일이었는데.. 저장했네? 이제 다른부서에 일 넘겨야지
            return redirect('articles:index')

    else:
        # GET 요청이 들어왔을 때는, Article 생성 할 수 있는 form을 렌더링
        article_form = ArticleForm()
    # 예 왜 if문 밖으로 나옴? -> POST 처리 작-성 후에 정리
    context = {
        'article_form': article_form
    }
    return render(request, 'articles/create.html', context)