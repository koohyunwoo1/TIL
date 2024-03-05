import sys
sys.stdin = open('input.txt')

N, K = map(int, input().split())

result = 1
for i in range(K):
    result = result * (N-i)
for i in range(1, K+1):
    result = result // i
print(result)