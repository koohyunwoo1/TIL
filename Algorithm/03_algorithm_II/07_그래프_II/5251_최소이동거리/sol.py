import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, E = map(int, input().split())
    for _ in range(E):
        s, e, w = map(int, input().split())
        # 구간 시작, 구간의 끝, 구간 거리
