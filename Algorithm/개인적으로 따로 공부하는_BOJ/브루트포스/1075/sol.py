import sys
input = sys.stdin.readline

N = int(input())
F = int(input())
front = N // 100
answer = front * 100

while answer % F != 0:
    answer += 1
print(str(answer)[-2:])