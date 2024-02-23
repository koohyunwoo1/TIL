import sys
sys.stdin = open('input.txt')

'''
착륙할때 예비 후보지가 4곳 이상인 곳을 찾아보자
'''
T = int(input())

di = [1, 0, -1, 0, 1, 1, -1, -1]
dj = [0, 1, 0, -1, 1, -1, 1, -1]



for tc in range(1, T+1):
    N, M = map(int, input().split())
    height = [list(map(int, input().split())) for _ in range(N)]


    
