import sys
sys.stdin = open('input.txt')

n = int(input())
num = input()
total = 0

for i in range(n):
    total += int(num[i])
print(total)