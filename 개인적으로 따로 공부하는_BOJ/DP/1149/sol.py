import sys
sys.stdin = open('input.txt')

N = int(input())

cost = [list(map(int, input().split())) for _ in range(N)]

'''
빨 초 파   - > 집을 짓는 비용
그 전에 칠한 색깔은 칠하지 않는다.

'''

dp = [[0] * 3  for _ in range(1001)]
dp[0] = cost[0]

for i in range(1, N):
    dp[i][0] = cost[i][0] + min(dp[i-1][1], dp[i-1][2])
    dp[i][1] = cost[i][1] + min(dp[i-1][0], dp[i-1][2])
    dp[i][2] = cost[i][2] + min(dp[i-1][0], dp[i-1][1])


min_cost = min(dp[N-1])

print(min_cost)