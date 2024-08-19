import sys
sys.stdin = open('input.txt')

from collections import deque

'''
L[0:N//2], L[N//2:N]
N // 2번째 원소와 오른쪽 원소가 먼저 복사되는 경우의 수를 출력한다.
'''

def merge_sort(arr):
    if len(arr) == 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    global cnt
    result = []

    left = deque(left)
    right = deque(right)
    # 오른쪽 원소가 먼저 복사되는 경우의 수를 출력하기 때문에
    # 왼쪽의 가장 마지막값이 크면 cnt를 1씩 높여준다.
    if left[-1] > right[-1]:
        cnt += 1

    while len(left) > 0 or len(right) > 0:   # 두 리스트 중 하나라도 남아있을 경우 반복한다.
        if len(left) > 0 and len(right) > 0:   # 두 리스트 다 원소가 남아있을 경우
            if left[0] < right[0]:
                result.append(left.popleft())

            else:
                result.append(right.popleft())



        elif len(left) > 0:    # 왼쪽 리스트만 원소가 남아있을 경우
            result.append(left.popleft())



        elif len(right) > 0:    # 오른쪽 리스트만 원소가 남아있을 경우
            result.append(right.popleft())


    return result


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    data = merge_sort(arr)

    print(f'#{tc} {data[N//2]} {cnt}')



