import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(N)]
    
    di = [1,0,-1,0]
    dj = [0,1,0,-1]

    result = []

    for i in range(N):
        for j in range(M):
            cnt = 0
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < N and 0 <= nj < M:
                    cnt += lst[ni][nj]
            result.append(cnt + lst[i][j])

    print(f'#{tc} {max(result)}')        
