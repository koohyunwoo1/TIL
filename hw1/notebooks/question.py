'''
함수를 정의할 때, 매개변수에 패킹을 사용해서
가변 인자로 받게 되면 튜플로 받는데...

왜, 변수에 패킹을 사용해서
다수의 데이터를 받으면 리스트로 받는 이유는 뭔가요?
'''
'''
tuple
- 순서가 있는 시퀀스 타입
- 순회가 가능한 iterable 한 데이터
- 여러개의 데이터를 담을수 있는 colletion
- 내부 요소를 변경 할 수 없는 immutable

list
- 순서가 있는 시퀀스 타입
- 순회가 가능한 iterable 한 데이터
- 여러개의 데이터를 담을수 있는 colletion
- 내부 요소를 변경 할 수 있는 mutable
'''
# 함수는, 입력값에 따른 정확한 출력값을 기대한다.
# 함수가 하는 일에 대해서 항상 같은 입력값에 같은 출력값이 나와야한다.
# 애초에 코드를 그렇게 안쓰면 되는거아님?
    # 매개변수로 넘겨 받은 데이터가 변경되지 않도록 코드를 쓴다.
    # 지극히 맞는말임. 그렇게 하라고, 일부러 tuple로 한번더 
def some_func(*args):
    print(args) # (1, 2, 3, 4)
    print(type(args)) # <class 'tuple'>

some_func(1, 2, 3, 4)

# 변수에 값을 할당할때의 기대값은,
# 특정 데이터를 편하게 참조 할 수 있는 기능
# 해당 데이터의 값을 변경하거나, 조작하거나, 활용하는 용도를 기대
a, *b, c = [1, 2, 3, 4, 5]
print(b)    # [2, 3, 4]
print(type(b)) # <class 'list'>

print([1, 2, 3, 4, 5])
print(*[1, 2, 3, 4, 5])

'''
함수 : 입력에 대한 출력이 있다.

기명 함수 정의 키워드
def 함수_이름(매개변수, 매개변수): (이름이 있어서 나중에 다시 부를 수 있음)
    함수 할일
- 코드 재사용 가능 
- a데이터도, b데이터도, c데이터도 매번 ㄱ함수를 거쳐야 한다..

익명 함수 정의 키워드
lambda (매개변수, 매개변수): 함수 할일
- 코드 재사용 불가능
- 아주 간단한 로직인데, 순회가능한 어떤 데이터에 대해서 
- 각 요소들에 대해서만 똑같은 로직 실행 해야 할 때.
'''
def my_sum(num1, num2):
    return num1 + num2
result = my_sum(1, 2)

my_sum_lambda = lambda num1, num2: num1 + num2
result_2 = my_sum_lambda(3, 4)
print(result, result_2)

a = [1, 2, 3]
b = [4, 5, 6]
result_3 = map(lambda num1, num2: num1 + num2, a, b)
print(list(result_3))

result_4 = map(my_sum, a, b)
print(list(result_4))