import sys
sys.stdin = open('input.txt')

N = int(input())
level = [int(input()) for _ in range(N)]

cnt = 0

for i in range(N-2, -1, -1):
    if level[i] >= level[i+1]:
        cnt += level[i] - level[i+1] + 1
        level[i] = level[i+1] -1

print(cnt)