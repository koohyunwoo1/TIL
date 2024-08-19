# import sys
# sys.stdin = open('input.txt')

N = int(input())

time = []
for j in range(N):
    left, right = map(int, input().split())
    time.append((left, right))
time.sort(key = lambda x: (x[1],x[0]))

cnt = 1
end_time = time[0][1]

for k in range(1, N):
    if time[k][0] >= end_time:
        cnt += 1
        end_time = time[k][1]


print(cnt)



