import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    lst = list(input())

    cnt = 0
    sum = 0 

    for i in lst:
        if i == 'O':
            cnt += 1
            sum += cnt
        else:
            cnt = 0

    print(sum)

               