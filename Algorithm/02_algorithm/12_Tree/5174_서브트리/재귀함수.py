import sys
sys.stdin = open('input.txt')


def preorder(node):
    global result
    if node:
        result += 1
        preorder(tree[node][0])
        preorder(tree[node][1])

T = int(input())
for tc in range(1, T + 1):
    E, N = map(int, input().split())
    tree = [[0, 0] for i in range(E+2)]
    lst = list(map(int, input().split()))

    for i in range(E):
        p = lst[i*2]
        c = lst[i*2+1]
        if tree[p][0] == 0:
            tree[p][0] = c
        else:
            tree[p][1] = c

    print()
    result = 0 # N번 노드가 가지고 있는 자손 노드들의 수