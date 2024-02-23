import sys
sys.stdin = open('input.txt')

A, B = map(int, input().split())
C = int(input())
A = A +  C // 60  # 60으로 나누었을때 몫
B = B +  C % 60  # 60으로 나누었을떄 나머지

if B >= 60:
    A = A + 1
    B = B - 60
if A >= 24:
    A = A - 24

print(A,B)