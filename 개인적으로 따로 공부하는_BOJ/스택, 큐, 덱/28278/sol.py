import sys
sys.stdin = open('input.txt')
'''
시간초과뜸

'''
N = int(input())
stack = []
for tc in range(N):
    lst = input()

    if len(lst) > 2:
        stack.append(int(lst[1:]))

    elif lst == '2':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif lst == '3':
        print(len(stack))
    elif lst == '4':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    else:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])