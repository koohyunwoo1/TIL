import sys
sys.stdin = open('input.txt')

'''
A와 B 가는길이 존재하는지 ?
갈림길 최대 2개이며 일방통행임
'''

for _ in range(10):
    tc, N = map(int, input().split())
    road = list(map(int, input().split()))

    adj_list = [[] for _ in range(100)]
    for i in range(N):
        adj_list[road[2*i]].append(road[2*i+1])
        print(adj_list)