import sys
from itertools import combinations
sys.stdin = open('input.txt')
'''
점원들이 쌓는 탑은 점원 1명 이상으로 이루어져 있다.
탑의 높이는 점원이 1명일 경우 그 점원의 키,
점원이 2명 이상일 경우, 탑을 만든 모든 점원의 키의 합

'''
T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    height = list(map(int, input().split()))
    result = 9999999999

    for i in range(1, N+1):
        a = list(combinations(height, i))

        for j in a:
            if sum(j) >= B:
                if sum(j) - B < result:
                    result = sum(j) - B

    print(f'#{tc} {result}')


'''
#1 1
#2 4
#3 27
#4 11
#5 42
#6 32
#7 2
#8 3
#9 25
#10 0
'''