import sys
sys.stdin = open('input.txt')

'''
    1. N개의 방을 모두 한번씩은 방문해야한다.
        -> 최소 N번 탐색해야한다.
        -> 이전에 방문한 곳은 방문해선 안된다.
    2. 항상 0번에서 출발한다.
        -> 함수 시작점 0으로 잡으면 되겠다.
    3. 마지막에 무조건 0번으로 돌아와야한다.
        -> 코드 짤때 이 부분은 어디에 써야할까?
    4. 갈 때, 올 때 값이 다르다.
'''

'''
    now -> 현재 위치 -> 현 위치에서 다음 위치로 이동 data[now][next]
        now -> 이전번의 next에 들어있던 값이 된다.
    acc -> 누적값
    # cnt -> 조사 횟수
'''
def search(now, acc):
    global result
    if acc > result:
        return
    # print(visited)
    # 언제까지 조사할 것이냐?
    '''
        이때까지 우리는 어떻게 조사했는가?
        이 방식이 모든 상황을 조사 했음을 판별 할 수 있느냐?
        if now == N:
    '''
    # if cnt == N-1:
    # if sum(visited) == N:   # N개의 방에 1씩 방문체크했다면, 다 더하면 N
    if all(visited):    # 모든 방을 방문 했다면...
        # 3. 마지막에 무조건 0번으로 돌아와야한다.
        acc += data[now][0]
        if result > acc:        # 최솟값 갱신
            result = acc
    else:
        # now 위치에서 next 위치로 가는 비용 알아내기
        for next in range(1, N):    # 0번 사무실에서 출발하고, 사무실은 조사대상아님
            # 다음 조사 가능한 값은?
            # 내 위치에서 내 위치로 이동할 수는 없으니
            # 다음 위치 next에 들어가는 방이, 이미 조사한적 있다면 패스
            if now != next and not visited[next]:
                visited[next] = 1   # next번째 조사한다로 기록해두고, 다음 조사
                # def search(now, acc)
                search(next, acc + data[now][next])
                visited[next] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N       # 모든 방 방문 여부 체크용 리스트
    visited[0] = 1          # 0번에서 출발함을 체크
    # for d in data:
    #     print(d)
    # 최종 결괏값
    result = N*101
    search(0, 0)
    print(f'#{tc} {result}')