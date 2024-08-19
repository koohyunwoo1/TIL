import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    # 한번 충전으로 최대한 이동할수있는 정류장 수 K
    # N : 종점
    # M : 충전기가 설치된 정류장의 수
    num = list(map(int, input().split()))

    cnt = 0 # 충전횟수
    loc = 0 # 현재위치

    while loc != N:
        if loc+K >= N:
            loc = N
            break
        for i in range(len(num)-1, -1, -1):
            if num[i] <= loc+K:
                cnt += 1
                loc = num[i]
                num = num[i+1:]
                break
            if i == 0:
                cnt = 0
                loc = N



    print(f'#{tc} {cnt}')