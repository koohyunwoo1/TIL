import sys
sys.stdin = open('input.txt')

T = int(input())
counts = 0
arr = [[0 for _ in range(100)] for _ in range(100)]

for tc in range(T):
    x, y = list(map(int, input().split()))
    for i in (x, x+10):
        for j in (y, y+10):
            arr[i][j] = 1

for arr_count in arr:
    counts += arr_count.count(1)

print(counts)


