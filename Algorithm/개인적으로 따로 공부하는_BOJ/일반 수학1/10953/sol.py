import sys
sys.stdin = open('input.txt')

T = int(input())
for i in range(T):
    A,B = map(int, input().split(','))

    print(A+B)
