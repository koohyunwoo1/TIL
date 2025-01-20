import sys
input = sys.stdin.readline

N = list(map(int, str(input().strip()))) 
result = 0

for i in N:
    result += i**5
    
print(result)