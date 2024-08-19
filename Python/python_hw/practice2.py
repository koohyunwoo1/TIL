# 연산자 우선순위
# 높은 순 -------------------------------------> 낮은 순
# ** -((음수 부호) * /  // %    + -


number = 10
double = 2 * number
print(double)

number = 5
print(double)    # double을 재할당 해주지 않았기 때문에 여전히 20

# Numeric Type
# int(정수형)
# float(실수형)


# sequence Types
# 여러개의 값들을 순서대로 나열하여 저장하는 유형

# 값들이 순서대로 나열(정렬 x )
# 각 값에 고유한 인덱스가 있어서 인덱스로 뽑을수있음.
# 인덱스 범위를 조절해 부분적인 값을 추출할수 있음.


# str(문자열)
# 문자들의 순서가 있는 변경 불가능한 시퀀스 자료형

# escape sequence 
# \n (줄 바꿈) \t (탭 키) \\ (백 슬래시) \'(작은 따옴표) \(큰 따옴표)

# 철수야 '안녕'
print('철수야 \'안녕\'')

# 이 다음은 엔터
# 입니다.

print('이 다음은 엔터\n입니다.')


#f-string

bugs = 'roaches'
counts = 13
area = 'living room'

print(f'Debugging{bugs}{counts}{area}')

# 인덱스
# 시퀀스 내의 값들에 대한 고유한 번호로, 그 값의 위치를 알려줌

# 슬라이싱
# 시퀀스 일부분을 선택하여 추출하는 작업

# 문자열은 불변 !!!


# 리스트(list)

# 데이터는 어떠한 자료형도 저장 할 수 있음.
my_list1 = [1,2,3,'python',['hello','world']]
print(my_list1[4])


# 리스트는 가변
my_list = [0,1,2]
my_list[0] = 'q'
print(my_list)



# 튜플
# 여러개의 값을 순서대로 저장하는 변경 불가능한 시퀀스 타입
# 데이터는 어떠한 자료형도 저장할 수 있음.


# 튜플은 불변 ! 
# 파이썬은 쉼표를 튜플 생성자로 사용하니 괄호는 생략 가능


# range 
# 연속된 정수 시퀀스를 생성하는 변경 불가능한 자료형
# 리스트로 형 변환시 데이터 확인 가능

a = range(1,5)
print(list(a))



# non-sequence Type (순서가 없는)

# dict(딕셔너리)

# key-value 쌍으로 이루어진 순서와 중복이 없는 변경 가능한 자료형

# key는 변경 불가능한 자료형만 사용 가능
# value는 모든 자료형 사용 가능


# set(세트)

# 순서와 중복이 없는 변경 가능한 자료형
# 중복이 없다

my_set_1 = {1,2,3}
my_set_2 = {1,4,5}

print(my_set_1 | my_set_2)  # 1,2,3,4,5 # 1이 중복되지만 2개가 생기지 않음.

# None
# 값이 없음을 표현

# Boolean
# 참과 거짓을 포현하는 자료형


# str list tuple set dict range
# # 변경 가능한 것
# list set dict
# # 순서가 있는
# str list tuple range


# num += 1      ==   num = num + 1

a = 20
a //= 3   # 3으로 나누었을때 몫   a = a // 3
print(a)


print(3 and 5)  # 5
print(3 and 0)  # 0
print(0 and 3)  # 0 
print(0 and 0)  # 0

print(5 or 3)   # 5
print(3 or 0)   # 3
print(0 or 3)   # 3
print(0 or 0)   # 0


# and문
# 첫번째 피연산자가 False 인 경우 False임
# 첫번째 피연산자가 True 인 경우 뒤에 나오는 것에 결정

# or문
# 첫번째 피연산자가 False 인 경우 뒤에 나오는 것에 결정
# 첫번째 피연산자가 True 인 경우 True로 결정

print(1 * 5)    # 5
print([1] * 5)   # [1, 1, 1, 1, 1]

def get_sum(num1, num2):
    return num1 + num2

num1 = 1
num2 = 2
sum_result = get_sum(num1,num2)
print(sum_result)


# abs(절대값)
result = abs(-1)
print(result)


def hello_sum(name):
    message = 'hello' + name
    return message

result = hello_sum('hyunwoo')
print(result)


def add_numbers(x,y):
    result = x + y
    return result

a = 2
b = 3
sum_result = add_numbers(a,b)
print(sum_result)


# 위치 인자
def greet(name, age):
    print(f'안녕하세요 ! {name}님 {age}살이시군요 !')

greet('hyunwoo',26)


# 함수 정의 시 매개변수 앞에 '*'를 붙여 사용하며, 여러개의 인자를 tuple로 처리
# 정해지지 않은 개수의 인자를 처리하는 인자
def calculate_sum(*args):
    print(args)
    total = sum(args)
    print(f'합계: {total}')

calculate_sum(2,3)


# 정해지지 않은 개수의 키워드 인자를 처리하는 인자 
# ** 를 붙여 사용함

def print_info(**kwargs):
    print(kwargs)


print_info(name = 'Eve', age = 30, sex = 'female')


# 수명주기 함수와 Scope


# #  ---------------------------
# def func():
#     num = 20
#     print('local', num)
# # ------------------------- local

# func()

# print('global', num)



num = 0

def increment():
    global num
    num = num + 1

print(num)   # 0

increment()  # 1
print(num)


# 재귀 함수
# 자기 자신을 함수로 호출 하는 함수


# 유용한 함수
# map
numbers = [1,2,3]
result = map(str, numbers)

print(result)
print(list(result))

# zip  # 튜플을 원소로 하는 zip object로 반환
girls = ['jane', 'ashley']
boys = ['peter', 'jay']
pair = zip(girls, boys)

print(pair)
print(list(pair))

packed_values = 1, 2, 3, 4, 5
print(packed_values) # 튜플로 묶임


numbers = (1,2,3,4,5)
a, *b, c = numbers   # *b는 남은 요소들을 list로 패킹하여 할당

print(b)

def my_func(*object):
    print(object)
    print(type(object))

my_func(1,2,3,4,5)

# 라이브러리 > 패키지 > 모듈

# pip : 외부 패키지들을 설치하도록 도와주는 파이썬의 패키지 관리 시스템


# 조건문
# 주어진 조건식을 평가하여 해당 조건이 참인 경우에만 코드 블록을 실행하거나 건너뜀

items = ['banana', 'apple', 'coconut']
for item in items:
    print(item)


dust = 480

if dust > 150:
    print('매우 나쁨')
    if dust > 300:
        print('엄청 위험함')
elif dust > 80:
    print('위험함')
elif dust > 30:
    print('버텅')
else:
    print('좋음')


# for i in range(5):
#     print(i)

# for i in range(5):
#     i = 5
#     print(i)


# for i in range(5):
#     i = [5]
#     print(i)

# for i in range(5):
#     i = [5]
#     print(i, end= '')

# for i in range(5):
#     i = (5)
#     print(i)

# for i in range(5):
#     i = (5,)
#     print(i)

my_dict = {
    'x' : 10,
    'y' : 20,
    'z' : 30
}

for i in my_dict:
    print(i)
    # print(my_dict[i])

numbers = [4,5,6,7,8]    

for i in range(len(numbers)):   #[8,10,12,14,16]
    numbers[i] = numbers[i]*2

print(numbers)

outers = ['A','B']
inners = ['c','d']

for outer in outers:
    for inner in inners:
        print(outer, inner)

elements = [['A','B'],['c','d']]

for elem in elements:
    for item in elem:
        print(elem)


# while문은 반드시 종료조건이 필수


