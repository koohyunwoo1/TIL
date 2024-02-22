import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    height = [list(map(int, input().split())) for _ in range(N)]

    pass
