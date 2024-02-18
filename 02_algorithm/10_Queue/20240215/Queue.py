'''
큐의 특성
선입선출구조
큐에 삽입한 순서대로 원소가 저장되어, 가장 먼저 삽입된 원소는 가장 먼저 삭제된다.


삽입 : enQueue
삭제 : deQueue



# 큐의 구현
# 삽입
def enQueue(item):
    global rear
    if isFull() : print("Queue_Full")
    else:
        rear = rear + 1
        Q[rear] = item

# 삭제
def deQueue()
    if(isEmpty()) then Queue_Empty():
        else{
            front = front + 1
        return Q[front]
        }
'''

from collections import deque

q = []
for i in range(1000000):
    q.append(i)
print('append')
while q:
    q.pop(0)
print('end')


dq = []
for i in range(1000000):
    dq.append(i)
print('append')
while dq:
    dq.popleft()
print('end')