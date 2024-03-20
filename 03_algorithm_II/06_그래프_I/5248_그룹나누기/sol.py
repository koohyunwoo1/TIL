import sys
sys.stdin = open('input.txt')

'''
한명이라도 같으면 같은조에 전부 속하게 됨

'''

def make_set(n):
    return [i for i in range(n)]

parents = make_set(5)
print(parents)

def find_set(x):
    if parents[x] == x:
        return

    return find_set(parents[x])

def union(x,y):
    x = find_set(x)
    y = find_set(y)

    if x == y:
        return

    if x < y:
        parents[y] = x
    else:
        parents[x] = y


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))

