# 20240118

# 2가지의 주제 모듈 / 제어문


# 모듈 -> 변수와 함수가 작성되어있는 파이썬 파일
# 모듈 하나는 파이썬 파일 하나 

# 파이썬의 math 모듈

########################
import math
print(math.pi)    # 모듈명.변수명
print(math.sqrt(4))   # 모듈명.함수명
########################### 위쪽이 아래쪽보다 더 명시적이다.

# 모듈은 반드시 import 하는 과정이 필요하다.

# help(math)  # 모듈에 대한 전반적인 설명이 나옴
            # bulit in : 내장되어있는


from math import pi, sqrt   # math로 부터 pi와 sqrt를 들고오겠다.

print(pi)
print(sqrt(4))


# 모듈 주의사항

# from math import pi, sqrt
# from my_math import sqrt
# # 같은 이름의 함수를 제공할 경우 from절에서는 문제가 발생할수있음.
# # 위에 방법을 쓰면 문제가 되지 않음.

# from math import *  # 모듈 math에 있는 모든 함수를 들고옴
#                     # 딱히 권장되지 않음.



# 우리가 정의한 모듈을 실제로 활용해보자 !

import my_math      # 다른 파일에서 만든 함수를 모듈로 끌어옴.


print(my_math.add(1, 2))


# 패키지의 종류 2가지
# PSL 내부 패키지 -> 설치 없이 바로 import하여 사용
# 외부 패키지 -> pip를 사용하여 설치 후 import 필수

# pip ? 외부 패키지들을 설치하도록 도와주는 시스템

# 패키지 설치 pip install SomePackage (터미널에서)


# 패키지 사용 목적
# 모듈들의 이름공간을 구분하여 충돌을 방지 모듈들을 효율적으로 관리하고 재사용할수있도록 돕는 역할



#### 제어문

# 코드의 실행흐름을 제어하는데 사용되는 구문
# 조건에 따라 코드 블록을 실행하거나 반복적으로 코드를 실행


#### 조건문

# 주어진 조건식을 평가하여 해당 조건이 참(True)인 경우에만 코드 블록을
# 실행하거나 건너뜀


# if / elif / else

####### 조건문 예시코드 
a = 3
if a > 3:
    print('3 초과')
else:
    print('3 이하')

print(a)
######## 복수 조건문 예시코드


dust = 35


if dust > 150:
    print('매우 나쁨')
elif dust > 80:
    print('나쁨')
elif dust > 30:
    print('보통')
else:
    print('좋음')


dust = 480

if dust > 150:
    print('매우 나쁨')
    if dust > 300:
        print('위험해요 ! 나가지 마세요!')
elif dust > 80:
    print('나쁨')
elif dust > 30:
    print('보통')
else:
    print('좋음')

############### 이런식으로 쓰면 결과가 2개 이상나와서 쓰면안됨.##########
# dust = 480    
# if dust > 300:
#     print('위험해요 ! 나가지 마세요!')
# if dust > 150:
#     print('매우 나쁨')
# elif dust > 80:
#     print('나쁨')
# elif dust > 30:
#     print('보통')
# else:
#     print('좋음')




#### 반복문

# for  while
    
# for : 시퀀스에 들어있는 순서대로 반복

# for 변수 in 반복 가능한 객체 : 
#   코드블록


# 반복 가능한 객체(iterable)
    
# for 문 예시
    

items = ['apple', 'banana', 'coconut']   # items의 길이만큼 반복(3)

for items_a in items:
    print(items_a)


country = 'korea'

for char in country:
    print(char)

# range의 순회
for i in range(5):
    print(i)



# 딕셔너리의 순회
my_dict = {
    'x' : 10,
    'y' : 20,
    'z' : 30,
}

for i in my_dict:
    print(i)    # 키 나오기
    print(my_dict[i])   # 값 나오기

# 리스트의 순회(numbers의 값을 모두 2배로 만드시오)
    
numbers = [4,6,10,-8,5]

for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2

print(numbers)



# 중첩된 반복문 

