import sys
sys.stdin = open('input.txt')

'''
오셀로 : 흑돌과 백돌을 가진 사람이 번갈아가면서 돌을 놓은 후, 
최종적으로 보드에 자신의 돌이 많은 사람이 이기는 게임이다.

만약 돌을 놓을 곳이 없다면 상대편 플레이어가 다시 돌을 놓는다.
보드에 빈 곳이 없거나 양 플레이어 모두 돌을 놓을 곳이 없으면 게임이 끝나고
그 때 보드에 있는 돌의 개수가 많은 플레이어가 승리하게 된다.
각 테스트 케이스마다 게임이 끝난 후 보드 위의 흑돌, 백돌의 개수를 출력한다.
'''

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
for tc in range(M):
    x, y, color = map(int, input().split())



