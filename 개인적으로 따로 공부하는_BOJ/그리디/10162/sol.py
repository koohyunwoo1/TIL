import sys
sys.stdin = open('input.txt')

T = int(input())

'''
A = 300
B = 60
C = 10

'''
A = 300
B = 60
C = 10

cnt_a = 0
cnt_b = 0
cnt_c = 0

if T % 10 != 0:
    print(-1)

else:
    while T > 0:
        if T >= A:
            T -= A
            cnt_a += 1
        elif T >= B:
            T -= B
            cnt_b += 1
        elif T >= C:
            T -= C
            cnt_c += 1

    print(cnt_a, cnt_b, cnt_c)

