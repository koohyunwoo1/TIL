import sys
input = sys.stdin.readline

a=int(input())
for i in range(1,a+1):
    print("*"*(a-i+1))