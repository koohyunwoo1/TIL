# 20240117

### python03 ###

# 함수(functions)
# 재사용 가능

# 두 수의 합을 구하는 코드
num1 = 5
num2 = 3
sum_result = num1 + num2
print(sum_result)

# 두 수의 합을 구하는 '함수'
def get_sum(num1, num2):
    return num1 + num2

# 함수 사용하여 결과 출력
num1 = 5
num2 = 3
sum_result = get_sum(num1, num2)
print(sum_result)


# 1. 내장함수
# 파이썬이 기본적으로 제공하는 함수(import 없이 사용 가능)
# print() 

# 절대값을 만드는 함수 abs

result = abs(-1)

print(result)

## 함수 호출
# function_name(arguments)

# 함수 구조
def make_sum(pram1, pram2):
    # 이것은 두 수를 받아
    # 두수의 합을 보여주는 함수입니다

    return pram1 + pram2


# 함수의 정의와 호출
def greet(name):     # def : 함수로 정의하겠다
                     # greet() : 우리가 정해준 함수명 얼마든지 바꿀수있음.
    # 입력된 이름 값에
    # 인사를 하는 메세지를 만드는 함수

    message = 'Hello, ' + name
    return message # return 키워드 이후에 반환할 값을 명시
                   # return 문은 함수의 실행을 종료하고, 결과를 호출 부분으로 반환
# 함수 호출
result = greet('Alice')
print(result) 

# 매개변수(parameter) : 함수를 정의할 때
# 인자(argument) : 함수를 호출할 때

# 매개변수와 인자 예시
def add_numbers(x,y):   # x와 y는 매개변수
    result = x + y
    return result

a = 3
b = 6
sum_result = add_numbers(a,b)  # a와 b는 인자
print(sum_result)


# 인자의 종류
# 위치 인자는 항상 키워드 인자보다 먼저 나와야한다.

def greet(name, age):
    print(f'안녕하세요, {name}님 ! {age}살이시군요')

greet('Alice', 25) # 안녕하세요, Alice님 ! 25살이시군요


# 기본 인자 값

def greet(name, age=30):
    print(f'안녕하세요, {name}님 ! {age}살이시군요')

# greet('Bob')    
greet('Charlie', 40)    # age에 들어간 40이 씹혀서 나옴

# 키워드 인자

# def greet(name, age):
#     print(f'안녕하세요, {name}님 ! {age}살이시군요')


# greet(age = 30 , 'Dave' ) #  에러 뜸 
                          # 단 , 호출 시 키워드 인자는 위치 인자 뒤에 위치해야함


# 임의의 인자 목록
# 가변인자
# 함수 정의 시 매개변수 앞에 '*'를 붙여 사용하며, 여러 개의 인자를 tuple로 하나로 묶음

def calculate_sum(*args):
    print(args)
    total = sum(args)
    print(f'합계 : {total}')

calculate_sum(1,2,3)


# 임의의 키워드 인자 목록

def print_info(**kwargs):
    print(kwargs)

print_info(name = 'Eve', age = 30)  # {'name' : 'Eve' , 'age' = 30}

# 함수 인자 권장 작성순서

def func(pos1 , pos2 , default_arg = 'default', *args , **kwargs):
  ...


def func(pos1 , pos2 , age=30, *args, **kwargs):
    print(pos1, pos2, age, args, kwargs)

# func(1,2,3,4,5)    # 1 2 3(4,5) {}

func(1,2,3, a=100 , b=200)    # 1 2 3 () {'a':100, 'b': 200}

# python의 범위(Scope)

# global scope : 코드 어디에서든 참조할 수 있는 공간
# local scope : 함수가 만든 scope(함수 내부에서만 참조 가능)

# local 

def func():
    num = 20
    print('local', num)

func()   # 함수가 종료되면서 num은 죽어버림


# local


# print('global', num)   # 에러가 뜸 num을 찾을수 없음

