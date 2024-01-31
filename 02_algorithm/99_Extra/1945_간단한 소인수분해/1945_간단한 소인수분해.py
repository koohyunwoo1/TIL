import sys
sys.stdin = open('input.txt')

T = int(input())

for i in range(1,T+1):
    N = int(input())
    result = [0]*5
    while N != 1:  # N이 1이 아닐때까지 반복
        if N % 2 == 0:
            N = N/2
            result[0] += 1
        if N % 3 == 0:
            N = N/3
            result[1] += 1
        if N % 5 == 0:
            N = N/5
            result[2] += 1
        if N % 7 ==0:
            N = N/7
            result[3] += 1
        if N % 11 ==0:
            N = N/11
            result[4] += 1

    print(f'#{i}', *result)  # *result = 리스트 제거 ?