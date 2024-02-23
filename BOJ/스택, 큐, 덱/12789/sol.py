import sys
sys.stdin = open('input.txt')

N = int(input())
num = list(map(int, input().split()))

stack = []
target = 1

while num:
    if num[0] == target:
        num.pop(0)
        target += 1
    else:
        stack.append(num.pop(0))

    while stack:
        if stack[-1] == target:
            stack.pop(-1)
            target += 1
        else:
            break


if len(stack) == 0:
    print('Nice')
else:
    print('Sad')






