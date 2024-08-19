from django.urls import path, include
from . import views


# 각 경로들에게 이름도 붙여준다.
urlpatterns = [
    # 각 경로를 사용자가 브라우저의 주소창에 직접 입력하는 것 외에도
    # 서비스를 구성할떄, 다른 views함수를 사용해야 하는 경우가 많다.
    # ex)  nav bar에서, 각 페이지로 이동하는  링크를 만들때
    # 아래 방식처럼 경로를 작성하지 않음....
    # <a href="http://127.0.0.1:"8000/articles/">HOME</a>
        # 경로에 지정해놓은 '이름' (변수)로  연결한다.
    # <a href="{% url '이름' %}">HOME</a>
    # name은 유지하고,  경로가 변경되더라도, name으로 부르고 있기 때문에
    # 경로가 직접 변경되더라도 해당 경로를 사용중인 모든코드를 수정할 필요 없다
    path('', views.index, name='index'),
]