import sys
input = sys.stdin.readline

n, k = map(int, input().split())

coins = []
for _ in range(n):
    coin = int(input())
    if coin <= k:  
        coins.append(coin)

dp = [float('inf')] * (10001) 
dp[0] = 0  

for coin in coins:
    for i in range(coin, k + 1):
        dp[i] = min(dp[i], dp[i - coin] + 1)

result = dp[k]
if result == float('inf'):
    print(-1)  
else:
    print(result)  
