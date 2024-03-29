import sys
from collections import deque
read = sys.stdin.readline

T = int(read())

for tc in range(T):
    N, M = map(int, read().split())
    important = list(map(int, read().split()))

    queue = deque()

    for i in range(N):
        if queue:
            queue.append(important.popleft())




