import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    bracket = input()

    stack = []
    for i in bracket:
        if i == '(':
            stack.append(i)
        else:
            if stack:
                stack.pop()
            else:
                print('NO')
                break


    else:
        if not stack:
            print('YES')
        else:
            print('NO')
