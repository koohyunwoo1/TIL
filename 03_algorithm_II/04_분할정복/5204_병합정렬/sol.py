import sys
sys.stdin = open('input.txt')
'''
L[0:N//2], L[N//2:N]
N // 2번째 원소와 오른쪽 원소가 먼저 복사되는 경우의 수를 출력한다.
'''


# 분할과정




# 병합과정

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))