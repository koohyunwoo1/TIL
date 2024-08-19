import sys
sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T+1):
    C = int(input())
    for i in [25, 10, 5, 1]:
        print(C // i, end=' ')
        C = C % i
    print()