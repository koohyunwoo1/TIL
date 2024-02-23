import sys
sys.stdin = open('input.txt')

arr = [[0  for _ in range(101)] for _ in range(101)]

T = 4

for tc in range(T):
    x1, y1, x2 ,y2 = map(int, input().split())

    for i in range(x1, x2):
        for j in range(y1, y2):
            arr[i][j] = 1

result = 0
for k in arr:
    result += sum(k)
print(result)