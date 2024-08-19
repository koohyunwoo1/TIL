import sys
sys.stdin = open('input.txt')

T = int(input())

arr = [[0 for _ in range(100)] for _ in range(100)]

for tc in range(1, T+1):
    N, M = map(int, input().split())

    for i in range(N, N+10):
        for j in range(M, M+10):
            arr[i][j] = 1

counts = 0
for i in range(100):
        counts += arr[i].count(1)


print(counts)


