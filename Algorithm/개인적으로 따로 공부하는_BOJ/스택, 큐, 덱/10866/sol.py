import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

from collections import deque

N = int(input())
d = deque()

for n in range(N):
    command = list(map(str, input().split()))

    if command[0] == 'push_front':
        d.appendleft(command[1])
    elif command[0] == 'push_back':
        d.append(command[1])
    elif command[0] == 'pop_front':
        if len(d) != 0:
            print(d.popleft())
        else:
            print(-1)
    elif command[0] == 'pop_back':
        if len(d) != 0:
            print(d.pop())
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(d))
    elif command[0] == 'empty':
        if len(d) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == 'front':
        if len(d) > 0:
            print(d[0])
        else:
            print(-1)
    elif command[0] == 'back':
        if len(d) > 0:
            print(d[-1])
        else:
            print(-1)