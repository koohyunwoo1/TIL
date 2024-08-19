import sys
sys.stdin = open('input.txt')

K = int(input())

stack = []

for i in range(K):
    num = int(input())
    if num == 0:
        stack.pop()
    else:
        stack.append(num)

print(sum(stack))