# 5/3 . PJT 08 - 영화

#### 프로젝트 개요
- AJAX와 JSON 데이터를 활용하는 커뮤니티 웹 서비스의 구성
- 장르 별 영화 데이터 조회가 가능한 애플리케이션 완성
- 영화 리뷰의 좋아요가 가능한 애플리케이션 완성
- 유저 간 팔로우가 가능한 애플리케이션 완성
- 알고리즘을 통한 영화 추천이 가능한 애플리케이션

#### 프로젝트 목표
- 데이터를 생성,조회,수정,삭제할 수 있는 애플리케이션 제작
- AJAX와 JSON에 대한 이해
- Many to one relationship(N:1)에 대한 이해
- Many to many relationship(N:M)에 대한 이해
- 추천 알고리즘 설계

#### A solve
- 유저 팔로우 기능
- 팔로우 버튼을 누르는 경우 , AJAX 기술을 이용하여 새로고침 없이 프로필 페이지 화면을 구성


- views.py follow 함수
- ![Alt text](image.png)
- boolean 데이터를 이용해서 팔로우 한사람이 이미 팔로워에 있다면 제거해주고 아니면 추가해준다.
- 그리고 json데이터로 return 해준다.

- ![Alt text](image-1.png)
-  event.preventDefault()
-  HTML에서 전달해준 pk값을 조회 및 저장해준다.
  
- 어려웠던 점

- base.html에 
   ```html
  {% block script %}
  {% endblock script %}
  ```
  을 쓰지 않아 html에서 결과가 나오지 않고 json데이터로 자꾸 넘어가였음. 기초적인것이지만 자꾸 까먹어 시간을 너무 많이 소비함.

#### B solve

- 시간 내에 풀지 못하였음.
