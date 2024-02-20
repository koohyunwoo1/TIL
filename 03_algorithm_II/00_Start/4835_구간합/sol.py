import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    ai = list(map(int, input().split()))

    # 최댓값 비교 대상 가장 작은 경우의 수 0
    max_num = 0
    # 최솟값 비교 대상 가장 큰 경우의 수
    # a가 가질 수 있는 최대 크기 10000
    # 구간합의 범위 M
    min_num = 10001 * M
    # N개의 정수, M개의 범위
    # 10 - 3 => 7 | 7개의 정수를 대상으로 조사
    for i in range(N - M + 1):
        temp = 0
        # 내 현재 위치부터 M개 까지
        for j in range(i, i + M):
            temp += ai[j]
        if max_num < temp:
            max_num = temp
        if min_num > temp:
            min_num = temp
    result = max_num - min_num
    print(f'#{tc} {result}')
