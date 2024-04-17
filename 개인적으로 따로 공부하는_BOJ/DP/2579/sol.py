import sys
sys.stdin = open('input.txt')

N = int(input())

score = [int(input()) for _ in range(N)]

dp = [0] * (N+1)

dp[1] = score[0]
if N > 1:
    dp[2] = score[0] + score[1]

for i in range(3, N+1):
    dp[i] = max(dp[i-2], dp[i-3] + score[i-2]) + score[i-1]

print(dp[N])
