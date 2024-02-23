import sys
from collections import deque
sys.stdin = open('input.txt')
'''
터진 풍선의 번호를 차례로 나열한다.
'''
N = int(input())
num = list(map(int, input().split()))

deque = deque()
for tc in range(1, N+1):
    deque.append(tc)

    for i in range(N):
        if deque.popleft():
            deque.rotate(num[i])
            pass