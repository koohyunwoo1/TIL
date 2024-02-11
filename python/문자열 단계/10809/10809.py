import sys
sys.stdin = open('input.txt')


S = input()
c = 'abcdefghijklmnopqrstuvwxyz'

for i in c:
    if i in S:
        print(S.index(i), end = ' ')
    else:
        print(-1, end=' ')