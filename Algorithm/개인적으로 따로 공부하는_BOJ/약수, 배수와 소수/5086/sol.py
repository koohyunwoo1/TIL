import sys
sys.stdin = open('input.txt')

while True:
    N, M = map(int, input().split())
    if N == 0 and M == 0:
        break
    if M % N == 0:
        print('factor')
    elif N % M == 0:
        print('multiple')
    else:
        print('neither')