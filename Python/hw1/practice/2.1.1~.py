# ctrl + alt + 방향키 위,아래 ㅣ 포커싱 증가
# ctrl + 왼쪽, 오른쪽 방향키
# alt + 방향키 ㅣ 포커싱 되어있는 줄 위치 이동
# alt + shift + 위 아래 방향키 ㅣ 포커싱 되어 있는 줄 복제
# shift insert 붙여넣기

# 2.1.1
a = int(input('숫자를입력해주세요 :'))

b = 0
while b < a:
    print('',a)
    b += 1

# 2.1.2
a1 = int(input('숫자를 입력해주세요 :'))   

b1 = 1
while b1 <= a1:
    print(b1,b1*b1)
    b1 += 1

# 2.1.3   # round(a,b) a를 소수점 b로 반올림
height = 100
bounce = 3 / 5

i = 1

while i <= 10:
    height = height * bounce
    print(i, round(height,4))
    i += 1

# 2.1.4
number = 358

rem = rev = 0
while number >= 1:
    rem = number % 10    # number를 10으로 나눈 나머지 8  , 다음은 5   ,  3
    rev = rev * 10 + rem  # 8  ,  85   ,   853
    number = number // 10 # number를 10으로 나눈 몫 35   ,  3     , 0

print(rev)

# 2.2 조건문  
# else 하나의 조건문 elif 여러개의 조건 
# == 앞의 값과 뒤의 값이 같은가 ?
a = 1234 * 4
b = 13456 / 2
if a > b:
    print('a')
else:
    print('b')

c = 15*5
d = 15 + 15 + 15+ 15+ 15

if c>d:
    print('c is greater than d')
elif c == d:
    print('c is equal to d')
elif c<d:
    print('c is less than d')
else:
    print('I don\'t know')

a = 48
b = 4
if a % b == 0:
    print(f'a는 b로 나누어 떨어집니다')
else:
    print(f'a는 b로 나누어 떨어지지 않습니다')

# 10보다 큰 숫자가 들어오면 멈추는 반복문 작성
    
max = 10

while True:
    num = int(input('수를 하나 입력해주세요 : '))
    if num > max:
        print(num,'is too big')
        break

# 2.2.1

num = int(input('숫자를 입력해주세요 : '))

if num == 1:
    print('일')
elif num == 2:
    print('둘')
elif num == 3:
    print('삼')

# 2.2.2
year = int(input('출생년도를 입력해주세요 : '))

gen = None

if year <= 1924:
    gen = '가장 위대한 시대'
elif year <= 1945:
    gen =  '침묵 세대' 
elif year <= 1964:
    gen = '베이비붐 세대'
elif year <= 1980:
    gen = 'X세대'
elif year <= 1996:
    gen = '밀레니얼'
elif year >= 1997:
    gen = 'Z세대'    

print(f"You're {gen}.")



# 2.2.3
num = int(input('정수를 입력해주세요 : '))
result = str(num)

if num >= 1000000:
    result = str(num // 1000000) + 'M'
elif num > 0:
    pass

print(result)

# 2.2.4
# num = num + 1 , num += 1
sum = 0
while True:

    num = int(input('정수를 입력해주세요 : '))
    if num < 0:
        break
    else:
        sum += num    # sum = sum + num
       
    print(sum)

# 2.2.5
# 서력 기원 연수가 4로 나누어 떨어지는 해는 윤년으로 한다. (1988년, 1992년, 1996년, 2004년, 2008년, 2012년, 2016년, 2020년, 2024년, 2028년, 2032년, 2036년, 2040년, 2044년 ...)
# 서력 기원 연수가 4, 100으로 나누어 떨어지는 해는 평년으로 한다. (1900년, 2100년, 2200년, 2300년, 2500년...)
# 서력 기원 연수가 4, 100, 400으로 나누어 떨어지는 해는 윤년으로 둔다. (2000년, 2400년...)  
# leap_year : 윤년
    
leay_year = None
   
year = int(input('년도를 입력해주세요 : '))
if year % 4 == 0:
    print(leay_year)
elif year % 100 == 0:
    print(leay_year)
elif year % 400 == 0:
    print(leay_year)




# 2.2.6
# # 전체 주석 달기 ctrl + k + c
# s = 'banana'
# s

# # if 'a' in s:
# #      if 'b' in 'banana':
# #        print('banana에는 a도 있고 b도 있어요!')

# # if 'a' in s and 'b' in s:
# #     print('banana는 a도 있고 b도 있어요 !')

# # if 'a' in s or 'c' in s:
# #     print('banana에는 a또는 c가 있어요  !' )

# # 'a' in s
# # 'b' in s
# # 'c' in s

# # a_in_s = 'a' in s
# # a_in_s
    
a = 3
b = 0

a / b

(a*b) > 0 and (a / b) > 0  # 왼쪽항부터 진행해서 오른쪽은 보지 않고 넘어감
                           # 그래서 에러가 안뜸
(a / b)>0 and (a * b) >0

# 2.2.7
year = int(input('당신의 태어난 년도는 어떻게 되십니까 ? : '))

gen = None

if year <= 1924:
    gen = '가장 위대한 시대'
elif year <= 1945 or (
    year <= 1954 and input("당신은 한국인입니까 ?(y/n) ") == 'y'
):
    gen = '침묵 세대'
elif year <= 1963 or (
    year <= 1964 and input("당신은 한국인입니까 ?(y/n) ") != 'y' 
):
    gen = '베이비 부머'
elif year <= 1980:
    gen = 'X세대'
elif year <= 1996:
    gen = '밀레니얼'
elif year >= 1997:
    gen = 'Z세대'
    
print(f"You're {gen}.")

# # 2.1.1
# a = int(input('숫자를입력해주세요 :'))

# b = 0
# while b < a:
#     print('',a)
#     b += 1

2.3 
# for를 사용하는 반복문
a = [4, 5, 6, 7]
for i in a:
    print(i)


# 2.3.1
num = int(input('숫자를 입력해주세요 : '))

for i in range(num): # num의 각항목 i에 대하여
    print('',num) 

# 2.3.2
num = int(input('숫자를 입력해주세요 : '))

for i in range(1, num+1):
    print(i,i*i)

# 2.3.3
# split() 문자열을 분해한 리스트를 만들수있다.
'한 국 음 식'.split()   # ex

