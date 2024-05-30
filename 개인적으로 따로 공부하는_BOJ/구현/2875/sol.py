import sys
sys.stdin = open('input.txt')

N, M, K = map(int,input().split())

cnt = 0

while N >= 2 and M >= 2 and N + M >= K + 3:
    N -= 2
    M -= 2
    cnt += 1

print(cnt)