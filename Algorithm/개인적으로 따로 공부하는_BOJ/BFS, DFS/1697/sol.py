from collections import deque

n, k = map(int, input().split())
visited = {}
def bfs(s):
    q = deque()
    q.append(s)
    visited[s] = 0
    while q:
        cur = q.popleft()
        if cur == k:
            return visited[k]
        for i in (cur+1, cur-1, cur * 2):
            if i not in visited: 
              visited[i] = visited[cur] + 1
              q.append(i)
print(bfs(n))