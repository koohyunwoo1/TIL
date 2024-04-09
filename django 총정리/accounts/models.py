from django.db import models
from django.contrib.auth.models import AbstractUser
# Create yor models here.
'''
    User Model을 처음부터 직접 만들거라면, models.Model
    근데, django가 이미 만들어둔 UserModel을 상속받으려면
'''
class User(AbstractUser):
    # follow 기능을 위한 User : User의 M:N 관계 정의
    '''
        중개 모델을 사용 할 수도 있지만 ,,,
        follow는 나와 상대의 id 정보만 있으면 된다,,
        만약, 구독 관계를 만들고자 한다면,,,?
            -> 구독 일자를 기록할 수 있으면 좋겠다.
            -> 중개 모델을 별도로 만드는게 좋겠다.
    '''
    # 변수 = models.MTMTF(대상, 제약조건, 역참조매니저명)
    # 주어를 생각 해 보자. 내가 . 참조하는 대상
    # user = User()
    # user.변수명.all() -> 내가 참조하고 있는 유저들
        # 역참조 매니저명 ?
        #  저 사람 기준으로 나를 본다면 
    # user.followers.all() - > 나를 참조하고 있는 유저들
    followings = models.ManyToManyField('self',symmetrical=False ,related_name='followers')
