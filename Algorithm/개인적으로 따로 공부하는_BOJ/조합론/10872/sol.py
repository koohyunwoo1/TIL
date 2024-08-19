import sys
sys.stdin = open('input.txt')

N = int(input())

num = 1
for i in range(1, N+1):
    num = num * i
print(num)