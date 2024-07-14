import sys
input = sys.stdin.readline

N = int(input())
cnt = 0

for i in range(1, N+1):
    if i < 100:
        cnt += 1
        
    else:
        num = list(map(int, str(i)))
        if num[1] - num[0] == num[2] - num[1]:
            cnt += 1
            
print(cnt)

