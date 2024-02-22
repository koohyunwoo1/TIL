import sys
sys.stdin = open('input.txt')

from collections import deque

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def BFS(x, y):
    q = deque([(x, y)])
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < 100 and 0 <= ny < 100 and maze[nx][ny] != 1:
                if maze[nx][ny] == 3:
                    return 1
                maze[nx][ny] = 1
                q.append((nx, ny))
    return 0

for _ in range(10):
    tc = int(input())
    maze = [list(map(int, input())) for _ in range(100)]
    result = None
    for i in range(100):
        for j in range(100):
            if maze[i][j] == 2:
                result = BFS(i, j)
                break
        if result != None:
            break
    print(f'#{tc} {result}')