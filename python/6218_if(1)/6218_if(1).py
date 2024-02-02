import sys
sys.stdin = open('input.txt')
T = int(input())

for i in range(1,T+1):
    if T % i == 0:
        print("%d(은)는 %d의 약수입니다." % (i, T))