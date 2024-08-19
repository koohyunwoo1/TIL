import sys
sys.stdin = open('input.txt')

A, B = map(int, input().split())

result = []
for i in range(1, B+1):
    for j in range(i):
        result.append(i)

print(sum(result[A-1:B]))
