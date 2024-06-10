import sys
sys.stdin = open('input.txt')

N = int(input())

dp = [float(input()) for _ in range(N)]

for i in range(1, N):
    dp[i] = max(dp[i], dp[i]*dp[i-1])
    
print('%0.3f' % max(dp))