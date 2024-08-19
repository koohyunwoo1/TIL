import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

from collections import deque

N = int(input())

d = deque()

for n in range(N):
    command = list(map(int, input().split()))


    if command[0] == 1:
        d.appendleft(command[1])
    elif command[0] == 2:
        d.append(command[1])
    elif command[0] == 3:
        if len(d) == 0:
            print(-1)
        else:
            print(d.popleft())
    elif command[0] == 4:
        if len(d) == 0:
            print(-1)
        else:
            print(d.pop())

    elif command[0] == 5:
        print(len(d))

    elif command[0] == 6:
        if len(d) == 0:
            print(1)
        else:
            print(0)

    elif command[0] == 7:
        if len(d) == 0:
            print(-1)
        else:
            print(d[0])

    else:
        if len(d) == 0:
            print(-1)
        else:
            print(d[-1])