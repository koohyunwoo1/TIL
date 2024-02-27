import sys
sys.stdin = open('input.txt')

T = int(input())

def check(x,y,total):
    global result
    if x == N-1 and y == N-1:
        total += arr[x][y]
        if total < result:
            result = total
            return

    if total > result:
        return

    dx = [1,0]
    dy = [0,1]

    for i in range(2):
        cx = x + dx[i]
        cy = y + dy[i]
        if x > N-1 or y > N-1:
            continue
        if not visited[x][y]:
            visited[x][y] = 1
            check(cx, cy, total + arr[x][y])
            visited[x][y] = 0

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int ,input().split())) for _ in range(N)]
    result = 10000
    visited = [[0 for _ in range(N)] for _ in range(N)]
    check(0, 0, 0)

    print(f'#{tc} {result}')
