from django.shortcuts import render

# Create your views here.
# 메인 페이지를 만드는 index라는 이름의 함수를 작성
def index(request):
    # render(요청객체, 템플릿경로)
    return render(request, 'index.html')