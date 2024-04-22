import sys
sys.stdin = open('input.txt')

N = int(input())

A = list(map(int, input().split()))


inc_dp = [1] * 100001
dec_dp = [1] * 100001


for i in range(1, N):
    if A[i] >= A[i-1]:
        inc_dp[i] = inc_dp[i-1] + 1


for i in range(1, N):
    if A[i] <= A[i-1]:
        dec_dp[i] = dec_dp[i-1] + 1


result = max(max(inc_dp), max(dec_dp))

print(result)
