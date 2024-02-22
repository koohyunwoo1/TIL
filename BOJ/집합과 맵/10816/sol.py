import sys
sys.stdin = open('input.txt')

N = int(input())
N_number = list(map(int, input().split()))
M = int(input())
M_number = list(map(int, input().split()))

cnt = {}

for i in N_number:
    if i in cnt:
        cnt[i] += 1
    else:
        cnt[i] = 1

for i in M_number:
    if i in cnt:
        print(cnt[i], end =' ')
    else:
        print(0, end =' ')