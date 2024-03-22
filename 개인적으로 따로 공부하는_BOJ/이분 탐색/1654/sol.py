import sys
sys.stdin = open('input.txt')

K, N = map(int, sys.stdin.readline().split())

length = []
for k in range(K):
    l = int(sys.stdin.readline())
    length.append(l)

left = 1
right = max(length)


while left <= right:
    mid = (left + right) // 2
    cnt = 0
    for i in length:
        cnt += i // mid
    if cnt >= N:
        left = mid + 1
    else:
        right = mid - 1

print(right)