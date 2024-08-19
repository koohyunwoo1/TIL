# from django.db import models

# class Article(models.Model):
#     pass

# article = Article()
# article.title = 'TITLE'

# 부모 클래스가 있고,
from typing import Any


class Father:
    # 클래스 속성
    gender = 'xy'
    # 부모 클래스의 메서드
    def save(self):
        print(f'{self.name} {self.age}')
        print('DB에 저장')

# 부모 클래스의 내용을 상속 받은 자식 클래스
class Child(Father):
    # 자식 클래스는 부모 클래스의 내용을 그대로 사용
    name = ''
    age = 0

# c1 객체는 Child 클래스의 인스턴스이다.
c1 = Child()
# c1.gender (Father 클래스의 속성) 을 조회가능
# print(c1.gender)
c1.name = '자식1의 이름'
c1.age = 29
c1.save()   # Father 클래스로부터 상속받은 메서드

c2 = Child()
c2.name = '자식2의 이름'
c2.age = 33
c2.save()

'''
class Article(models.Model):
    title = models.CharField(max_length=100)
    ...
'''

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.p1 = Point(x1, y1)
        self.p2 = Point(x2, y2)

p1 = Point(0, 0)
p2 = Point(2, 2)
r1 = Rectangle(p1.x, p1.y, p2.x, p2.y)