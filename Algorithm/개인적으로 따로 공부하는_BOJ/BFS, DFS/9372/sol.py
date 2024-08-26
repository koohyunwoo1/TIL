import sys
input = sys.stdin.readline

def dfs(node, cnt):
    visit[node] = 1
    for i in Tree[node] :
        if visit[i] == 0:
            cnt = dfs(i, cnt+1)
    return cnt

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    Tree = [[] for _ in range(N+1)]
    
    for _ in range(M):
        u, v = map(int, input().split())
        Tree[u].append(v)
        Tree[v].append(u)

    visit = [0] * (N+1)
    visit[1] = 0
    result = dfs(1, 0)
    print(result)