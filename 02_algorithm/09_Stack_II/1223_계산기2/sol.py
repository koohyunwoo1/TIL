import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    arr = list(input())
    oper = ['+', '*']
    stack = []

    for i in arr:
        if i.isdigit():
            stack.append(i)
            # print(stack)
    