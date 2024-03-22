import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    N = int(input())
    lst1 = set(map(int, input().split()))
    M = int(input())
    lst2 = list(map(int, input().split()))

    for num in lst2:
        if num in lst1:
            print(1)
        else:
            print(0)




