import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    n = int(input())
    dp = [0] * 100001
