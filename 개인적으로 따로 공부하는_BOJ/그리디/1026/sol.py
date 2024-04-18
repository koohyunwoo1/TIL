import sys
sys.stdin = open('input.txt')

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
ans = 0

for i in range(N):
    x = A[i]
    y = B.pop(B.index(max(B)))
    ans += x * y

print(ans)