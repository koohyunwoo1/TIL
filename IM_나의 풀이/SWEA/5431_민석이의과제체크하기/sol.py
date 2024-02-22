import sys
sys.stdin = open('input.txt')

'''
과제를 제출하지 않은 사람의 번호를 오름차순으로 출력하라
'''

T = int(input())

for tc in range(1,T+1):
    N, K = map(int, input().split())
    number = list(map(int, input().split()))
    # 2 5 3    # 4 6
    print(f'#{tc}', end=' ')

    for i in range(1, N+1):
        if i not in number:
            print(i, end=' ')

    print()