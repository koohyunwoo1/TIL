import sys
sys.stdin = open('input.txt')

n = int(input())

dp = [-1] * 100001
# dp = [-1] * (n+1)

dp[2] = 1
# 동전을 쓴 횟수
dp[3] = -1
dp[5] = 1
dp[4] = 2

for i in range(6, n+1):
    if dp[i-5] == -1 and dp[i-2] == -1:
        # 5원으로도 2원으로도 만들수 없는 경우
        dp[i] = -1
    elif dp[i-5] == -1:
        # 5원으로 만들 수 없는 경우
        dp[i] = dp[i-2] + 1
    elif dp[i-2] == -1:
        dp[i] = dp[i-5] + 1
    else:
        dp[i] = min(dp[i-5] + 1, dp[i-2] + 1)

print(dp[n])