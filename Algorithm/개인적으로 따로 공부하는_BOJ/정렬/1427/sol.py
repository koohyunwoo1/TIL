import sys
sys.stdin = open('input.txt')

num = list(map(int, input()))
num = sorted(num, reverse=True)

for i in num:
    print(i, end='')


