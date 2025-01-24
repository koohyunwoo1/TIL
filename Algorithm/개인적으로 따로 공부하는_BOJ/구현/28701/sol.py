import sys
input = sys.stdin.readline

n = int(input())
a = 0
c = 0

for i in range(1, n+1):
    a += i
    c += i**3
    
print(a)    
print(a**2)    
print(c)    