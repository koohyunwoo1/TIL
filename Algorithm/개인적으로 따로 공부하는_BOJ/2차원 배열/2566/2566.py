import sys
sys.stdin = open('input.txt')

arr = []
for tc in range(9):
    ar = list(map(int, input().split()))
    arr.append(ar)

max_num = 0
max_row , max_col = 0, 0

for i in range(9):
    for j in range(9):
        if max_num <= arr[i][j]:
            max_row, max_col = i + 1, j + 1
            max_num =  arr[i][j]

print(max_num)
print(max_row, max_col)
