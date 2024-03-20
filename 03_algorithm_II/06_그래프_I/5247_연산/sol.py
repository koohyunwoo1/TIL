import sys
from collections import deque
sys.stdin = open('input.txt')
'''
자연수 N에 몇 번의 연산을 통해 다른 자연수 M을 만들려고 한다.
사용할 수 있는 연산 +1 , -1, *2, -10
최소 몇번의 연산을 거쳐야 하는지 ?

N - > M 최단 경로
BFS
'''

def BFS(left, right):

    queue = deque([(left, 0)])
    visited = []
    visited.append(left)

    while queue:
        start, cnt = queue.popleft()

        if start == right:
            return cnt

        for num in (start + 1, start - 1, start * 2, start - 10):
            if 1 <= num <= 1000000 and num not in visited:
                queue.append((num, cnt+1))
                visited.append(num)



T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    result = BFS(N, M)
    print(f'{tc} {result}')