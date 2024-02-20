import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int,input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    di = [1, 0, -1, 0]
    dj = [0, 1, 0, -1]

    max_flower = 0

    for i in range(N):
        for j in range(M):
            total = arr[i][j]

            for k in range(4):
                for l in range(1, arr[i][j] + 1):
                    ni = i + di[k] * l
                    nj = j + dj[k] * l
                    if 0 <= ni < N and 0 <= nj < M:
                        total += arr[ni][nj]

            if total > max_flower:
                max_flower = total

    print(f'#{tc} {max_flower}')


    

