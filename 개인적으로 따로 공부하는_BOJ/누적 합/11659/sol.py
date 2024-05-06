import sys
input = sys.stdin.readline

m, n = map(int, input().split())
arr = list(map(int, input().split()))
sum = [0]
temp = 0


for i in arr:
    temp += i
    sum.append(temp)
    
for i in range(n):
    a, b = map(int, input().split())
    print(sum[b] - sum[a-1])