outers = ['A', 'B']
inners = ['c', 'd']

for outer in outers:        # 1
    for inner in inners:      # 2
        print(outer, inner)



# 1이 먼저 실행되고 다음으로 2가 실행.
# 다음으로 1은 가만히 있고 2가 한번 더 실행.
# 다음으로 1이 실행되고 2가 실행
# 1이 실행되고 2가 한번 더 실행
'''
A c
A d
B c
B d
'''


# 중첩 리스트 순회

elementes = [['A','B'],['c','d']]   # 요소가 2개

for ele in elementes:
    print(ele)

'''

['A', 'B']
['c', 'd']

'''
# 중첩 리스트 순회

elementes = [['A','B'],['c','d']]   # 요소가 2개

for ele in elementes:
    for item in ele:
        print(item)


# while문
# 주어진 조건식이 참인 동안 코드를 반복해서 실행
# 조건식이 거짓이 될때까지 실행

# a = 0
# while a < 3:
#     print(a)
#     a += 1    # a = a + 1
# print('끝')

number = int(input('양의 정수를 입력해주세요 : '))

while number <= 0:
    if number < 0:
        print('음수를 입력했습니다')
    else:
        print('0은 양의 정수가 아닙니다')
    number = int(input('양의 정수를 입력해주세요 : '))
print('잘했습니다 ! ')


# 적절한 반복문 활용하기
# for 
# 반복횟수가 명확하게 정해져 있는 경우
# 예를들어 리스트,튜플,문자열 등과 같은 시퀀스 형식의 데이터를 처리할때

# while 
# 반복횟수가 불명확하거나 조건에 따라 반복을 종료해야할 때 유용
# 예를 들어 사용자의 입력을 받아서 특정 조건이 충족될 때 까지 반복


# 반복 제어

# break         continue
# 반복을 중단   다음 반복으로 건너뜀


# break문 예시
number = int(input('양의 정수를 입력해주세요 : '))

while number <= 0:
    if number == -9999:
        print('프로그램을 종료합니다.')
        break

    if number < 0:
        print('음수를 입력했습니다')
    else:
        print('0은 양의 정수가 아닙니다')
    number = int(input('양의 정수를 입력해주세요 : '))
print('잘했습니다 ! ')

    
numbers = [1, 3, 5, 7, 8, 9, 11]
found_even = False
for num in numbers:
    if num % 2 == 0:
        print('첫 번째 짝수를 찾았습니다:', num)
        found_even = True
        break
if not found_even:
    print('짝수를 찾지 못했습니다')


# 홀수만 출력하는 코드
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in numbers:
    if num % 2 == 0:   # 2로 나눴을 때 나머지가 0인것은
        continue       # 제외한다.
    print(num)


# list Comprehension 간결하고 효율적인 리스트 생성 방법
# 가독성이 그리 좋아보이지 않음.
    
# 사용 전
numbers = [1,2,3,4,5]
sq_numbers = []

for num in numbers:
    sq_numbers.append(num**2)

print(sq_numbers)

# 사용 후
numbers = [1,2,3,4,5]
sq_numbers = [num**2 for num in numbers]

print(sq_numbers)



###---------------------------------------------------

# pass 
# 아무런 동작도 수행하지 않고 넘어가는 역할


# 파이썬 가상 환경 설정
# 왜 하나요 ?
# 현재 프로젝트를 위한 환경 설정을 위해서

# 어떻게 하나요 ?

'''
bash
# 대체로 폴더명은 venv로 작성한다.

$ python -m venv {폴더 명}   # venv 폴더가 생성된다.
# 가상환경 활성화
$ source venv/Scripts/Activate
# 사용할 외부 라이브러리 설치
$ pip install requests
# 패키지 목록 확인
$ pip list
# 활성화된 가상환경에 설치된 패키지 목록만 기록
$ pip freeze > requirements.txt
# 가상환경 종료
$ deactivate

# requirements.txt에 기록된 패키지 설치
$ pip install -r requirements.txt
'''