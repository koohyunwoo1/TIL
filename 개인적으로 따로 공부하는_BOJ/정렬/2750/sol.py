import sys
sys.stdin = open('input.txt')

N = int(input())
lst = []

for tc in range(N):
    lst.append(int(input()))

for i in range(len(lst)):
    for j in range(len(lst) -1 -i):
        if lst[j] > lst[j+1]:
            lst[j] , lst[j+1] = lst[j+1] , lst[j]

for k in lst:
    print(k)