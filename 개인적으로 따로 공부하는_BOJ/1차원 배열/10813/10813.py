import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
# N : 바구니의 수 M : 바구니 교환 횟수
basket = []
for a in range(1, N+1):
    basket.append(a)

for m in range(1, M+1):
    i, j = map(int, input().split())
    basket[i-1], basket[j-1] = basket[j-1], basket[i-1]

print(*basket)