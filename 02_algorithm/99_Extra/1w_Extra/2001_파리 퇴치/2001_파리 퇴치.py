import sys
sys.stdin = open('input.txt')

# N x N 배열 안의 숫자는 해당 영역에 존재하는 파리의 개수를 의미한다.

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_cnt = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            cnt = 0
            for k in range(M):
                for l in range(M):
                    cnt += arr[i+k][j+l]
            if max_cnt < cnt:
                max_cnt = cnt


    print(f'#{tc} {max_cnt}')