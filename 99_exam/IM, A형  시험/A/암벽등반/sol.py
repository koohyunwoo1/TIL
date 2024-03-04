import sys
sys.stdin = open('input.txt')
'''
목표지점이 3
출발지점이 2
1 -> 발을 디딜곳이 있는 곳
0 -> 발을 디딜곳이 없는 곳
한번에 최대로 올라갈수있는 높이가 즉 난이도이다.
'''
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    start = 0, 0
    end = 0, 0

    for i in range(N):
        for j in range(M):


