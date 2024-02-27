# 20240116 

### python 02
# list : 여러 개의 값을 순서대로 저장하는 **변경 가능한** 시퀀스 자료형
# 대괄호([])로 표기
# 0개 이상의 객체를 포함
# 어떤 자료형도 저장할수있음.

my_list_1 = []  # 0개의 객체

my_list_2 = [1,'a', 3 ,'b',5]

my_list_3 = [1,2,3,'python',['hello','world','!!!']] # 두번쨰 대괄호는 리스트가 아님.

my_list = [1,'a',3,'b',5]

### 리스트의 시퀀스 특징 ###

# 인덱싱
print(my_list[1])    # a

# 슬라이싱
print(my_list[2:4])  
print(my_list[:3])
print(my_list[3:])
print(my_list[0:5:2])
print(my_list[::-1])

# 길이
print(len(my_list))

# 중첩된 리스트 접근

my_list = [1,2,3,'python',['hello','world','!!!']]

print(len(my_list))   # 5
print(my_list[4][-1])   # !!!
print(my_list[-1][1][0])   # w
# 앞은 0부터 뒤는 -1부터

# 리스트는 가변(변경 가능)
my_list = [1,2,3]
my_list[0] = 100

print(my_list)   # [100,2,3]

# tuple
# 여러개의 값을 순서대로 순서대로 저장하는 변경불가능한 시퀀스 자료형
# 0개 이상의 객체를 포함
# 소괄호()로 표기
# 데이터는 어떤 자료형도 저장할 수 있음

my_tuple_1 = ()

my_tuple_2 = (1,)
# (1) 이렇게 했을 경우 정수 1로 출력됨
my_tuple_3 = (1, 'a', 3 , 'b', 5)

### 튜플의 시퀀스 특징 = 리스트의 시퀀스 특징 ###
## 대괄호와 소괄호의 차이


####### 튜플은 불변(변경 불가)

my_tuple = (1,'a', 3 ,'b',5 )
my_tuple

my_tuple[1] = 'z' # 변경되지 않음


# range
# ##연속된 정수 시퀀스##를 생성하는 변경 불가능한 자료형

# range 표현

# range(n)
# 0부터 n-1까지의 숫자의 시퀀스

# range(n, m)
# n부터 m-1까지의 숫자 시퀀스

my_range_1 = range(5)
my_range_2 = range(1,10)

print(my_range_1) # range(0,5)
print(my_range_2) # range(1,10)

####### 리스트로 타입을 변환 시 데이터 확인 가능 #####

print(list(my_range_1))  # [0,1,2,3,4]
print(list(my_range_2))  # [1,2,3,4,5,6,7,8,9]


### dice(딕셔너리)  ###
# key-value 쌍으로 이루어진 순서와 중복이 없는 변경가능한 자료형

# 딕셔너리 표현 
# 중괄호({})로 표기

my_dict_1 = {}
my_dict_2 = {'key': 'value'}
my_dict_3 = {'apple' : 12 , 'lsit' : {1,2,3}}

print(my_dict_1)  # {}  # 딕셔너리 값은 0
print(my_dict_2)  # {'key': 'value}  # 딕셔너리 값은 1
print(my_dict_3)  # {'apple' : 12, 'list' : [1,2,3]}  # 딕셔너리 값은 2


my_dict = {
    'apple' : 12, 
    'list' : [1,2,3]
}
# 순서가 없기 때문에 인덱스로 접근이 불가능하다.
# 딕셔너리의 값은 반드시 키로 접근을 해야된다.
# 숫자로 하지 말라는 뜻인듯 ?

print(my_dict['apple'])   # 12  # 키의 값이 나옴
print(my_dict['list'])   # [1,2,3] # 키의 값이 나옴

# 값 변경
my_dict['apple'] = 100
print(my_dict)  # {'apple' : 100, 'list' = [1,2,3]}

# 중복이 안됨
my_dict = {
    'apple' : 12, 
    'list' : [1,2,3],
    'apple' : 100
}

print(my_dict)

# 키가 중복이 되지 않음 마지막에 넣은 키값이 갱신이 됨.


# 중복된 것 들을 제거할 때 사용함.. !!!! 2일차 필수과제 2번째 문제에서 풀때 쓰면 유용할듯
#non-sequence
### set
# 순서와 중복이 없는 변경 가능한 자료형
# 중괄호({})로 표기

my_set_1 = set()  # 빈 세트
my_set_2 = {1,2,3}
my_set_3 = {1,1,1}

print(my_set_1)  # set()
print(my_set_2)  # {1,2,3} # 순서가 없음
print(my_set_3)  # {1}  # 중복이 안된다.

my_set_1 = {1,2,3}
my_set_2 = {3,6,9}

# set에서만 가능함
# 합집합
print(my_set_1 | my_set_2)  # {1,2,3,6,9}

# 차집합
print(my_set_1 - my_set_2)  # {1,2}

# 교집합
print(my_set_1 & my_set_2)

# None = 값이 없음

variable = None

print(variable) # None

# 불리언 표현 참과 거짓을 표현

bool_1 =True
bool_2 = False
print(bool_1)
print(bool_2)
print(3>1)
print('3' !=3) # '3'은 3이 아니다

# Collection
# 여러 개의 항목 또는 요소를 담는 자료 구조
# str list tuple set dict

# 변경 가능 여부
# X    O    X    O    O
# 중복 가능 여부
# O    O    O    X    X 


# 암시적 형변환
# 파이썬이 자동으로 형변환해주는 것

print(3 + 5.0) # int와 float가 만나면 float로 바뀜

print(True + 3)  # 4 # 불리언과 뉴메릭이 만나면 불리언이 숫자로 바뀜

print(True + False)  # True = 1 , False = 0

# 명시적 형변환
# 개발자가 직접 형변환을 하는 것

print(int('1'))

print(str(1) + '등' )

print(float('3.5'))

print(int(3.5))

print(int('3.5'))

# 연산자

# 산술 연산자

# a += b   # a = a + b

y = 10
y -= 4   # y = y-4
print(y)

z = 7
z += 5   # z = z+5
print(z)  # 12


# 비교연산자
# == 같음
#  != 같지 않음  # 연산자 상에서는 !는 not
#  is 같음
#  is not 같지 않음

# -----> True or Fasle의 답이 나올수 밖에 없음

3 == 3.0
3 is 3.0

print(1 == True)
print(1 is True)


# 논리 연산자

print(True and False)  # False

print(True or False)   # True

print(not True)   # False

print(not 0)    # True


num = 15
result = (num>10) and (num % 2 == 0)  # 나머지가 0인지
print(result)    # False

name = 'Alice'
age = 25
result = (name == 'Alice') or (age == 30)
print(result)   # True

word = 'hello'
numbers = [1,2,3,4,5]

print('h' in word)
print('z' in word)

print(4 not in numbers)
print(6 not in numbers)


##### \n 줄바꿈 키
#### f 스트링 : ex ) print(f'{bugs} {counts} {area}'


# 형변환 문제는 시험에 안나올듯 ?