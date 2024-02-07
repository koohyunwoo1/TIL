import sys
sys.stdin = open('input.txt')

T = int(input())


class Stack:
    # stack을 생성 할 때 필요한 값이 있는데,
    # stack의 크기를 지정해야한다.
    def __init__(self, size):
        self.size= size
        self.data = [None] * size # 값이 없음을 나타내는 None
        self.top = -1 # 초기 값이 없으므로, top의 위치는 -1

    def push(self, item):   # stack에 값 삽입 -> 삽입할 대상 item을 인자로 받는다.
        self.top += 1 # top위치 1 증가
        if self.is_full():    # stack이 가득 찼다면
            print('Stack is Full!!!')
        else:
        # 받아온 item을 내 data에 top 번째 위치에 삽입한다.
            self.data[self.top] = item

    def get(self):
        return self.data[self.top]
    
    def __str__(self):    # instance print했을때, stack안의 data를 바로 출력
        return f'{self.data}'

    def pop(self):
        if self.is_empty():
            print('Stack is Empty!!')
        else:
            self.top -= 1
            return self.data[self.top + 1]
    
    def is_empty(self):
        # top이 -1을 가리키고 있다면 stack은 비었다.
        return self.top == -1
    
    def is_full(self):
        return self.size == self.top + 1

# stack 사이즈 100짜리 생성후, 출력
stack = Stack(100)
for i in range(99):
    stack.push(99)
stack.push(151359135)
for i in range(99):
    stack.pop()
stack = Stack(100)

print(stack.size)
print(stack.data)
print(stack.top)
stack.push(10)
print(stack.data)
print(stack.top)
print(stack.get())
print(stack)
print(stack.pop())