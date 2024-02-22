import sys
sys.stdin = open('input.txt')

'''
당근의 크기가 연속으로 커지는 개수를 출력해라
'''
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    size = list(map(int, input().split()))

    cnt = 1
    mx = 1

    for i in range(1, N):
        if size[i] == size[i-1] + 1:
            cnt += 1
        else:
            if mx < cnt:
                mx = cnt
                cnt = 1
    if mx < cnt:
        mx = cnt


    print(f'#{tc} {mx}')