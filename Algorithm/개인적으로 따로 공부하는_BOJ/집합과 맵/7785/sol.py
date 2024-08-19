import sys
sys.stdin = open('input.txt')

'''
이름 별로 enter 있는데 leave가 없으면 출력
그 대신 남아있는 사람은 사전 순의 역순으로 한줄에 한명씩 출력함

'''
n = int(input())
for tc in range(n):
    name, go = map(str, input().split())
pass