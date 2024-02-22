import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    num = list(map(int, input().split()))
    for i in range(N):
        num.sort(reverse=True)
    print(f'#{tc} {sum(num[:K])}')



