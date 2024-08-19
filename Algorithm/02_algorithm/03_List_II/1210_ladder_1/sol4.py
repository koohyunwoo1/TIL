import sys
sys.stdin = open('input.txt')


# 위로 올라가는 경우의 우선순위가 제일 낮기 떄문
# 좌 우 상
dx = [0, 0, -1]
dy = [-1, 1, 0]

def search(x, y):
    if x == 0:  # 제일 위에까지 왔다면
        return y    # 그떄의 y값 반환하고 종료
    # 아직 제일 위에까지 못왔으면 계속 조사
    for i in range(3): # 3방향 조사
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 100 and 0 <= ny < 100 and arr[nx][ny] == 1 and not visited[nx][ny]:
            visited[nx][ny] = 1 # 방문 표시
            return search(nx, ny)   # 이동 | x = nx, y = ny와 같은 동작

for _ in range(10):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    # 방문 표시용 리스트
    visited = [[0] * 100 for _ in range(100)]
    # 출발 지점
    for i in range(100):
        if arr[99][i] == 2:
            result = search(99, i)
    print(f'#{tc} {result}')