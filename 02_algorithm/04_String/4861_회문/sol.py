import sys
sys.stdin = open('input.txt')

T = int(input())

for _ in range(1, T+1):
    N, M = map(int, input().split())

    arr = [input() for _ in range(N)]
    print(arr)

    # 가로에서 회문하는 경우
    for i in range(N):
        for j in range(N - M + 1):

            pass
