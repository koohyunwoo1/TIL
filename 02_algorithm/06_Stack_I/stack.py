##### 202040207


### stack

# 마지막에 삽입한 자료를 가장 먼저 꺼낸다.
# 후입선출

# 스택에서 마지막 삽입된 원소의 위치를 top(stack point) 라고한다.

# 스택의 push 알고리즘
# append 메소드를 통해 리스트의 마지막에 데이터를 삽입

# 연습문제1
# 스택을 구현해보자
# 구현한 스택을 이용하여 3개의 데이터를 스택에 저장하고 다시 3번 꺼내서 출력
def push(n):
    global top
    top += 1
    if top == size:
        print('Overflow!')
    else:
        stack[top] = n

top = -1
size = 10
stack = [0] * size  # 최대 10개의 원소를 저장하는 경우(push)

top += 1
stack[top] = 10

top += 1
stack[top] = 20

push(30)

while top >= 0:
    top -= 1
    print(stack[top+1])


# 연습문제2
# 괄호의 짝을 검사하는 프로그램을 작성해보자
# 작성한 프로그램으로 다음 괄호 사용을 검사해 봅시다.
    
'''
())
하나 푸시하고 하나 꺼내고 하나 꺼내는데 없으니깐 오류  
(()  
하나 푸시하고 하나 푸시하고 하나 꺼내는데 하나 남음
()
하나 푸시하고 하나 꺼냄

'''

