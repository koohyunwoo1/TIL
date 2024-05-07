import sys
input = sys.stdin.readline

N = int(input()) 
# 찾을 값
M = int(input())
# 고장난 버튼의 갯수

breakdown = list(map(int, input().split()))

button = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, '+', '-']

cnt = 100

