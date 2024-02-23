import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(N)]

    max_cnt = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            cnt = 0
            for k in range((M // 2) -1, (M // 2) + 1):
                for l in range((M // 2) -1, (M // 2) + 1):
                    cnt += lst[i+k][j+l]

            if max_cnt < cnt:
                max_cnt = cnt


    print(max_cnt)

