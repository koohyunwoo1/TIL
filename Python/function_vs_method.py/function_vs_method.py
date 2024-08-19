# function_vs_method.py (특히, str.method)
# 헷갈리기 시작하는 것
# 언제 어느 순간의 어떤 함수는 이렇게 작동하는데
# 얘는 왜 이렇게 작동함?
# 이거 외워야 함?
# 외우다 -> 이해의 범주
# 무엇을 외우냐에 따라 달라지는데...
# str.title() 타이틀 메서드를 외워버림.
# str.upper() 메서드도 외움
# str.lower() 메서드도 외우
# str.join() 메서드도 외우고
# str.is_decimal() 메서드도 외우고
# 외워야 하는 것 : str이란 무엇인가
# print('a'.zfill(4))
# a = 'a'
# while len(a) != 4:
#     a = '0' + a
# print(a)

# list의 메서드는 대체적으로 원본을 바꾸는게 하는 일임
# -> list는 원본을 바꿀 수 있으니까 원본을 바꿈
# 메서드라는 것 자체가 ~~의 함수
# list.append(a) -> 반환값이 None
# list.extend -> 반환값이 None
# list.pop -> 반환값이 있음
# list.remove -> 반환값이 None
    # 함수는 return 하는게 일이아니라
    # 함수는 무언가 input에 대한 처리를 하는 것이 함수가 하는일

# 파이썬은 함수의 return 값이 반드시 존재한다. (return을 정의안하면 None)
# 와
# 함수는 반드시 어떤 값을 반환해야 한다. X
# 두 이야기는 다른이야기

# 근데 문자열 메서드는 죄다 반환값이 있는것 같음
# 문자열은 원본 수정이 안되니까.
a = 'hello, world'
b = a.title()
print(b)