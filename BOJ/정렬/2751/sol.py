import sys
sys.stdin = open('input.txt')

T = int(input())
num = []

for tc in range(T):
    num.append(int(input()))

num.sort()

for i in num:
    print(i)