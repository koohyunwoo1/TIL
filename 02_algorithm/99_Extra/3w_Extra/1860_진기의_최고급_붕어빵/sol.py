import sys
sys.stdin = open('input.txt')

from collections import deque

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    arr = list(map(int, input().split()))
    q = deque(sorted(arr))  # 손님 출몰 시간 정렬 후 q 삽입
    # 누적 빵 개수 기록
    # w -> 매시간 0초부터 마지막 손님 방문시간 + 1
    '''
        M = 2, K = 2 인경우,
        w//M * K
        0초  -> 0//2 == 0 * 2 = 0
        1초  -> 1//2 == 0 * 2 = 0
        2초  -> 2//2 == 1 * 2 = 2
        3초  -> 3//2 == 1 * 2 = 2
        4초  -> 4//2 == 2 * 2 = 4
    '''
    bread = [w//M*K for w in range(q[-1] + 1) ]
    result = 'Possible' # 가능하다고 가정하고,
    cnt = 1             # 방문한 손님 수 카운트
    prev = q[0]         # 이전 방문한 손님 시간 기록
    while q:            # 모든 손님 방문때까지
        time = q.popleft()  # 손님 방문 시간 기록
        '''
            이전번 손님의 방문 시간이 prev
            이번 손님의 방문 시간과 next
            같다면 prev == next
            손님은 한 번에 한개만 가져가므로 항상 빵은 1개씩 감소
        '''
        if time == prev:
            bread[time] -= 1
        else:
            '''
                이전번 손님과 이번 손님이 서로 다른 시간에 방문한다면,
                빵은 누적값으로 기록해 두었으므로 누적 손님 값만큼 감소해야함
                2초때 손님이 방문했을때 빵을 1개 감소했었다면
                이후, 3초때 손님이 방문한다면 기록된 2개가 아닌,
                과거 시간에 손님이 사간 빵 1개 만큼도 감소시켜야하므로 누적 방문 손님 수가 필요함

                2초때 손님 방문            3초때 손님 방문
                0초 1초 2초 3초 4초 5초 => 0초 1초 2초 3초 4초 5초
                0개 0개 1개 2개 4개 4개 => 0개 0개 1개 0개 4개 4개

                이러면 과거에 방문한 손님 (2초)의 빵 수가 문제되지 않는가?
                -> 손님 방문 시간을 정렬한 후, FIFO 하고 있으므로,
                -> 현재시간보다 과거 시간에 손님이 방문 할 경우 없음
            '''
            bread[time] -= cnt
        cnt += 1                # 방문 손님수 누적
        if bread[time] < 0:     # 해당 시간에 빵이 모자라면
            result = 'Impossible'
            break
        prev = time             # 현재 방문한 손님 시간 기록

    print(f'#{tc} {result}')