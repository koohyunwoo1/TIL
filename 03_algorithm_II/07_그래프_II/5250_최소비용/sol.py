import sys
from collections import deque
sys.stdin = open('input.txt')

# 테스트 케이스의 개수를 입력받음
T = int(input())

# 각 테스트 케이스에 대해 반복
for tc in range(1, T + 1):
    # 격자의 크기를 입력받음
    N = int(input())

    # 격자 내 각 셀의 높이를 입력받음
    height = [list(map(int, input().split())) for _ in range(N)]

    # 가능한 이동 방향: 위, 아래, 오른쪽, 왼쪽
    di = [1, -1, 0, 0]
    dj = [0, 0, 1, -1]

    # 각 셀까지의 최소 비용을 저장할 2차원 배열 초기화
    min_cost = [[float('Inf')] * N for _ in range(N)]
    # 시작 지점까지의 비용은 0
    min_cost[0][0] = 0

    # BFS 탐색을 위한 큐 초기화 (시작점: (0, 0))
    queue = deque([(0, 0)])

    # BFS 탐색 수행
    while queue:
        # 큐에서 현재 셀을 꺼냄
        i, j = queue.popleft()

        # 인접한 모든 셀을 탐색
        for k in range(4):
            ni = i + di[k]  # 다음 셀의 행 인덱스 계산
            nj = j + dj[k]  # 다음 셀의 열 인덱스 계산

            # 다음 셀이 격자 범위 내에 있는지 확인
            if 0 <= ni < N and 0 <= nj < N:
                # 다음 셀까지의 새로운 비용 계산
                new_cost = max(0, height[ni][nj] - height[i][j]) + 1

                # 다음 셀까지의 비용이 현재까지의 최소 비용보다 작으면
                # 최소 비용을 업데이트하고 다음 셀을 큐에 추가하여 계속 탐색
                if min_cost[i][j] + new_cost < min_cost[ni][nj]:
                    min_cost[ni][nj] = min_cost[i][j] + new_cost
                    queue.append((ni, nj))

    # 현재 테스트 케이스에서 우하단 셀까지의 최소 비용 출력
    print(f'#{tc} {min_cost[N - 1][N - 1]}')


