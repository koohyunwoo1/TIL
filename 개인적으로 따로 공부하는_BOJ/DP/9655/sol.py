import sys
sys.stdin = open('input.txt')

N = int(input())

if N % 2 == 0:
    print('CY')
else:
    print('SK')


