import sys
from collections import deque
sys.stdin = open('input.txt')

N, K = map(int, input().split())

deque = deque()

for i in range(1, N+1):
    deque.append(i)

result = []
while deque:
    for i in range(K-1):
        deque.append(deque.popleft())
    result.append(deque.popleft())

print('<' + ', '.join(map(str, result)) + '>')
