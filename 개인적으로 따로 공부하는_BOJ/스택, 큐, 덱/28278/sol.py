import sys
sys.stdin = open('input.txt')

N = int(input())
stack = []
for tc in range(1, N+1):
    command = input().rstrip()

    if len(command) > 2:
        stack.append(int(command[2:]))

    elif command == '2':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())

    elif command == '3':
        print(len(stack))

    elif command == '4':
        if stack:
            print(0)
        else:
            print(1)

    elif command == '5':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
