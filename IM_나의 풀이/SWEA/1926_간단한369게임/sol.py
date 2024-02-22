import sys
sys.stdin = open('input.txt')

N = int(input())

for i in range(1,N+1):
    num = str(i)

    cnt = 0
    cnt = num.count('3') + num.count('6') + num.count('9')

    if cnt > 0:
        print('-' * cnt, end= ' ')
    else:
        print(num, end= ' ')

