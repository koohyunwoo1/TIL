import sys
sys.stdin = open('input.txt')

num = int(input())
number = list(map(int, input().split()))

lst = []
for i in range(num):
    lst.insert(number[i], i+1)

print(*lst[::-1])