import sys
sys.stdin = open('input.txt')

N = int(input())
# range => start, end, step
for i in range(N, -1, -1):
    print(i)