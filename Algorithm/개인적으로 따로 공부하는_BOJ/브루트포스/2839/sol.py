import sys
sys.stdin = open('input.txt')

N = int(input())


cnt = 0

while N >= 0: # N이 0이 되면 끝이난다.
    if N % 5 == 0:
        cnt += (N // 5)
        print(cnt)
        break
    N -= 3
    # print(N)
    cnt += 1
    # print(cnt)
else:
    print(-1)