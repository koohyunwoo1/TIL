import sys
sys.stdin = open('input.txt')

num = list(map(int, input().split()))

arr = [1,2,3,4,5,6,7,8]

if num == arr:
    print('ascending')
elif num == arr[-1]:
    print('descending')
else:
    print('mixed')