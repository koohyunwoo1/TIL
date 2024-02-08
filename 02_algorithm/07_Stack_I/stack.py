#### 202040208


# DP
# def f(i, k):
#     if i == k:
#         print('end')
#     else:
#         f(i+1, k)

# f(0,1000)


# DFS
# 깊이 우선 탐색

'''
시작 정점의 한 방향으로 갈 수 있는 경로가 있는 곳 까지
깊이 탐색해 가다가 더 이상 갈곳이 없게 되면, 가장 마지막에 만났던
갈림길 간선이 있는 정점으로 되돌아와서 다른 방향의 정점으로 탐색을
계속 반복하여 결국 모두 순회하는 방법
'''
'''
시작 정점 v를 결정하여 방문한다.
정점 v에 인접한 정점 중에서
1. 방문하지 않은 정점 w가 있으면, 정점 v를 스택에 push하고 정점  w를 방문
그리고 w를 v로 하여 다시 반복

2. 방문하지 않은 정점이 없으면,탐색의 방향을 바꾸기 위해서 스택을 pop하여 받은
가장 마지막 방문 정점을  v로 하여 다시 반복
'''
'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''

def dfs(i):
    visited[i] = 1
    print(i)
        # 현재 방문한 정점에 인접하고 방문안한 정점이 있으면
    for w in adjl[i]:
        if visited[w] == 0:
            dfs(w)


V, E = map(int, input().split())
arr = list(map(int, input().split()))


# 인접리스트
adjl = [[] for _ in range(V+1)]
for i in range(E):
    n1, n2 = arr[i*2], arr[i*2+1]
    adjl[n1].append(n2)
    adjl[n2].append(n1)
visited = [0] *(V+1)
dfs(1)

# BFS
# 너비 우선 탐색