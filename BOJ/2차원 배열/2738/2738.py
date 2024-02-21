import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())

A = []
B = []

for i in range(N):
    i = list(map(int, input().split()))
    A.append(i)
    # print(A)
for i in range(N):
    i = list(map(int, input().split()))
    B.append(i)
    # print(B)
for i in range(N):
    for j in range(M):
        print(A[i][j] + B[i][j], end = ' ')
    print()