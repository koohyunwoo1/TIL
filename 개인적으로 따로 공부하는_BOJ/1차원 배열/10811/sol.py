import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())

basket = []
for n in range(1, N+1):
    basket.append(n)

for m in range(M):
    i, j = map(int, input().split())
    rev = basket[i-1:j]
    rev.reverse()
    basket[i-1:j] = rev

print(*basket)