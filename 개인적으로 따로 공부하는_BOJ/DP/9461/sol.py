import sys
sys.stdin = open('input.txt')

T = int(input())

for _ in range(T):
    N = int(input())

    dp = [1] * 101

    for i in range(4, N+1):
        dp[i] = dp[i-2] + dp[i-3]

    print(dp[N])

'''
    뒤에서 2번째 3번쨰 더한 값이 현재값
1 1 1 2 2 3 4 5 7 9 12 16 21 28 37 49 65 86 

'''