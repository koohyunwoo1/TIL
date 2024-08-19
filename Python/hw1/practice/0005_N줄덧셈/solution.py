import sys
sys.stdin = open('input.txt')

# 자연수 주어짐
N = int(input())

result = 0

for num in range(1, N+1):
    result += num
print(result)