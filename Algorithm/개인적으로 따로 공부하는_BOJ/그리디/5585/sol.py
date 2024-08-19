import sys
sys.stdin = open('input.txt')

M = int(input())

money = [500, 100, 50, 10, 5, 1]

m = 1000 - M
cnt = 0

for mon in money:
    cnt += m // mon
    m %= mon

print(cnt)

