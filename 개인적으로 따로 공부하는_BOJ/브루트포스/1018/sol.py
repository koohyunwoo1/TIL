import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())

arr = [list(map(str, input())) for _ in range(N)]

di = [1,0,-1,0]
dj = [0,1,0,-1]

for i in range(M):
    for j in range(N):
        cnt = 0
        for k in range(4):
            ni = di
            pass