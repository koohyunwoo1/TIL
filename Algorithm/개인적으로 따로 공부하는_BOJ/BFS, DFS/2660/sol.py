N = int(input())
M = int(input())

graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def DFS(v, cnt):
    visited[v] = True
    for i in graph[v]:
        if visited[i] == False:
            visited[i] = True
            cnt = DFS(i, cnt + 1)


    return cnt


print(DFS(1, 0))