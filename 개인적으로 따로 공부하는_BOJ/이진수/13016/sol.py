
import sys
sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):
    n, num = input().split()

    num = int(num, 16)
    ans = format(num, '#b')

    ans = ans[2:]

    if len(ans) % 4 != 0:
        print(f'#{tc} 0{ans}')
    else: print(f'#{tc} {ans}')
