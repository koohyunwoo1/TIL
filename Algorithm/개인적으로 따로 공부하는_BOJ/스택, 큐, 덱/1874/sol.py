import sys
sys.stdin = open('input.txt')

n = int(input())

stack = []
result = []
start = 1

for _ in range(n):
    end = int(input())
    while start <= end:
        stack.append(start)
        result.append('+')
        start += 1

    if stack[-1] == end:
        stack.pop()
        result.append('-')

    else:
        print('NO')
        break

else:
    for i in result:
        print(i, end=' ')
