import sys
sys.stdin = open('input.txt')

N = int(input())

dp = [-1 for _ in range(5001)]

dp[3] = 1
dp[5] = 1

if N <= 5:
    print(dp[N])

else:
    pass