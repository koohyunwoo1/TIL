import sys
sys.stdin = open('input.txt')
'''
가장 큰거랑 가장 작은값이랑 바꾸는데
'''


T = int(input())
for tc in range(1, T+1):
    num, change = map(str, input().split())
