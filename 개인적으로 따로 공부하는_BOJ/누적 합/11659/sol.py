# import sys
# sys.stdin = open('input.txt')


import sys
input = sys.stdin.readline

m, n = map(int, input().split())
arr = list(map(int, input().split()))
p_sum = [0]

temp = 0
for i in arr:
    temp += 1
    p_sum.append(temp)
    
for i in range(n):
    a, b = map(int, input().split())
    print(p_sum[b]-p_sum[a-1])