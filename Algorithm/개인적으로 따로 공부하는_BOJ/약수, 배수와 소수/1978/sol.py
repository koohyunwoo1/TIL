import sys
sys.stdin = open('input.txt')

N = int(input())
lst = list(map(int, input().split()))

decimal = 0

for i in lst:
    if i == 1:
        continue

    for x in range(2, i):
        if (i % x == 0):
            break
    else:
        decimal += 1


print(decimal)