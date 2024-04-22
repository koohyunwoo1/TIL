import sys
sys.stdin = open('input.txt')

S = int(input())
n = 1

while n * (n + 1) / 2 <= S:
    n += 1
result = n - 1
print(result)

