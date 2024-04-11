import sys
sys.stdin = open('input.txt')

H, M = map(int, input().split())

if M > 45:
    print(H, M-45)
elif H > 0 and M <= 45:
    print(H-1, M+15)
else:
    print(23, M+15)