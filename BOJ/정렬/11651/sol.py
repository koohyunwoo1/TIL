import sys
sys.stdin = open('input.txt')

T = int(input())

lst = []
for tc in range(T):
    [x, y] = map(int, input().split())
    lst.append([y, x])

lst_a = sorted(lst)

for y, x in lst_a:
    print(x, y)