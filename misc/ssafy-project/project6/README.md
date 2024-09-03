# Django 활용
## 프로젝트 목표
이 프로젝트의 목표는 커뮤니티 웹 서비스를 구축하는 것입니다. 이를 위해 다음과 같은 기능을 구현할 것입니다:

1. 모델 관계 및 인증 시스템 설정: Django를 사용하여 데이터베이스 모델 간의 관계를 설정하고, Django의 인증 시스템을 통해 사용자 로그인, 로그아웃, 회원가입 등의 기능을 구현할 것입니다.
2. 영화 데이터 CRUD 기능: 영화 데이터의 생성(Create), 조회(Read), 수정(Update), 삭제(Delete) 기능을 제공하는 애플리케이션을 개발할 것입니다.
사용자 관리 기능: 사용자의 로그인, 로그아웃, 회원가입 기능을 제공하는 애플리케이션을 개발할 것입니다.
3. 모델 관계 구현: 영화, 댓글, 사용자 등의 모델 간의 관계를 설정하고 관련된 기능을 구현할 것입니다.
4. GitHub Branch 기능 활용: Git을 사용하여 프로젝트를 관리하고, GitHub의 Branch 기능을 활용하여 다양한 기능을 개발하고 테스트할 것입니다.
위의 목표를 달성하기 위해 Django 웹 프레임워크를 사용하여 데이터 처리, 모델 관계 설정, 사용자 인증 등의 기술을 활용할 것입니다.
---
## 기술 스택
- Python
- Django
- Git branch
---
## 어려웠던 점
  - branch를 활용하여 서로 다른 Working Directory에서 작업 후 merge하는 과정을 반복 진행해 보았습니다. 처음 몇 번의 Merge는 충돌현상 없이 잘 진행 되었는데, 코드가 길어질 수록 충돌 빈도가 많아져 두 코드를 비교하는 과정에 많은 시간이 소요되었습니다.
  
  - 작업 중인 환경에서 git branch의 HEAD를 옮겨가면서 commit 및 pull을 진행하는 과정에서, 파일 내용이 유실되는 등의 문제가 발생하였습니다. branch 수가 더 많이 있었더라면, 코드가 사라졌을 때에도 복구할 백업 자료들이 남아있었을 것 같다는 아쉬움이 있었습니다.
  
  - view 함수의 요구 명세를 하나씩 따라가는 과정에서, 두 애플리케이션이 다른 작업환경에 존재해서 결과를 즉시 확인하기 어려웠습니다. 모델 설정 및 migrate가 곧바로 진행되지 않아 어느정도 완성 후에 발생했던 오류들을 따라가면서 비효율적인 코딩이 되었던 것 같습니다.

  - 모델간의 M:N 관계에서, 역참조 하는 메커니즘의 이해가 어려웠습니다.
---
## 해결
 - pull을 하는 과정에서, 현재 HEAD 위치를 master가 아닌 각자의 branch로 옮겨 충돌을 최소화 할 수 있었습니다.
 - 코드를 비교하는 시간이 많아져서 서로의 작업 파일을 최대한 건드리지 않고, 변경 사항을 pull 받아와 사용하면서 파일 간의 충돌을 줄일 수 있었습니다.
 -  최소한의 기본 요구사항을 작성한 후 그 상태에서 시작함으로써 작성한 코드의 결과를 곧바로 확인할 수 있게 한 이후로, 조금 더 효율적인 코드 작성이 가능해져 수월한 코드 작성이 진행될 수 있었습니다.
  - ```python
    class Movie(models.Model):
      user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
      like_user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')
      title = models.CharField(max_length = 10)
      content = models.TextField()
      created_at = models.DateTimeField(auto_now_add = True)
      updated_at = models.DateTimeField(auto_now = True)
    ```
  - ```python
    def likes(request, movies_pk):

    movie = Movie.objects.get(pk=movies_pk)

    if request.user in movie.like_users.all():
        movie.like_users.remove(request.user)
    else:
        movie.like_users.add(request.user)

    return redirect('movies:detail', movies_pk)
    ```
  
  위 코드처럼 역참조명을 설정해주어서 역참조를 위한 코드를 입력하는 과정에서도 이해가 될 수 있게 했습니다.
