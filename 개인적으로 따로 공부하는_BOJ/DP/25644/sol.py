import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
result, result1 = 0, 0 

for i in range(N-1,-1,-1):
    result = max(result, lst[i])
    result1 = max(result1, result - lst[i])
    
print(result1)