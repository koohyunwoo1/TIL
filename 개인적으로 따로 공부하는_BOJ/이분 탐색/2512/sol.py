import sys
sys.stdin = open('input.txt')

N = int(input())

lst = list(map(int, input().split()))
M = int(input())

left = 0
right = max(lst)

while left <= right:
    mid = (left + right) // 2
    cnt = 0

    for i in lst:
        if i > mid:
            cnt += mid
        else:
            cnt += i

    if cnt < M:
        left = mid + 1
    else:
        right = mid - 1

print(right)


