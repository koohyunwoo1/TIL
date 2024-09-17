import sys
n = int(input())
queue = []
for i in range(n):
    com = sys.stdin.readline().split()
    if com[0] == 'push':
        queue.append(com[1])
    elif com[0] == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.pop(0))  
    elif com[0] == 'size':
        print(len(queue))
    elif com[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif com[0] == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif com[0] == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])