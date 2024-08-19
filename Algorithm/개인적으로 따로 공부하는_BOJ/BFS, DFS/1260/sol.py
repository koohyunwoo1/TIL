'''
첫째줄에 DFS 둘째줄에 BFS
DFS : 인접한 노드 중 시작점 V부터 숫자가 작은 노드 부터 방문, 이미 방문 -> 다시 돌아감
BFS : 너비 우선
'''
from sys import stdin
read = stdin.readline

N, M, V = map(int, read().split())

graph = [[0]*(N+1) for _ in range(N+1)]
visited = [False]*(N+1)

for _ in range(M):
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1


def dfs(V):
    visited[V] = True
    print(V, end=' ')
    for i in range(1, N+1):
        if not visited[i] and graph[V][i] == 1:
            dfs(i)


def bfs(V):
    visited[V] = False
    queue = [V]
    while queue:
        V = queue.pop(0)
        print(V, end=" ")
        for i in range(1, N+1):
            if visited[i] and graph[V][i] == 1:
                queue.append(i)
                visited[i] = False


dfs(V)
print()
bfs(V)