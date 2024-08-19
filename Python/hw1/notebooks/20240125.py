# 20240125
# 상속이 필요한 이유 ?
# 1. 코드 재사용
# 2. 계층 구조
# 3. 유지 보수의 용이성


# 클래스 상속

class Person:   # Person이라는 class
    def __init__(self, name, age):   # 생성자 함수   # 2개의 인자
        self.name = name
        self.age = age

    def talk(self):      # talk라는 메서드
        print(f'반갑습니다. {self.name}입니다.')   # 이미 프린트가 되어있음.


# s1 = Person("김학생", 23)    # 인스턴스
# s1.talk()   # 반갑습니다. 김학생입니다.

# s2 = Person("박교수", 59)    # 인스턴스
# s2.talk()   # 반갑습니다. 박교수입니다.



    # 상위클래스의 이름을 괄호안에 넣어야 됨.  
    # Person 클래스로부터 상속을 받는다.
class Professor(Person):   # Professor라는 class
    def __init__(self, name, age, department):  # 생성자 함수   # 3개의 인자
        self.name = name
        self.age = age
        self.department = department
    
    def talk(self):
        print(f'반갑습니다. {self.name}입니다. 저는 {self.age}살이고, 학과는 {self.department}입니다.')
    # 상속된 클래스는 부모클래스의 talk라는 메서드 함수를 사용할수있음.

class Student(Person):    # Student라는 class
    def __init__(self, name, age, gpa):   # 생성자 함수 # 4개의 인자
        self.name = name
        self.age = age
        self.gpa = gpa



p1 = Professor('박교수', 59, '컴퓨터공학과')
s1 = Student('김학생', 23, 4.5)


# print(p1.department)
# print(s1.gpa)
# p1.talk()
# s1.talk()

# p1.talk()

########################SUPER#########################

class Person:   # 부모 클래스
    def __init__(self, name, age, number, email):
        self.name = name
        self.age = age
        self.number = number
        self.email = email

    def talk(self):
        print(f'저는 {self.name}이고 나이는{self.age}입니다.')


class Student(Person):
    def __init__(self, name, age, number, email, student_id):
        self.name = name
        self.age = age
        self.number = number
        self.email = email
        self.student_id = student_id

# 위의 적은 코드를 super로 줄일수 있음.
# init된 부모클래스를 그대로 들고와서 student_id만 들고오면 어떨까 ?
class Student(Person):
    def __init__(self, name, age, number, email, student_id):
        super().__init__(name, age, number, email)
        self.student_id = student_id



s1 = Student('구현우', 26, 55119357, 'kjklovekhw@naver.com', 2)  # 인스턴스
s1.talk()  # 메서드를 이용해서 출력
print(s1.name)  # 이런식으로 이름만 출력가능 !

#############################################################
# 다중 상속
# 중복된 속성이나 메서드가 있는 경우 상속 순서에 의해 결정됨.


class Person:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        return f'안녕, {self.name}'


class Mom(Person):
    gene = 'XX'

    def swim(self):
        return '엄마가 수영'


class Dad(Person):
    gene = 'XY'

    def walk(self):
        return '아빠가 걷기'

# 2개의 클래스를 상속 받음(다중 상속)
class FirstChild(Dad,Mom):
    def swim(self):
        return '첫째가 수영'
    
    def cry(self):
        return '첫째가 응애'
    

baby1 = FirstChild('구현우')
print(baby1.swim())
print(baby1.cry())
print(baby1.walk())
print(baby1.gene)  # FirstChild를 클래를 설정할때 Dad를 먼저 적었기 때문에 
                   # 성별은 XY가 나오게 됨.


#######################super 내장함수를 이용해서 다중 상속을 풀어보자############################
class ParentA:
    def __init__(self):
        self.value_a = 'ParentA'  # 생성자 함수의 내용

    def show_value(self):
        print(f'Value from ParentA: {self.value_a}')


class ParentB:
    def __init__(self):
        self.value_b = 'ParentB'

    def show_value(self):
        print(f'Value from ParentB: {self.value_b}')


class Child(ParentA,ParentB):
    def __init__(self):
        super().__init__()  # A의 생성자 함수를 가져옴.
        self.value_c = 'Child'


    def show_value(self):
        super().show_value()
        print(f'Value from Child: {self.value_c}')


child = Child()
child.show_value()
print(child.value_a)
print(child.value_c)


####################### 예시 2 ########################
class A:              # 부모 클래스 
    def __init__(self):
        print('A Constructor')


class B(A):
    def __init__(self):
        super().__init__()
        print('B Constructor')


class C(A):
    def __init__(self):
        super().__init__()
        print('C Constructor')


class D(B, C):
    def __init__(self):
        super().__init__()
        print('D Constructor')


obj = D()

print(D.mro())
# 출력결과는 ACBD


# 에러와 예외

# 예외

#Built-in Exceptions
# ZeroDivisionError : 나누기 또는 모듈로 연산의 두 번째 인자가 0일때 발생
# NameError : 지역 or 전역 이름을 찾을 수 없을 때
# TypeError : 타입 불일치, 인자 누락, 인자 초과, 인자 타입 불일치
# ValueError 
# IndexError : 시퀀스 인덱스가 범위를 벗어날 때 발생
# KeyError : 딕셔너리에 해당 키가 존재하지 않는 경우
# ModuleNotFoundError : 모듈을 찾을 수 없을 때 발생
# ImportError : 임포트 하려는 이름을 찾을 수 없을 때 발생
# Keyboardinterrupt : 사용자가 Control-C 또는 Delete를 누를 때 발생
# IndentationError : 잘못된 들여쓰기와 관련된 문법 오류
