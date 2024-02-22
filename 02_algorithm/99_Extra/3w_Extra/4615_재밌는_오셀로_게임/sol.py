import sys
sys.stdin = open('input.txt')

# 상 하 좌 우, 좌상, 우상, 우하, 좌하
dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, 1, -1]

def change(x, y, c):
    for i in range(8):  # 모든 방면 조사
        stack = []      # 바꿔야 할 돌 목록을 담을 곳
        nx = x + dx[i]  # 다음 x 좌표
        ny = y + dy[i]  # 다음 y 좌표
        # 범위를 벗어나지 않는동안 계속해서 조사
        while 0 <= nx < N and 0 <= ny < N:
            # c == 2 (W) 일때, c%2(0) + 1 == 1 (B)
            # c == 1 (B) 일때, c%2(1) + 1 == 2 (W)
            # 내가 흰돌일 때, 검은돌만 골라서 바꾼다.
            # 벽인 (0) 도 무시하여야 함
            if matrix[nx][ny] == c%2+1:
                stack.append((nx, ny))  # 나와 다른 색의 돌을 스택에 모으고
                nx = nx+dx[i]   # 현재 이동 방향으로 계속 이동
                ny = ny+dy[i]
            # 나와 다른 색의 돌을 바꿔나가다가,
            # 나와 같은 색의 돌을 만나면
            elif matrix[nx][ny] == c:
                for i, j in stack:      # 스택에 모아둔 다른 색의 돌들을 전부
                    matrix[i][j] = c    # 내 돌색으로 바꾼다
                break                   # 조사 종료
            else:       # 만약 다른색도, 같은색도 아닌 0을 만나면
                break   # 그냥 종료
        # for m in matrix:  # 돌이 놓여지는 과정
        #     print(m)
        # print()

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    # y, x, c (1=B, 2=W)
    turn = [list(map(int, input().split())) for _ in range(M)]
    matrix = [[0]*(N) for _ in range(N)]    # 판의 크기
    mid = N // 2
    # 중앙을 계산 하는 방식이 문제에서는 index 번호보다 1 크게 잡고 있으므로
    # 0번 index부터 사용한다고 가정하면 mid - 1 위치가 흰색 돌의 왼쪽 위 시작점
    matrix[mid-1][mid-1], matrix[mid][mid] = 2, 2   # 흰돌
    matrix[mid-1][mid], matrix[mid][mid-1] = 1, 1   # 검은돌

    for i in range(M):
        # 마찬가지로, index보다 1 높은 수가 주어지므로
        # 각 값에 1을 뺀 위치에 돌을 두고
        # 예를들어, y,x = 1,2 라면, 실제로는 matrix[0][1] 위치에 돌을 두어야 한다.
        y = turn[i][0] - 1
        x = turn[i][1] - 1
        c = turn[i][2]
        matrix[x][y] = c
        # 오셀로 룰에 따라 뒤집어야 할 돌을 찾아서 뒤집는다.
        change(x, y, c)
    # 모든 조사를 마친뒤, 돌의 수를 센다.
    W = 0
    B = 0
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 1:
                B += 1
            elif matrix[i][j] == 2:
                W += 1
    print(f'#{tc} {B} {W}')

