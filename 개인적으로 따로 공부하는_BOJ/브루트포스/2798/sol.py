import sys
sys.stdin = open('input.txt')
'''
카드의 합이 M을넘지 않는 한도 내에서, 카드의 합을 최대한 크게 만드는 게임이다.
N장의 카드 중에서 3장의 카드를 골라야한다.

'''

N, M = map(int, input().split())
num = list(map(int, input().split()))

result = []

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            total = num[i] + num[j] + num[k]
            if total > M:
                continue
            else:
                result.append(total)

print(max(result))
