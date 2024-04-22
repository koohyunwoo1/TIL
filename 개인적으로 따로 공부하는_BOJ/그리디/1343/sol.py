import sys
sys.stdin = open('input.txt')

S = input()

S = S.replace('XXXX', 'AAAA')
S = S.replace('XX', 'BB')

if 'X' in S:
    print(-1)
else:
    print(S)
