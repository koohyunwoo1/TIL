import sys
sys.stdin = open('input.txt')

N = int(input())
lst = set()
cnt = 0

for i in range(N):
    S = str(input())
    lst.add(S)


for i in lst:
    if i != 'ENTER':
        cnt += 1

print(cnt)