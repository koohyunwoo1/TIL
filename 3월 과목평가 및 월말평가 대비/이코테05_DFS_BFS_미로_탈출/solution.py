import sys
from collections import deque
sys.stdin = open('input.txt')

def bfs():
    queue = deque([[0, 0]])

    while queue:
        x, y = queue.popleft()
        for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
            nx, ny = x + dx, y + dy
            if (0 <= nx < n) and (0 <= ny < m) and graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append([nx, ny])

    return graph[n - 1][m - 1]


n, m = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(n)]

print(bfs())