import sys
sys.stdin = open('algo2_sample_in.txt')

T = int(input())

for _ in range(1, T+1):
    N = list(map(int, input().split()))
    K = list(map(int, input().split()))

