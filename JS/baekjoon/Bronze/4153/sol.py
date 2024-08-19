import sys
sys.stdin = open('input.txt')


while True:
    lst = list(map(int, input().split()))
    lst.sort()
    if lst[0] == lst[1] == lst[2] == 0:
        break
    
    if lst[0] ** 2 + lst[1] ** 2 == lst[2] ** 2:
        print('right')
    else:
        print('wrong')
