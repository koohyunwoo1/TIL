import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    n, m = map(int,input().split())

    dp = [[0] * [m + 1] for _ in range(n+1)]

    for i in range(m+1):
        dp[1][i] = 1