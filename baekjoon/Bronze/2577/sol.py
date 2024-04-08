import sys
sys.stdin = open('input.txt')

A = int(input())
B = int(input())
C = int(input())

num = A * B * C
num = list(str(num))

for i in range(10):
    print(num.count(str(i)))