# LEGB Rule : 스코프 범위 B->L은 찾을수없다.

print(sum)   # <built - in fuction sum>
print(sum(range(3)))

sum = 5

print(sum)
print(sum(range(3)))


# 퀴즈
a = 1
b = 2

# -------------------------
def enclosed():
    a = 10
    c = 3

    def local(c):
        print(a,b,c)   # 10 2 500
                       # a는 공간안에 10 b는 글로벌영역 2
                       # c는 호출 local(500)의 500

    local(500)
    print(a,b,c)     # 10 2 3
                     # a는 공간안에 10 b는 글로벌 2 c는 공간안의 3
# -----------------------------
enclosed()
print(a, b)  # 1 2    # 글로벌 공간안에 1 2 


num = 0 # 전역 변수

def increment():
    global num     # num를 전역 변수로 선언
    num += 1

print(num)   # 0
increment()
print(num)   # 1



# 'global' 키워드 주의 사항
# global 키워드 선언 전에 접근 시

# num = 0

# def increment():
#     print(num)
#     global num
#     num += 1 # num = num + 1


# 매개변수에 global 사용 불가
# num = 0 
# def increment(num):
#     global num
#     num += 1


# 재귀함수
#자기자신을 호출하는 함수
#목적 : 큰단위를 작은단위로 풀어가면서 쓰는 함수 


# 예시 팩토리얼 !

def factorial(n):

    if n == 0:
        return 0
    
    return n * factorial(n-1)

result = factorial(5)
print(result)

# 유용한 내장 함수

# map함수 zip 함수

# map(function, iterable(반복 가능한, (문자열 튜플 리스트 range)))

numbers = [1,2,3]
result = map(str, numbers)  # 함수의 이름만 씀

print(result)
print(list(result))   # 쓰고자 하는 타입을 변환을 해줘야 보임


numbers = input().split()

print(numbers)  # ['1', '2', '3', '4', '5']

result = map(int, numbers)
print(list(result)) [1, 2, 3, 4, 5]


result = list(map(int, input().split()))
print(result)


# zip(*iterables)

girls = ['jane', 'ashley', 'apple']
boys = ['peter', 'jay']
pair = zip(girls, boys)

print(pair)
print(list(pair))


# 쌍이 맞지 않더라도 앞의 것만 우선순위로 쌍이 묶인다.  

# lambda 함수
# 이름 없이 정의되고 사용되는 ***익명 함수***

# df 대신 lambda 키워드 사용
# map이랑 많이 쓰임

addition = lambda x,y : x + y

result = addition(3,5)
print(result)

# 각각의 값을 제곱

numbers = [1, 2, 3, 4, 5]

def func(x):
    return x ** 2

result = list(map(func, numbers))
print(result)

result2 = list(map(lambda x: x**2, numbers))



# Packing & Unpacking

# Packing 

# '*'을 활용한 패킹

# *b는 남은 요소들을 리스트로 패킹하여 할당

numbmers = [1,2,3,4,5]
a, *b, c =numbmers

print(a)
print(b)
print(c)


# print함수에서 임의의 가변 인자를 작성할 수 있었던 이유

def my_func(*objects):
    print(objects)
    print(type(objects))

my_func(1,2,3,4,5)



# Unpacking

# 튜플이나 리스트 등의 객체의 요소들을 개별 변수에 할당

packed_values = 1,2,3,4,5
a, b, c, d, e = packed_values

print(a,b,c,d,e)


names = ['alice', 'jane', 'peter']
print(*names)

#############

def my_function(x, y, z):
    print(x, y, z)


my_dict = {'x': 1, 'y' : 2, 'z' : 3}
my_function(**my_dict)





############################## 온라인 강의 끝 #########

## 별칭 설정하는 법
# vim ~/.bashrc
# alias nb="jupyter notebook" 주피터 노트북을 nb로 열겠다
# source ~/.bashrc 
# nb (주피터 노트북 열림)