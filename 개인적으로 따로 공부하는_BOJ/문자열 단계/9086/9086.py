import sys
sys.stdin = open('input.txt')

T = int(input())

for i in range(T):
    S = input()
    print(f'{S[0]}{S[-1]}')
    # print(S[-1])