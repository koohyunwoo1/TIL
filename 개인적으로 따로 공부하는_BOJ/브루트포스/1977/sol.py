import sys
input = sys.stdin.readline

m = int(input())
n = int(input())

arr = []
cnt = 0

for i in range(1, 101):
    if m <= i ** 2 and i ** 2 <= n:
        cnt += i ** 2
        arr.append(i ** 2)

if cnt == 0 and len(arr) == 0:
    print(-1)
else:
    print(cnt)
    print(arr[0])