import sys
sys.stdin = open('input.txt')

N = int(input())
result = []
for i in range(N):
    num = int(input())
    result.append(num)
    result.sort()

for i in result:
    print(i)