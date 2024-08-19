import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    N = int(input())

    pascal = []

    for i in range(N):
        temp = []
        for j in range(i+1):
            if j == 0 or j == i:
                temp.append(1)
            else:
                temp.append(pascal[i-1][j] + pascal[i-1][j-1])
        pascal.append(temp)

    print(f'#{tc}')
    for i in pascal:
        print(*i)

# 강사님 풀이
        
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    print(f'#{tc}')
    for i in range(N):
        ans = str(11 ** i)
        print(' '.join(ans))
        

import sys
sys.stdin = open('input.txt')

memo = [[1] * 10 for _ in range(10)]

for i in range(1, 10):
    for j in range(1, 10):
        if i != j:
            memo[i][j] = memo[i - 1][j - 1] + memo[i - 1][j]


# for i in range(10):
#     print(memo[i])

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    print(f'#{tc}')
    for i in range(N):
        print(*memo[i][:i+1])
