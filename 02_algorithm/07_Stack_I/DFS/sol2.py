import sys
sys.stdin = open('input.txt')

def DFS(start):
    stack = [start] # 다음 조사 대상
    while stack:    # 조사 대상이 없어질때까지
        now = stack.pop()   # LIFO
        if visited[now] == 0:
            visited[now] = 1  # 방문 표시
            print(now, end=' ')
            # 0번 노드 제외 모든 노드번호가 now번 위치에서 이동 가능한지 판별
            for next in range(V, 0, -1):
            # for next in range(1, V + 1):
                # adj[now == 1][next == 1~7]
                # adj[1][2] or adj[1][3] == 1
                if visited[next] == 0 and adj[now][next] == 1:
                    stack.append(next)



V, E = map(int, input().split())
arr = list(map(int, input().split()))
visited = [0] * (V + 1) # 0번 노드 없음.
print(arr)
# 인접 행렬
adj = [[0] * (V + 1) for _ in range(V + 1)]

for idx in range(E):
    adj[arr[idx * 2]][arr[idx * 2 + 1]] = 1
    adj[arr[idx * 2 + 1]][arr[idx * 2]] = 1

for i in range(V + 1):
    print(adj[i])

DFS(1)