# 20240124


# 절차 지향 프로그래밍 
# 프로그램을 '데이터'와 '절차'로 구성하는 방식

# 객체 지향 프로그래밍(OOP)
# 데이터와 해당 데이터를 조작하는 메서드를 하나의 객체로 묶어 관리하는 방식

# 객체란 ?
# 클래스에서 정의한 것을 토대로 메모리에 할당된 것
# 변수,함수,클래스   등등등~~~~~~~~~

# 클래스로 만든 객체를 '인스턴스'라고도 함
# 가수(클래스)    - > 아이유는 객체다(o)
            #   - > 아이유는 인스턴스다(x)
            #   - > 아이유는 가수의 인스턴스다(o)

# 객체(object)의 특징
# 타입 : 어떤 연산자와 조작이 가능한가 ?
# 속성 : 어떤 상태(데이터)를 가지는가 ?
# 조작법(method) : 어떤 함수를 할 수 있는가 ?



# 클래스 ?
# 파이썬에서 타입을 표현하는 방법

# 클래스 구성
class Person:
    pass

# 클래스 정의
class Person:
    # 속성
    song_name = '잘 지내길 바래'   # 클래스 변수

    def __init__(self, name):
        self.name = name    # 인스턴스 변수
    
    def singing(self):
        return f'{self.name}이/가 노래합니다.'   # 인스턴스 메서드
# 인스턴스 생성
singer1 = Person('KIM SEOUNG MIN')
# singer2 = Person('BTS')
# 메서드 호출
print(singer1.singing())
# print(singer2.singing())
# 속성(변수)  접근
print(singer1.song_name)  # singer1에서 먼저 찾은 후 없으면 class로 넘어감.

########################

class Person:      #  Person이라는 class 생성
    name = 'unknown'  # class 변수 생성

    def talk(self):   # 인스턴스 메서드 만들때 self를 처음으로 만들어줘야됨.
                      # 예외 없음.
        print(self.name)

p1 = Person()
p1.talk()

p2 = Person()
p2.name = 'kim'    # 인스턴스 변수 변경
p2.talk()

print(Person.name)
print(p1.name)        # 인스턴스.속성을 했을 때 자기 한테 먼저 찾음
print(p2.name)        # 인스턴스.속성을 했을 때 자기 한테 먼저 찾음, kim라는 변수가 있기 때문에 kim출력

p2.ssafy = 11
print(p2.ssafy)


# 인스턴스 메서드 구조
# 반드시 첫 번째 매개변수로 인스턴스 자신(self)을 전달받음.


# 생성자 메서드
class Person:

    def __init__(self, name):
        print(f'인스턴스가 생성되었습니다. {name}')
    


person1 = Person('지민')


# 클래스 메서드
# 호출하는 클래스가 첫번째 매개변수로 들어와야한다.
class Person:
    count = 0

    def __init__(self, name):
        self.name = name
        Person.count += 1


    @classmethod
    def number_of_pupulation(cls):
        print(f'인구수는 {cls.count}입니다')


person1 = Person('iu')
person2 = Person('BTS')

Person.number_of_pupulation()


# 스태틱(정적)메서드
# 호출 시 필수적으로 작성해야 할 매개변수가 없음.
class MyClass:

    @staticmethod
    def static_method(arg1,):
        pass

class StringUtils:
    @staticmethod
    def reverse_string(string):
        return string[::-1]
    
    @staticmethod
    def capitalize_string(string):
        return string.capitalize()


text = 'hello, world'

reversed_text = StringUtils.reverse_string(text)
print(reversed_text)

capitalized_text = StringUtils.capitalize_string(text)
print(capitalized_text)


# 매직 메서드 
# 인스턴스 메서드
# __init__(self ~) 이런 문법

