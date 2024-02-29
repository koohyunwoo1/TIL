import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num = list(map(int, input().split()))

    for i in range(N):
        number = max(num) - min(num)
    print(f'#{tc} {number}')