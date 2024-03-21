import sys
sys.stdin = open('input.txt')

N = int(input())

bulls = 1
cnt = 1

while bulls < N:
    bulls += 6 * cnt
    cnt += 1

print(cnt)