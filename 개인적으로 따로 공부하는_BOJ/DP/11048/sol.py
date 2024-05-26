import sys
input = sys.stdin.readline

N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * (M+1) for _ in range(N + 1)]
print(dp)

