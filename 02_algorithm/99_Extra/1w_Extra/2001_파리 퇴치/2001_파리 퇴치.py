import sys
sys.stdin = open('input.txt')

# N x N 배열 안의 숫자는 해당 영역에 존재하는 파리의 개수를 의미한다.

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    s = []
    for i in range(N-M+1):
        pass

    # 파리채를 내려칠곳을 알아야함.
    # 그리고 그 후에 잡을수있는 파리의 수 