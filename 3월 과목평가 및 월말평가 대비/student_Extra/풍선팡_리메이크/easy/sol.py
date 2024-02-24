import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = []
    for _ in range(N):
        flower = list(map(int, input().split()))
        arr.append(flower)

    max_flower = 0

    for i in range(N):
        for j in range(M):
            flower_count = arr[i][j]
            if flower_count % 2 == 0:
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nx = i + dx
                    ny = j + dy
                    if 0 <= nx < N and 0 <= ny < M:
                        flower_count += arr[nx][ny]

            else:
                for dx, dy in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
                    nx = i + dx
                    ny = j + dy
                    if 0 <= nx < N and 0 <= ny < M:
                        flower_count += arr[nx][ny]

            if max_flower < flower_count:
                max_flower = flower_count

    print(f'#{tc} {max_flower}')

