import sys
sys.stdin = open('input.txt')

n = int(input())


def fabonazi_dp(n):
    dp = [0] * (n+1)
    dp[0] = 0
    dp[1] = 1

    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]

    result = dp[n]
    return result

print(fabonazi_dp(n))


