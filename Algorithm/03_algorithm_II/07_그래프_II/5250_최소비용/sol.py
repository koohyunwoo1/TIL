import sys
from collections import deque
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):

    N = int(input())

    height = [list(map(int, input().split())) for _ in range(N)]

    di = [1, -1, 0, 0]
    dj = [0, 0, 1, -1]

    min_cost = [[float('Inf')] * N for _ in range(N)]
    # 시작 지점까지의 비용은 0
    min_cost[0][0] = 0

    queue = deque([(0, 0)])

    while queue:

        i, j = queue.popleft()

        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]

            # 범위 안에 있고
            if 0 <= ni < N and 0 <= nj < N:
                # 높이차이가 음수인 경우가 발생하면 음수로 하면 안되서
                # 0으로 해주기 위해서 0이랑 비교해줌

                new_cost = max(0, height[ni][nj] - height[i][j]) + 1

                # 다음까지의 비용이 현재까지의 최소 비용보다 작으면
                # 최소 비용을 업데이트하고 다음을 큐에 추가하여 계속 탐색
                if min_cost[i][j] + new_cost < min_cost[ni][nj]:
                    min_cost[ni][nj] = min_cost[i][j] + new_cost
                    queue.append((ni, nj))


    print(f'#{tc} {min_cost[N - 1][N - 1]}')


