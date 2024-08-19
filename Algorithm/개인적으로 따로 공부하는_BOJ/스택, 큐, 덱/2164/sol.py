import sys
from collections import deque
sys.stdin = open('input.txt')

N = int(input())

deque = deque()
for i in range(1, N+1):
    deque.append(i)

while len(deque) > 1:
    deque.popleft()
    num = deque.popleft()
    deque.append(num)

print(deque[0])




