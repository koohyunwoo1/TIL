import sys
sys.stdin = open('input.txt')

N, K = map(int, input().split())
x = list(map(int, input().split()))
x.sort()

print(x[-K])