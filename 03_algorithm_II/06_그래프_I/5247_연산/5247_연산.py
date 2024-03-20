import sys
sys.stdin = open('input.txt')

'''
자연수 N에 몇 번의 연산을 통해 다른 자연수 M을 만들려고 한다.
사용할 수 있는 연산 +1 , -1, *2, -10
최소 몇번의 연산을 거쳐야 하는지 ?

N - > M 최단 경로
'''
def DFS(left, right):

    stack = []
    stack.append((left, 0))
    visited = set()
    visited.add(left)

    while stack:
        start, cnt = stack.pop(0)

        if start == right:
            return cnt

        for num in (start + 1, start - 1, start * 2, start - 10):
            if 1 <= num <= 1000000 and num not in visited:
                stack.append((num, cnt + 1))
                visited.add(num)



T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    result = DFS(N, M)
    print(f'#{tc} {result}')
