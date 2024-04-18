import sys
sys.stdin = open('input.txt')

# N = int(input())
# A = list(map(int, input().split()))
#
# dp = [0] * 1001
#
# dp[1] = A[0]
#
# for i in range(2, N+1):
#     for j in range(1, i):
#         if A[j-1] < A[i-1]:
#             dp[i] = max(dp[i], dp[j] + A[i-1])
#
#
# print(max(dp))


N = int(input())
A = list(map(int, input().split()))

dp = [0] * N

dp[0] = A[0]

for i in range(1, N):
    for j in range(i):
        if A[j] < A[i]:
            dp[i] = max(dp[i], dp[j])
    dp[i] += A[i]

print(max(dp))
