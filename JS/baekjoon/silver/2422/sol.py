import sys
sys.stdin = open('input.txt')


N, M = map(int, input().split())
# N은 아이스크림의 종류 수
# M은 섞어먹으면 안 되는 조합의 개수
for i in range(M):
    num = list(map(int, input().split()))
    