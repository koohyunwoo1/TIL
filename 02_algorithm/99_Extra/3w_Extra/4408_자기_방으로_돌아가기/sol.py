import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * 201
    '''
    0 1 3 5 7 9
    x - - - - -
    0 2 4 6 8 10
    1번과 2번은 같은 복도를 공유한다.
    
    1 -> 3으로 이동한다면
    1번 2번 복도를 사용한다.
    
    4 -> 2로 이동하여도
    2번과 1번 복도를 사용한다.
    
    각 방번호 n에 대해
    n//2 + 1 번 복도는 공유되는 복도이다.
    
    n이 짝수인 경우, n-1과 n은 같은 복도를 공유한다.
    n이 홀수인 경우, n과 n+1은 같은 복도를 공유한다.
    
    홀수번의 경우만 복도 사용 여부를 체크한다.
    '''
    # 정방향 이동시
    for i in range(N):
        for k in range(data[i][0]-1, data[i][1]+1):
            if k % 2:
                visited[k//2+1] += 1
    # 역방향 이동시
    for i in range(N):
        for k in range(data[i][0]-1, data[i][1]-2, -1):
            if k % 2:
                visited[k//2+1] += 1
    # 같은 복도를 공유한 최대 누적 사람수가 단위간 이동시간
    print(f'#{tc} {max(visited)}')
