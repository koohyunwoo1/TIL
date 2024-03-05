import sys
sys.stdin = open('input.txt')

N, M = map(int,input().split())

basket = [0 for _ in range(N)]

for m in range(M):
    i, j, k = map(int, input().split())
    # i번 바구니부터 j번 바구니까지 k번 번호가 적혀져 있는 공을 넣는다.
    for n in range(i, j+1):
        basket[n-1] = k

for n in range(N):
    print(basket[n], end=' ')

