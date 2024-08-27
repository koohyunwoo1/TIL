import sys
input = sys.stdin.readline

n , m = map(int, input().split())
dp = [[[0] for _ in range(n)] for _ in range(n)]
arr = [list(map(int ,input().split())) for _ in range(n)]

for _ in range(m):
    x1, y1, x2, y2 = list(map(int, input().split()))
    
