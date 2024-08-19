import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, S = map(str, input().split())
    N = int(N)

