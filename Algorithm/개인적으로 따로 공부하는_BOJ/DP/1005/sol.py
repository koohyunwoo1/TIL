import sys
from collections import deque

input = sys.stdin.readline

# 테스트 케이스 수 T
T = int(input())

for _ in range(T):
    # 건물의 개수 N과 건설 순서 규칙의 개수 K
    N, K = map(int, input().split())
    
    # 각 건물의 건설에 걸리는 시간
    construction_time = list(map(int, input().split()))
    
    # 그래프와 진입 차수
    graph = [[] for _ in range(N + 1)]
    indegree = [0] * (N + 1)
    
    # 건설 순서 규칙 입력
    for _ in range(K):
        X, Y = map(int, input().split())
        graph[X].append(Y)  # X 건물 건설 후 Y 건물 건설 가능
        indegree[Y] += 1  # Y의 진입 차수 증가
    
    # 최종 건설해야 할 건물 번호 W
    W = int(input())
    
    # 각 건물의 완공 시간을 저장하는 리스트
    dp = [0] * (N + 1)
    
    # 큐를 사용하여 위상 정렬 수행
    queue = deque()
    
    # 진입 차수가 0인 건물의 초기 건설 시간 설정
    for i in range(1, N + 1):
        dp[i] = construction_time[i - 1]
        if indegree[i] == 0:
            queue.append(i)
    
    while queue:
        current = queue.popleft()
        
        # 현재 건물로부터 연결된 모든 건물에 대해
        for next_building in graph[current]:
            # 현재 건물의 완공 시간 + 다음 건물의 건설 시간을 계산
            dp[next_building] = max(dp[next_building], dp[current] + construction_time[next_building - 1])
            # 진입 차수 감소
            indegree[next_building] -= 1
            
            # 진입 차수가 0이 되면 큐에 추가
            if indegree[next_building] == 0:
                queue.append(next_building)
    
    # 최종 건물 W의 완공 시간 출력
    print(dp[W])
