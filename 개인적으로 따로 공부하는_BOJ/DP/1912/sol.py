import sys
sys.stdin = open('input.txt')

n = int(input())
num = list(map(int, input().split()))

dp = [0] * 100001
dp[0] = num[0]
max_sum = dp[0]

for i in range(1, n):
    dp[i] = max(num[i], dp[i-1] + num[i])
    max_sum = max(max_sum, dp[i])

print(max_sum)

