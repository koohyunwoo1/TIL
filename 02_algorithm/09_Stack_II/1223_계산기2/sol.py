import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    arr = input()
    stack = []
    cnt = 0

    while cnt < N:
            if arr[cnt].isdigit():
                stack.append(int(arr[cnt]))
                cnt += 1
            elif arr[cnt] == '*':
                stack.append(stack.pop() * int(arr[cnt+1]))
                cnt += 2
            else:
                cnt += 1
    print(f'#{tc} {sum(stack)}')


