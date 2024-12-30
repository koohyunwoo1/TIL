import sys

input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
buckets = [i for i in range(1, N+1)]

for _ in range(M):
    i, j, k = map(int, input().split())
    i, j, k = i-1, j-1, k-1
    buckets = buckets[:i] + buckets[k:j+1] + buckets[i:k] + buckets[j+1:]
    
print(*buckets)