import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())

lst = [list(map(str, input())) for _ in range(N)]

