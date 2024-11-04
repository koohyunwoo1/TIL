import sys
input = sys.stdin.readline

m, p = map(int, input().split())
print(m // p)
print(m % p)