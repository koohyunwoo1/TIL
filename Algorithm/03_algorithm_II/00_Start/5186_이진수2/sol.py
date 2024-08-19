import sys
sys.stdin = open('input.txt')


T = int(input())

for tc in range(1, T+1):
    data = float(input())
    result = ''
    cnt = 0
    while data != 0:
        data *= 2
        if data >= 1:
            data -= 1
            result += '1'
        else:
            result += '0'
        cnt += 1
        if cnt > 12:
            result = 'overflow'
            break
    print(f'#{tc} {result}')