import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_cnt = 0

    for i in range(N-M+1):
        for j in range(N-M+1):
            cnt = 0
            cnt2 = 0

            for k in range(M):
                for l in range(M):
                    cnt += arr[i+k][j+l]
                    if k != 0 and k != M-1 and l != 0 and l != M-1:
                        cnt2 += arr[i+k][j+l]

            if max_cnt < cnt - cnt2:
                max_cnt = cnt - cnt2


    print(f'#{tc} {max_cnt}')





















'''
T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(N)]

    max_cnt = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            cnt = 0
            cnt2 = 0
            for k in range(M):
                for l in range(M):
                    # cnt2 = 0
                    cnt += lst[i+k][j+l]
                    if k != 0 and k != M-1 and l != 0 and l != M-1:
                        cnt2 += lst[i+k][j+l]

            if max_cnt < cnt - cnt2:
                max_cnt = cnt - cnt2

    print(f'#{tc} {max_cnt}')
'''
