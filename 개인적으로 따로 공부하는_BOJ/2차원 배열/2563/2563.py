import sys
sys.stdin = open('input.txt')

T = int(input())

arr = [[0 for _ in range(100)] for _ in range(100)]

for tc in range(T):
    x, y = map(int, input().split())

    for i in range(x, x+10):
        for j in range(y, y+10):
            arr[i][j] = 1

counts = 0
for arr_count in range(100):
    counts += arr[arr_count].count(1)

print(counts)


