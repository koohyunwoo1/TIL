## 20240122

# 자료 구조

# 각 데이터의 효율적인 저장, 관리를 위한 구조를 나눠 놓은 것


# 메서드
# 객체에 속한 함수

print(type('1'))
print(type(['1']))
# print(help(str))

def append():
    pass

# append()    # 함수 호출
# 리스트.append # 메서드 호출
# 객체.메서드()


print('hello'.capitalize())

numbers = [1,2,3]
numbers.append(4)   # 4추가

print(numbers)


# s.find(x)   # x의 첫 번째 위치를 반환. 없으면 -1을 반환
# x.index(x)   # x의 첫 번째 위치를 반환. 없으면 오류발생
# s.isalpha()   # 알파벳 문자 여부     # True  False
# s.isupper()    # 알파벳이 모두 대문자인지 # True  False
# s.islower()     # 알파벳이 모두 소문자인지 # True  False

# find 

my_str = 'banana'
print(my_str.find('a'))   # 1
print(my_str.find('z'))    # -1 값이 없기 때문에 -1을 반환

# # index
# my_str = 'banana'
# print(my_str.index('a'))   # 1
# print(my_str.index('z'))    # 에러 뜸

# isalpha   # 문자열이 알파벳으로만 구성이 되어있는지 알기 위한것.
string1 = 'Hello'
string2 = '123'
print(string1.isalpha())   # True
print(string2.isalpha())   # False


# .replace
text = 'Hello, world! '
new_text = text.replace('world', 'Python')   # (old , new) # old를 new로 바꿔줌
print(new_text)

# .strip
# 문자열의 시작과 끝에 있는 공백 혹은 지정한 문자를 제거

text = '    Hello, world!    '  # 공백하고 지정한 문제가 같이 있으면 지정한 문제만 제거가 됨.
new_text = text.strip()
print(new_text)

# .split(sep=None, maxsplit= -1)
# 지정한 문자를 구분자로 문자열을 분리하여 문자열의 리스트로 반환
text = 'Hello, world!'
words = text.split(',')
print(words)      # ['Hello', ' world!']


# 'separator'.join(iterable)
# iterable 요소들을 원래의 문자열을 구분자로 이용하여 하나의 문자열로 연결

words = ['Hello', 'world!']
text = '-'.join(words)
print(text)   # Hello-world!


text = 'heLLo, woRld!'

new_text = text.swapcase().replace('l','z')

print(new_text)   #HEzzo, WOrLD!

# 시퀀스 데이터 구조
# 리스트 값 추가 및 삭제 메서드

my_list = [1,2,3]


my_list.append(4)    # 리스트채로 들어감.
# print(my_list.append([10,9,8]))   # None
print(my_list)


# extend
my_list.extend([4,5,6])  # 리스트채로 들어가지 않고 요소로 들어감
print(my_list)

# insert

my_list.insert(3, 'ssafy')  # 인덱스 상 3번째 순서에 문자열 'ssafy' 추가
print(my_list)

# remove

my_list.remove(4)  #(중복이 있을 경우) 검색 했을때 첫번째 순서를 제거해줌
print(my_list)

# pop # 아무런 옵션을 주지 않으면 마지막것을 제거
item1 = my_list.pop()   
print(item1)  # 6

item2 = my_list.pop(0)  
print(item2) # 1

print(my_list)  # 6 ,1 이 제거된 my_list 값 출력

# clear
# 리스트의 모든 항목을 삭제

index = my_list.index(2)
print(index)    # 0  2의 인덱스 위치가 0이기 때문이다.

my_list = [1, 2, 3, 2, 3, 3]
count_num = my_list.count(3)
print(count_num)   # 3  my_list안에 들어있는 3의 개수를 세라

my_list = [3,2,1]
# print(my_list.sort())  # None
my_list.sort()
# sort는 원본을 바꾸기 때문에 원본 my_list를 출력해야한다.
print(my_list)

my_list.sort(reverse=False)   # False는 오름차순 
print(my_list)                # True는 내림차순


my_list = [1,3,2,8,1,9]
my_list.reverse()   # list의 안에 값을 뒤집어서 출력함.
print(my_list)

# a = [1,2,3,4]
# b = a     # 주소를 할당한것이기에 a값도 100으로 바뀜.
            # 리스트는 가변이기에 바뀔수 있음.
  
# b[0] = 100     

# print(a)
# print(b)



# 정수형은 불변이기에 바뀌지 않는다.
a = 100
b = a 

b = 9
print(a,b)    # 100 9

# 할당
original_list = [1,2,3]
copy_list = original_list

copy_list[0] = 'hello'
print(original_list)
 
 # 얕은 복사
a = [1,2,3]
b = a[:]

b[0] = 100

print(a,b)  # [1,2,3][100,2,3]

# 얕은 복사의 한계
a = [1,2, [100,200]]
b = a[:]

b[2][0] = 999

print(a,b)  # [1, 2, [999, 200]] [1, 2, [999, 200]]


# 깊은 복사
import copy # 내장함수

original_list = [1,2,[1,2]]
deep_copied_list = copy.deepcopy(original_list)

deep_copied_list[2][0] = 100

print(original_list)    # [1, 2, [1, 2]]
print(deep_copied_list)   # [1, 2, [100, 2]]
