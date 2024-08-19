import sys
from heapq import heappush, heappop
sys.stdin = open('input.txt')


def prim(start):
    heap = list()
    MST = [0] * V

    sum_weight = 0

    heappush(heap, (0, start))

    while heap:
        weight, v = heappop(heap)

        if MST[v]:
            continue

        # 방문 처리
        MST[v] = 1
        # 누적합 추가
        sum_weight += weight

        # 갈수 있는 노드를 보면서
        for next_v in range(V):
            # 갈 수 없는 지점이면 continue
            if graph[v][next_v] == 0:
                continue

            # 이미 방문한 지점이면 continue
            if MST[next_v]:
                continue

            heappush(heap, (graph[v][next_v], next_v))

    return sum_weight

T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    graph = [[0] * V for _ in range(V)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        # 정점 번호를 0부터 시작하도록 조정
        graph[s-1][e-1] = w
        # graph[e-1][s-1] = w

    result = prim(1)
    print(f'#{tc} {result}')

