import sys
sys.stdin = open('input.txt')


def quick_sort(arr):
    if len(arr) <= 1:   # 종료 조건 1 이하이면 이미 정렬이 되어있을거임.
        return arr

    pivot = arr[len(arr) // 2]
    arr1, arr2, arr3 = [], [], []

    for num in arr:
        if num < pivot:
            arr1.append(num)
        elif num == pivot:
            arr2.append(num)
        else:
            arr3.append(num)

    return quick_sort(arr1) + arr2 + quick_sort(arr3)

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    s_arr = quick_sort(arr)
    idx = len(s_arr) // 2
    print(f'#{tc} {s_arr[idx]}')
