import sys, time
sys.stdin = open('input.txt')
'''
정류장에는 교체용 충전기가 있는 교환기가 있고,
충전지마다 최대로 운행할 수 있는 정류장 수가 정해져있다.
'''
T = int(input())

for tc in range(1, T+1):
    N, *M = map(int, input().split())

    M = [0] + M
    # 충전해서 최대 어디까지 갈수 있나
    station = [0 for _ in range(N)]
    for i in range(N):
        station[i] = i + M[i]
        # station : 인덱스값 + 충전하면 몇 정류장을 갈 수 있는지

    cnt = -1 # 충전횟수
            # 첫 정류장의 충전횟수는 포함시키지 않을려고 -1을 해줌
    target = N # 목적지
    idx = 1  # 현재 위치

    while target > 1:
    # 목적지가 현재위치에 도착하면 while문 종료
        if station[idx] >= target:
            cnt += 1
            target = idx
            # 목적지를 줄여주고
            idx = 1
            # 현재위치를 초기화 시켜준다.
        else:
            idx += 1

    print(f'#{tc} {cnt}')

# 0 3 5 4 5
#    1 2 3 4
#
# 0 3 3 6 6 7 11 11 10 10 station
#    1 2 3 4 5 6   7   8   9 idx
#
# 0 2 3 5 5 7 8 8 10 10
#    1 2 3 4 5 6 7  8  9
