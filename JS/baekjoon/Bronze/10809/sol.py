import sys
sys.stdin = open('input.txt')

S = input()
alphavet = 'abcdefghijklmnopqrstuvwxyz'

for i in alphavet:
    if i in S:
        print(S.index(i), end =' ')
    else:
        print(-1, end =' ')