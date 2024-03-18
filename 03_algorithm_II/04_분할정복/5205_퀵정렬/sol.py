import sys
sys.stdin = open('input.txt')


def quick_sort(arr):
    if len(arr) == 1:
        return arr

    pivot = arr[len(arr) // 2]

    lesser_arr, equal_arr, greater_arr = [], [], []

    for num in arr:
        if num < pivot:
            lesser_arr.append(num)
        elif num > pivot:
            greater_arr.append(num)
        else:
            equal_arr.append(num)

    return quick_sort((lesser_arr)) + quick_sort(equal_arr) + quick_sort(greater_arr)


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    a = sorted(list(map(int, input().split())))

    print(f'#{tc} {a[N//2]}')

