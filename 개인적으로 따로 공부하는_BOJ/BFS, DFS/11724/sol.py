from sys import stdin
read = stdin.readline

# 출발지를 주지 않음.

N, M = map(int, read().split())

for _ in range(M):
    left, right = map(int, read().split())

    graph = [[0] for _ in range(N + 1)]
    graph[left].append(right)
    graph[right].append(left)

visited = [False] * (N+1)

