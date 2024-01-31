import sys
sys.stdin = open('input.txt')
# n = int(input())

for _ in range(1, 11):
    test_cast = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    
    list_sum = []
    row_sum = 0
    column_sum = 0
    diagonal_sum = 0

    for i in arr:
        pass



