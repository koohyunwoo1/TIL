import sys
sys.stdin = open('input.txt')
'''
적어도 M미터를 들고 가기위해 설정해야 하는 절단기 높이의 최댓값
'''


N, M = map(int, input().split())
lst = list(map(int, input().split()))

left = 1
right = max(lst)

while left <= right:
    mid = (left + right) // 2
    cnt = 0

    for i in lst:
        if i > mid:
            cnt += i - mid

    if cnt >= M:
        left = mid + 1
    else:
        right = mid - 1

print(right)
