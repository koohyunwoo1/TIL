import sys
sys.stdin = open('input.txt')

n, k = map(int, input().split())

coins = []
for i in range(n):
    coins.append(int(input()))
coins.sort()

dp = [0] * (k+1)
dp[0] = 1
for c in coins:
    for i in range(c, k+1):
        dp[i] += dp[i-c]
print(dp[k])