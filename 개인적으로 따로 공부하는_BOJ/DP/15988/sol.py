import sys
sys.stdin = open('input.txt')

dp = [1,2,4,7]
for i in range(int(input())):
    n = int(input())
    for j in range(len(dp), n):
        dp.append((dp[-3]+dp[-2]+dp[-1])%1000000009)
    print(dp[n-1])