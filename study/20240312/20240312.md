# Django
## 왜 Django를 사용할까 ?

- 다양성
- python 기반으로 소셜 미디어 및 빅데이터 관리 등 광범위한 서비스 개발에 적합
  
- 확장성
- 대량의 데이터에 대해 빠르고 유연하게 확장할 수 있는 기능을 제공
  
- 보안
- 취약점으로부터 보호하는 보안 기능이 기본적으로 내장되어 있음
  
- 커뮤니티 지원
- 개발자를 위한 지원, 문서 및 업데이트를 제공하는 활성화 된 커뮤니티

### 가상환경
#### Python 애플리케이션과 그에 따른 패키지들을 격리하여 관리할 수 있는 독립적인 실행 환경

- 내가 진행하는 폴더에 넣어주면 됨
- off 하는 법 ctrl + c

#### 가상환경 설정하는 법
1. 가상 환경 venv 생성
  python -m venv venv
  
2. 가상 환경 활성화
  source venv/Scripts/activate

3. 환경에 설치된 패키지 목록 확인
  pip list

4. 의존성 패키지 목록 생성
  pip freeze > requirements.txt



#### project 파일의 구조

- settings.py
- 프로젝트의 모든 설정을 관리
- 수업시간에 수정 함

- urls.py
- 요청 들어오는 URL에 따라 이에 해당하는 적절한 views를 연결
- 수업시간에 수정 함
- 
- __init__.py
- 해당 폴더를 패키지로 인식하도록 설정하는 파일

- asgi.py
- 비동기식 웹 서버와의 연결 관련 설정
  
- wsgi.py
- 웹 서버와의 연결 관련 설정
- 
- manage.py
- Django 프로젝트와 다양한 방법으로 상호작용 하는 커멘드라인 유틸리티



#### app 구조
- admin.py
- 관리자용 페이지 설정
- 
- models.py
- DB와 관련된 Model을 정의
- MTV 패턴의 M
- 
- views.py
- HTTP 요청을 처리하고 해당 요청에 대한 응답을 반환
- (url, model, template과 연계)



#### requirements.txt에 적힌 대로 버전에 맞게 모든 패키지들을 설치한다.
- pip install -r requirements.txt

#### 순서
- python -m venv venv
- source venv/Scripts/activate
- pip install Django
- pip list(패키지 확인)
- pip freeze > requirements.txt (깔려있는 패키지들을 txt파일에 저장)
- django-admin startproject my_first_pjt . (my_first_pjt 는 프로젝트의 이름 . 은 현재 위치에 만든다)
- python manage.py startapp articles (articles라는 이름을 가진 app 만들기, 복수형으로 만들어주는게 좋음)
  