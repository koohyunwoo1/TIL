# import sys
# from collections import deque
# read = sys.stdin.readline

# T = int(read())
#
# for tc in range(T):
#     N, M = map(int, read().split())
#     important = list(map(int, read().split()))
#
#     queue = deque()
#
#     for i in range(N):
#         if queue:
#             queue.append(important.popleft())

import sys
sys.stdin = open('input.txt')


from collections import deque

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    queue = deque(map(int, input().split()))
    queue = deque([(i, idx) for idx, i in enumerate(queue)])

    count = 0
    while True:
        if queue[0][0] == max(queue, key=lambda x: x[0])[0]:
            count += 1
            if queue[0][1] == M:
                print(count)
                break
            else:
                queue.popleft()
        else:
            queue.append(queue.popleft())