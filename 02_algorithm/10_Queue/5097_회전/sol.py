import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    num = list(map(int, input().split()))
    for i in range(M):
        num.append(num.pop(0))
    print(f'#{tc} {num[0]}')