import sys
sys.stdin = open('input.txt')


'''
숫자를 만나면 stack에 푸시
연산자를 만나면 필요한만큼의 숫자를  스택에서 pop하고
연산 결과를 다시 스택에 push함
스택에 있는 숫자를 2개 꺼내야함.

'''
T = int(input())

for tc in range(1,T+1):
    forth = list(input().split())
    print(forth)
    operator = ['*','/','+','-']
    stack = []

    for i in forth:
        if i.isdigit():
            stack.append(i)
            # print(stack)
            # 숫자만 뽑아서 stack에 추가해준다.
        elif i in operator:
            # 연산자이고
            if stack:
                # stack이 비어있지 않으면
                num1 = int(stack.pop())
                if stack:
                    num2 = int(stack.pop())
                    if i == '+':
                        stack.append(num2 + num1)
                    if i == '-':
                        stack.append(num2 - num1)
                    if i == '*':
                        stack.append(num2 * num1)
                    if i == '/':
                        stack.append(num2 // num1)
    if len(stack) == 1:
        print(f'#{tc} {stack[0]}')
    else:
        print(f'#{tc} error')