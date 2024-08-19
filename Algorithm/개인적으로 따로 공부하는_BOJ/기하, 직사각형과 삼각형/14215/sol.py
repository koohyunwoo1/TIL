import sys
sys.stdin = open('input.txt')

lst = sorted(map(int, input().split()))
result = lst[0] + lst[1] + min(lst[2], lst[0]+lst[1]-1)
print(result)

