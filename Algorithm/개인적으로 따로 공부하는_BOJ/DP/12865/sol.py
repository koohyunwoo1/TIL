import sys
input = sys.stdin.readline

n, k = map(int, input().split())
# k : 최대로 넣을 수 있는 무게
# n : 물품의 수
dp = [0] * (k+1)

for i in range(n):
    w, v = map(int, input().split())
    # w : 물건의 무게
    # v : 물건의 가치
    for j in range(k, w-1, -1):
        dp[j] = max(dp[j], dp[j-w] + v)

print(dp[k])