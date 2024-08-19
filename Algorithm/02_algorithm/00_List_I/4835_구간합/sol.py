import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    num = list(map(int, input().split()))

    result = []

    for i in range(N-M+1):
        num_sum = sum(num[i:i+M])
        result.append(num_sum)

    print(f'#{tc} {max(result) - min(result)}')