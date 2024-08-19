import sys
sys.stdin = open('input.txt')

N = int(input())

DP = [float('inf')] * (N + 1)

DP[0] = 0
for i in range(3, N + 1):
    if i >= 3:
        DP[i] = min(DP[i], DP[i - 3] + 1)
    if i >= 5:
        DP[i] = min(DP[i], DP[i - 5] + 1)

if DP[N] == float('inf'):
    print(-1)
else:
    print(DP[N])
