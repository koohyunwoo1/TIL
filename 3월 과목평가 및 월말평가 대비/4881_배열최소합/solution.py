import sys
sys.stdin = open('input.txt')
'''
세로로 같은 줄에서 두 개 이상의 숫자를 고를수 없음.
'''
'''
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]

    min_sum = 0

    for i in range(N):
        min_sum += min(lst[i])
        min_index = lst[i].index(min(lst[i]))
        # print(min_index)
        for j in range(N):
            for k in range(N):
                if j == min_index and k != i:
                    lst[k][j] = 999999999999999999999999999999999999999999999999999999


    print(lst)

    print(f'#{tc} {min_sum}')

'''
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]

    pass

