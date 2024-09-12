import sys
input = sys.stdin.readline

a = list(map(int, input().split()))
min = min(a)
while True:
    cnt = 0
    for i in a:
        if min % i == 0:
            cnt += 1
    if cnt > 2:
        break
    min  += 1
print(min)