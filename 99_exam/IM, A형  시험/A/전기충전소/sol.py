import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    x, y, d = map(int, input().split())

    x1 = -15
    y2 = 15

    arr = [[0 for _ in range(15)] for _ in range(15)]

    di = [1,0,-1,0]
    dj = [0,1,0,-1]

    for i in range(15):
        cnt = 0
        for j in range(15):
            pass

