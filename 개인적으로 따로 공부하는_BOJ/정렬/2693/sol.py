import sys
input = sys.stdin.readline

T = int(input())

for i in range(1, T+1):
    lst = list(map(int, input().split()))
    lst.sort()

    print(lst[7])