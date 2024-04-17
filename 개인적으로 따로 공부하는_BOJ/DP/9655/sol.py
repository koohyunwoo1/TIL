import sys
sys.stdin = open('input.txt')

N = int(input())

# 상근이가 게임 먼저 시작
# 1 1 3
# 3 1 1
# 1 3 1
# 1 1 1 1 1

dp = [0] * 1001

