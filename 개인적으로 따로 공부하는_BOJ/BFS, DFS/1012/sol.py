import sys
sys.stdin = open('input.txt')

def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False

    if field[x][y] == 1 and visited[x][y] == 0:
        visited[x][y] = 1
        dfs(x + 1, y)
        dfs(x - 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)
        return True
    return False

T = int(input())

for tc in range(1, T+1):
    m, n, k = map(int, input().split())

    field = [[0] * m for _ in range(n)]
    visited = [[0] * m for _ in range(n)]
    cnt = 0

    # 배추밭 표시
    for _ in range(k):
        y, x = map(int, input().split())
        field[x][y] = 1


    for i in range(n):
        for j in range(m):
            if dfs(i, j) == True:
                cnt += 1

    print(cnt)