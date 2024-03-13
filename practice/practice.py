import sys
sys.stdin = open('input.txt')

def search(arr, target, left, right):
    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] > target:
            right = mid - 1

        else:
            left = mid + 1


n, k = map(int, input().split())
lst = [int(input()) for _ in range(n)]



