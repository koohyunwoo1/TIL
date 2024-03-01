import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    num = list(map(int, input().split()))

