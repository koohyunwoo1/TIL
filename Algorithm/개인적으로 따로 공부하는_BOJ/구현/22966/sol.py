import sys
input = sys.stdin.readline

a = int(input())
title = []
num = []

for i in range(a):
    b, c = input().split()
    title.append(b)
    num.append(c)
    
for i in range(len(num)):
    if num[i] == min(num):
        print(title[i])