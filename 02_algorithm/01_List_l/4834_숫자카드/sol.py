import sys
sys.stdin = open('sample_input.txt')
# 가장 많은 카드의 숫자와 장수를 출력해라
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    num = list(map(int, input()))

    lst = [0 for _ in range(10)]

    for i in num:
        lst[i] += 1

    max_cnt = 0
    result = 0

    for i in range(10):

        if max_cnt <= lst[i]:
            max_cnt = lst[i]
            result = i

    print(f'#{tc} {result} {max_cnt}')



